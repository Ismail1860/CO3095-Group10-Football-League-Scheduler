"""Football League Scheduler: text menu entry point.

Run with:  python main.py

This file only reads input and calls the functions in the league package.
All rules live in league/; menu options print "Not implemented yet" until
the matching story is merged.
"""

SETUP_MENU = [
    "Create a league (Jose-1)",
    "Register a team (Jose-2)",
    "Assign a stadium (Jose-3)",
    "Check a squad (Jose-4)",
    "Change a team's status (Jose-5)",
    "Readiness check (Jose-6)",
    "Withdraw a team (Jose-7)",
    "Edit league settings (Jose-8)",
]

FIXTURES_MENU = [
    "Generate fixtures (Yousef-1 to Yousef-7)",
    "Regenerate fixtures (Yousef-8)",
    "Search and filter fixtures (Yousef-9)",
]

CONSTRAINTS_MENU = [
    "Check a venue for clashes (Anay-1)",
    "Check rest days (Anay-2)",
    "Check a TV slot (Anay-3)",
    "Postpone a match (Anay-4)",
    "Find the next free date (Anay-5)",
    "Reschedule a match (Anay-6)",
    "Check fixture congestion (Anay-7)",
    "Resolve a cup clash (Anay-8)",
    "Decide an abandoned match (Anay-9)",
]

RESULTS_MENU = [
    "Record a result (Ismail-1, Ismail-2)",
    "Show the league table (Ismail-3, Ismail-4, Ismail-6)",
    "Apply or reverse a points deduction (Ismail-5)",
    "Show a team's form (Ismail-7)",
    "Season summary report (Ismail-8)",
    "Title or relegation decided? (Ismail-9)",
]

STORAGE_MENU = [
    "Load a league from file (Jose-9)",
    "Save the league to file (Jose-9)",
]

MAIN_MENU = [
    ("League & team setup", SETUP_MENU),
    ("Fixtures", FIXTURES_MENU),
    ("Constraints & rescheduling", CONSTRAINTS_MENU),
    ("Results & standings", RESULTS_MENU),
    ("Save / Load", STORAGE_MENU),
]


def read_choice(prompt):
    """Read one line of input; return None at end of input."""
    try:
        return input(prompt).strip()
    except EOFError:
        return None


def show_menu(title, options, back_label):
    """Print a numbered menu."""
    print()
    print(f"=== {title} ===")
    for number, label in enumerate(options, start=1):
        print(f"  {number}. {label}")
    print(f"  0. {back_label}")


def run_sub_menu(title, options):
    """Show a sub-menu until the user goes back."""
    while True:
        show_menu(title, options, "Back")
        choice = read_choice("Choose an option: ")
        if choice is None or choice == "0":
            return
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            print("Not implemented yet")
        else:
            print("Please enter one of the numbers shown.")


def main():
    """Show the main menu until the user quits."""
    print("Football League Scheduler")
    titles = [title for title, _ in MAIN_MENU]
    while True:
        show_menu("Main menu", titles, "Quit")
        choice = read_choice("Choose an option: ")
        if choice is None or choice == "0":
            print("Goodbye.")
            return
        if choice.isdigit() and 1 <= int(choice) <= len(MAIN_MENU):
            title, options = MAIN_MENU[int(choice) - 1]
            run_sub_menu(title, options)
        else:
            print("Please enter one of the numbers shown.")


if __name__ == "__main__":
    main()
