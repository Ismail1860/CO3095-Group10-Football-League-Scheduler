"""Ismail-7: Show a team's form and streaks (owner: Ismail Mahomed).

Summarise a team's recent results and its current winning, unbeaten and winless
streaks.
"""

from typing import List, Optional, Tuple

from league.constants import FORM_LENGTH_DEFAULT, VenueFilter
from league.models import Match, FormSummary


def get_form(
    team_id: str,
    team_ids: List[str],
    matches: List[Match],
    win_pts: int,
    draw_pts: int,
    length: int = FORM_LENGTH_DEFAULT,
    venue: str = VenueFilter.ALL_VENUES,
) -> Tuple[Optional[FormSummary], List[str]]:
    """Ismail-7: Show a team's form and streaks.

    User story:
        As a supporter, I want to see a team's last few results and its current
        winning, unbeaten or winless run, so that I can tell how they're
        playing at the moment.

    Acceptance criteria:
        1) Reject an unknown team.
        2) Reject a form length outside 1-10 (default 5).
        3) If no matches are played, return 'no form'.
        4) If fewer matches than the form length, use all played matches and
           flag it.
        5) Map each result to W, D or L from this team's point of view.
        6) A forfeit win counts as W, a forfeit loss as L.
        7) Track the current winning streak.
        8) Track the current unbeaten streak (wins and draws).
        9) Track the current winless streak.
        10) Filter by home only, away only or all.
        11) Flag 'in form' if 2.0 or more points per game over the window,
            'poor form' if under 1.0.

    Args:
        team_id: team to summarise.
        team_ids: known team IDs (AC1).
        matches: all matches.
        win_pts: points for a win (AC11 points per game).
        draw_pts: points for a draw (AC11).
        length: number of recent matches (1-10).
        venue: 'home', 'away' or 'all'.

    Returns:
        (FormSummary, []) on success; (None, errors) on rejection.
    """
    raise NotImplementedError
