FROM python:3.11-bullseye


RUN pip install --upgrade pip && \
    pip install --no-cache-dir "poetry" && \
    poetry config virtualenvs.in-project true

WORKDIR /app

COPY . .

RUN poetry install --no-root

ENTRYPOINT ["python", "-m", "t9autocomplete_demo"]