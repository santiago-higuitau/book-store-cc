"""Tipos del dominio. No dependen de ninguna librería externa."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class EventType(str, Enum):
    VIEW = "view"
    PURCHASE = "purchase"


@dataclass(frozen=True)
class Book:
    book_id: str
    category: str


@dataclass(frozen=True)
class Interaction:
    session_id: str
    book_id: str
    event_type: EventType


@dataclass(frozen=True)
class Recommendation:
    book_id: str
    score: float


class UnknownBookError(KeyError):
    """El libro consultado no existe en el modelo."""
