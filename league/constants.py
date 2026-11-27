"""Shared constants for the Football League Scheduler.

Every value here is either stated in an acceptance criterion (the story key
is given in the comment) or was agreed by the team in the design proposal
(marked "team decision").
"""

from datetime import time


class LeagueFormat:
    """League formats (Jose-1 AC7, Yousef-1 AC9)."""

    SINGLE = "single"
    DOUBLE = "double"
    ALL = (SINGLE, DOUBLE)


class TeamStatus:
    """Team statuses (Jose-5)."""

    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    WITHDRAWN = "WITHDRAWN"
    ALL = (ACTIVE, SUSPENDED, WITHDRAWN)


class MatchStatus:
    """Match statuses (Anay-4, Anay-9, Ismail-1, Jose-7)."""

    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    PLAYED = "PLAYED"
    POSTPONED = "POSTPONED"
    CANCELLED = "CANCELLED"
    ABANDONED = "ABANDONED"  # abandoned, decision not yet confirmed
    EXPUNGED = "EXPUNGED"
    ALL = (SCHEDULED, IN_PROGRESS, PLAYED, POSTPONED, CANCELLED, ABANDONED,
           EXPUNGED)


class ResultType:
    """How a result was reached (Ismail-2 AC5-6)."""

    NORMAL = "NORMAL"
    FORFEIT = "FORFEIT"
    BOTH_FORFEIT = "BOTH_FORFEIT"
    ALL = (NORMAL, FORFEIT, BOTH_FORFEIT)


class PostponementReason:
    """Allowed postponement reasons (Anay-4 AC5)."""

    WEATHER = "weather"
    PITCH = "pitch"
    CUP = "cup"
    INTERNATIONAL = "international"
    SAFETY = "safety"
    OTHER = "other"
    ALL = (WEATHER, PITCH, CUP, INTERNATIONAL, SAFETY, OTHER)


class AbandonmentCause:
    """Causes of an abandoned match (Anay-9 AC2-7)."""

    WEATHER = "WEATHER"
    FLOODLIGHTS = "FLOODLIGHTS"
    HOME_CONDUCT = "HOME_CONDUCT"
    AWAY_CONDUCT = "AWAY_CONDUCT"
    BOTH_CONDUCT = "BOTH_CONDUCT"
    ALL = (WEATHER, FLOODLIGHTS, HOME_CONDUCT, AWAY_CONDUCT, BOTH_CONDUCT)


class AbandonmentDecision:
    """Outcomes of an abandonment decision (Anay-9 AC3-7)."""

    REPLAY = "REPLAY"
    RESULT_STANDS = "RESULT_STANDS"
    AWARDED_HOME = "AWARDED_HOME"
    AWARDED_AWAY = "AWARDED_AWAY"
    NO_POINTS = "NO_POINTS"
    ALL = (REPLAY, RESULT_STANDS, AWARDED_HOME, AWARDED_AWAY, NO_POINTS)


class VenueFilter:
    """Venue filters. Yousef-9 AC4 uses "any"; Ismail-7 AC10 uses "all"."""

    HOME = "home"
    AWAY = "away"
    ANY = "any"
    ALL_VENUES = "all"
    FIXTURE_FILTERS = (HOME, AWAY, ANY)   # Yousef-9
    FORM_FILTERS = (HOME, AWAY, ALL_VENUES)  # Ismail-7


class Zone:
    """League table zones (Ismail-6)."""

    CHAMPION = "CHAMPION"
    PROMOTION = "PROMOTION"
    QUALIFICATION = "QUALIFICATION"
    PLAYOFF = "PLAYOFF"
    SAFE = "SAFE"
    RELEGATION = "RELEGATION"
    ALL = (CHAMPION, PROMOTION, QUALIFICATION, PLAYOFF, SAFE, RELEGATION)


class ClinchStatus:
    """Outcomes of Ismail-9."""

    CHAMPION = "CHAMPION"
    NOT_DECIDED = "NOT_DECIDED"
    RELEGATED = "RELEGATED"
    SAFE = "SAFE"
    ALL = (CHAMPION, NOT_DECIDED, RELEGATED, SAFE)


class ClinchTarget:
    """What Ismail-9 is asked to decide."""

    TITLE = "title"
    RELEGATION = "relegation"
    ALL = (TITLE, RELEGATION)


class DeductionStatus:
    """Points deduction statuses (Ismail-5 AC8, AC10)."""

    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    REVERSED = "REVERSED"
    ALL = (ACTIVE, SUSPENDED, REVERSED)


class DeductionAction:
    """Actions accepted by Ismail-5 process_deduction (team decision OQ-5)."""

    APPLY = "apply"
    REVERSE = "reverse"
    ALL = (APPLY, REVERSE)


class CheckStatus:
    """Statuses carried by CheckResult."""

    # Jose-6 AC11
    READY = "READY"
    READY_WITH_WARNINGS = "READY_WITH_WARNINGS"
    NOT_READY = "NOT_READY"
    # Yousef-7 AC11
    VALID = "VALID"
    VALID_WITH_WARNINGS = "VALID_WITH_WARNINGS"
    INVALID = "INVALID"
    # Anay-1 AC9
    NO_CLASH = "NO_CLASH"
    WARNING = "WARNING"
    CLASH = "CLASH"
    # Anay-3 AC10
    ALLOWED = "ALLOWED"
    ALLOWED_WITH_WARNING = "ALLOWED_WITH_WARNING"
    REJECTED = "REJECTED"
    # Anay-2 AC3-5 and Anay-7 AC4-6 (WARNING shared with Anay-1)
    OK = "OK"
    FAIL = "FAIL"
    CRITICAL = "CRITICAL"


