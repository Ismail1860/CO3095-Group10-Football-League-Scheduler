"""Ismail-6: Show promotion, play-off and relegation zones (owner: Ismail Mahomed).

Label every place in a sorted table as champion, promotion or qualification,
play-off, safe or relegation.
"""

from typing import List, Tuple

from league.models import TableRow


def assign_zones(
    sorted_rows: List[TableRow],
    promotion: int,
    playoff: int,
    relegation: int,
    top_division: bool,
) -> Tuple[List[Tuple[int, str, str]], List[str]]:
    """Ismail-6: Show promotion, play-off and relegation zones.

    User story:
        As a supporter, I want each place in the table labelled as promotion,
        play-off, safe or relegation, so that I can see what each team is
        playing for.

    Acceptance criteria:
        1) Reject if zone sizes overlap or exceed the number of teams.
        2) Positions 1..automatic promotion → PROMOTION.
        3) Next play-off positions → PLAYOFF.
        4) Bottom relegation positions → RELEGATION.
        5) Everyone else → SAFE.
        6) If promotion size is 0, the top position is CHAMPION only.
        7) Withdrawn teams count as relegated and the relegation zone shrinks
           by one.
        8) If the league is top division, promotion zones become
           'qualification' zones.
        9) A team with a points deduction can move zone: recalculated each
           time.
        10) Return position, team and zone for every team.

    Args:
        sorted_rows: table rows in final order.
        promotion: automatic promotion places.
        playoff: play-off places.
        relegation: relegation places.
        top_division: league is the top division (AC8).

    Returns:
        ((position, team ID, Zone value) for every team, errors).
    """
    raise NotImplementedError
