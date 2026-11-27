"""Yousef-8: Regenerate fixtures after a pre-season change (owner: Yousef Rwis).

Rebuild the fixtures after a team joins or leaves before the season starts,
restoring the old list if the new one is invalid.
"""

from datetime import date
from typing import List, Tuple

from league.models import League


def regenerate_fixtures(
    league: League,
    today: date,
    reason: str,
) -> Tuple[bool, List[str]]:
    """Yousef-8: Regenerate fixtures after a pre-season change.

    User story:
        As the fixture secretary, I want to rebuild the fixtures if a team
        joins or drops out before the season starts, so that the schedule
        always matches who is actually in the league.

    Acceptance criteria:
        1) Reject if the season has started.
        2) Reject if no team change happened since the last generation.
        3) If a team was added and the count becomes odd, add a bye.
        4) If a team was removed and the count becomes even, remove the bye.
        5) Keep existing round dates where the round count is unchanged.
        6) If the round count changes, re-run date assignment (Yousef-4).
        7) Keep derby pairs that are still valid, drop pairs with removed
           teams.
        8) Re-run validation (Yousef-7).
        9) If validation fails, restore the previous fixture list.
        10) Log the regeneration with the reason.

    Args:
        league: the league (teams, fixtures, byes, derby pairs,
            generated_team_ids).
        today: date of the request.
        reason: reason recorded in the log (AC10).

    Returns:
        (True, messages) when new fixtures are in place; (False, errors) when
        rejected or restored.
    """
    raise NotImplementedError
