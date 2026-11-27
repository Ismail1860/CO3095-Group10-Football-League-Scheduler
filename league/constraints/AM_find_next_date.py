"""Anay-5: Find the next free date for a postponed match (owner: Anay Makan).

Suggest the earliest date that works for both teams and the venue for a
postponed match, explaining rejected candidates.
"""

from datetime import date
from typing import Dict, List, Optional, Tuple

from league.models import Stadium, Match, CupRound


def find_next_date(
    match: Match,
    fixtures: List[Match],
    stadium: Stadium,
    team_ids: List[str],
    cup_rounds: List[CupRound],
    today: date,
    deadline: date,
    blackout_dates: List[date],
    preferred_date: Optional[date] = None,
) -> Tuple[Optional[date], Dict[str, int], Optional[int], List[str]]:
    """Anay-5: Find the next free date for a postponed match.

    User story:
        As the fixture secretary, I want the system to suggest the earliest
        date that works for both teams and the venue, so that postponed games
        get rearranged quickly.

    Acceptance criteria:
        1) Reject if the match is not postponed.
        2) Search from tomorrow up to the rearrangement deadline.
        3) Skip blackout dates.
        4) Skip dates where either team plays (uses Anay-2).
        5) Skip dates with a venue clash (uses Anay-1).
        6) Prefer midweek dates over weekends.
        7) Skip dates that would give either team 3 consecutive home or away
           games.
        8) Skip dates after the second-last round (all postponed matches must
           finish before the final round).
        9) If the deadline is reached, report that no date is available.
        10) If both clubs proposed a preferred date and it is valid, return
            that first.
        11) Return the chosen date and how many candidates were rejected, and
            why.
        12) Report the number of days of notice the date gives.

    Args:
        match: the postponed match.
        fixtures: all matches.
        stadium: the match's stadium (for Anay-1).
        team_ids: team IDs (for Anay-2).
        cup_rounds: cup rounds (for Anay-2).
        today: search starts tomorrow.
        deadline: last date allowed for rearrangement.
        blackout_dates: dates with no football.
        preferred_date: date both clubs proposed (AC10).

    Returns:
        (chosen date or None, rejected candidates counted by reason, days of
        notice, errors).
    """
    raise NotImplementedError
