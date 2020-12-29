#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/wait.h>
#include <fcntl.h> /* Constantes para função open() */

#include "utilities.h"

int main(int argc, const char* argv[])
{
    int fd, leitura;
	char buffer;
	long int total = 0;
	char* resultado;
	if(argc > 2){
		printf("Too many arguments.\n");
		exit(EXIT_FAILURE);
	} else if(argc < 2){
		printf("Missing arguments.\n");
		exit(EXIT_FAILURE);
	}
	fd = open(argv[1], O_RDONLY);
	/* Check file valid. If not, return error. */
	if(fd < 0){
		printf("Não foi possível abrir o ficheiro.");
		return WEXITSTATUS(fd);
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
	printf("Resultado: ");
	write(STDOUT_FILENO, resultado, strsize(resultado));
	printf("\n");
	close(fd);
	return 0;
}
