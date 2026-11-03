"""Construcción de la matriz sesión por libro a partir de interacciones."""
from __future__ import annotations

from typing import Dict, List, Mapping, Sequence, Tuple

from scipy.sparse import csr_matrix

from .domain import EventType, Interaction


def build_session_item_matrix(
    interactions: Sequence[Interaction],
    event_weights: Mapping[EventType, float],
) -> Tuple[csr_matrix, List[str]]:
    """Devuelve la matriz (sesiones x libros) y la lista de libros en el orden de sus columnas."""
    strongest = _strongest_weight_per_session_book(interactions, event_weights)
    sessions = sorted({session for session, _ in strongest})
    book_ids = sorted({book for _, book in strongest})

    row_of = {session: row for row, session in enumerate(sessions)}
    column_of = {book: column for column, book in enumerate(book_ids)}

    rows = [row_of[session] for session, _ in strongest]
    columns = [column_of[book] for _, book in strongest]
    values = list(strongest.values())
    matrix = csr_matrix((values, (rows, columns)), shape=(len(sessions), len(book_ids)))
    return matrix, book_ids


def _strongest_weight_per_session_book(
    interactions: Sequence[Interaction],
    event_weights: Mapping[EventType, float],
) -> Dict[Tuple[str, str], float]:
    strongest: Dict[Tuple[str, str], float] = {}
    for interaction in interactions:
        key = (interaction.session_id, interaction.book_id)
        weight = event_weights[interaction.event_type]
        strongest[key] = max(weight, strongest.get(key, 0.0))
    return strongest
