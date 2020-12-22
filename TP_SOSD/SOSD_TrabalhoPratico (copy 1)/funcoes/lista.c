#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char* argv[])
{
    if(argc > 3){
		printf("Too many arguments.\n");
		exit(EXIT_FAILURE);
	} else if(argc < 3){
		printf("Missing arguments.\n");
		exit(EXIT_FAILURE);
	}

    return 0;
}