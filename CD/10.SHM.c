#include <stdio.h>
#include <stdlib.h>

// Function demonstrating stack memory
void stackExample() {
    int stackVar;
    int stackArr[3]; // small fixed-size stack array

    printf("STACK MEMORY EXAMPLE\n");
    printf("Enter a value for stackVar: ");
    scanf("%d", &stackVar);

    printf("Enter 3 values for stackArr: ");
    for(int i = 0; i < 3; i++)
        scanf("%d", &stackArr[i]);

    printf("\nStackVar = %d\n", stackVar);
    printf("stackArr = ");
    for(int i = 0; i < 3; i++)
        printf("%d ", stackArr[i]);
    printf("\n\n");
}

// Function demonstrating heap memory
void heapExample() {
    int *heapVar = (int *)malloc(sizeof(int));
    if(heapVar == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }

    printf("HEAP MEMORY EXAMPLE\n");
    printf("Enter a value for heapVar: ");
    scanf("%d", heapVar);

    int n;
    printf("Enter size of heapArr: ");
    scanf("%d", &n);

    int *heapArr = (int *)malloc(n * sizeof(int));
    if(heapArr == NULL) {
        printf("Memory allocation failed!\n");
        free(heapVar);
        return;
    }

    printf("Enter %d values for heapArr: ", n);
    for(int i = 0; i < n; i++)
        scanf("%d", &heapArr[i]);

    printf("\nHeapVar = %d\n", *heapVar);
    printf("heapArr = ");
    for(int i = 0; i < n; i++)
        printf("%d ", heapArr[i]);
    printf("\n");

    free(heapVar);
    free(heapArr);
}

int main() {
    printf("=== STACK AND HEAP MEMORY DEMONSTRATION ===\n\n");

    stackExample(); // Stack demonstration
    heapExample();  // Heap demonstration

    printf("\nProgram completed successfully!\n");
    return 0;
}
