#include <stdlib.h>

int **my2DAlloc(int rows, int cols) {
    if (rows <= 0 || cols <= 0) {
        return NULL; 
    }

    int **arr = (int **)malloc(rows * sizeof(int *));
    if (arr == NULL) {
        return NULL;  
    }

    for (int i = 0; i < rows; i++) {
        arr[i] = (int *)malloc(cols * sizeof(int));
        if (arr[i] == NULL) {
            for (int j = 0; j < i; j++) {
                free(arr[j]);
            }
            free(arr);
            return NULL;
        }
    }

    return arr;
}