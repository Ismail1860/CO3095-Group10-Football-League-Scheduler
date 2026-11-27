"""Yousef-7: Validate the fixture list (owner: Yousef Rwis).

Check a complete fixture list for mistakes before publication and return one
verdict with every message.
"""

from datetime import date
from typing import List, Tuple

from league.constants import DERBY_MIN_GAP_DEFAULT
from league.models import Match, CheckResult


def validate_fixtures(
    fixtures: List[Match],
    team_ids: List[str],
    fmt: str,
    season_start: date,
    season_end: date,
    byes: List[Tuple[int, str]],
    derby_pairs: List[Tuple[str, str]],
    min_gap: int = DERBY_MIN_GAP_DEFAULT,
) -> CheckResult:
    """Yousef-7: Validate the fixture list.

    User story:
        As the fixture secretary, I want the full fixture list checked for
        mistakes (a team playing twice in a round, wrong number of meetings,
        clashing venues), so that we never publish a broken schedule.

    Acceptance criteria:
        1) Fail if any pair meets the wrong number of times for the format.
        2) Fail if a team appears twice in the same round.
        3) Fail if a team plays itself.
        4) Fail if home/away counts per team differ by more than 1.
        5) Fail if any team has 3 consecutive home or away games.
        6) Fail if a round has no date.
        7) Fail if the same stadium hosts two matches on one date.
        8) Warn if a team has more than one bye.
        9) Warn if derby spacing rules are broken.
        10) Warn if any match is outside the season dates.
        11) Return VALID, VALID_WITH_WARNINGS or INVALID with all messages.

    Note: an acceptance-criterion wording change is pending (OQ-22). Re-sync
    this docstring when docs/user_stories.csv is updated.

    Args:
        fixtures: every league match.
        team_ids: active team IDs.
        fmt: a LeagueFormat value.
        season_start: season start.
        season_end: season end.
        byes: (round_no, team_id) byes (AC8).
        derby_pairs: derby pairs (AC9).
        min_gap: derby leg spacing (AC9).

    Returns:
        status VALID, VALID_WITH_WARNINGS or INVALID with all messages (AC11).
    """
    raise NotImplementedError
