FROM ubuntu:24.04@sha256:4f1db91d9560cf107b5832c0761364ec64f46777aa4ec637cca3008f287c975e AS builder

RUN apt update -y && apt install -y gcc make

WORKDIR /build
COPY babyheap.c .
COPY Makefile .
RUN make

WORKDIR /out
RUN cp /build/babyheap .
RUN cp /lib/x86_64-linux-gnu/libc.so.6 .
RUN cp /lib64/ld-linux-x86-64.so.2 .

FROM scratch AS output

WORKDIR /out
COPY --from=builder /out .