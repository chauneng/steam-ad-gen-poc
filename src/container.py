"""Dependency Injection Container for the application."""

from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    """Simple Container for Dependency Injection."""

    # Configuration provider
    config = providers.Configuration(json_files=["local.config.json"])
    config.load()


if __name__ == "__main__":
    # Testing the container setup
    container = Container()
    # Load the configuration
    cfg = container.config()
    # Accessing a specific configuration value
    print(cfg["database"]["host"])
