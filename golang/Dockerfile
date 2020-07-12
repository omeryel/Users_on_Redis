# Dockerfile for gRPC Go
FROM golang:1.9

# install protobuf from source
RUN apt-get update && \
    apt-get -y install git unzip build-essential autoconf libtool
RUN git clone https://github.com/google/protobuf.git && \
    cd protobuf && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    ldconfig && \
    make clean && \
    cd .. && \
    rm -r protobuf

workdir /usr/src/app

run go get -u github.com/golang/protobuf/proto
run go get -u google.golang.org/grpc
run go get -u google.golang.org/grpc/codes
run go get -u google.golang.org/grpc/status
run go get -u google.golang.org/protobuf/reflect/protoreflect
run go get -u google.golang.org/protobuf/runtime/protoimpl

cmd ["go","run","client.go"]
