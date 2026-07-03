from datetime import datetime, timezone
from pathlib import Path
import subprocess

from src.core.project_identity import get_project_identity


ROOT_DIR = Path(__file__).resolve().parents[2]


def _get_git_commit() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception:
        return "unknown"


def get_report_header() -> dict:
    identity = get_project_identity()

    return {
        "project": identity.get("display_name", "HunterMini"),
        "project_name": identity.get("project_name", "HunterMini"),
        "version": identity.get("version", "1.0.0"),
        "build": identity.get("build", "v1.0.0"),
        "git_commit": _get_git_commit(),
        "environment": identity.get("environment", "validation"),
        "experiment_id": identity.get("active_experiment", "EXP-001"),
        "experiment_name": identity.get("experiment_name", "Unknown Experiment"),
        "experiment_status": identity.get("experiment_status", "Unknown"),
        "experiment_version": identity.get("experiment_version", "Unknown"),
        "database": identity.get("database_name", "Hunter_mini.db"),
        "database_path": identity.get("database_path", "data/Hunter_mini.db"),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def format_report_header_text() -> str:
    header = get_report_header()

    return (
        f"{header['project']} | "
        f"Version: {header['version']} | "
        f"Build: {header['build']} | "
        f"Commit: {header['git_commit']} | "
        f"Env: {header['environment']} | "
        f"Experiment: {header['experiment_id']} - {header['experiment_name']} | "
        f"DB: {header['database']} | "
        f"Generated: {header['generated_at_utc']}"
    )


def print_report_header():
    header = get_report_header()
    for key, value in header.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print_report_header()
