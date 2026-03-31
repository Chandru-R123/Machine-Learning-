#include <stdio.h>
#include <string.h>

#define MAX_TAC 10
#define MAX_LEN 50

int main() {
    int n;
    printf("=== FLOW GRAPH CONSTRUCTION ===\n");
    printf("Enter number of statements (max 10): ");
    scanf("%d", &n);

    char stmt[MAX_TAC][MAX_LEN];
    int next[MAX_TAC][2], count[MAX_TAC];

    for(int i=0; i<n; i++) {
        printf("Enter statement %d: ", i+1);
        getchar(); // consume newline
        fgets(stmt[i], MAX_LEN, stdin);
        stmt[i][strcspn(stmt[i], "\n")] = 0; // remove newline

        printf("Enter number of successors (0,1,2) for statement %d: ", i+1);
        scanf("%d", &count[i]);
        for(int j=0; j<count[i]; j++) {
            printf("Enter successor %d: ", j+1);
            scanf("%d", &next[i][j]);
        }
    }

    printf("\nFLOW GRAPH:\n");
    for(int i=0; i<n; i++) {
        printf("Node %d: %s --> ", i+1, stmt[i]);
        for(int j=0; j<count[i]; j++)
            printf("%d ", next[i][j]);
        printf("\n");
    }

    return 0;
}
