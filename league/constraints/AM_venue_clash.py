"""Anay-1: Check a venue for clashes (owner: Anay Makan).

Check whether a stadium is free for a match on a proposed date, listing every
conflict found.
"""

from datetime import date, time
from typing import List, Optional

from league.models import Stadium, Match, CheckResult


def check_venue_clash(
    match: Optional[Match],
    proposed_date: date,
    proposed_kickoff: Optional[time],
    stadium: Optional[Stadium],
    fixtures: List[Match],
) -> CheckResult:
    """Anay-1: Check a venue for clashes.

    User story:
        As the fixture secretary, I want to know if a stadium is already booked
        or unavailable on a given date, so that a ground is never
        double-booked.

    Acceptance criteria:
        1) Reject if the match or stadium does not exist.
        2) Clash if the same stadium hosts another match that day.
        3) Clash if the stadium is marked unavailable that day.
        4) Clash if a ground-share partner is at home that day.
        5) For ground shares, allow back-to-back days only if at least 24 hours
           apart.
        6) Ignore postponed or cancelled matches when checking.
        7) Ignore the match being checked (rescheduling the same match).
        8) Warn (not clash) for a non-football event within 24 hours.
        9) Return NO_CLASH, WARNING or CLASH with the conflicting item.
        10) Check all stadium rules before returning, so every conflict is
            listed.

    Args:
        match: the match being placed, or None if not found.
        proposed_date: date being checked.
        proposed_kickoff: kick-off being checked (AC5).
        stadium: the stadium, or None if not found.
        fixtures: all league matches.

    Returns:
        status NO_CLASH, WARNING or CLASH; messages name each conflicting match
        or date (AC9-10).
    """
    raise NotImplementedError
