#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/wait.h>
#include <fcntl.h>

int main(int argc, const char* argv[])
{
    int fd;
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
		printf("Não foi possível abrir o ficheiro.\n");
		return WEXITSTATUS(fd);
	}
    close(fd);
    return unlink(argv[1]);
}