from pathlib import Path
from datetime import datetime, timezone
import yaml


ROOT_DIR = Path(__file__).resolve().parents[2]
ACTIVE_EXPERIMENT_PATH = ROOT_DIR / "experiments" / "active.yaml"


def _read_yaml(path: Path) -> dict:
    if not path.exists():
        return {}

    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def get_active_experiment() -> dict:
    data = _read_yaml(ACTIVE_EXPERIMENT_PATH)
    experiment = data.get("experiment", data)

    return {
        "id": experiment.get("id", "EXP-001"),
        "name": experiment.get("name", "Unknown Experiment"),
        "goal": experiment.get("goal", ""),
        "status": experiment.get("status", "Unknown"),
        "version": experiment.get("version", "Unknown"),
        "build": experiment.get("build", "Unknown"),
        "started_at": experiment.get("started_at", ""),
        "database": experiment.get("database", "data/Hunter_mini.db"),
        "notes": experiment.get("notes", []),
    }


def get_active_experiment_id() -> str:
    return get_active_experiment().get("id", "EXP-001")


def get_experiment_trade_metadata() -> dict:
    experiment = get_active_experiment()

    return {
        "experiment_id": experiment["id"],
        "experiment_name": experiment["name"],
        "experiment_version": experiment["version"],
        "experiment_build": experiment["build"],
        "experiment_status": experiment["status"],
        "tracked_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def format_experiment_text() -> str:
    experiment = get_active_experiment()

    return (
        f"{experiment['id']} | "
        f"{experiment['name']} | "
        f"Status: {experiment['status']} | "
        f"Version: {experiment['version']} | "
        f"Build: {experiment['build']}"
    )


def print_active_experiment():
    experiment = get_active_experiment()
    for key, value in experiment.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print_active_experiment()
