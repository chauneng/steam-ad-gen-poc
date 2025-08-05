"""Database manager for handling database connections and operations."""

from typing import Dict, List, Union

from sqlalchemy import URL, Engine
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


class DatabaseManager:
    """Manager for handling database connections and operations using SQLAlchemy."""

    __connections: Dict[str, Union[Engine, AsyncEngine]]

    def __init__(self):
        """Initialize the DatabaseManager."""
        self.__connections = {}
        self.__session_factories = {}

    def create_db_url(self, db_config: Dict[str, str]) -> str:
        """
        Create a SQLAlchemy URL from the given database configuration.

        Args:
            db_config (Dict[str, str]): Database configuration dictionary.

        Returns:
            URL: SQLAlchemy URL object.
        """
        driver = (
            f"{db_config.get('type', 'postgresql')}+{db_config.get('dbapi', 'psycopg')}"
        )
        return URL.create(
            drivername=driver,
            username=db_config["user"],
            password=db_config["password"],
            host=db_config.get("host", "localhost"),
            port=int(db_config.get("port", 5432)),
            database=db_config["name"],
        ).render_as_string(hide_password=False)

    def create_asynchronous_connection(
        self, alias: str, db_config: Dict[str, str]
    ) -> AsyncEngine:
        """
        Create an asynchronous engine from the given configuration.

        Raises:
            ValueError: If the alias already exists.
        """
        if alias in self.__connections:
            raise ValueError(f"Connection alias '{alias}' already exists.")

        driver = (
            f"{db_config.get('type', 'postgresql')}+{db_config.get('dbapi', 'psycopg')}"
        )
        url = URL.create(
            drivername=driver,
            username=db_config["user"],
            password=db_config["password"],
            host=db_config.get("host", "localhost"),
            port=int(db_config.get("port", 5432)),
            database=db_config["name"],
        )
        engine = create_async_engine(
            url,
            pool_size=int(db_config.get("pool_size", 5)),
            max_overflow=int(db_config.get("max_overflow", 10)),
            pool_timeout=int(db_config.get("pool_timeout", 30)),
            echo=bool(db_config.get("echo", False)),
            future=True,
        )
        self.__connections[alias] = engine

        session_factory = async_sessionmaker(
            bind=engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
            future=True,
        )
        self.__session_factories[alias] = session_factory

        return engine

    def get_session_factory(self, alias: str) -> async_sessionmaker:
        """
        Retrieve a session factory by alias.

        Args:
            alias (str): The connection alias.

        Returns:
            async_sessionmaker: The session factory associated with the alias.
        """
        try:
            return self.__session_factories[alias]
        except KeyError as exc:
            raise KeyError(f"Session factory '{alias}' does not exist.") from exc

    def get_connection(self, alias: str) -> Union[Engine, AsyncEngine]:
        """
        Retrieve an engine by alias.

        Raises:
            KeyError: If alias not found.
        """
        try:
            return self.__connections[alias]
        except KeyError as exc:
            raise KeyError(f"Connection alias '{alias}' does not exist.") from exc

    async def dispose_connection(self, alias: str) -> None:
        """
        Dispose a single connection, awaiting async engines.

        Raises:
            KeyError: If alias not found.
        """
        if alias not in self.__connections:
            raise KeyError(f"Connection alias '{alias}' does not exist.")
        engine = self.__connections.pop(alias)
        if isinstance(engine, AsyncEngine):
            # first close async engine
            await engine.dispose()
            # then dispose sync pool
            engine.sync_engine.dispose()
        else:
            engine.dispose()

    async def dispose_all_connections(self) -> None:
        """
        Dispose all connections, awaiting async if needed.
        """
        # collect aliases to avoid mutation issues
        aliases: List[str] = list(self.__connections.keys())
        for alias in aliases:
            await self.dispose_connection(alias)

    @property
    def aliases(self) -> List[str]:
        """List current connection aliases."""
        return list(self.__connections.keys())
