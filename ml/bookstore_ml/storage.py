"""Lectura y escritura de datos (CSV) y de artefactos del modelo (npy y json, sin pickle)."""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable, List

import numpy as np

from .domain import Book, EventType, Interaction
from .model import ItemSimilarityModel

CATALOG_FILE = "catalog.csv"
INTERACTIONS_FILE = "interactions.csv"
SIMILARITY_FILE = "similarity.npy"
METADATA_FILE = "meta.json"

_INTERACTION_COLUMNS = ["session_id", "book_id", "event_type"]


def read_catalog(path: Path) -> List[Book]:
    with path.open(newline="", encoding="utf-8") as handle:
        return [Book(row["book_id"], row["category"]) for row in csv.DictReader(handle)]


def read_interactions(path: Path) -> List[Interaction]:
    with path.open(newline="", encoding="utf-8") as handle:
        return [
            Interaction(row["session_id"], row["book_id"], EventType(row["event_type"]))
            for row in csv.DictReader(handle)
        ]


def write_interactions(path: Path, interactions: Iterable[Interaction]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(_INTERACTION_COLUMNS)
        for item in interactions:
            writer.writerow([
                item.session_id,
                item.book_id,
                item.event_type.value
            ])
            count += 1
    return count


class ModelStore:
    def __init__(self, directory: Path) -> None:
        self._directory = directory

    def save(self, model: ItemSimilarityModel) -> None:
        self._directory.mkdir(parents=True, exist_ok=True)
        np.save(self._directory / SIMILARITY_FILE, model.similarity, allow_pickle=False)
        metadata = {"book_ids": model.book_ids, "popularity": model.popularity.tolist()}
        (self._directory / METADATA_FILE).write_text(json.dumps(metadata), encoding="utf-8")

    def load(self) -> ItemSimilarityModel:
        similarity = np.load(self._directory / SIMILARITY_FILE, allow_pickle=False)
        metadata = json.loads((self._directory / METADATA_FILE).read_text(encoding="utf-8"))
        popularity = np.asarray(metadata["popularity"], dtype=np.float32)
        return ItemSimilarityModel(metadata["book_ids"], similarity, popularity)
