#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/wait.h>
#include <fcntl.h> /* Constantes para função open() */

int main(int argc, const char* argv[])
{
    int fd, leitura;
	char buffer[21];
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
	/* Read */
	leitura = read(fd, buffer, sizeof(buffer)-1);
	while(leitura > 0){
		write(STDOUT_FILENO, buffer, leitura);
		leitura = read(fd, buffer, sizeof(buffer)-1);
	}
	printf("\n\n");
	/* -1 houve erro */
	if (leitura == -1) return 1;
	close(fd);
	return 0;
}
