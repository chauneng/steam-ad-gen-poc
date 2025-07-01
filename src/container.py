"""Dependency Injection Container for the application."""

from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    """Simple Container for Dependency Injection."""

    # Configuration provider
    config = providers.Configuration()

