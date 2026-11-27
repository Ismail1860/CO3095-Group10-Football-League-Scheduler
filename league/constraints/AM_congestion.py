"""Anay-7: Warn about fixture congestion (owner: Anay Makan).

Find a team's most congested rolling window of matches and warn when it exceeds
the limit.
"""

from datetime import date
from typing import Dict, List, Optional, Tuple

from league.models import Match, CupRound, CheckResult


def check_congestion(
    team_id: str,
    team_ids: List[str],
    fixtures: List[Match],
    cup_rounds: List[CupRound],
    away_miles: Dict[str, float],
    window_days: int,
    limit: int,
) -> Tuple[CheckResult, Optional[date], Optional[date]]:
    """Anay-7: Warn about fixture congestion.

    User story:
        As a team manager, I want a warning when my team has too many games
        packed into a short period, so that we can ask for a rearrangement
        early.

    Acceptance criteria:
        1) Reject an unknown team.
        2) Reject a window of 0 days or less.
        3) Count matches (league + cup) inside the rolling window.
        4) OK if the count is at or under the limit.
        5) WARNING if the count is 1 over the limit.
        6) CRITICAL if the count is 2 or more over the limit.
        7) Count postponed matches only if they already have a new date.
        8) Escalate one level if the window includes 2 away games over 200
           miles (travel).
        9) Escalate one level if the window ends in the final 3 rounds.
        10) Return the worst window found and its dates.

    Args:
        team_id: team to check.
        team_ids: known team IDs (AC1).
        fixtures: all league matches.
        cup_rounds: cup rounds (AC3).
        away_miles: match ID -> travel miles for the away team (AC8).
        window_days: length of the rolling window.
        limit: maximum matches allowed in the window.

    Returns:
        (status OK, WARNING or CRITICAL with messages, worst window start,
        worst window end).
    """
    raise NotImplementedError
