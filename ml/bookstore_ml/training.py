"""Entrenamiento: calcula similitud coseno entre libros a partir de las sesiones."""
from __future__ import annotations

from types import MappingProxyType
from typing import Mapping, Sequence

import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

from .domain import EventType, Interaction
from .model import ItemSimilarityModel
from .session_matrix import build_session_item_matrix

DEFAULT_EVENT_WEIGHTS: Mapping[EventType, float] = MappingProxyType(
    {EventType.VIEW: 1.0, EventType.PURCHASE: 3.0}
)


def train_model(
    interactions: Sequence[Interaction],
    event_weights: Mapping[EventType, float] = DEFAULT_EVENT_WEIGHTS,
) -> ItemSimilarityModel:
    if not interactions:
        raise ValueError("No hay interacciones para entrenar")
    matrix, book_ids = build_session_item_matrix(interactions, event_weights)
    return ItemSimilarityModel(book_ids, _item_similarity(matrix), _popularity(matrix))


def _item_similarity(matrix: csr_matrix) -> np.ndarray:
    similarity = cosine_similarity(matrix.T, dense_output=True)
    np.fill_diagonal(similarity, 0.0)
    return similarity.astype(np.float32)


def _popularity(matrix: csr_matrix) -> np.ndarray:
    return np.asarray(matrix.sum(axis=0), dtype=np.float32).ravel()
