#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <pwd.h>
#include <stdio.h>
#include <stdlib.h>

char* getFileType(int mode);
char* getUserName(int id);

int main(int argc, const char* argv[])
{
	struct stat inf;

	if(argc > 2){
		printf("Too many arguments.\n");
		exit(EXIT_FAILURE);
	} else if(argc < 2){
		printf("Missing arguments.\n");
		exit(EXIT_FAILURE);
	}

	if (stat(argv[1], &inf) == -1) {
		perror("ERRO: ");
		exit(EXIT_FAILURE);
	}

	printf("Tipo de Ficheiro: %s\n", getFileType(inf.st_mode));
	printf("I-node: %ld\n", inf.st_ino);
	printf("Dono: %s\n", getUserName(inf.st_uid));

	return 0;
}

char* getFileType(int mode){
	if (S_ISREG(mode)){ return ("Ficheiro Normal"); }
	else if (S_ISDIR(mode)){ return ("Diretoria"); }
	else if (S_ISLNK(mode)){ return ("Link"); }
	else if (S_ISCHR(mode)){ return ("Caracteres"); }
	else if (S_ISBLK(mode)){ return ("Bloco"); }
	else if (S_ISFIFO(mode)){ return ("FIFO/pipe"); }
	/*if (S_ISSOCK(mode)){ return ("Socket"); }*/
	
	else return ("ERRO");
}

char* getUserName(int id){
	struct passwd *pass;
	pass = getpwuid(id);
	return (pass->pw_name);
}