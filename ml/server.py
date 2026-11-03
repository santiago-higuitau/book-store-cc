"""Adaptador HTTP del contrato de inferencia de SageMaker: GET /ping y POST /invocations."""
from __future__ import annotations

import json
import logging
import os
from functools import partial
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import List, Optional

from bookstore_ml.serving import InvalidRequestError, RecommendationService, format_response, parse_request
from bookstore_ml.storage import ModelStore

DEFAULT_MODEL_DIR = "/opt/ml/model"
DEFAULT_PORT = 8080
MAX_BODY_BYTES = 64 * 1024

logger = logging.getLogger("server")


class InvocationHandler(BaseHTTPRequestHandler):
    def __init__(self, service: RecommendationService, *args, **kwargs) -> None:
        self._service = service
        super().__init__(*args, **kwargs)

    def do_GET(self) -> None:
        if self.path == "/ping":
            self._reply(200, "")
        else:
            self._reply_error(404, "ruta no encontrada")

    def do_POST(self) -> None:
        if self.path != "/invocations":
            self._reply_error(404, "ruta no encontrada")
            return
        try:
            self._reply(200, self._invoke(self._read_body()))
        except _PayloadTooLargeError:
            self._reply_error(413, "cuerpo demasiado grande")
        except InvalidRequestError as error:
            self._reply_error(400, str(error))
        except Exception:
            logger.exception("Error al procesar la invocación")
            self._reply_error(500, "error interno")

    def _invoke(self, body: bytes) -> str:
        return format_response(self._service.recommend(parse_request(body)))

    def _read_body(self) -> bytes:
        length = int(self.headers.get("Content-Length", 0))
        if length > MAX_BODY_BYTES:
            raise _PayloadTooLargeError()
        return self.rfile.read(length)

    def _reply_error(self, status: int, message: str) -> None:
        self._reply(status, json.dumps({"error": message}))

    def _reply(self, status: int, body: str) -> None:
        payload = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


class _PayloadTooLargeError(Exception):
    pass


def main(argv: Optional[List[str]] = None) -> None:
    logging.basicConfig(level=logging.INFO)
    model_dir = Path(os.environ.get("MODEL_DIR", DEFAULT_MODEL_DIR))
    port = int(os.environ.get("PORT", DEFAULT_PORT))
    service = RecommendationService(ModelStore(model_dir).load())
    server = ThreadingHTTPServer(("0.0.0.0", port), partial(InvocationHandler, service))
    logger.info("Sirviendo modelo de %s en el puerto %s", model_dir, port)
    server.serve_forever()


if __name__ == "__main__":
    main()
