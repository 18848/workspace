#include <unistd.h>
#include <stdlib.h>

#include "ficheiro.h"
#include "utilities.h"

int main()
{
    int leitura = 0;
    char* buffer = 0;
    int stringSize = 0;
    char* string = 0;
    do
    {
        write(STDOUT_FILENO, "%", 2);
        leitura = read(STDIN_FILENO, buffer, 1);
        if(leitura == -1){
            write(STDOUT_FILENO, "\n\nAn error ocurred.\n", 21);
            exit(-1);
        }
        while(leitura > 0 && *buffer != '\n'){
            leitura = read(STDIN_FILENO, buffer, 1);
            if(*buffer != '\n') {
                string[stringSize++] = *buffer;
            }
        }
        string[stringSize] = '\0';
        write(STDOUT_FILENO, "\n", 2);
    } while (strcmp(string, "termina"));
    
    return 0;
}


int teste()
{
    int status;
    /* Funcao Mostra Ficheiro */
    write(STDOUT_FILENO, "Funcao Mostra Ficheiro:\n\n", 26);
    status = mostra("teste/mostra.txt");
    if(status == -1)
        write(STDERR_FILENO, "Nao foi possivel abrir o ficheiro. Nao existe.\n", 48);
    else if(status == 1)
        write(STDERR_FILENO, "Erro na leitura do ficheiro.\n", 30);
    
    /* Funcao Conta Ficheiro */
    write(STDOUT_FILENO, "\n\nFuncao Conta Ficheiro:\n\n", 27);
    status = conta("teste/conta.txt");
    if(status == -1)
        write(STDERR_FILENO, "Nao foi possivel abrir o ficheiro.\n", 36);
    else if(status == 1)
        write(STDERR_FILENO, "Erro na leitura do ficheiro.\n", 30);

    /* Funcao Apaga Ficheiro */
    write(STDOUT_FILENO, "\n\nFuncao Apaga Ficheiro:\n\n", 27);
    status = apaga("teste/apaga.txt");
    if(status == -1)
        write(STDERR_FILENO, "Nao foi possivel eliminar o ficheiro.\n", 39);

    return 0;
}
