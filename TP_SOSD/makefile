all: Program clean

Program: main.o ficheiro.o utilities.o
	gcc -g -o Program main.o ficheiro.o utilities.o

main.o: main.c ficheiro.h
	gcc -g -o main.o main.c -c -W -Wall -ansi -pedantic

ficheiro.o: ficheiro.c ficheiro.h utilities.h
	gcc -g -o ficheiro.o ficheiro.c -c -W -Wall -ansi -pedantic

utilities.o: utilities.c utilities.h
	gcc -g -o utilities.o utilities.c -c -W -Wall -ansi -pedantic

clean:
	rm -rf *o *~ 