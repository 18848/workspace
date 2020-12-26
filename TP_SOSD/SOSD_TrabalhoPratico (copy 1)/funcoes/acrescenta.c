#include <fcntl.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char* argv[])
{
	int fd1, fd2, leitura;
	char buffer[21];

    if(argc > 3){
		printf("Too many arguments.\n");
		exit(EXIT_FAILURE);
	} else if(argc < 3){
		printf("Missing arguments.\n");
		exit(EXIT_FAILURE);
	}

	fd1 = open(argv[1], O_RDONLY);
	if(fd1 < 0){
		printf("Não foi possível aceder a %s\n", argv[1]);
		return WEXITSTATUS(fd1);
	}

	fd2 = open(argv[2], O_WRONLY | O_APPEND);
	if(fd2 < 0){
		printf("Não foi possível aceder a %s\n", argv[2]);
		return WEXITSTATUS(fd2);
	}

	/* Read */
	leitura = read(fd1, buffer, sizeof(buffer)-1);
	while(leitura > 0){
		write(fd2, buffer, leitura);
		leitura = read(fd1, buffer, sizeof(buffer)-1);
	}
	
	/* -1 houve erro */
	if (leitura == -1) 
		return 1;
	
	close(fd1);
	close(fd2);

	return 0;
}