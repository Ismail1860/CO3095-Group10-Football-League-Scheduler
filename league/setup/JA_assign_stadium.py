"""Jose-3: Assign a stadium (including ground shares) (owner: Jose Africa).

Give a team a home stadium, handling ground shares (max two tenants) and
releasing the team's previous stadium.
"""

from typing import List, Optional

from league.models import League, Team, Stadium


def assign_stadium(
    league: League,
    team: Optional[Team],
    stadium: Optional[Stadium],
    force: bool = False,
) -> List[str]:
    """Jose-3: Assign a stadium (including ground shares).

    User story:
        As a league admin, I want to give each team a home stadium and allow
        two teams to share one, so that we never end up with two home games at
        the same ground on the same day.

    Acceptance criteria:
        1) Reject if the stadium does not exist.
        2) Reject if the team does not exist.
        3) Allow immediately if the stadium has no current tenant.
        4) Reject if the stadium already has 2 tenants (max ground share).
        5) Reject if the tenant team is withdrawn (ground share must be with an
           active team).
        6) Reject if capacity is below the league minimum.
        7) Reject if the stadium's unavailable dates cover more than 25% of the
           season.
        8) Mark both teams as ground-share partners when a second tenant is
           added.
        9) Reject re-assigning a team to the stadium it already uses.
        10) If the team had a previous stadium, release it and update that
            stadium's tenant list.
        11) Block the change after fixtures are generated unless forced by an
            administrator.

    Args:
        league: the league (min capacity, season dates, teams, fixtures).
        team: the team, or None if it does not exist.
        stadium: the stadium, or None if it does not exist.
        force: administrator override after fixtures exist (AC11).

    Returns:
        [] when assigned; otherwise the error messages.
    """
    raise NotImplementedError