class FormFlag:
    """Form flags (Ismail-7 AC3, AC11)."""

    NO_FORM = "NO_FORM"
    IN_FORM = "IN_FORM"
    POOR_FORM = "POOR_FORM"
    NORMAL = "NORMAL"


class Setting:
    """League setting names accepted by Jose-8 edit_league_setting (AC1)."""

    NAME = "name"
    TEAM_COUNT = "team_count"
    FORMAT = "fmt"
    WIN_POINTS = "win_points"
    DRAW_POINTS = "draw_points"
    LOSS_POINTS = "loss_points"
    SEASON_START = "season_start"
    SEASON_END = "season_end"
    PROMOTION_PLACES = "promotion_places"
    PLAYOFF_PLACES = "playoff_places"
    RELEGATION_PLACES = "relegation_places"
    ALL = (NAME, TEAM_COUNT, FORMAT, WIN_POINTS, DRAW_POINTS, LOSS_POINTS,
           SEASON_START, SEASON_END, PROMOTION_PLACES, PLAYOFF_PLACES,
           RELEGATION_PLACES)


# Placeholders and roles
BYE = "BYE"      # Yousef-1 AC4
ADMIN = "ADMIN"  # Anay-4 AC8: requests must come from the league administrator

# League setup (Jose-1, Jose-2, Jose-3, Jose-4)
MIN_TEAMS = 4
MAX_TEAMS = 24
MAX_TENANTS = 2
MAX_UNAVAILABLE_FRACTION = 0.25
SQUAD_MIN = 18
SQUAD_MAX = 25
MIN_GOALKEEPERS = 2
MAX_LOANS = 5
SHIRT_MIN = 1
SHIRT_MAX = 99
MIN_PLAYER_AGE = 16
DEFAULT_MIN_CAPACITY = 5000          # team decision (OQ-9)
DEFAULT_FORFEIT_SCORE = (3, 0)       # (winner, loser), team decision
ZONE_LOCK_FINAL_ROUNDS = 5           # Jose-8 AC9

# Fixture generation (Yousef)
DERBY_MIN_GAP_DEFAULT = 6            # Yousef-5 AC5
MAX_DERBIES_PER_ROUND = 2            # Yousef-5 AC7
MIDWEEK_MIN_GAP_DAYS = 3             # Yousef-4 AC6
MAX_MIDWEEK_PER_4_WEEKS = 2          # Yousef-4 AC7
HIGH_CAPACITY = 30000                # Yousef-6 AC5
FILTER_LIMIT = 50                    # Yousef-9 AC10

# Kick-off times (Yousef-6, Anay-3)
SATURDAY_KICKOFF = time(15, 0)
SUNDAY_KICKOFF = time(14, 0)
MIDWEEK_KICKOFF = time(19, 45)
DERBY_LATEST = time(18, 0)
MANUAL_EARLIEST = time(12, 0)
MANUAL_LATEST = time(20, 0)
FINAL_ROUND_KICKOFF = time(15, 0)    # team decision (OQ-9)
EVENING_FROM = time(18, 0)           # team decision (OQ-9)
TV_BLACKOUT_START = time(14, 45)
TV_BLACKOUT_END = time(17, 15)

# Constraints and rescheduling (Anay)
REST_MIN_HOURS = 48                  # Anay-2 AC3, AC6
REST_EVENING_HOURS = 72              # Anay-2 AC4-5
TV_NOTICE_DAYS = 35                  # Anay-3 AC3 (5 weeks)
TV_WARN_ROUNDS_LEFT = 10             # Anay-3 AC6
DEFAULT_MAX_TV_PICKS = 10            # team decision (OQ-9)
DEFAULT_MIN_TV_PICKS = 2             # team decision (OQ-9)
POSTPONE_NOTICE_DAYS = 7             # Anay-4 AC7
POSTPONE_REVIEW_COUNT = 3            # Anay-4 AC9
TUESDAY_NOTICE_DAYS = 28             # Anay-6 AC6
MOVE_AGREEMENT_DAYS = 14             # Anay-6 AC7
SHORT_NOTICE_DAYS = 7                # Anay-6 AC9
TRAVEL_MILES = 200                   # Anay-7 AC8
CONGESTION_FINAL_ROUNDS = 3          # Anay-7 AC9
RESULT_STANDS_MINUTE = 80            # Anay-9 AC4

# Results and standings (Ismail)
MAX_SCORE = 30                       # Ismail-1 AC3
MAX_DEDUCTION = 30                   # Ismail-5 AC3
FORM_LENGTH_MIN = 1                  # Ismail-7 AC2
FORM_LENGTH_MAX = 10
FORM_LENGTH_DEFAULT = 5
IN_FORM_PPG = 2.0                    # Ismail-7 AC11
POOR_FORM_PPG = 1.0

# Storage (Jose-9)
FILE_VERSION = 2                     # team decision (OQ-19): version 1 is the
                                     # documented older shape to migrate from
REQUIRED_SECTIONS = ("version", "league", "teams", "stadiums", "players",
                     "matches", "results")
