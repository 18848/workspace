#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <limits.h>

#include "utilities.h"

char* itostring(long int num){
    int i=0;
    int digit;
    char* number = malloc(20);
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
    return number;
}