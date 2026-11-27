"""Shared data models for the Football League Scheduler.

Rules for this file:
- Dataclasses only: no methods and no logic.
- Every field is used by at least one acceptance criterion; the comment
  names the story and criterion (for example "Jose-3 AC7").
- Status-like fields hold the plain strings defined in league.constants.
- Collections are lists (not dicts keyed by ID) so the JSON file can show
  duplicate IDs (Jose-9 AC7).
"""

from dataclasses import dataclass, field
from datetime import date, time
from typing import List, Optional, Tuple

from league.constants import (
    DEFAULT_FORFEIT_SCORE,
    DEFAULT_MAX_TV_PICKS,
    DEFAULT_MIN_CAPACITY,
    DEFAULT_MIN_TV_PICKS,
    DeductionStatus,
    MatchStatus,
    ResultType,
    TeamStatus,
)


@dataclass
class Player:
    """A registered player (Jose-4)."""

    player_id: str                # Jose-4 AC8, AC10, e.g. "P0001"
    name: str                     # Jose-4 AC10
    team_id: str                  # Jose-4 AC8
    shirt_number: int             # Jose-4 AC5-6
    date_of_birth: date           # Jose-4 AC7
    is_goalkeeper: bool = False   # Jose-4 AC3
    is_loan: bool = False         # Jose-4 AC4


@dataclass
class Stadium:
    """A ground that one or two teams use (Jose-2, Jose-3, Anay-1)."""

    stadium_id: str               # Jose-3 AC1, Anay-1 AC1, e.g. "S001"
    name: str                     # Jose-2 AC7
    capacity: int                 # Jose-2 AC8, Jose-3 AC6, Yousef-6 AC5
    tenant_ids: List[str] = field(default_factory=list)  # Jose-3 AC3-4, AC10; Anay-1 AC4
    unavailable_dates: List[date] = field(default_factory=list)  # Jose-3 AC7, Jose-6 AC10, Yousef-4 AC10, Anay-1 AC3
    event_dates: List[date] = field(default_factory=list)  # Anay-1 AC8 (non-football events)


@dataclass
class Team:
    """A club in the league (Jose-2, Jose-3, Jose-5, Jose-7)."""

    team_id: str                  # e.g. "T001", created by Jose-2
    name: str                     # Jose-2 AC4, Yousef-9 AC1, Ismail-3 AC7
    short_code: str               # Jose-2 AC5-6
    stadium_id: Optional[str] = None                 # Jose-2 AC7, Jose-3, Jose-6 AC3
    status: str = TeamStatus.ACTIVE                  # Jose-5, Jose-7 AC1, Yousef-1 AC3
    suspension_end: Optional[date] = None            # Jose-5 AC4-5
    ground_share_partner_id: Optional[str] = None    # Jose-3 AC8, Yousef-2 AC5, Jose-7 AC8
    expunged: bool = False                           # Jose-7 AC4, Ismail-2 AC7


@dataclass
class Result:
    """The score of a match. Forfeits hold the awarded score in the goals."""

    match_id: str                 # Jose-9 AC9
    home_goals: int               # Ismail-1 AC2-3, Ismail-2
    away_goals: int               # Ismail-1 AC2-3, Ismail-2
    result_type: str = ResultType.NORMAL  # Ismail-2 AC5-6, Ismail-4 AC11, Ismail-7 AC6


@dataclass
class Match:
    """One league fixture."""

    match_id: str                 # e.g. "M001"; Jose-9 AC9, Anay-1 AC7
    round_no: int                 # Yousef-7, Yousef-9 AC2, Anay-5 AC8, Jose-8 AC9
    home_team_id: str
    away_team_id: str
    stadium_id: Optional[str] = None          # Yousef-7 AC7, Anay-1 AC2
    match_date: Optional[date] = None         # Yousef-4, Ismail-1 AC4, Ismail-9 AC11
    kickoff: Optional[time] = None            # Yousef-6, Anay-1 AC5, Anay-2 AC4
    status: str = MatchStatus.SCHEDULED       # Anay-4, Ismail-1 AC5-6, AC9
    result: Optional[Result] = None           # Ismail-1, Ismail-2
    is_tv: bool = False                       # Anay-3 AC4-6
    tv_original_date: Optional[date] = None   # Anay-3 AC11
    tv_original_kickoff: Optional[time] = None  # Anay-3 AC11
    date_history: List[date] = field(default_factory=list)  # Anay-6 AC11
    postponement_reason: Optional[str] = None  # Anay-4 AC5, AC10
    postponement_note: Optional[str] = None    # Anay-4 AC6
    postponed_on: Optional[date] = None        # Anay-4 AC10
    high_priority: bool = False                # Anay-8 AC4
    needs_admin_decision: bool = False         # Anay-8 AC9
    cup_round_id: Optional[str] = None         # Anay-8 AC7, AC10
    abandon_minute: Optional[int] = None       # Anay-9 AC4, AC11
    abandon_cause: Optional[str] = None        # Anay-9 AC2, AC11
    abandon_decision: Optional[str] = None     # Anay-9 AC10-11


@dataclass
class PointsDeduction:
    """A points sanction against a team (Ismail-5)."""

    deduction_id: str             # Ismail-5 AC9, e.g. "D001"
    team_id: str                  # Ismail-5 AC1, Ismail-8 AC10
    points: int                   # positive number deducted; Ismail-5 AC2-3
    reason: str                   # Ismail-5 AC4
    status: str = DeductionStatus.ACTIVE  # Ismail-5 AC8, AC10


