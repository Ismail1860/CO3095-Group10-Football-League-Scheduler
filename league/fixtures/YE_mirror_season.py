"""Yousef-3: Mirror the second half of the season (owner: Yousef Rwis).

Build the second half of a double round-robin by reversing home and away from
the first half, fixing any streak or ground-share problems.
"""

from typing import List, Optional, Tuple



def mirror_second_half(
    first_half: List[List[Tuple[str, str]]],
    byes: List[Optional[str]],
    fmt: str,
    ground_share_pairs: List[Tuple[str, str]],
) -> Tuple[List[List[Tuple[str, str]]], List[Optional[str]], List[str]]:
    """Yousef-3: Mirror the second half of the season.

    User story:
        As the fixture secretary, I want the second half of a double
        round-robin to reverse the home and away teams from the first half, so
        that every team hosts every opponent once.

    Acceptance criteria:
        1) Reject if format is single (no second half).
        2) Reject if the first half is incomplete.
        3) Reverse home/away for every first-half match.
        4) Keep byes in the same relative round.
        5) If mirroring creates 3 consecutive home or away games, swap with the
           next round.
        6) If mirroring makes ground-share partners both at home, swap with the
           next round.
        7) If no swap fixes it, report the conflict.
        8) The same pair must not meet in the last round of the first half and
           the first round of the second half.
        9) Check each pair meets exactly twice, once at each ground.

    Args:
        first_half: first-half rounds with home/away set.
        byes: first-half bye per round.
        fmt: a LeagueFormat value.
        ground_share_pairs: teams sharing a stadium.

    Returns:
        (second-half rounds, second-half byes, errors or reported conflicts).
    """
    raise NotImplementedError
