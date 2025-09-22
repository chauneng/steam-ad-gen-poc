"""Database manager for handling database connections and operations."""

from typing import Dict, List

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.dto.config import DatabaseConfig


class DatabaseManager:
    """Manager for handling database connections and operations using SQLAlchemy."""

    _connections: Dict[str, AsyncEngine]
    _session_factories: Dict[str, async_sessionmaker[AsyncSession]]

    def __init__(self, config: DatabaseConfig) -> None:
        """Initialize the DatabaseManager."""
        self._connections = {}
        self._session_factories = {}
        self.create_connection("default", config)

    def create_db_url(self, db_config: DatabaseConfig) -> str:
        """
        Create a SQLAlchemy URL from the given database configuration.

        Args:
            db_config: Database configuration.

        Returns:
            URL: SQLAlchemy URL object.
        """
        driver = f"{db_config.type}+{db_config.dbapi}"
        return URL.create(
            drivername=driver,
            username=db_config.user,
            password=db_config.password,
            host=db_config.host,
            port=db_config.port,
            database=db_config.name,
        ).render_as_string(hide_password=False)

    def create_connection(self, alias: str, db_config: DatabaseConfig) -> AsyncEngine:
        """
        Create an asynchronous engine from the given configuration.

        Raises:
            ValueError: If the alias already exists.
        """
        if alias in self._connections:
            raise ValueError(f"Connection alias '{alias}' already exists.")

        driver = f"{db_config.type}+{db_config.dbapi}"
        url = URL.create(
            drivername=driver,
            username=db_config.user,
            password=db_config.password,
            host=db_config.host,
            port=db_config.port,
            database=db_config.name,
        )
        engine = create_async_engine(
            url,
            pool_size=int(db_config.pool_size),
            max_overflow=int(db_config.max_overflow),
            pool_timeout=int(db_config.pool_timeout),
            echo=bool(db_config.echo),
            future=True,
        )
        self._connections[alias] = engine

        session_factory = async_sessionmaker(
            bind=engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
            future=True,
        )
        self._session_factories[alias] = session_factory

        return engine

    def get_session_factory(self, alias: str) -> async_sessionmaker[AsyncSession]:
        """
        Retrieve a session factory by alias.

        Args:
            alias (str): The connection alias.

        Returns:
            async_sessionmaker: The session factory associated with the alias.
        """
        try:
            return self._session_factories[alias]
        except KeyError as exc:
            raise KeyError(f"Session factory '{alias}' does not exist.") from exc

    def get_connection(self, alias: str) -> AsyncEngine:
        """
        Retrieve an engine by alias.

        Raises:
            KeyError: If alias not found.
        """
        try:
            return self._connections[alias]
        except KeyError as exc:
            raise KeyError(f"Connection alias '{alias}' does not exist.") from exc

    async def dispose_connection(self, alias: str) -> None:
        """
        Dispose a single connection, awaiting async engines.

        Raises:
            KeyError: If alias not found.
        """
        if alias not in self._connections:
            raise KeyError(f"Connection alias '{alias}' does not exist.")
        engine = self._connections.pop(alias)
        await engine.dispose()
        # then dispose sync pool
        engine.sync_engine.dispose()

    async def dispose_all_connections(self) -> None:
        """
        Dispose all connections, awaiting async if needed.
        """
        # collect aliases to avoid mutation issues
        aliases: List[str] = list(self._connections.keys())
        for alias in aliases:
            await self.dispose_connection(alias)

    @property
    def aliases(self) -> List[str]:
        """List current connection aliases."""
        return list(self._connections.keys())
