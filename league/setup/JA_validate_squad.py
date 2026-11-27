"""Jose-4: Check a squad against registration rules (owner: Jose Africa).

Check one team's squad against the league's registration rules and list every
failure with the player concerned.
"""

from datetime import date
from typing import List, Optional, Tuple

from league.models import Player


def validate_squad(
    players: List[Player],
    team_id: str,
    other_team_player_ids: List[str],
    registration_deadline: Optional[date],
    window_start: Optional[date],
    window_end: Optional[date],
    today: date,
) -> List[Tuple[str, Optional[str]]]:
    """Jose-4: Check a squad against registration rules.

    User story:
        As a team manager, I want my squad checked against the league's
        registration rules (squad size, goalkeepers, loans, shirt numbers), so
        that I know before the season whether my team is eligible.

    Acceptance criteria:
        1) Reject fewer than 18 registered players.
        2) Reject more than 25 registered players.
        3) Reject fewer than 2 goalkeepers.
        4) Reject more than 5 loan players.
        5) Reject duplicate shirt numbers.
        6) Reject shirt numbers outside 1-99.
        7) Reject any player under 16.
        8) Reject a player registered to another team in the same league.
        9) After the registration deadline, only allow changes during the
           transfer window.
        10) Return each failing rule with the player it applies to.

    Args:
        players: the squad being checked.
        team_id: the team the squad belongs to.
        other_team_player_ids: player IDs registered to other teams in the
            league.
        registration_deadline: league registration deadline.
        window_start: transfer window start.
        window_end: transfer window end.
        today: date of the check.

    Returns:
        Each failing rule as (message, player_id or None); empty list means the
        squad is valid (AC10).
    """
    raise NotImplementedError
