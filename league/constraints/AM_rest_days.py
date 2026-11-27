"""Anay-2: Check rest days between matches (owner: Anay Makan).

Check that both teams get enough rest before and after a proposed match,
reporting each team separately.
"""

from datetime import date, time
from typing import Dict, List, Optional

from league.models import Match, CupRound, CheckResult


def check_rest_days(
    home_id: str,
    away_id: str,
    team_ids: List[str],
    proposed_date: date,
    kickoff: time,
    fixtures: List[Match],
    cup_rounds: List[CupRound],
    exclude_match_id: Optional[str] = None,
) -> Dict[str, CheckResult]:
    """Anay-2: Check rest days between matches.

    User story:
        As the fixture secretary, I want to check that both teams get at least
        48 hours between games (more after an evening kick-off), so that
        players get fair recovery time.

    Acceptance criteria:
        1) Reject if either team does not exist.
        2) Find each team's nearest match before and after the proposed date.
        3) Fail if any gap is under 48 hours.
        4) Fail if the gap is under 72 hours after an evening (19:45) kick-off.
        5) Warn if the gap is under 72 hours otherwise.
        6) Fail if a team has a cup match within 48 hours.
        7) Ignore postponed or cancelled matches.
        8) Check both teams and report each team separately.
        9) If no previous or next match exists, treat that side as OK.

    Args:
        home_id: home team ID.
        away_id: away team ID.
        team_ids: known team IDs (AC1).
        proposed_date: proposed match date.
        kickoff: proposed kick-off.
        fixtures: all league matches.
        cup_rounds: cup rounds (AC6).
        exclude_match_id: match being moved, ignored when searching (suggested,
            not in the acceptance criteria).

    Returns:
        team ID -> CheckResult with status OK, WARNING or FAIL. If a team is
        unknown, the dict holds that ID with FAIL and the reason.
    """
    raise NotImplementedError
