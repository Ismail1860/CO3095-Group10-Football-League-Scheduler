"""Ismail-9: Has the title or relegation been decided? (owner: Ismail Mahomed).

Decide whether a team has mathematically won the title, been relegated or is
safe, and how many points it needs.
"""

from typing import Dict, List, Optional, Tuple

from league.models import TableRow


def check_clinched(
    team_id: str,
    sorted_rows: List[TableRow],
    games_left: Dict[str, int],
    win_pts: int,
    relegation_places: int,
    target: str,
) -> Tuple[Optional[str], int, List[str]]:
    """Ismail-9: Has the title or relegation been decided?.

    User story:
        As a supporter, I want to know when a team has mathematically won the
        league or been relegated, so that it can be confirmed as soon as nobody
        can catch them.

    Acceptance criteria:
        1) Reject an unknown team.
        2) Max possible points = current points + games left × points for a
           win.
        3) CHAMPION if the leader's points exceed every other team's maximum.
        4) If the leader's points equal a rival's maximum, CHAMPION only if the
           rival can't overtake on goal difference this season.
        5) Otherwise NOT_DECIDED for the title.
        6) RELEGATED if the team's maximum is below the points of the team just
           above the relegation zone.
        7) If the team's maximum equals that team's points, decide on goal
           difference as above.
        8) SAFE if the team's points exceed the maximum of every team in the
           relegation zone.
        9) Point deductions are included in current points.
        10) Withdrawn teams are excluded.
        11) If any matches are postponed with no date, still count them as
            games left.
        12) Return status and the number of points needed to secure the
            outcome.

    Note: an acceptance-criterion wording change is pending (OQ-26). Re-sync
    this docstring when docs/user_stories.csv is updated.

    Args:
        team_id: team being checked.
        sorted_rows: current table in order.
        games_left: team ID -> games left, including undated postponements
            (AC11).
        win_pts: points for a win (AC2).
        relegation_places: size of the relegation zone.
        target: ClinchTarget.TITLE or ClinchTarget.RELEGATION.

    Returns:
        (ClinchStatus value, points needed to secure the outcome, errors).
    """
    raise NotImplementedError
