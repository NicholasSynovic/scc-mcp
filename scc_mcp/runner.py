"""scc invocation and path-safety helpers.

Implemented in a later commit. This module owns locating the external ``scc``
binary, validating that a target path is safe to scan, and running ``scc`` as a
subprocess with a timeout.
"""
