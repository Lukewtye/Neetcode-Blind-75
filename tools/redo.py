#!/usr/bin/env python3
"""Report which problems are due for a from-scratch redo.

Reads git history only. A problem's latest commit status wins:
  clean              -> done, nothing owed
  slow | solution    -> owed a redo about 7 days after that commit

    python3 tools/redo.py
"""
import datetime
import re
import subprocess
import sys

WINDOW_DAYS = 7
PATTERN = re.compile(r"^(?P<problem>.+?): (?P<status>clean|slow|solution)$")

try:
    log = subprocess.run(
        ["git", "log", "--date=short", "--pretty=format:%ad%x09%s"],
        capture_output=True, text=True, check=True,
    ).stdout
except subprocess.CalledProcessError:
    sys.exit("not a git repo, or no commits yet")

latest = {}  # problem -> (date, status); git log is newest-first
for line in log.splitlines():
    if "\t" not in line:
        continue
    date_str, subject = line.split("\t", 1)
    m = PATTERN.match(subject.strip())
    if not m:
        continue
    problem = m.group("problem")
    if problem in latest:
        continue
    latest[problem] = (
        datetime.date.fromisoformat(date_str),
        m.group("status"),
    )

today = datetime.date.today()
due, upcoming = [], []
for problem, (date, status) in latest.items():
    if status == "clean":
        continue
    age = (today - date).days
    (due if age >= WINDOW_DAYS else upcoming).append((age, problem, status, date))

due.sort(reverse=True)
upcoming.sort(reverse=True)

if due:
    print("DUE NOW (redo from scratch, do not open the old file):")
    for age, problem, status, date in due:
        print(f"  {problem:<32} {status:<9} {date}  ({age}d ago)")
else:
    print("DUE NOW: nothing")

if upcoming:
    print("\nUPCOMING:")
    for age, problem, status, date in upcoming:
        print(f"  {problem:<32} {status:<9} {date}  (redo in {WINDOW_DAYS - age}d)")

clean = sum(1 for _, s in latest.values() if s == "clean")
print(f"\n{len(latest)} problems tracked, {clean} currently clean.")
