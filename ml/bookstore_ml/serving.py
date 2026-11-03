"""Lógica de servicio: validar la petición, elegir la estrategia y dar formato a la respuesta."""
from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Protocol, Union

from .domain import Recommendation

DEFAULT_LIMIT = 5
MAX_LIMIT = 20


class InvalidRequestError(ValueError):
    """La petición no cumple el contrato JSON esperado."""


class Strategy(str, Enum):
    SIMILAR = "similar"
    POPULAR = "popular"


@dataclass(frozen=True)
class RecommendationRequest:
    book_id: str
    limit: int = DEFAULT_LIMIT


@dataclass(frozen=True)
class RecommendationResult:
    strategy: Strategy
    items: List[Recommendation]


class Recommender(Protocol):
    def knows(self, book_id: str) -> bool: ...

    def recommend(self, book_id: str, limit: int) -> List[Recommendation]: ...

    def popular(self, limit: int, exclude_book_id: Optional[str] = None) -> List[Recommendation]: ...


class RecommendationService:
    def __init__(self, recommender: Recommender) -> None:
        self._recommender = recommender

    def recommend(self, request: RecommendationRequest) -> RecommendationResult:
        if self._recommender.knows(request.book_id):
            similar = self._recommender.recommend(request.book_id, request.limit)
            if similar:
                return RecommendationResult(Strategy.SIMILAR, similar)

        popular = self._recommender.popular(request.limit, request.book_id)
        return RecommendationResult(Strategy.POPULAR, popular)


def parse_request(body: Union[str, bytes]) -> RecommendationRequest:
    payload = _load_json_object(body)
    return RecommendationRequest(_read_book_id(payload), _read_limit(payload))


def format_response(result: RecommendationResult) -> str:
    return json.dumps(
        {
            "strategy": result.strategy.value,
            "recommendations": [{"book_id": r.book_id, "score": round(r.score, 4)} for r in result.items],
        }
    )


def _load_json_object(body: Union[str, bytes]) -> dict:
    try:
        payload = json.loads(body)
    except (TypeError, ValueError) as error:
        raise InvalidRequestError("El cuerpo no es JSON válido") from error
    if not isinstance(payload, dict):
        raise InvalidRequestError("El cuerpo debe ser un objeto JSON")
    return payload


def _read_book_id(payload: dict) -> str:
    book_id = payload.get("book_id")
    if not isinstance(book_id, str) or not book_id.strip():
        raise InvalidRequestError("book_id es obligatorio")
    return book_id.strip()


def _read_limit(payload: dict) -> int:
    limit = payload.get("limit", DEFAULT_LIMIT)
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= MAX_LIMIT:
        raise InvalidRequestError(f"limit debe ser un entero entre 1 y {MAX_LIMIT}")
    return limit
