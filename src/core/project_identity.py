from pathlib import Path
import yaml


ROOT_DIR = Path(__file__).resolve().parents[2]
PROJECT_CONFIG_PATH = ROOT_DIR / "config" / "project.yaml"
ACTIVE_EXPERIMENT_PATH = ROOT_DIR / "experiments" / "active.yaml"


def _read_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def get_project_identity() -> dict:
    project_config = _read_yaml(PROJECT_CONFIG_PATH)
    active_experiment = _read_yaml(ACTIVE_EXPERIMENT_PATH)

    project = project_config.get("project", {})
    experiment_ref = project_config.get("experiment", {})
    database = project_config.get("database", {})
    runtime = project_config.get("runtime", {})

    experiment_data = active_experiment.get("experiment", active_experiment)

    return {
        "project_name": project.get("name", "HunterMini"),
        "display_name": project.get("display_name", "HunterMini"),
        "version": project.get("version", "1.0.0"),
        "build": project.get("build", "v1.0.0"),
        "environment": project.get("environment", "validation"),
        "active_experiment": experiment_ref.get("active") or experiment_data.get("id", "EXP-001"),
        "experiment_name": experiment_data.get("name", "Unknown Experiment"),
        "experiment_status": experiment_data.get("status", "Unknown"),
        "experiment_version": experiment_data.get("version", "Unknown"),
        "database_name": database.get("name", "Hunter_mini.db"),
        "database_path": database.get("path", "data/Hunter_mini.db"),
        "pm2_name": runtime.get("pm2_name", "HunterMini"),
        "port": runtime.get("port", 8083),
    }


def print_project_identity():
    identity = get_project_identity()
    for key, value in identity.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print_project_identity()
