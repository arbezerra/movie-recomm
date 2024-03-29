FROM python:3.10-alpine as builder
WORKDIR /app

RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev \
            libpq-dev

RUN python3 -m venv /app/venv
ENV PATH=/app/venv/bin:$PATH

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

FROM python:3.10-alpine as runner
WORKDIR /app
RUN apk add --no-cache pcre libpq libgomp libstdc++

COPY --from=builder /app /app
COPY . .

ENV PATH=/app/venv/bin:/app:$PATH
ENV PYTHONUNBUFFERED 1
ENTRYPOINT [ "./entrypoint.sh" ]
CMD ["uwsgi", "--ini", "/app/wsgi.ini"]
