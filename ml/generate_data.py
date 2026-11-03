"""CLI: genera sesiones sintéticas (interactions.csv) a partir de un catálogo (catalog.csv)."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Optional

from bookstore_ml.simulation import SessionSimulator, SimulationConfig
from bookstore_ml.storage import INTERACTIONS_FILE, read_catalog, write_interactions


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--sessions", type=int, default=SimulationConfig.sessions)
    parser.add_argument("--seed", type=int, default=SimulationConfig.seed)
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> None:
    args = parse_args(argv)
    config = SimulationConfig(sessions=args.sessions, seed=args.seed)
    simulator = SessionSimulator(read_catalog(args.catalog), config)
    count = write_interactions(args.output_dir / INTERACTIONS_FILE, simulator.run())
    print(f"{count} interacciones en {args.output_dir / INTERACTIONS_FILE}")


if __name__ == "__main__":
    main()
