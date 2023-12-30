FROM python:3.10-slim as builder
WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev build-essential

RUN python3 -m venv /app/venv
ENV PATH=/app/venv/bin:$PATH

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

FROM python:3.10-slim as runner
WORKDIR /app
RUN apt-get update \
    && apt-get -y install libpq5

COPY --from=builder /app /app
COPY . .

ENV PATH=/app/venv/bin:/app:$PATH
ENV PYTHONUNBUFFERED 1
CMD ["python3", "-u", "main.py"]
