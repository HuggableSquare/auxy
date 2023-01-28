FROM python:3.10-alpine

RUN pip install poetry

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .

ENTRYPOINT ["./docker-entrypoint.sh"]
