"""Punto de entrada del contenedor: elige la operación según el primer argumento.

SageMaker ejecuta la imagen con `train` (entrenamiento) o `serve` (inferencia).
`generate` produce los datos sintéticos con la misma imagen.
"""
from __future__ import annotations

import sys
from typing import Callable, Dict, List

import generate_data
import server
import train

COMMANDS: Dict[str, Callable[[List[str]], None]] = {
    "generate": generate_data.main,
    "train": train.main,
    "serve": server.main,
}


def main(argv: List[str]) -> int:
    if len(argv) < 2 or argv[1] not in COMMANDS:
        print(f"Uso: entrypoint.py {{{'|'.join(COMMANDS)}}} [opciones]", file=sys.stderr)
        return 2
    COMMANDS[argv[1]](argv[2:])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
