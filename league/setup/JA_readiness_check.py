"""Jose-6: Readiness check before generating fixtures (owner: Jose Africa).

Report whether the league is ready for fixture generation, listing every
failure and warning.
"""

from datetime import date

from league.models import League, CheckResult


def check_readiness(
    league: League,
    today: date,
) -> CheckResult:
    """Jose-6: Readiness check before generating fixtures.

    User story:
        As the fixture secretary, I want a readiness report on the league
        before I generate fixtures, so that the generator never runs on missing
        stadiums, bad squads or impossible dates.

    Acceptance criteria:
        1) Fail if the league has fewer than 4 active teams.
        2) Warn if the team count is odd (a bye will be needed).
        3) Fail if any active team has no stadium.
        4) Fail if any team's squad is invalid (uses Jose-4).
        5) Fail if fixtures already exist.
        6) Fail if season dates are missing or invalid.
        7) Fail if the number of available weekends is less than the number of
           rounds.
        8) Warn if there are ground-share pairs (constraint for Yousef-2).
        9) Warn if no derby pairs are defined.
        10) Warn if any stadium has unavailable dates inside the season.
        11) Return status READY, READY_WITH_WARNINGS or NOT_READY with all
            messages.

    Args:
        league: the league to check.
        today: date of the check (needed by Jose-4).

    Returns:
        status READY, READY_WITH_WARNINGS or NOT_READY with all messages
        (AC11).
    """
    raise NotImplementedError
