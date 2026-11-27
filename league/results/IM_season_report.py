"""Ismail-8: Season summary report (owner: Ismail Mahomed).

Build the season summary report and write it to a text file.
"""

from typing import Dict, List, Optional, Tuple

from league.models import Match, TableRow


def build_season_report(
    table_rows: List[TableRow],
    matches: List[Match],
    team_names: Dict[str, str],
    season_finished: bool,
    output_path: str,
) -> Tuple[Optional[str], List[str]]:
    """Ismail-8: Season summary report.

    User story:
        As a league admin, I want a summary of the season (best attack, best
        defence, biggest win, longest unbeaten run), so that I can share the
        key stats with clubs.

    Acceptance criteria:
        1) Reject if no matches are played.
        2) Mark the report as provisional if the season is not finished.
        3) Best attack: most goals scored (ties listed together).
        4) Best defence: fewest goals conceded (ties listed together).
        5) Biggest win: largest margin, then most goals scored.
        6) Highest-scoring match.
        7) Longest unbeaten run (uses Ismail-7).
        8) Exclude expunged results.
        9) Include the number of postponed and abandoned matches.
        10) Include total points deducted per team, if any.
        11) Write the report to a text file; report an error if writing fails.

    Note: an acceptance-criterion wording change is pending (OQ-25). Re-sync
    this docstring when docs/user_stories.csv is updated.

    Args:
        table_rows: current table.
        matches: all matches.
        team_names: team ID -> name.
        season_finished: False marks the report provisional (AC2).
        output_path: text file to write.

    Returns:
        (report text, []) when written; (None, errors) otherwise.
    """
    raise NotImplementedError
