#include <unistd.h>
#include <stdlib.h>

#include "utilities.h"

int itostring(long int num, char** destiny){
    int i=0;
    int digit;
    char number[20];
    int pos = 19;
    number[pos--] = '\0';
    while(num != 0){
        digit = num % 10;
        num = num / 10;
        number[pos--] = '0' + digit;
    }
    while(i < 20 && pos < 20){
        number[i++] = number[++pos];
    }
    *destiny = number;
    return 0;
}

int strcopy(char* dest, char* src){
    int i = 0;
    for(; src[i] != '\0'; i++) dest[i] = src[i];
    dest[i] = '\0';
    return 0;
}


int strsize(const char* string){
    int i;
    for(i = 0; string[i] != '\0' && string[i] != '\n'; i++);
    return i;
}

int strcmp(const char* first, const char* sec){
    int i = 0;
    /* Para tamanhos diferentes retorna a diferença de tamanho 
    do primeiro para o segundo, em numero de bytes. */
    if(strsize(first) != strsize(sec)){
        return (strsize(first) - strsize(sec))*4;
    }
    /* Se caracter diferente retorna -1. */
    for(; ; i++){
        if(first[i] != sec[i]){
            return -1;
        }
    }
    return 0;
}

char* str_append(const char* first, const char* sec){
    int i = 0;
    int j = 0;
    int sizeFirst = strsize(first);
    int sizeSec = strsize(sec);
    char* result = malloc(sizeFirst + sizeSec + 1);
    while (i < sizeFirst)
    {
        result[j++] = first[i++];
    }
    i = 0;
    while (i < sizeSec)
    {
        result[j++] = sec[i++];
    }
    result[j] = '\0';
    return result;    
}
