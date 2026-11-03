"""Entrypoint de entrenamiento (SageMaker script mode o línea de comandos)."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import List, Optional

from bookstore_ml.domain import EventType
from bookstore_ml.storage import INTERACTIONS_FILE, ModelStore, read_interactions
from bookstore_ml.training import train_model

DEFAULT_INPUT_DIR = "/opt/ml/input/data/train"
DEFAULT_MODEL_DIR = "/opt/ml/model"


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path(os.environ.get("SM_CHANNEL_TRAIN", DEFAULT_INPUT_DIR)))
    parser.add_argument("--output", type=Path, default=Path(os.environ.get("SM_MODEL_DIR", DEFAULT_MODEL_DIR)))
    parser.add_argument("--view-weight", type=float, default=1.0)
    parser.add_argument("--purchase-weight", type=float, default=3.0)
    args, _ = parser.parse_known_args(argv)
    return args


def main(argv: Optional[List[str]] = None) -> None:
    args = parse_args(argv)
    weights = {EventType.VIEW: args.view_weight, EventType.PURCHASE: args.purchase_weight}
    interactions = read_interactions(args.input / INTERACTIONS_FILE)

    model = train_model(interactions, weights)
    ModelStore(args.output).save(model)
    print(f"Modelo entrenado: {len(model.book_ids)} libros, {len(interactions)} interacciones")


if __name__ == "__main__":
    main()
