"""Ismail-4: Head-to-head mini-table for tied teams (owner: Ismail Mahomed).

Build a head-to-head mini-table for two or more tied teams and order them,
saying which criterion decided each place.
"""

from typing import Dict, List, Tuple

from league.models import Match


def build_h2h_table(
    team_ids: List[str],
    matches: List[Match],
    win_pts: int,
    draw_pts: int,
    loss_pts: int,
    team_names: Dict[str, str],
    decides_place: bool,
) -> Tuple[List[Tuple[str, str]], bool, List[str]]:
    """Ismail-4: Head-to-head mini-table for tied teams.

    User story:
        As a supporter, I want a mini-table of the games between teams that are
        still level, so that ties between three or more teams are broken
        fairly.

    Acceptance criteria:
        1) Reject fewer than 2 teams.
        2) Only include matches where both teams are in the tied group.
        3) Ignore unplayed, postponed and abandoned-without-result matches.
        4) If any match in the group is unplayed, mark the mini-table as
           provisional.
        5) Score each match with league points (win/draw/loss).
        6) Count away goals separately.
        7) If one team is separated, remove it and re-apply to the remaining
           tied teams.
        8) If no team separates, fall back to play-off flag or alphabetical (as
           Ismail-3).
        9) A 2-team tie uses the same logic (no special case).
        10) Return the ordered group and the criterion that decided each place.
        11) A forfeited match counts with its awarded score.

    Args:
        team_ids: the tied teams.
        matches: all matches.
        win_pts: points for a win.
        draw_pts: points for a draw.
        loss_pts: points for a loss (AC5).
        team_names: team ID -> name (AC8 alphabetical fallback).
        decides_place: the position decides title, promotion or relegation
            (AC8).

    Returns:
        (ordered (team_id, deciding criterion) pairs, provisional flag,
        errors).
    """
    raise NotImplementedError
