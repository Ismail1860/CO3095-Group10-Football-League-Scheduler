"""Jose-9: Save and load the league from a file (owner: Jose Africa).

Load a league from, and save it to, a JSON file with clear errors, never
damaging the previous file.
"""

from typing import List, Optional, Tuple

from league.models import League


def load_league(
    path: str,
) -> Tuple[Optional[League], List[str]]:
    """Jose-9: Save and load the league from a file.

    User story:
        As a league admin, I want the league saved to and loaded from a JSON
        file with clear error messages, so that nothing is lost between
        sessions and a corrupt file doesn't wipe our data.

    Acceptance criteria:
        1) File not found → clear error.
        2) Empty file → clear error.
        3) Invalid JSON → clear error.
        4) Missing required top-level section → name the section.
        5) File version newer than supported → reject.
        6) File version older → migrate known fields.
        7) Duplicate team IDs in file → reject.
        8) Fixture referencing an unknown team → reject.
        9) Result recorded for a fixture that does not exist → reject.
        10) On save, write to a temporary file first and replace only on
            success.
        11) On save failure, keep the previous file intact and report the
            error.

    Args:
        path: path of the JSON file.

    Returns:
        (League, []) when the file is valid; (None, errors) otherwise (AC1-9).
    """
    raise NotImplementedError


def save_league(
    league: League,
    path: str,
) -> List[str]:
    """Jose-9: Save and load the league from a file.

    User story:
        As a league admin, I want the league saved to and loaded from a JSON
        file with clear error messages, so that nothing is lost between
        sessions and a corrupt file doesn't wipe our data.

    Acceptance criteria:
        1) File not found → clear error.
        2) Empty file → clear error.
        3) Invalid JSON → clear error.
        4) Missing required top-level section → name the section.
        5) File version newer than supported → reject.
        6) File version older → migrate known fields.
        7) Duplicate team IDs in file → reject.
        8) Fixture referencing an unknown team → reject.
        9) Result recorded for a fixture that does not exist → reject.
        10) On save, write to a temporary file first and replace only on
            success.
        11) On save failure, keep the previous file intact and report the
            error.

    Note: this is the story's second function; the main function for the
    complexity rule is the other one in this module.

    Args:
        league: the league to save.
        path: destination path.

    Returns:
        [] when saved; otherwise the error, with the previous file left intact
        (AC10-11).
    """
    raise NotImplementedError
