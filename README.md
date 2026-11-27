# CO3095 Group 10: Football League Scheduler

## 1. Project summary

A text-based Python application for running a football league. A league
administrator can set up a league and its teams, generate a fair fixture list
(round-robin pairings, balanced home and away games, dates and kick-off times),
handle scheduling constraints such as venue clashes, rest days, TV picks,
postponements and cup clashes, and record results to produce a league table
with tie-breakers, zones, form and a season report. Data is saved to JSON files
in `data/`. The project was built for CO3095 Software Measurement and Quality
Assurance at the University of Leicester using Scrum, with black-box,
white-box, symbolic execution and concolic testing for every function.

## 2. Requirements

- Python 3.9 or newer. The code uses no syntax newer than Python 3.9.
- The application itself uses only the Python standard library.
- Test tools (pinned in `requirements.txt`): `pytest` 8.3.5 and `coverage` 7.6.12.

Install the test tools from the project folder:

```
python -m pip install -r requirements.txt
```

On macOS or Linux, use `python3` instead of `python` if `python` is not found.

## 3. Uncompress and open in PyCharm (Charles Wilson lab)

1. Copy the submitted `.zip` file to your home drive.
2. Right-click the file and choose **Extract All...** (Windows) or
   double-click it (macOS). Note the folder it creates, for example
   `CO3095-Group10-Football-League-Scheduler`.
3. Start **PyCharm** and choose **File > Open...**.
4. Select the extracted folder (the one that contains `main.py` and
   `README.md`) and click **OK**. If asked, choose **Trust Project**.
5. Set the interpreter: **File > Settings > Project > Python Interpreter**
   (macOS: **PyCharm > Settings**). Click **Add Interpreter > Add Local
   Interpreter**, choose **Virtualenv Environment > New**, select a
   Python 3.9 or newer base interpreter, and click **OK**.
6. Open PyCharm's **Terminal** tab (bottom of the window). It opens in the
   project folder with the virtual environment active. Install the test
   tools:

   ```
   python -m pip install -r requirements.txt
   ```

7. Check the install:

   ```
   python -m pytest --version
   python -m coverage --version
   ```

All commands below are run from this Terminal, inside the project folder.

## 4. Run the application

```
python main.py
```

Choose options by typing their number and pressing Enter; `0` goes back or
quits. Alternatively, right-click `main.py` in PyCharm and choose
**Run 'main'**.

## 5. Run the tests for each technique separately

Each team member has their own test package named after their student ID, with
one sub-package per technique:

```
<studentid>/test/blackbox/<technique>/
<studentid>/test/whitebox/<technique>/
```

Run one technique for one member, for example Ismail's boundary value
analysis tests:

```
python -m pytest im248/test/blackbox/boundary_value_analysis -v
```

Run everything for one member, or every test in the project:

```
python -m pytest im248 -v
python -m pytest -v
```

Technique folders:

| Black-box | White-box |
|---|---|
| `equivalence_partitioning` | `statement_coverage` |
| `boundary_value_analysis` | `branch_coverage` |
| `category_partition` | `path_coverage` |
| `random_testing` | `symbolic_execution` |
| | `concolic_testing` |

Each technique folder contains a `_TEMPLATE.py` comment header. Copy it to
`test_<PREFIX>_<module>.py` (for example `test_IM_record_result.py`) to start
a test file; files named `_TEMPLATE.py` are not collected by pytest.

## 6. Measure coverage for each technique

Coverage is measured on the `league` package only (see `.coveragerc`). For one
technique:

```
python -m coverage erase
python -m coverage run -m pytest im248/test/whitebox/branch_coverage
python -m coverage report -m
python -m coverage html -d docs/coverage_reports/im248_branch_coverage
```

Open `docs/coverage_reports/im248_branch_coverage/index.html` in a browser to
see the line-by-line report. Repeat with each member's student ID and each
technique folder.

To measure branch coverage as well as line coverage, add `--branch` to the
`run` command:

```
python -m coverage run --branch -m pytest im248/test/whitebox/branch_coverage
```

## 7. Team

| Name | Student ID | Module prefix | Area |
|---|---|---|---|
| Jose Africa | ja551 | `JA_` | League and team setup (`league/setup/`) |
| Yousef Rwis | ye21 | `YE_` | Fixture generation (`league/fixtures/`) |
| Anay Makan | am1458 | `AM_` | Constraints and rescheduling (`league/constraints/`) |
| Ismail Mahomed | im248 | `IM_` | Results and standings (`league/results/`) |

User stories and acceptance criteria: `docs/user_stories.csv`.

## 8. Links

- GitHub repository: https://github.com/Ismail1860/CO3095-Group10-Football-League-Scheduler
- TODO (team): confirm the repository is public before submission.
- GitHub Project board: TODO (team): add the board link.

## Project layout

```
main.py                 text menu (entry point)
league/models.py        shared data models (dataclasses)
league/constants.py     shared constants
league/setup/           Jose's modules (JA_*)
league/fixtures/        Yousef's modules (YE_*)
league/constraints/     Anay's modules (AM_*)
league/results/         Ismail's modules (IM_*)
<studentid>/test/       each member's black-box and white-box tests
data/                   league JSON files saved at runtime
docs/                   user stories, planning, tracking, CMMI, symbolic trees,
                        coverage reports
```
