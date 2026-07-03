import sqlite3
from pathlib import Path

from src.core.experiment import get_experiment_trade_metadata
from src.core.project_identity import get_project_identity


ROOT_DIR = Path(__file__).resolve().parents[3]


def _column_exists(cursor, table_name: str, column_name: str) -> bool:
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [row[1] for row in cursor.fetchall()]
    return column_name in columns


def _add_column_if_missing(cursor, table_name: str, column_name: str, column_type: str):
    if not _column_exists(cursor, table_name, column_name):
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")
        print(f"Added column: {column_name}")
    else:
        print(f"Column already exists: {column_name}")


def migrate():
    identity = get_project_identity()
    db_path = ROOT_DIR / identity.get("database_path", "data/Hunter_mini.db")

    if not db_path.exists():
        raise FileNotFoundError(f"Database not found: {db_path}")

    metadata = get_experiment_trade_metadata()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    _add_column_if_missing(cursor, "trades", "experiment_id", "VARCHAR(32)")
    _add_column_if_missing(cursor, "trades", "experiment_name", "VARCHAR(128)")
    _add_column_if_missing(cursor, "trades", "experiment_version", "VARCHAR(32)")
    _add_column_if_missing(cursor, "trades", "experiment_build", "VARCHAR(64)")
    _add_column_if_missing(cursor, "trades", "experiment_status", "VARCHAR(32)")
    _add_column_if_missing(cursor, "trades", "experiment_tracked_at", "DATETIME")

    cursor.execute("""
        UPDATE trades
        SET
            experiment_id = COALESCE(experiment_id, ?),
            experiment_name = COALESCE(experiment_name, ?),
            experiment_version = COALESCE(experiment_version, ?),
            experiment_build = COALESCE(experiment_build, ?),
            experiment_status = COALESCE(experiment_status, ?),
            experiment_tracked_at = COALESCE(experiment_tracked_at, ?)
        WHERE experiment_id IS NULL
    """, (
        metadata["experiment_id"],
        metadata["experiment_name"],
        metadata["experiment_version"],
        metadata["experiment_build"],
        metadata["experiment_status"],
        metadata["tracked_at_utc"],
    ))

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS ix_trades_experiment_id
        ON trades (experiment_id)
    """)

    conn.commit()
    conn.close()

    print("Experiment tracking migration completed.")
    print(f"Database: {db_path}")
    print(f"Experiment: {metadata['experiment_id']} - {metadata['experiment_name']}")


if __name__ == "__main__":
    migrate()
