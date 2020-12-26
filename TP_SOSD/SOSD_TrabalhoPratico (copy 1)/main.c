#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>

#include "funcoes/utilities.h"

void stringSpliter(char *str);

int main()
{
    char input[256] = "";
    int pid;
    char *args[] = {""};

    int size;

    while (strcmp(input, "termina") != /*0*/4){
        printf("%% ");
        fgets(input, 256, stdin);

        stringSpliter(input);

        /*size = strsize(input);
        input[size] = '/0';

        printf("\t%d \t%d\n\n", strcmp(input, "termina"), size);*/


    }

    /*char *args[] = {"informa", "teste/mostra.txt"};

        pid = fork();

        if(pid == -1){
            printf("erro");
            exit(EXIT_FAILURE);
        }

        if (pid == 0){
            execv(args[0], args);
        } else {
            wait(NULL);
            printf("\n\nCorreu bem.\n\n");
        }*/

    return 0;
}

void stringSpliter(char *str){
	char *ptr = strtok(str, " ");

	while(ptr != NULL)
	{
		printf("'%s'\n", ptr);
		ptr = strtok(NULL, " ");
	}

	printf("\n");
}