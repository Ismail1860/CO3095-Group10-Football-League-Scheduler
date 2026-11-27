"""Ismail-1: Record a match result (owner: Ismail Mahomed).

Validate and record the final score of a match, marking it PLAYED.
"""

from datetime import date
from typing import List, Optional, Tuple

from league.models import Match, Result


def record_result(
    match: Optional[Match],
    home_goals: int,
    away_goals: int,
    today: date,
    override: bool = False,
    reason: Optional[str] = None,
) -> Tuple[Optional[Result], List[str]]:
    """Ismail-1: Record a match result.

    User story:
        As the fixture secretary, I want to enter the final score of a match,
        so that the league table is built from accurate results.

    Acceptance criteria:
        1) Reject if the match does not exist.
        2) Reject a negative score.
        3) Reject a score over 30 (likely data entry error).
        4) Reject a result for a match dated in the future.
        5) Reject a result for a postponed or cancelled match.
        6) Reject a result for an abandoned match awaiting decision.
        7) If a result already exists, reject unless 'override' is set.
        8) An override requires a reason and is logged.
        9) Set status to PLAYED.
        10) Trigger a team record update (Ismail-2).

    Args:
        match: the match, or None if not found.
        home_goals: home score.
        away_goals: away score.
        today: date of entry.
        override: replace an existing result (AC7).
        reason: reason for the override (AC8).

    Returns:
        (new Result, []) when recorded; (None, errors) when rejected. For an
        accepted override the caller, which passed override=True, logs it
        (AC8).
    """
    raise NotImplementedError
