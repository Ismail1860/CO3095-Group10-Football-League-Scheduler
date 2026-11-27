"""Yousef-9: Search and filter fixtures (owner: Yousef Rwis).

Return the fixtures matching the supplied filters, sorted, limited to 50, with
a truncation flag.
"""

from datetime import date
from typing import Dict, List, Optional, Tuple

from league.constants import VenueFilter
from league.models import Match


def filter_fixtures(
    fixtures: List[Match],
    team_names: Dict[str, str],
    total_rounds: int,
    team: Optional[str] = None,
    round_no: Optional[int] = None,
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    venue: str = VenueFilter.ANY,
    include_postponed: bool = False,
) -> Tuple[List[Match], bool, List[str]]:
    """Yousef-9: Search and filter fixtures.

    User story:
        As a supporter, I want to filter fixtures by team, round, date range
        and home or away, so that I can find the games I care about without
        scrolling through the whole list.

    Acceptance criteria:
        1) Reject an unknown team name.
        2) Reject a round number outside 1..total rounds.
        3) Reject a date range where start is after end.
        4) Reject a venue filter other than home/away/any.
        5) Venue filter without a team → reject (home/away needs a team).
        6) Apply each filter only if it was supplied.
        7) Exclude postponed matches unless include_postponed is set.
        8) Sort by date, then kick-off time, then home team.
        9) Return an empty list (not an error) when nothing matches.
        10) Limit results to 50 and report if truncated.

    Args:
        fixtures: all matches.
        team_names: team ID -> team name (AC1, AC8).
        total_rounds: number of rounds in the season (AC2).
        team: team name to filter on.
        round_no: round to filter on.
        date_from: first date to include.
        date_to: last date to include.
        venue: 'home', 'away' or 'any'.
        include_postponed: keep postponed matches (AC7).

    Returns:
        (matching matches, True if more than 50 matched, errors).
    """
    raise NotImplementedError
