#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>

#define TESTE "\n\nPassou aqui\n\n"


int main()
{
    /*char input[256] = "";*/
    int pid;
    int input = 1;

    while (/*strcmp(input, "termina")*/ input != 0){
        printf("%% ");
        scanf("%d", &input);
        /*fgets(input, 256, stdin);
        printf("\n%s\n\n", input);*/

        char *args[] = {"./informa", "teste/mostra.txt"};

        pid = fork();

        if(pid == -1){
            printf("erro");
            exit(EXIT_FAILURE);
        }

        if (pid == 0){
            execv(args[0], args);
        } else {
            wait(NULL);
            printf("\n\nCorreu bem ou mal %s %s\n\n", args[0], args[1]);
        }
    }

    return 0;
}

