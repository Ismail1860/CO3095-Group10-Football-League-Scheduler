"""Ismail-2: Update team records after a result (owner: Ismail Mahomed).

Update both teams' table rows from one result, including forfeits and
overrides.
"""

from typing import List, Optional

from league.models import Team, Match, Result, PointsDeduction, TableRow


def update_team_records(
    home_row: Optional[TableRow],
    away_row: Optional[TableRow],
    result: Result,
    win_pts: int,
    draw_pts: int,
    loss_pts: int,
    previous_result: Optional[Result] = None,
) -> List[str]:
    """Ismail-2: Update team records after a result.

    User story:
        As the fixture secretary, I want each team's played, won, drawn, lost,
        goals and points updated when a result goes in (forfeits included), so
        that the table always matches the results.

    Acceptance criteria:
        1) Reject if the result's teams are not in the league.
        2) Home win: home gets win points, away gets loss points.
        3) Away win: away gets win points, home gets loss points.
        4) Draw: both get draw points.
        5) Forfeit: winner gets the forfeit score and win points, loser gets
           loss points.
        6) Both teams forfeit: both get 0 points and a loss.
        7) Result of an expunged team: ignore it.
        8) Override of a previous result: reverse the old result first.
        9) Update goals for, goals against and goal difference.
        10) Update the home/away split counters.

    Args:
        home_row: home team's row, or None if not in the league.
        away_row: away team's row, or None if not in the league.
        result: the result to apply.
        win_pts: points for a win.
        draw_pts: points for a draw.
        loss_pts: points for a loss.
        previous_result: result being overridden (AC8).

    Returns:
        [] when both rows are updated; otherwise the errors.
    """
    raise NotImplementedError


def rebuild_table(
    teams: List[Team],
    matches: List[Match],
    deductions: List[PointsDeduction],
    win_pts: int,
    draw_pts: int,
    loss_pts: int,
) -> List[TableRow]:
    """rebuild_table (Ismail-2 helper).

    Helper, not a user story function (exempt from the complexity rule).
    Rebuilds the table after a deduction, withdrawal, expunge or override
    (OQ-11). Owner: Ismail.

    Args:
        teams: all teams.
        matches: all matches.
        deductions: all deductions.
        win_pts: points for a win.
        draw_pts: points for a draw.
        loss_pts: points for a loss.

    Returns:
        A fresh table built from every PLAYED match, with active deductions
        applied.
    """
    raise NotImplementedError
