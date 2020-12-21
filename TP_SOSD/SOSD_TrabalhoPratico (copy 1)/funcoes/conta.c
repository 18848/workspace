#include <unistd.h>
#include <stdlib.h>
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
		write(STDERR_FILENO, "Too many arguments.\n", 21);
		exit(EXIT_FAILURE);
	} else if(argc < 2){
		write(STDERR_FILENO, "Missing arguments.\n", 20);
		exit(EXIT_FAILURE);
	}
	fd = open(argv[1], O_RDONLY);
	/* Check file valid. If not, return error. */
	if(fd < 0){
		write(STDERR_FILENO, "Não foi possível abrir o ficheiro.", 37);
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
	write(STDOUT_FILENO, "Resultado: ", 12);
	write(STDOUT_FILENO, resultado, sizeof(resultado));
	write(STDOUT_FILENO, "\n", 2);
	close(fd);
	return 0;
}
