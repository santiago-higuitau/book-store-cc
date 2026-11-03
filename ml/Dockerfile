ARG PYTHON_IMAGE=python:3.13-slim
FROM ${PYTHON_IMAGE}

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /opt/program

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bookstore_ml ./bookstore_ml
COPY entrypoint.py generate_data.py train.py server.py ./

# SageMaker agrega "train" o "serve" como argumento
ENTRYPOINT ["python", "entrypoint.py"]
