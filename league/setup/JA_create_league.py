"""Jose-1: Create a league (owner: Jose Africa).

Validate the settings for a new league and build the League if every rule
passes, reporting all failures at once.
"""

from datetime import date
from typing import List, Optional, Tuple

from league.models import League


def create_league(
    name: str,
    team_count: int,
    start_date: Optional[date],
    end_date: Optional[date],
    fmt: str,
    win_pts: int,
    draw_pts: int,
    loss_pts: int,
    existing_names: List[str],
) -> Tuple[Optional[League], List[str]]:
    """Jose-1: Create a league.

    User story:
        As a league admin, I want to set up a new league with its season dates,
        format and points system, so that everything is configured before teams
        start registering.

    Acceptance criteria:
        1) Reject empty or whitespace-only league name.
        2) Reject a name already used by another league.
        3) Reject team count below 4.
        4) Reject team count above 24.
        5) Reject season end date on or before start date.
        6) Reject a season shorter than the minimum weeks needed for the
           format.
        7) Format must be 'single' or 'double' round-robin, else reject.
        8) Points for a win must be greater than points for a draw, else
           reject.
        9) Points for a loss must be 0 or less than points for a draw, else
           reject.
        10) Return a list of all validation errors rather than stopping at the
            first.

    Args:
        name: proposed league name.
        team_count: number of teams the league will hold.
        start_date: season start date.
        end_date: season end date.
        fmt: LeagueFormat.SINGLE or LeagueFormat.DOUBLE.
        win_pts: points for a win.
        draw_pts: points for a draw.
        loss_pts: points for a loss.
        existing_names: names of leagues already saved in data/.

    Returns:
        (League, []) when valid; (None, every error message) when not (AC10).
    """
    raise NotImplementedError
