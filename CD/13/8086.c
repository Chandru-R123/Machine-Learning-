#include <stdio.h>
#include <string.h>

#define MAX_TAC 10
#define MAX_LEN 50

int main() {
    int n;
    printf("=== THREE-ADDRESS CODE TO 8086 ASSEMBLY ===\n");
    printf("Enter number of TAC statements (max 10): ");
    scanf("%d", &n);

    char tac[MAX_TAC][MAX_LEN];

    for(int i=0; i<n; i++) {
        printf("Enter TAC statement %d: ", i+1);
        getchar(); // consume leftover newline
        fgets(tac[i], MAX_LEN, stdin);
        tac[i][strcspn(tac[i], "\n")] = 0; // remove newline
    }

    printf("\nGenerated 8086 Assembly:\n");
    for(int i = 0; i < n; i++) {
        char *eq = strchr(tac[i], '=');
        if(eq) {
            char lhs[10], rhs[20];
            sscanf(tac[i], "%s = %s", lhs, rhs);

            char op;
            char var1[10], var2[10];
            if(sscanf(rhs, "%s %c %s", var1, &op, var2) == 3) {
                printf("MOV AX, %s\n", var1);
                switch(op) {
                    case '+': printf("ADD AX, %s\n", var2); break;
                    case '-': printf("SUB AX, %s\n", var2); break;
                }
                printf("MOV %s, AX\n", lhs);
            } else {
                printf("MOV %s, %s\n", lhs, rhs);
            }
        }
    }

    return 0;
}
