.PHONY: all clean

all: babyheap

babyheap: babyheap.o
	gcc -Wl,-z,relro,-z,now -o babyheap babyheap.o

babyheap.o: babyheap.c
	gcc -Wall -Wextra -Wpedantic -c -o babyheap.o babyheap.c

clean:
	rm -f babyheap.o babyheap