"""Progress dashboard: run each day's tagged tests and print a table.

Usage: `make status` (or `python scripts/status.py`).

Days with no automated tests (1 and 4) are verified manually; see the
"Done when" list in docs/day-0N.md and the checklist in PROGRESS.md.
"""
import subprocess
import sys

DAYS = {
    1: "Hello, gateway (manual)",
    2: "Dice parser",
    3: "Embed helper",
    4: "Cogs & config (manual)",
    5: "Poll state",
    6: "Durations & reminder storage",
    7: "Automod rules",
}
MANUAL = {1, 4}


def run_day(n: int) -> str:
    if n in MANUAL:
        return "manual"
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-m", f"day{n}", "-q", "-x", "--no-header"],
        capture_output=True,
        text=True,
    )
    # pytest exit codes: 0 = all passed, 5 = no tests collected
    return {0: "PASS", 5: "no tests"}.get(proc.returncode, "todo")


def main() -> None:
    print(f"{'Day':<4}{'Topic':<34}Status")
    print("-" * 52)
    done = 0
    for n, topic in DAYS.items():
        status = run_day(n)
        done += status == "PASS"
        print(f"{n:<4}{topic:<34}{status}")
    print("-" * 52)
    print(f"{done} of {len(DAYS) - len(MANUAL)} automated days passing. Tick PROGRESS.md for the rest.")


if __name__ == "__main__":
    main()
