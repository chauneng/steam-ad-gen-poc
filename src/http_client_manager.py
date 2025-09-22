from typing import Dict
import httpx
import asyncio
import logging
from dto.config import HttpClientConfig

logger = logging.getLogger(__name__)


class HttpClientManager:
    """
    HTTP 통신을 위한 클라이언트를 관리한다.
    """

    def __init__(self, config: HttpClientConfig) -> None:
        self._clients: Dict[str, httpx.AsyncClient] = {}
        self._lock = asyncio.Lock()
        self._make_client(config)

    def _make_client(self, config: HttpClientConfig) -> httpx.AsyncClient:
        """httpx.AsyncClient 생성"""
        if config.name in self._clients:
            raise ValueError(f"HTTP client with name '{config.name}' already exists.")
        timeout = httpx.Timeout(
            connect=config.timeout_connect, read=config.timeout_read
        )
        limits = httpx.Limits(
            max_connections=config.max_connections,
            max_keepalive_connections=config.max_keepalive_connections,
        )
        return httpx.AsyncClient(
            timeout=timeout,
            limits=limits,
            headers=config.headers,
            http2=config.http2,
        )

    def get_client(self, name: str = "default") -> httpx.AsyncClient:
        """named client 반환"""
        if name in self._clients:
            return self._clients[name]
        raise ValueError(f"No HTTP client found with name '{name}'")

    async def close_all(self) -> None:
        """모든 client 닫기"""
        async with self._lock:
            clients = list(self._clients.values())
            self._clients.clear()

        results = await asyncio.gather(
            *(c.aclose() for c in clients),
            return_exceptions=True,
        )
        for r in results:
            if isinstance(r, Exception):
                logger.warning("Error closing httpx.AsyncClient: %s", r)
