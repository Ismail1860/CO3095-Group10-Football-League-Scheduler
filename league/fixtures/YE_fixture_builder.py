"""Fixture-generation helper (owner: Yousef Rwis).

Not a user story module; see generate_fixture_list.
"""

from datetime import date
from typing import List, Tuple

from league.models import League


def generate_fixture_list(
    league: League,
    today: date,
) -> Tuple[bool, List[str]]:
    """generate_fixture_list (Yousef helper).

    Helper, not a user story function (exempt from the complexity rule). Runs
    the fixture pipeline Yousef-1 -> Yousef-2 -> Yousef-3 -> Yousef-5 ->
    Yousef-4 -> Yousef-6 -> Yousef-7 and builds the Match objects (OQ-8).
    Reused by Yousef-8. Owner: Yousef.

    Args:
        league: the league to generate fixtures for.
        today: date of generation.

    Returns:
        (True, messages) when league.matches, league.byes and
        league.generated_team_ids are filled; (False, errors) otherwise.
    """
    raise NotImplementedError
