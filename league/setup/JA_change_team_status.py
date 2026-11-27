"""Jose-5: Change a team's status (owner: Jose Africa).

Move a team between ACTIVE, SUSPENDED and WITHDRAWN under the disciplinary
rules, log the change, and list the future fixtures affected.
"""

from datetime import date
from typing import List, Optional, Tuple

from league.models import League, Team


def change_team_status(
    league: League,
    team: Optional[Team],
    new_status: str,
    reason: Optional[str],
    end_date: Optional[date],
    today: date,
    confirmed: bool = False,
    override: bool = False,
) -> Tuple[List[str], List[str]]:
    """Jose-5: Change a team's status.

    User story:
        As a league admin, I want to move a team between active, suspended and
        withdrawn, so that disciplinary decisions are recorded properly and the
        affected fixtures are easy to find.

    Acceptance criteria:
        1) Reject an unknown status value.
        2) Reject a change to the same status.
        3) Active → suspended allowed only with a reason.
        4) Suspension must have an end date after today.
        5) Suspended → active allowed only on or after the suspension end date,
           unless overridden.
        6) Active or suspended → withdrawn requires administrator confirmation.
        7) Withdrawn is final: reject any change away from withdrawn.
        8) Before the season starts, withdrawing removes the team instead of
           marking it.
        9) Log every status change with date and reason.
        10) Return the list of future fixtures affected by the change.

    Args:
        league: the league (teams, fixtures, season start, log).
        team: the team, or None if not found.
        new_status: a TeamStatus value.
        reason: reason for the change (required for suspension).
        end_date: suspension end date.
        today: date of the change.
        confirmed: administrator confirmation for withdrawal (AC6).
        override: allow early return from suspension (AC5).

    Returns:
        (IDs of future matches affected, errors). Errors empty means the change
        was applied.
    """
    raise NotImplementedError
