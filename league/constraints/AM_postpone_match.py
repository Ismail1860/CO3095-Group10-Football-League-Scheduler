"""Anay-4: Postpone a match (owner: Anay Makan).

Formally postpone a match with a valid reason, recording why and when, and flag
teams with many postponements.
"""

from datetime import date
from typing import Dict, List, Optional, Tuple

from league.models import Match


def postpone_match(
    match: Optional[Match],
    reason: str,
    note: Optional[str],
    requested_by: str,
    today: date,
    postponed_counts: Dict[str, int],
) -> Tuple[List[str], bool]:
    """Anay-4: Postpone a match.

    User story:
        As the fixture secretary, I want to postpone a match and record why
        (weather, pitch, cup, international duty and so on), so that games that
        can't go ahead are handled formally rather than just disappearing.

    Acceptance criteria:
        1) Reject if the match does not exist.
        2) Reject if the match is already played.
        3) Reject if the match is already postponed.
        4) Reject if the match is in progress.
        5) Reason must be one of weather, pitch, cup, international, safety,
           other.
        6) Reason 'other' requires a free-text explanation.
        7) Cup or international postponements require at least 7 days' notice.
        8) A club cannot postpone its own match: the request must come from the
           league administrator.
        9) If a team already has 3 or more postponed matches, flag for review.
        10) Set status to POSTPONED and record reason and date.

    Args:
        match: the match, or None if not found.
        reason: a PostponementReason value.
        note: free-text explanation (required for 'other').
        requested_by: ADMIN or the requesting team's ID.
        today: date of the request.
        postponed_counts: team ID -> matches already postponed (AC9).

    Returns:
        (errors, flagged for review). Errors empty means the match is now
        POSTPONED.
    """
    raise NotImplementedError
