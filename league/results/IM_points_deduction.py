"""Ismail-5: Apply or reverse a points deduction (owner: Ismail Mahomed).

Apply a points deduction to a team, or reverse one after a successful appeal.
"""

from typing import List, Optional, Tuple

from league.models import PointsDeduction, TableRow


def process_deduction(
    action: str,
    row: Optional[TableRow],
    deductions: List[PointsDeduction],
    points: int = 0,
    reason: Optional[str] = None,
    suspended: bool = False,
    deduction_id: Optional[str] = None,
) -> Tuple[Optional[str], List[str]]:
    """Ismail-5: Apply or reverse a points deduction.

    User story:
        As a league admin, I want to deduct points from a team (and reverse it
        if an appeal succeeds), so that sanctions show up correctly in the
        table.

    Acceptance criteria:
        1) Reject an unknown team.
        2) Reject a deduction of 0.
        3) Reject a deduction greater than 30.
        4) A reason is required.
        5) Allow a deduction before the season starts (team starts negative).
        6) Allow the total to go negative.
        7) Reject a deduction for a withdrawn team.
        8) A suspended deduction is recorded but not applied until activated.
        9) Reversing a deduction requires the original deduction ID.
        10) Reject reversing an already reversed deduction.
        11) Trigger a standings recalculation.

    Args:
        action: DeductionAction.APPLY or DeductionAction.REVERSE.
        row: the team's row, or None if the team is unknown.
        deductions: all deductions in the league.
        points: points to deduct (apply).
        reason: reason (apply, AC4).
        suspended: record without applying (AC8).
        deduction_id: deduction to reverse (AC9).

    Returns:
        (the deduction ID applied or reversed, []) on success; (None, errors)
        on rejection. The caller then rebuilds the table (AC11).
    """
    raise NotImplementedError
