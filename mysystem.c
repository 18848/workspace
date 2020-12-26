#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

#include "funcoes/utilities.h"
#include "mysystem.h"

int mysystem(char* cmd, char* const* args){
    int retstatus;
    pid_t pid;

    if(command_construct(&cmd) == -1){
        write(STDERR_FILENO, "Erro na construção do comando.", 33);
        exit(EXIT_FAILURE);
    }

/**/
    write(STDOUT_FILENO, "Command: ", 10);
    write(STDOUT_FILENO, cmd, strsize(cmd));
    write(STDOUT_FILENO, "\n", 2);
    write(STDOUT_FILENO, "Filename: ", 11);
    write(STDOUT_FILENO, args[1], strsize(args[1]));
    write(STDOUT_FILENO, "\n", 2);
/**/
    pid = fork();

    if (pid == -1) {
        write(STDERR_FILENO, "Erro no fork.\n", 15);
        exit(EXIT_FAILURE);
    }

    if (pid == 0) /* filho */
    {
        execvp(cmd, args);
        write(STDERR_FILENO, "Erro no exec.\n", 15);
        exit(EXIT_FAILURE);
    }

    wait(&retstatus);
    return WEXITSTATUS(retstatus);
}

int command_construct(char** cmd){
    int initialSize = strsize(*cmd);
    char* result = str_append("./", *cmd);
    *cmd = result;
    if(strsize(*cmd) < initialSize + 2) return -1;
    return 0;
}
