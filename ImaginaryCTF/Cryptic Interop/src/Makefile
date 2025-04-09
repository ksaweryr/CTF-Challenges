all: jar

jar: Main.class libinterop.so.enc
	jar --create --file CrypticInterop.jar --main-class org.imaginaryctf.CrypticInterop.Main org/imaginaryctf/CrypticInterop/Main.class libinterop.so.enc

libinterop.so.enc: libinterop.so
	python3 encrypt.py

libinterop.so: Main.o Util.a
	g++ -shared -fPIC -o libinterop.so -pthread Main.o Util.a -lc

Main.o: Main.cpp headers
	g++ -c -fPIC -I/usr/lib/jvm/temurin-21-jdk-amd64/include -I/usr/lib/jvm/temurin-21-jdk-amd64/include/linux Main.cpp -o Main.o

Main.class: org/imaginaryctf/CrypticInterop/Main.java
	javac org/imaginaryctf/CrypticInterop/Main.java

Util.a: Util.go
	go build -buildmode=c-archive Util.go

headers: org/imaginaryctf/CrypticInterop/Main.java Util.go
	javac -h . org/imaginaryctf/CrypticInterop/Main.java
	go tool cgo -exportheader util.h Util.go

clean:
	rm *.o *.so org/imaginaryctf/CrypticInterop/*.class *.a *.h *.jar *.enc