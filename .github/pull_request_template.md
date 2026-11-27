## Linked issue

Closes #<!-- issue number -->

## User story

Story key: <!-- e.g. Ismail-1 -->

## What changed

<!-- Short description of the code added or changed. -->

## Tests added (by technique)

| Technique | Test file(s) | Number of tests | Passing |
|---|---|---|---|
| Equivalence partitioning | | | |
| Boundary value analysis | | | |
| Category partition | | | |
| Random testing | | | |
| Statement coverage | | | |
| Branch coverage | | | |
| Path coverage | | | |
| Symbolic execution | | | |
| Concolic testing | | | |

## Coverage

Coverage of the changed module: <!-- e.g. 92% statements, 88% branches -->

## Reviewer checklist

- [ ] Every acceptance criterion in the docstring is handled.
- [ ] Docstring still matches `docs/user_stories.csv`.
- [ ] Function signature matches the agreed contract (no extra parameters).
- [ ] Cyclomatic complexity of the story's main function is 10 or more.
- [ ] Each test has a comment stating story key, technique, input and expected result.
- [ ] All tests pass locally (`python -m pytest <studentid>`).
- [ ] Symbolic tree and path conditions added under `docs/symbolic/`.
- [ ] Coverage report exported under `docs/coverage_reports/`.

## Reminder

Do **not** delete this branch after merging. Story branches are kept as evidence of development.
