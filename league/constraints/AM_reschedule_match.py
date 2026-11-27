"""Anay-6: Reschedule a match (owner: Anay Makan).

Move a match to a new date after checking notice periods, agreements and the
venue and rest rules, and record the old date.
"""

from datetime import date
from typing import List, Tuple

from league.models import Stadium, Match, CupRound


def reschedule_match(
    match: Match,
    new_date: date,
    today: date,
    season_end: date,
    clubs_agree: bool,
    admin_override: bool,
    fixtures: List[Match],
    stadium: Stadium,
    team_ids: List[str],
    cup_rounds: List[CupRound],
) -> Tuple[List[str], bool, List[str]]:
    """Anay-6: Reschedule a match.

    User story:
        As the fixture secretary, I want to move a match to a new date, with
        checks for notice periods and the clubs' agreement, so that every
        rearrangement follows the rules.

    Acceptance criteria:
        1) Reject if the match is played or cancelled.
        2) Reject if the new date is the same as the current one.
        3) Reject a new date after the season end.
        4) Reject a new date with a venue clash (Anay-1).
        5) Reject a new date that breaks rest rules (Anay-2).
        6) Tuesday match with under 28 days' notice: allow only a 24-hour move
           to Wednesday.
        7) A move of more than 14 days requires both clubs' agreement.
        8) A move into the final round requires administrator override.
        9) Notify both clubs; if less than 7 days' notice, flag as
           SHORT_NOTICE.
        10) Update status from POSTPONED to SCHEDULED if it was postponed.
        11) Record the old date in the match history.

    Args:
        match: the match to move.
        new_date: requested date.
        today: date of the request.
        season_end: season end.
        clubs_agree: both clubs agree (AC7).
        admin_override: administrator override (AC8).
        fixtures: all matches.
        stadium: the match's stadium (for Anay-1).
        team_ids: team IDs (for Anay-2).
        cup_rounds: cup rounds (for Anay-2).

    Returns:
        (errors, True if SHORT_NOTICE, notification messages for both clubs).
    """
    raise NotImplementedError
