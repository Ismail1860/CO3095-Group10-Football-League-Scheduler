"""Anay-9: Decide what happens to an abandoned match (owner: Anay Makan).

Decide the outcome of an abandoned match from its cause and apply it once
confirmed.
"""

from typing import List, Optional, Tuple

from league.models import Match


def decide_abandonment(
    match: Match,
    cause: str,
    minute: int,
    home_goals: int,
    away_goals: int,
    let_result_stand: bool,
    forfeit_score: Tuple[int, int],
    confirmed: bool,
) -> Tuple[Optional[str], List[str]]:
    """Anay-9: Decide what happens to an abandoned match.

    User story:
        As a league admin, I want the outcome of an abandoned match decided by
        the cause (weather, crowd trouble, one or both teams' conduct), so that
        abandonments are treated the same way every time.

    Acceptance criteria:
        1) Reject if the match was not in progress.
        2) Reject an unknown abandonment cause.
        3) Cause outside both clubs' control (weather, floodlights): replay in
           full.
        4) Exception: if 80 or more minutes were played, the league can let the
           result stand.
        5) Caused by conduct of the home team or its supporters: award match to
           away team.
        6) Caused by conduct of the away team or its supporters: award match to
           home team.
        7) Caused by conduct of both teams: no points for either side, no
           replay.
        8) Awarded matches use the league forfeit score, or the actual score if
           the winner was leading by more.
        9) A replay is sent to Anay-5 to find a date.
        10) Points are not counted until the decision is confirmed.
        11) Record the minute of abandonment and the decision.

    Args:
        match: the abandoned match.
        cause: an AbandonmentCause value.
        minute: minute of abandonment.
        home_goals: score when abandoned.
        away_goals: score when abandoned.
        let_result_stand: league chooses to keep the result after 80+ minutes
            (AC4).
        forfeit_score: league forfeit score (winner, loser).
        confirmed: decision confirmed, so points may count (AC10).

    Returns:
        (AbandonmentDecision value, errors).
    """
    raise NotImplementedError
