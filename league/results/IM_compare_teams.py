"""Ismail-3: Compare two teams with the tie-breakers (owner: Ismail Mahomed).

Compare two table rows using the Premier League tie-breakers, for use as a sort
comparator.
"""


from league.models import TableRow


def compare_teams(
    row_a: TableRow,
    row_b: TableRow,
    h2h_points_a: int,
    h2h_points_b: int,
    h2h_away_goals_a: int,
    h2h_away_goals_b: int,
    h2h_complete: bool,
    decides_place: bool,
) -> int:
    """Ismail-3: Compare two teams with the tie-breakers.

    User story:
        As a supporter, I want teams on the same points separated by goal
        difference, then goals scored, then head-to-head, so that league
        positions are decided the way the Premier League does it.

    Acceptance criteria:
        1) Higher points ranks first.
        2) If points are equal, higher goal difference ranks first.
        3) If still equal, more goals scored ranks first.
        4) If still equal, more head-to-head points ranks first.
        5) If still equal, more away goals in head-to-head matches ranks first.
        6) If still equal and the position decides the title, promotion or
           relegation, flag a play-off.
        7) Otherwise order alphabetically.
        8) Withdrawn teams are always ranked last.
        9) A team with expunged results compares on its remaining results.
        10) If head-to-head matches are not all played, skip the head-to-head
            criteria.
        11) Return -1, 0 or 1 (for use as a sort comparator).

    Args:
        row_a: first team's row.
        row_b: second team's row.
        h2h_points_a: head-to-head points of team A.
        h2h_points_b: head-to-head points of team B.
        h2h_away_goals_a: head-to-head away goals of team A.
        h2h_away_goals_b: head-to-head away goals of team B.
        h2h_complete: all head-to-head matches played (AC10).
        decides_place: the position decides title, promotion or relegation
            (AC6).

    Returns:
        -1 if A ranks above B, 1 if B ranks above A, 0 only when a play-off is
        needed (AC6, AC11).
    """
    raise NotImplementedError
