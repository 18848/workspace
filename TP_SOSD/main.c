#include <unistd.h>

#include "ficheiro.h"

int main(/* int argc, char const *argv[] */)
{
    int status;
    /* Funcao Mostra Ficheiro */
    write(STDOUT_FILENO, "Funcao Mostra Ficheiro:\n\n", 26);
    status = mostraFicheiro("teste/mostra.txt");
    if(status == -1)
        write(STDERR_FILENO, "Não foi possível abrir o ficheiro.", 37);
    else if(status == 1)
        write(STDERR_FILENO, "Erro na leitura do ficheiro.", 29);
    
    /* Funcao Conta Ficheiro */
    write(STDOUT_FILENO, "\n\nFuncao Conta Ficheiro:\n\n", 26);
    status = contaFicheiro("teste/conta.txt");
    if(status == -1)
        write(STDERR_FILENO, "Não foi possível abrir o ficheiro.", 37);
    else if(status == 1)
        write(STDERR_FILENO, "Erro na leitura do ficheiro.", 29);

    /* Funcao Apaga Ficheiro */
    write(STDOUT_FILENO, "\n\nFuncao Apaga Ficheiro:\n\n", 26);
    status = apagaFicheiro("teste/apaga.txt");
    if(status == -1)
        write(STDERR_FILENO, "Não foi possível abrir o ficheiro.", 37);
    else if(status == 1)
        write(STDERR_FILENO, "Erro na leitura do ficheiro.", 29);

    return 0;
}
