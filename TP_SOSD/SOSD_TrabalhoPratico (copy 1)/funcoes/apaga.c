#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <fcntl.h>

int main(int argc, const char* argv[])
{
    int fd;
    if(argc > 2){
		write(STDERR_FILENO, "Too many arguments.\n\n", 21);
		exit(EXIT_FAILURE);
	} else if(argc < 2){
		write(STDERR_FILENO, "Missing arguments.\n\n", 20);
		exit(EXIT_FAILURE);
	}
	fd = open(argv[1], O_RDONLY);
	/* Check file valid. If not, return error. */
	if(fd < 0){
		write(STDERR_FILENO, "Não foi possível abrir o ficheiro.\n\n\n", 37);
		return WEXITSTATUS(fd);
	}
    close(fd);
    return unlink(argv[1]);
}