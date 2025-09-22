# src/dto/config.py
from __future__ import annotations

from typing import Any, Dict, Literal

from pydantic import BaseModel, Field, field_validator, model_validator


class AppConfig(BaseModel):
    environment: Literal["local", "docker", "production"] = Field(...)
    database: DatabaseConfig
    http_clients: Dict[str, HttpClientConfig]

    @field_validator("http_clients", mode="before")
    @classmethod
    def http_clients_not_empty(cls, v: Any) -> Dict[str, HttpClientConfig]:
        if not v:
            raise ValueError(
                "http_clients must contain at least one client configuration"
            )
        return v

    @model_validator(mode="after")
    def check_http_client_consistency(self) -> "AppConfig":
        """
        모델 인스턴스 수준의 추가 검증:
        - max_keepalive_connections <= max_connections
        """
        for name, client in self.http_clients.items():
            if client.max_keepalive_connections > client.max_connections:
                raise ValueError(
                    f"http_clients['{name}'].max_keepalive_connections "
                    "cannot be greater than max_connections"
                )
        return self


class DatabaseConfig(BaseModel):
    type: str = Field(..., description="데이터베이스 타입 (예: postgresql, mysql 등)")
    dbapi: str = Field(..., description="DBAPI 드라이버 (예: psycopg)")
    name: str
    user: str
    password: str
    host: str
    port: int = Field(..., ge=1, le=65535)
    pool_size: int = Field(5, ge=0)
    max_overflow: int = Field(10, ge=0)
    pool_timeout: int = Field(30, ge=0)
    echo: bool = Field(False)
    future: bool = Field(True)

    @field_validator("type", "dbapi", mode="before")
    @classmethod
    def lower_str(cls, v: Any) -> Any:
        if isinstance(v, str):
            return v.lower()
        return v


class HttpClientConfig(BaseModel):
    timeout_connect: float = Field(..., ge=0, description="초 단위")
    timeout_read: float = Field(..., ge=0, description="초 단위")
    max_connections: int = Field(..., ge=1)
    max_keepalive_connections: int = Field(..., ge=0)
    headers: Dict[str, str] = Field(default_factory=dict)
    http2: bool = Field(False)
