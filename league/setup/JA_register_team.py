"""Jose-2: Register a team (owner: Jose Africa).

Add a validated team to the league, creating its home stadium when the stadium
name is new.
"""

from typing import List, Optional, Tuple

from league.models import League, Team


def register_team(
    league: Optional[League],
    name: str,
    short_code: str,
    stadium_name: str,
    capacity: int,
) -> Tuple[Optional[Team], List[str], List[str]]:
    """Jose-2: Register a team.

    User story:
        As a league admin, I want to add a team to the league with its name,
        short code and home ground, so that only valid teams with unique names
        end up in the competition.

    Acceptance criteria:
        1) Reject if the league does not exist.
        2) Reject if fixtures have already been generated (registration
           closed).
        3) Reject if the league is already full.
        4) Reject a duplicate team name (case-insensitive).
        5) Short code must be exactly 3 letters, else reject.
        6) Reject a duplicate short code.
        7) Reject if no home stadium is given.
        8) Reject if stadium capacity is below the league minimum.
        9) Flag (warn, not reject) if the team's stadium is already used by
           another team.

    Args:
        league: the league, or None if it does not exist.
        name: team name.
        short_code: three-letter code.
        stadium_name: home stadium name; empty means none given.
        capacity: stadium capacity (used when the stadium is new).

    Returns:
        (Team, [], warnings) on success; (None, errors, []) on rejection. AC9
        produces a warning, not an error.
    """
    raise NotImplementedError
