#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>

#define TESTE "\n\nPassou aqui\n\n"


int main()
{
    char input[256] = "";
    int pid;

    while (strcmp(input, "termina") != 0){
        printf("%% ");
        fgets(input, 256, stdin);
        printf("\n%s\n\n", );

        strtok(input)

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

