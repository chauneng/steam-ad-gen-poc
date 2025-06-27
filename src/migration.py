"""Migration script to run Alembic migrations."""

from alembic import command
from alembic.config import Config


def run_migrations(db_url: str, alembic_ini_path: str):
    """
    Run Alembic migrations.
    Args:
        db_url (str): The database URL to connect to.
        alembic_ini_path (str): Path to the Alembic configuration file.
    """
    cfg = Config(alembic_ini_path)
    cfg.set_main_option("sqlalchemy.url", db_url)
    command.upgrade(cfg, "head")
