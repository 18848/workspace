#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>

#include "funcoes/utilities.h"

void stringSpliter(char *str, char *args[]);
void restoreArray(char *args[]);

int main()
{
    char input[256] = "";
    int pid, err = 0;
    char *args[3];

    while (strncmp(input, "termina", 7) != 0){

        restoreArray(args);

        printf("%% ");
        fgets(input, 256, stdin);
        printf("\n");

        stringSpliter(input, args);

        pid = fork();

        if(pid == -1){
            printf("erro");
            exit(EXIT_FAILURE);
        }

        if (pid == 0){
            err = execv(args[0], args);
        } else {
            wait(NULL);
            printf("\n\nTerminou comando %s com codigo %d.\n\n", args[0], err);
        }
    }



    return 0;
}

void stringSpliter(char *str, char *args[]){

    int i=0, size;
	char *ptr = strtok(str, " ");

	while(ptr != NULL)
	{
        args[i] = ptr;
		ptr = strtok(NULL, " ");
        i++;
	}

    size = strsize(args[i-1]);
    args[i-1][size] = '\0';
}

void restoreArray(char *args[]){

    int i;

    for (i=0; sizeof(*args) != i; i++){
        args[i] = NULL;
    }
}