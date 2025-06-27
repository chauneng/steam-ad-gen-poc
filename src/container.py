"""Dependency Injection Container for the application."""

from dependency_injector import containers, providers

from .database_manager import DatabaseManager


class Container(containers.DeclarativeContainer):
    """Simple Container for Dependency Injection."""

    # Configuration provider
    config = providers.Configuration()

    # database provider
    db_manager = providers.Singleton(DatabaseManager)
