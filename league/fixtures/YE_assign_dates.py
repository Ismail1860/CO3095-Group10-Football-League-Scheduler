"""Yousef-4: Put dates on each round (owner: Yousef Rwis).

Give every round a date, mainly Saturdays, skipping blackouts and adding
Tuesday rounds when the calendar is tight.
"""

from datetime import date
from typing import Dict, List, Optional, Tuple



def assign_round_dates(
    num_rounds: int,
    start_date: Optional[date],
    end_date: Optional[date],
    blackout_dates: List[date],
    stadium_unavailable: Dict[str, List[date]],
) -> Tuple[List[date], List[str], List[str]]:
    """Yousef-4: Put dates on each round.

    User story:
        As the fixture secretary, I want each round given a date, mainly
        Saturdays, skipping international breaks and adding midweek rounds if
        the calendar is tight, so that the whole season fits between the start
        and end dates.

    Acceptance criteria:
        1) Reject if season dates are missing.
        2) Default to Saturdays.
        3) Skip blackout dates (international breaks, Christmas Day).
        4) If a Saturday is a blackout, try the Sunday of the same weekend.
        5) If there aren't enough weekends, insert midweek (Tuesday) rounds.
        6) A midweek round must be at least 3 days from the weekend rounds
           either side.
        7) No more than 2 midweek rounds in any 4-week period.
        8) If rounds still don't fit, fail with the number of missing dates.
        9) The last round of the season is always on a weekend.
        10) If any team's stadium is unavailable on the round date, flag it for
            Anay-1.
        11) Return the date for every round.

    Args:
        num_rounds: number of rounds to date.
        start_date: season start.
        end_date: season end.
        blackout_dates: dates with no football.
        stadium_unavailable: team ID -> dates its stadium is unavailable
            (AC10).

    Returns:
        (one date per round, flags for Anay-1 about unavailable stadiums,
        errors including the number of missing dates).
    """
    raise NotImplementedError
