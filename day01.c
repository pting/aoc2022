#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define BUFSIZE 80

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int main() {
    char path[BUFSIZE] = "input01.txt";
    char *envvar = "AOC_INPUT";
    const int N = 3;

    // Make sure envar actually exists
    if(getenv(envvar)){
        if(snprintf(path, BUFSIZE, "%s", getenv(envvar)) >= BUFSIZE){
            fprintf(stderr, "BUFSIZE of %d was too small. Aborting\n", BUFSIZE);
            exit(1);
        }
    }
    printf("AOC_INPUT: %s\n", path);

    FILE *fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen(path, "r");
    if (fp == NULL)
        exit(1);

    int result[N] = { 0 };
    int temp = 0;

    while ((read = getline(&line, &len, fp)) != -1) {
        // printf("Retrieved line of length %zu:\n", read);
        int num = atoi(line);
        // printf("New line: %i, len: %i\n", num, (int)strlen(line));
        
        if (num > 0) {
            temp += num;
            // printf("-- %i\n", temp);
        } else {
            // printf("temp = %i, result[0] = %i\n", temp, result[0]);
            if (temp > result[0]) {
                result[0] = temp;
                qsort(result, N, sizeof(int), cmpfunc);
                // printf("result: \n");
            }
            temp = 0;
        }
    }

    //add all elements to the variable sum.
    int sum = 0;
    for(int i = 0; i < N; i++) {
        // printf("[%d] ", result[i]);
        sum += result[i];
    }
    
    printf("\nResult: %i\n", sum);

    fclose(fp);
    if (line)
        free(line);

    return 0;
}