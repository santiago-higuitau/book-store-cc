"""Simulación de sesiones de navegación y compra sobre un catálogo real."""
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Dict, Iterator, List, Sequence, Tuple

from .domain import Book, EventType, Interaction

Segment = Tuple[str, ...]

DEFAULT_SEGMENTS: Tuple[Segment, ...] = (
    ("Machine Learning", "Data Systems", "Data Engineering"),
    ("Software Engineering", "Software Architecture"),
    ("Programming", "Computer Science", "Distributed Systems"),
)


@dataclass(frozen=True)
class SimulationConfig:
    sessions: int = 3000
    seed: int = 42
    segments: Tuple[Segment, ...] = DEFAULT_SEGMENTS
    segment_affinity: float = 0.8
    min_views: int = 2
    max_views: int = 6
    purchase_probability: float = 0.35


class SessionSimulator:
    """Genera sesiones donde cada visitante pertenece a un segmento con categorías afines."""

    def __init__(self, catalog: Sequence[Book], config: SimulationConfig = SimulationConfig()) -> None:
        if not catalog:
            raise ValueError("El catálogo está vacío")
        self._config = config
        self._rng = random.Random(config.seed)
        self._all_books = [book.book_id for book in catalog]
        self._segment_books = self._books_per_segment(catalog)

    def run(self) -> Iterator[Interaction]:
        for number in range(self._config.sessions):
            yield from self._simulate_session(f"s{number:06d}")

    def _books_per_segment(self, catalog: Sequence[Book]) -> List[List[str]]:
        segment_of: Dict[str, int] = {
            category: index for index, segment in enumerate(self._config.segments) for category in segment
        }
        segments: List[List[str]] = [[] for _ in self._config.segments]
        for book in catalog:
            if book.category in segment_of:
                segments[segment_of[book.category]].append(book.book_id)
        non_empty = [books for books in segments if books]
        if not non_empty:
            raise ValueError("Ninguna categoría del catálogo pertenece a un segmento")
        return non_empty

    def _simulate_session(self, session_id: str) -> Iterator[Interaction]:
        segment = self._rng.choice(self._segment_books)
        for book_id in self._choose_viewed_books(segment):
            yield Interaction(session_id, book_id, EventType.VIEW)
            if self._rng.random() < self._config.purchase_probability:
                yield Interaction(session_id, book_id, EventType.PURCHASE)

    def _choose_viewed_books(self, segment: Sequence[str]) -> List[str]:
        wanted = min(self._rng.randint(self._config.min_views, self._config.max_views), len(self._all_books))
        chosen: List[str] = []
        while len(chosen) < wanted:
            chosen.append(self._rng.choice(self._candidates(segment, chosen)))
        return chosen

    def _candidates(self, segment: Sequence[str], chosen: Sequence[str]) -> List[str]:
        in_segment = [b for b in segment if b not in chosen]
        if in_segment and self._rng.random() < self._config.segment_affinity:
            return in_segment
        return [b for b in self._all_books if b not in chosen]
