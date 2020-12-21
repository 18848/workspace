#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/wait.h>

#include "mysystem.h"
#include "funcoes/utilities.h"

int teste()
{
    char* cmd = "mostra";
    int status = 0;
    char* filename = "teste/mostra.txt";
    write(STDOUT_FILENO, "\nFilename: ", 12);
    write(STDOUT_FILENO, filename, strsize(filename));
    write(STDOUT_FILENO, "\n", 2);

    write(STDOUT_FILENO, "Command: ", 10);
    write(STDOUT_FILENO, cmd, strsize(cmd));
    write(STDOUT_FILENO, "\n", 2);
    status = mysystem(cmd, &filename);
    return status;
}


int main()
{
    int leitura;
    int size;
    char* buffer = "";
    char cmd[20];
    char* args[20];
    /*while(strcmp(*cmd, "termina") != 0){*/
    size = 0;
    while(1){
        write(STDOUT_FILENO, "% ", 3);
        read(STDIN_FILENO, cmd, 19);
        cmd[strsize(cmd) - 1] = '\0';
        write(STDOUT_FILENO, cmd, strsize(cmd));
        args[size] = cmd;
        write(STDOUT_FILENO, "\n", 2);
        write(STDOUT_FILENO, args[size], strsize(args[size]));
        write(STDOUT_FILENO, "\n", 2);
        size++;
    }

    return 0;
}

