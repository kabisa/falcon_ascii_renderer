FROM frolvlad/alpine-python3

RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
    build-base \
    libjpeg-turbo-dev \
    python3-dev \
    zlib-dev

RUN pip3 install --no-cache pipenv

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

WORKDIR /app

COPY Pipfile* ./

RUN pipenv install --system --ignore-pipfile --dev

COPY . .
