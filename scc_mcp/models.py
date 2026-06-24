"""Shared Pydantic input models and enums for scc tools."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ResponseFormat(str, Enum):
    """Output format for tool responses."""

    MARKDOWN = "markdown"
    JSON = "json"


class SccBaseInput(BaseModel):
    """Common inputs shared by scc tools.

    Most tools scan a path and support filtering plus a choice of output format.
    The default output is human-readable markdown; ``json`` returns structured
    data.
    """

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        extra="forbid",
    )

    path: Optional[str] = Field(
        default=None,
        description=(
            "Directory or file to scan. Defaults to the current working "
            "directory. Must be readable and executable by the process."
        ),
    )
    response_format: ResponseFormat = Field(
        default=ResponseFormat.MARKDOWN,
        description="'markdown' for human-readable output or 'json' for structured data.",
    )
    include_ext: list[str] = Field(
        default_factory=list,
        description="Limit to these file extensions (e.g. ['go', 'py']).",
    )
    exclude_ext: list[str] = Field(
        default_factory=list,
        description="Ignore these file extensions (e.g. ['json', 'lock']).",
    )
    exclude_dir: list[str] = Field(
        default_factory=list,
        description="Directories to exclude (e.g. ['vendor', 'node_modules']).",
    )

    def filter_args(self) -> list[str]:
        """Build scc CLI flags for the include/exclude filters."""
        args: list[str] = []
        if self.include_ext:
            args += ["--include-ext", ",".join(self.include_ext)]
        if self.exclude_ext:
            args += ["--exclude-ext", ",".join(self.exclude_ext)]
        if self.exclude_dir:
            args += ["--exclude-dir", ",".join(self.exclude_dir)]
        return args
