#include <sys/types.h>
#include <dirent.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

char* getFileType(int type);

int main(int argc, const char* argv[])
{
	DIR *dir;
	struct dirent *d;
	char cwd[200];

    if(argc > 2){
		printf("Too many arguments.\n");
		exit(EXIT_FAILURE);
	} else if(argc < 1){
		printf("Missing arguments.\n");
		exit(EXIT_FAILURE);
	}

	if (argc == 1){
		argv[1] = getcwd(cwd, sizeof(cwd));
	}

	if ((dir = opendir(argv[1])) == NULL){
		perror("ERRO");
		exit(1);
	}

	while((d = readdir(dir)) != NULL){
			printf("%s - %s\n", d->d_name, getFileType(d->d_type));
	}

	closedir(dir);

    return 0;
}

char* getFileType(int type){
	if (/*DT_REG(type)*/ type == 8){ return ("File"); }
	else if (/*DT_DIR(type)*/ type == 4){ return ("Dir"); }
	else return ("Outro");
}