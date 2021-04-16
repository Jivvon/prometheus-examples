FROM python:3.7-alpine

RUN apk update && \
        apk add --no-cache \
        bash

# python 기본 패키지
RUN apk add --update build-base python3-dev py-pip
RUN apk --no-cache add curl

ENV LIBRARY_PATH=/lib:/usr/lib
ENV PYTHONUNBUFFERD 1

EXPOSE 8080

WORKDIR /app
COPY . /app

RUN --mount=type=cache,target=$PIP_CACHE_DIR pip3 install -r requirements.txt
ENTRYPOINT ["python", "/app/server-prometheus-client.py"]
#ENTRYPOINT ["python", "/app/server-http.py"]
