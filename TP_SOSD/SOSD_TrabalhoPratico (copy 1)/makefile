all: Funcoes Program clean

Funcoes: mostra conta apaga informa acrescenta lista

utilities.o: funcoes/utilities.c funcoes/utilities.h
	gcc -g -o utilities.o funcoes/utilities.c -c -W -Wall -ansi -pedantic

mostra: mostra.o 
	gcc -g -o mostra mostra.o
	chmod u+x mostra
	
mostra.o: funcoes/mostra.c 
	gcc -g -o mostra.o funcoes/mostra.c -c -W -Wall -ansi -pedantic

conta: conta.o utilities.o
	gcc -g -o conta conta.o utilities.o
	chmod u+x conta
	
conta.o: funcoes/conta.c 
	gcc -g -o conta.o funcoes/conta.c -c -W -Wall -ansi -pedantic

apaga: apaga.o 
	gcc -g -o apaga apaga.o
	chmod u+x apaga

apaga.o: funcoes/apaga.c
	gcc -g -o apaga.o funcoes/apaga.c -c -W -Wall -ansi -pedantic

informa: informa.o 
	gcc -g -o informa informa.o
	chmod u+x informa

informa.o: funcoes/informa.c
	gcc -g -o informa.o funcoes/informa.c -c -W -Wall -ansi -pedantic

acrescenta: acrescenta.o 
	gcc -g -o acrescenta acrescenta.o
	chmod u+x acrescenta

acrescenta.o: funcoes/acrescenta.c
	gcc -g -o acrescenta.o funcoes/acrescenta.c -c -W -Wall -ansi -pedantic

lista: lista.o 
	gcc -g -o lista lista.o
	chmod u+x lista

lista.o: funcoes/lista.c
	gcc -g -o lista.o funcoes/lista.c -c -W -Wall -ansi -pedantic

Program: main.o utilities.o mysystem.o
	gcc -g -o Program main.o utilities.o mysystem.o

main.o: main.c 
	gcc -g -o main.o main.c -c -W -Wall -ansi -pedantic

mysystem.o: mysystem.c mysystem.h
	gcc -g -o mysystem.o mysystem.c -c -W -Wall -ansi -pedantic

clean:
	rm -rf *o *~ 

wipe:
	rm -rf *o Program mostra conta apaga informa acrescenta lista