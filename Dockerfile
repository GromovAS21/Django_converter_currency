FROM python:3.12-slim

WORKDIR /app

COPY ./pyproject.toml ./

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev --no-root

COPY . .

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8080"]