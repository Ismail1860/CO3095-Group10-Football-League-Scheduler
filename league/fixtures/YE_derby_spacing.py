"""Yousef-5: Spread out the derbies (owner: Yousef Rwis).

Keep derbies off the first and last rounds and spaced apart by swapping whole
rounds, reporting derbies that cannot be placed.
"""

from typing import List, Optional, Tuple

from league.constants import DERBY_MIN_GAP_DEFAULT


def space_derbies(
    rounds: List[List[Tuple[str, str]]],
    byes: List[Optional[str]],
    derby_pairs: List[Tuple[str, str]],
    team_ids: List[str],
    min_gap: int = DERBY_MIN_GAP_DEFAULT,
) -> Tuple[List[List[Tuple[str, str]]], List[Optional[str]], List[Tuple[str, str]], List[str]]:
    """Yousef-5: Spread out the derbies.

    User story:
        As the fixture secretary, I want derby matches kept off the first and
        last rounds and spaced apart, so that rivalry games aren't bunched
        together.

    Acceptance criteria:
        1) Skip if no derby pairs are defined.
        2) Reject a derby pair containing an unknown team.
        3) A derby must not be in round 1.
        4) A derby must not be in the final round.
        5) The two legs of a derby must be at least N rounds apart
           (configurable, default 6).
        6) A team must not play derbies in consecutive rounds.
        7) No more than 2 derbies in the same round.
        8) Fix a violation by swapping whole rounds, never individual matches.
        9) Re-check home/away break rules after any swap.
        10) Report derbies that could not be placed.

    Args:
        rounds: all rounds (both halves).
        byes: bye per round (moves with its round).
        derby_pairs: derby pairs.
        team_ids: known team IDs (AC2).
        min_gap: minimum rounds between the two legs (AC5).

    Returns:
        (reordered rounds, matching byes, derbies that could not be placed,
        errors).
    """
    raise NotImplementedError
