"""Anay-8: Sort out cup clashes (owner: Anay Makan).

Postpone and rearrange league matches that clash with a cup round, and report
every match affected.
"""

from datetime import date
from typing import List, Tuple

from league.models import League, CupRound


def resolve_cup_clash(
    cup_round: CupRound,
    league: League,
    today: date,
) -> Tuple[List[str], List[str]]:
    """Anay-8: Sort out cup clashes.

    User story:
        As the fixture secretary, I want league games moved automatically when
        a team reaches a cup round on the same date, so that cup runs don't
        cause double-bookings.

    Acceptance criteria:
        1) Reject if the cup date is outside the season.
        2) No clash if neither team in the league match is in the cup that day.
        3) If one team is in the cup, postpone the league match (Anay-4, reason
           'cup').
        4) If both teams are in the cup, postpone and mark as high priority to
           rearrange.
        5) A cup replay creates a clash on the replay date as well.
        6) A cup final weekend postpones every league match involving the
           finalists.
        7) If the team is knocked out, cancel provisional postponements for
           later rounds.
        8) A postponed match created here goes straight into Anay-5 for a new
           date.
        9) If no new date exists, flag for administrator decision.
        10) Record the link between the cup round and the postponed league
            match.
        11) Report all league matches affected.

    Args:
        cup_round: the cup round causing the clash.
        league: the league (fixtures, season dates, stadiums, blackouts, cup
            rounds).
        today: date of the check.

    Returns:
        (IDs of league matches affected, errors).
    """
    raise NotImplementedError
