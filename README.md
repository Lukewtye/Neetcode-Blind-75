# practice

Daily coding practice. One problem, one commit. No commit means it did not
happen.

Rules I am holding myself to (from the Summer 2026 CS Foundations Sprint):

- First attempt is mine alone. No AI, no autocomplete, no docs during the
  attempt. AI reviews afterward only.
- 35-minute stuck rule: write down exactly where I am stuck in `stuck/`,
  study the solution, then re-implement from memory.
- Every file opens with two comment lines: approach, then time/space
  complexity. If I cannot state the complexity, I do not own the solution.

## Layout

```
exercism/                  Exercism Python track (week-1 diagnostic)
neetcode/<section>/        NeetCode roadmap, one folder per section
stuck/                     stuck-point notes, one markdown file per incident
tools/                     repo scripts (not practice code)
```

Sections are created as I reach them. Current: `arrays-hashing`.

## Commit convention

```
<problem>: clean      would pass an interview
<problem>: slow       solved, but over time or ugly
<problem>: solution   needed the answer
```

`<problem>` is the file's basename without extension, e.g.
`two-sum: clean`. Anything landing as `slow` or `solution` gets redone from
scratch about seven days later. `tools/redo.py` reads git history and tells
me what is due.

The commit log is the ground truth for this repo. There is no separate
tracker, and nothing here should be backfilled after the fact.

## Note on problem statements

Solutions and my own notes only. Problem statements are not reproduced here.
