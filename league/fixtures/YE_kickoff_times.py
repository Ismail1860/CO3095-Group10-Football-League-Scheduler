"""Yousef-6: Set kick-off times (owner: Yousef Rwis).

Choose an allowed kick-off time for one match from the default slots, TV picks,
police rules and manual requests.
"""

from datetime import date, time
from typing import List, Optional, Tuple



def assign_kickoff(
    match_date: date,
    is_derby: bool,
    capacity: int,
    tv_slot: Optional[time],
    played_previous_sunday: bool,
    is_final_round: bool,
    ground_share_match_same_day: bool,
    manual_time: Optional[time] = None,
) -> Tuple[Optional[time], List[str]]:
    """Yousef-6: Set kick-off times.

    User story:
        As the fixture secretary, I want a kick-off time set for each match
        using the default slots, TV picks and the police rule on evening
        derbies, so that every fixture has a time that's actually allowed.

    Acceptance criteria:
        1) Saturday default is 15:00.
        2) Sunday default is 14:00.
        3) Midweek default is 19:45.
        4) Derbies cannot kick off after 18:00 (police safety rule).
        5) High-capacity stadiums (over 30,000) cannot host evening derbies.
        6) Matches picked for TV move to the broadcaster slot (uses Anay-3).
        7) A team cannot have a Sunday game followed by a Tuesday evening game.
        8) Ground-share stadiums cannot host two matches on the same day.
        9) Matches in the final round all kick off at the same time.
        10) Reject a manually supplied time outside 12:00-20:00.

    Note: an acceptance-criterion wording change is pending (OQ-21). Re-sync
    this docstring when docs/user_stories.csv is updated.

    Args:
        match_date: date of the match.
        is_derby: True if the pair is in league.derby_pairs.
        capacity: home stadium capacity.
        tv_slot: broadcaster slot if Anay-3 allowed a TV pick.
        played_previous_sunday: either team played the Sunday before (AC7).
        is_final_round: match is in the final round (AC9).
        ground_share_match_same_day: the shared stadium already hosts a match
            that day (AC8).
        manual_time: time requested by the fixture secretary.

    Returns:
        (kick-off time, []) when allowed; (None, errors) when no allowed time
        exists.
    """
    raise NotImplementedError
