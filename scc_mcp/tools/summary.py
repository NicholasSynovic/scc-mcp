"""Summary tools backed by ``scc --format json2``.

json2 returns a project-level summary (per-language CLOC) plus COCOMO cost
estimates in a single call, so count_lines, by_extension, and cost_estimate all
share it.
"""

from __future__ import annotations

from typing import Any, Optional

from pydantic import Field

from ..format import markdown_table, render
from ..models import ResponseFormat, SccBaseInput
from ..runner import run_scc_json

# Numeric CLOC fields carried per language in json2's languageSummary.
_METRIC_FIELDS = ("Code", "Comment", "Blank", "Lines", "Complexity", "Count")


class CostEstimateInput(SccBaseInput):
    """Inputs for COCOMO cost estimation."""

    cocomo_project_type: str = Field(
        default="organic",
        description="COCOMO model type: 'organic', 'semi-detached', or 'embedded'.",
    )
    currency_symbol: Optional[str] = Field(
        default=None,
        description="Currency symbol for the cost estimate (default '$').",
    )


def _json2(params: SccBaseInput) -> dict[str, Any]:
    """Run scc json2 with the params' filters applied."""
    args = ["--format", "json2", *params.filter_args()]
    return run_scc_json(args, path=params.path)


def _totals(languages: list[dict[str, Any]]) -> dict[str, int]:
    """Sum the numeric CLOC fields across all languages."""
    return {field: sum(int(lang.get(field, 0)) for lang in languages) for field in _METRIC_FIELDS}


def register(mcp: Any) -> None:
    """Register the summary tools on the given FastMCP instance."""

    @mcp.tool(
        name="scc_count_lines",
        annotations={
            "title": "Count Lines of Code",
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        },
    )
    def scc_count_lines(params: SccBaseInput) -> str:
        """Count lines of code under a path, summarized per language plus totals.

        Args:
            params (SccBaseInput): path (default CWD), response_format, and
                include/exclude filters.

        Returns:
            str: markdown table (default) or JSON with per-language and total
            Code/Comment/Blank/Lines/Complexity counts.
        """
        data = _json2(params)
        languages = data.get("languageSummary", [])
        totals = _totals(languages)

        rows = [
            {
                "Language": lang["Name"],
                "Files": lang.get("Count", 0),
                "Code": lang.get("Code", 0),
                "Comment": lang.get("Comment", 0),
                "Blank": lang.get("Blank", 0),
                "Lines": lang.get("Lines", 0),
            }
            for lang in languages
        ]
        rows.append(
            {
                "Language": "TOTAL",
                "Files": totals["Count"],
                "Code": totals["Code"],
                "Comment": totals["Comment"],
                "Blank": totals["Blank"],
                "Lines": totals["Lines"],
            }
        )
        md = markdown_table(
            rows, ["Language", "Files", "Code", "Comment", "Blank", "Lines"]
        )
        return render(
            {"languages": languages, "totals": totals},
            params.response_format,
            markdown=md,
        )

    @mcp.tool(
        name="scc_by_extension",
        annotations={
            "title": "CLOC by Language/Extension",
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        },
    )
    def scc_by_extension(params: SccBaseInput) -> str:
        """Break down code counts per language/extension under a path.

        Args:
            params (SccBaseInput): path (default CWD), response_format, and
                include/exclude filters.

        Returns:
            str: markdown table (default) or JSON with one row per language
            (file count and Code/Comment/Blank/Lines).
        """
        data = _json2(params)
        languages = data.get("languageSummary", [])
        rows = [
            {
                "Language": lang["Name"],
                "Files": lang.get("Count", 0),
                "Code": lang.get("Code", 0),
                "Comment": lang.get("Comment", 0),
                "Blank": lang.get("Blank", 0),
                "Lines": lang.get("Lines", 0),
                "Complexity": lang.get("Complexity", 0),
            }
            for lang in languages
        ]
        md = markdown_table(
            rows,
            ["Language", "Files", "Code", "Comment", "Blank", "Lines", "Complexity"],
        )
        return render(rows, params.response_format, markdown=md)

    @mcp.tool(
        name="scc_cost_estimate",
        annotations={
            "title": "COCOMO Cost Estimate",
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        },
    )
    def scc_cost_estimate(params: CostEstimateInput) -> str:
        """Estimate development cost, schedule, and team size via COCOMO.

        Args:
            params (CostEstimateInput): path (default CWD), response_format,
                filters, cocomo_project_type, and currency_symbol.

        Returns:
            str: markdown (default) or JSON with estimatedCost,
            estimatedScheduleMonths, and estimatedPeople.
        """
        args = [
            "--format",
            "json2",
            "--cocomo-project-type",
            params.cocomo_project_type,
            *params.filter_args(),
        ]
        if params.currency_symbol:
            args += ["--currency-symbol", params.currency_symbol]
        data = run_scc_json(args, path=params.path)

        estimate = {
            "estimatedCost": data.get("estimatedCost"),
            "estimatedScheduleMonths": data.get("estimatedScheduleMonths"),
            "estimatedPeople": data.get("estimatedPeople"),
        }
        symbol = params.currency_symbol or "$"
        md = "\n".join(
            [
                f"# COCOMO Estimate ({params.cocomo_project_type})",
                "",
                f"- **Estimated cost**: {symbol}{estimate['estimatedCost']:,.2f}",
                f"- **Estimated schedule**: {estimate['estimatedScheduleMonths']:.2f} months",
                f"- **Estimated people**: {estimate['estimatedPeople']:.2f}",
            ]
        )
        return render(estimate, params.response_format, markdown=md)
