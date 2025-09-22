"""Dependency Injection Container for the application."""

from dependency_injector import containers, providers

from .database_manager import DatabaseManager
from .http_client_manager import HttpClientManager


class Container(containers.DeclarativeContainer):
    """Simple Container for Dependency Injection."""

    # Configuration provider
    config = providers.Configuration()

    # database provider
    db_manager = providers.Singleton(DatabaseManager, config=config.database)

    # HTTP client provider
    http_client = providers.Singleton(HttpClientManager, config=config.http_clients)
