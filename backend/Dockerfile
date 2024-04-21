FROM python:3.11

RUN mkdir /opt/data4good

WORKDIR /opt/data4good

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

CMD ["poetry" , "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]