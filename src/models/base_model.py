"""Base model for all database models using SQLAlchemy ORM with PostgreSQL."""

from sqlalchemy import Column, text
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, declared_attr


class BaseModel(DeclarativeBase):
    """
    BaseModel ensures all models use the same database.
    """


class CommonMixin:
    """
    CommonMixin provides automatic table naming.
    """

    __abstract__ = True

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()


class TimestampMixin:
    """
    TimestampMixin adds created_at and updated_at fields,
    managed at the database level using NOW().
    """

    __abstract__ = True

    created_at = Column(
        TIMESTAMP(timezone=False),
        server_default=text("NOW()"),
        nullable=False,
    )
    updated_at = Column(
        TIMESTAMP(timezone=False),
        server_default=text("NOW()"),
        server_onupdate=text("NOW()"),
        nullable=False,
    )


class SoftDeleteMixin:
    """
    SoftDeleteMixin adds a deleted_at field for soft deletion.
    """

    __abstract__ = True

    deleted_at = Column(
        TIMESTAMP(timezone=False),
        nullable=True,
    )
