"""Modelo item-item: guarda similitudes y popularidad y responde consultas."""
from __future__ import annotations

from itertools import islice
from typing import Iterator, List, Optional, Sequence

import numpy as np

from .domain import Recommendation, UnknownBookError


class ItemSimilarityModel:
    def __init__(self, book_ids: Sequence[str], similarity: np.ndarray, popularity: np.ndarray) -> None:
        size = len(book_ids)
        if similarity.shape != (size, size) or popularity.shape != (size,):
            raise ValueError("Dimensiones inconsistentes entre libros, similitud y popularidad")
        self._book_ids = list(book_ids)
        self._row_of = {book_id: row for row, book_id in enumerate(self._book_ids)}
        self._similarity = similarity
        self._popularity = popularity

    @property
    def book_ids(self) -> List[str]:
        return list(self._book_ids)

    @property
    def similarity(self) -> np.ndarray:
        return self._similarity

    @property
    def popularity(self) -> np.ndarray:
        return self._popularity

    def knows(self, book_id: str) -> bool:
        return book_id in self._row_of

    def recommend(self, book_id: str, limit: int) -> List[Recommendation]:
        row = self._row_of.get(book_id)
        if row is None:
            raise UnknownBookError(book_id)
        return self._rank(self._similarity[row], limit, excluded_row=row)

    def popular(self, limit: int, exclude_book_id: Optional[str] = None) -> List[Recommendation]:
        excluded_row = self._row_of.get(exclude_book_id) if exclude_book_id else None
        return self._rank(self._popularity, limit, excluded_row)

    def _rank(self, scores: np.ndarray, limit: int, excluded_row: Optional[int]) -> List[Recommendation]:
        ranked = (
            Recommendation(self._book_ids[row], float(scores[row]))
            for row in self._descending_rows(scores)
            if row != excluded_row and scores[row] > 0
        )
        return list(islice(ranked, limit))

    @staticmethod
    def _descending_rows(scores: np.ndarray) -> Iterator[int]:
        return iter(np.argsort(-scores, kind="stable"))
