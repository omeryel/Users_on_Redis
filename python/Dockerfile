FROM python:latest

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


RUN  python -m pip install grpcio-tools
RUN  python -m pip install grpcio
ONBUILD COPY .  /usr/src/app
ADD .  /usr/src/app

CMD ["python"]