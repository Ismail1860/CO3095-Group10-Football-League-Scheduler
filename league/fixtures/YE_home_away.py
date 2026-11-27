"""Yousef-2: Balance home and away games (owner: Yousef Rwis).

Decide home and away for every pairing so no team has three in a row at home or
away, respecting ground shares, and count breaks.
"""

from typing import Dict, List, Optional, Tuple



def assign_home_away(
    rounds: List[List[Tuple[str, str]]],
    byes: List[Optional[str]],
    ground_share_pairs: List[Tuple[str, str]],
) -> Tuple[List[List[Tuple[str, str]]], Dict[str, int], List[str]]:
    """Yousef-2: Balance home and away games.

    User story:
        As the fixture secretary, I want home and away games spread evenly for
        each team, with no more than two in a row at home or away, so that no
        club gets a lopsided run.

    Acceptance criteria:
        1) Alternate home/away for each team where possible.
        2) A 'break' is two consecutive home or two consecutive away games.
        3) Reject any assignment creating 3 consecutive home games.
        4) Reject any assignment creating 3 consecutive away games.
        5) Ground-share partners must not both be at home in the same round.
        6) A team's first and last match must not both be away.
        7) A team's first two matches must not both be home or both be away.
        8) A team with a bye keeps its home/away pattern after the bye.
        9) If no valid assignment exists for a round, flip the fixed team's
           venue and retry once.
        10) If still invalid, report the round and team that could not be
            satisfied.
        11) Return the number of breaks per team.

    Args:
        rounds: rounds from generate_pairings.
        byes: bye team per round.
        ground_share_pairs: teams sharing a stadium.

    Returns:
        (rounds with (home, away) order fixed, number of breaks per team,
        errors naming the round and team that failed).
    """
    raise NotImplementedError
