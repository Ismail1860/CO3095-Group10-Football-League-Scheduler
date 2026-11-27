"""Anay-3: Check TV slot rules (owner: Anay Makan).

Check a TV pick against the broadcast rules and, when allowed, move the match
and record its original slot.
"""

from datetime import date, time
from typing import List, Optional

from league.models import Match, CupRound, CheckResult


def check_tv_slot(
    match: Optional[Match],
    slot_date: date,
    slot_time: time,
    today: date,
    clubs_agree: bool,
    max_picks: int,
    min_picks: int,
    rounds_left: int,
    fixtures: List[Match],
    team_ids: List[str],
    cup_rounds: List[CupRound],
) -> CheckResult:
    """Anay-3: Check TV slot rules.

    User story:
        As the fixture secretary, I want a TV pick checked against the
        broadcast rules, including the Saturday 2:45 to 5:15pm blackout and the
        notice period, so that moves for TV follow league regulations.

    Acceptance criteria:
        1) Reject if the match does not exist.
        2) Reject a TV slot between 14:45 and 17:15 on a Saturday (UK
           blackout).
        3) Reject a pick made with less than 5 weeks' notice, unless both clubs
           agree.
        4) Reject if two TV matches share the same slot.
        5) Reject if a team exceeds its maximum TV picks per season.
        6) Warn if a team falls below its minimum TV picks with less than 10
           rounds left.
        7) Moving to a Sunday must still meet rest rules (uses Anay-2).
        8) Moving to a Friday is blocked for a team that played on the Tuesday
           before.
        9) Final-round matches cannot be moved for TV.
        10) Return ALLOWED, ALLOWED_WITH_WARNING or REJECTED with the reason.
        11) Record the original slot so the move can be undone.

    Args:
        match: the match, or None if not found.
        slot_date: broadcast date.
        slot_time: broadcast kick-off.
        today: date of the pick.
        clubs_agree: both clubs agree to short notice (AC3).
        max_picks: maximum TV picks per team per season.
        min_picks: minimum TV picks per team per season.
        rounds_left: rounds remaining in the season (AC6).
        fixtures: all matches (TV counts, final round, Tuesday games).
        team_ids: team IDs (for Anay-2).
        cup_rounds: cup rounds (for Anay-2).

    Returns:
        status ALLOWED, ALLOWED_WITH_WARNING or REJECTED with the reason
        (AC10).
    """
    raise NotImplementedError
