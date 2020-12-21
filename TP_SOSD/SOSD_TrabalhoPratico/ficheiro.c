/* #include <stdlib.h> */

#include <unistd.h>
#include <fcntl.h> /* Constantes para função open() */

#include "ficheiro.h"
#include "utilities.h"


int mostra(char* nome){
	int fd, leitura;
	char buffer[21];
	fd = open(nome, O_RDONLY);
	/* Check file valid */
	if(fd < 0) return -1;
	/* Read */
	leitura = read(fd, buffer, sizeof(buffer)-1);
	while(leitura > 0){
		write(STDOUT_FILENO, buffer, leitura);
		leitura = read(fd, buffer, sizeof(buffer)-1);
	}
	write(STDOUT_FILENO, "\n", 2);
	/* -1 houve erro */
	if (leitura == -1) return 1;
	close(fd);
	return 0;
}

int conta(char* nome){
	int fd, leitura;
	char buffer;
	long int total = 0;
	char* resultado;
	fd = open(nome, O_RDONLY);

	/* Check file valid */
	if(fd == -1){
		write(STDERR_FILENO, "Não foi possível abrir o ficheiro.", 37);
		return -1;
	}
	/* Check character -> increment */
	leitura = read(fd, &buffer, sizeof(buffer));
	while(leitura > 0){
		leitura = read(fd, &buffer, sizeof(buffer));
		total++;
	}
	/* -1 houve erro */
	if (leitura == -1) return 1;
	itostring(total, &resultado);
	write(STDOUT_FILENO, "Resultado: ", 12);
	write(STDOUT_FILENO, resultado, sizeof(resultado));
	write(STDOUT_FILENO, "\n", 2);
	close(fd);
	return 0;
}

int apaga(char* nome){
	return unlink(nome);
}