@dataclass
class CupRound:
    """A cup round that can clash with league matches (Anay-2, Anay-7, Anay-8)."""

    cup_round_id: str             # Anay-8 AC10, e.g. "C001"
    name: str                     # Anay-8 AC11
    cup_date: date                # Anay-8 AC1-2, Anay-2 AC6, Anay-7 AC3
    team_ids: List[str]           # Anay-8 AC2-4
    replay_date: Optional[date] = None   # Anay-8 AC5
    is_final: bool = False               # Anay-8 AC6
    eliminated_team_ids: List[str] = field(default_factory=list)  # Anay-8 AC7


@dataclass
class TableRow:
    """One team's line in the league table (Ismail-2 to Ismail-9).

    withdrawn and expunged are copied from the Team when the table is
    rebuilt, so Ismail's functions only need rows.
    """

    team_id: str                  # Ismail-2 AC1, Ismail-6 AC10
    team_name: str                # Ismail-3 AC7
    played: int = 0
    won: int = 0
    drawn: int = 0
    lost: int = 0
    goals_for: int = 0            # Ismail-2 AC9, Ismail-3 AC3
    goals_against: int = 0        # Ismail-2 AC9
    goal_difference: int = 0      # Ismail-2 AC9, Ismail-3 AC2
    points: int = 0               # net of active deductions; Ismail-9 AC9
    points_deducted: int = 0      # Ismail-5, Ismail-8 AC10
    home_won: int = 0             # Ismail-2 AC10 (home/away split)
    home_drawn: int = 0
    home_lost: int = 0
    away_won: int = 0
    away_drawn: int = 0
    away_lost: int = 0
    withdrawn: bool = False       # Ismail-3 AC8, Ismail-5 AC7, Ismail-6 AC7, Ismail-9 AC10
    expunged: bool = False        # Ismail-2 AC7


@dataclass
class LogEntry:
    """One recorded change (Jose-5 AC9, Jose-7 AC11, Jose-8 AC10,
    Yousef-8 AC10, Ismail-1 AC8)."""

    on: date
    source: str                   # story key, e.g. "Jose-5"
    subject_id: str               # team, match or league name affected
    message: str


@dataclass
class CheckResult:
    """Shared verdict: a CheckStatus value plus every message.

    Used by Jose-6, Yousef-7, Anay-1, Anay-2 (one per team), Anay-3, Anay-7.
    """

    status: str
    messages: List[str] = field(default_factory=list)


@dataclass
class FormSummary:
    """Output of Ismail-7 get_form."""

    results: List[str]            # "W", "D", "L", most recent last; AC5-6
    short_window: bool            # fewer matches than requested; AC4
    win_streak: int               # AC7
    unbeaten_streak: int          # AC8
    winless_streak: int           # AC9
    form_flag: str                # FormFlag value; AC3, AC11


@dataclass
class League:
    """A whole league: settings plus everything in it. One per JSON file."""

    name: str                           # Jose-1 AC1-2, Jose-8 AC2
    team_count: int                     # Jose-1 AC3-4, Jose-2 AC3, Jose-8 AC3, AC8
    fmt: str                            # Jose-1 AC7, Yousef-1, Yousef-3 AC1
    season_start: Optional[date]        # Jose-1 AC5-6, Jose-6 AC6, Yousef-4 AC1
    season_end: Optional[date]          # as above, Jose-8 AC7, Anay-6 AC3
    win_points: int                     # Jose-1 AC8, Ismail-2, Ismail-9 AC2
    draw_points: int                    # Jose-1 AC8-9, Ismail-2 AC4
    loss_points: int                    # Jose-1 AC9, Ismail-2 AC2-3
    min_capacity: int = DEFAULT_MIN_CAPACITY          # Jose-2 AC8, Jose-3 AC6
    forfeit_score: Tuple[int, int] = DEFAULT_FORFEIT_SCORE  # Jose-7 AC6, Anay-9 AC8
    promotion_places: int = 0           # Jose-8 AC8-9, Ismail-6
    playoff_places: int = 0             # Ismail-6 AC3
    relegation_places: int = 0          # Jose-8 AC8-9, Ismail-6, Ismail-9
    top_division: bool = False          # Ismail-6 AC8
    derby_pairs: List[Tuple[str, str]] = field(default_factory=list)  # Jose-6 AC9, Yousef-5, Yousef-7 AC9, Yousef-8 AC7
    blackout_dates: List[date] = field(default_factory=list)          # Jose-6 AC7, Yousef-4 AC3, Anay-5 AC3
    registration_deadline: Optional[date] = None   # Jose-4 AC9
    transfer_window_start: Optional[date] = None   # Jose-4 AC9
    transfer_window_end: Optional[date] = None     # Jose-4 AC9
    max_tv_picks: int = DEFAULT_MAX_TV_PICKS       # Anay-3 AC5
    min_tv_picks: int = DEFAULT_MIN_TV_PICKS       # Anay-3 AC6
    is_void: bool = False                          # Jose-7 AC9
    teams: List[Team] = field(default_factory=list)
    stadiums: List[Stadium] = field(default_factory=list)
    players: List[Player] = field(default_factory=list)
    matches: List[Match] = field(default_factory=list)
    byes: List[Tuple[int, str]] = field(default_factory=list)  # (round_no, team_id); Yousef-1 AC6, Yousef-7 AC8
    cup_rounds: List[CupRound] = field(default_factory=list)
    deductions: List[PointsDeduction] = field(default_factory=list)
    table: List[TableRow] = field(default_factory=list)
    generated_team_ids: List[str] = field(default_factory=list)  # Yousef-8 AC2-4
    log: List[LogEntry] = field(default_factory=list)
