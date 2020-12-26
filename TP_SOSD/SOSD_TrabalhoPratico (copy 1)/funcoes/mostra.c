#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <fcntl.h> /* Constantes para função open() */

int main(int argc, const char* argv[])
{
    int fd, leitura;
	char buffer[21];
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
	/* Read */
	leitura = read(fd, buffer, sizeof(buffer)-1);
	while(leitura > 0){
		write(STDOUT_FILENO, buffer, leitura);
		leitura = read(fd, buffer, sizeof(buffer)-1);
	}
	write(STDOUT_FILENO, "\n\n", 3);
	/* -1 houve erro */
	if (leitura == -1) return 1;
	close(fd);
	return 0;
}
