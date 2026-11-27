"""Jose-8: Edit league settings once the season is set up (owner: Jose Africa).

Change one league setting, refusing changes that are locked once fixtures,
results or the season have started, and log accepted changes.
"""

from datetime import date
from typing import List

from league.models import League


def edit_league_setting(
    league: League,
    setting: str,
    value: object,
    today: date,
    existing_names: List[str],
) -> List[str]:
    """Jose-8: Edit league settings once the season is set up.

    User story:
        As a league admin, I want to change league settings, but with some of
        them locked once fixtures or results exist, so that a late change can't
        break the schedule or the table.

    Acceptance criteria:
        1) Reject an unknown setting name.
        2) Name change allowed at any time but must stay unique.
        3) Team count change blocked once fixtures exist.
        4) Format change blocked once fixtures exist.
        5) Points system change blocked once the first result is recorded.
        6) Start date change blocked once the season has started.
        7) End date can be extended but not moved before the last scheduled
           fixture.
        8) Zone sizes (promotion/relegation) cannot exceed half the team count.
        9) Zone size change blocked in the final 5 rounds.
        10) Every accepted change is logged with old and new value.

    Args:
        league: the league.
        setting: a Setting name.
        value: the new value (str, int or date depending on the setting).
        today: date of the change.
        existing_names: names of other saved leagues (AC2).

    Returns:
        [] when the change is applied and logged; otherwise the errors.
    """
    raise NotImplementedError
