"""Jose-7: Team withdraws mid-season (owner: Jose Africa).

Handle a team leaving during the season: expunge or award its matches depending
on how many are played, and keep the table fair.
"""

from datetime import date
from typing import Dict, List, Optional, Tuple

from league.models import League, Team


def withdraw_team(
    league: League,
    team: Optional[Team],
    reason: str,
    today: date,
) -> Tuple[Dict[str, List[str]], List[str]]:
    """Jose-7: Team withdraws mid-season.

    User story:
        As a league admin, I want to handle a team pulling out during the
        season (expunging or awarding its matches depending on how far in we
        are), so that the table stays fair for everyone else.

    Acceptance criteria:
        1) Reject if the team is already withdrawn.
        2) Reject if the season has finished.
        3) If the season has not started, remove the team and flag fixtures for
           regeneration.
        4) If fewer than half of the team's matches are played, expunge all its
           results.
        5) If half or more are played, keep played results.
        6) Then award remaining matches to opponents using the league's forfeit
           score.
        7) Cancel all future fixtures involving the team.
        8) Free any ground-share partner's stadium constraints.
        9) If withdrawal leaves fewer than 4 active teams, mark the league as
           void.
        10) Request a standings recalculation (uses Ismail-2).
        11) Record the withdrawal reason and date.
        12) Return a summary of expunged, awarded and cancelled matches.

    Note: an acceptance-criterion wording change is pending (OQ-17). Re-sync
    this docstring when docs/user_stories.csv is updated.

    Args:
        league: the league.
        team: the withdrawing team, or None if not found.
        reason: reason for withdrawal (AC11).
        today: date of withdrawal.

    Returns:
        ({'expunged': [...], 'awarded': [...], 'cancelled': [...]} match IDs,
        errors) (AC12).
    """
    raise NotImplementedError
