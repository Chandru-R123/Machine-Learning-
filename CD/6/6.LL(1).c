#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX 100

char grammar[20][20][20]; // grammar[i][j] = jth production of ith non-terminal
char nonTerminals[20];
int prodCount[20];
int n;

char first[20][20];
char follow[20][20];
char terminals[20];
int tCount = 0;
char startSymbol;

// Map non-terminal to index
int ntIndex(char c) {
    for (int i = 0; i < n; i++)
        if (nonTerminals[i] == c) return i;
    return -1;
}

// Check if char exists in set
int contains(char arr[][20], int index, char c) {
    for (int i = 0; arr[index][i] != '\0'; i++)
        if (arr[index][i] == c) return 1;
    return 0;
}

// Add char to set, return 1 if added
int addToSet(char arr[][20], int index, char c) {
    if (!contains(arr, index, c)) {
        int len = strlen(arr[index]);
        arr[index][len] = c;
        arr[index][len + 1] = '\0';
        return 1;
    }
    return 0;
}

// Find terminals
void findTerminals() {
    tCount = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < prodCount[i]; j++) {
            for (int k = 0; k < strlen(grammar[i][j]); k++) {
                char c = grammar[i][j][k];
                if (!isupper(c) && c != '#' && !contains(terminals, 0, c)) {
                    terminals[tCount++] = c;
                }
            }
        }
    }
    terminals[tCount++] = '$';
}

// Compute FIRST sets
void computeFirst() {
    int changed;
    do {
        changed = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < prodCount[i]; j++) {
                char *prod = grammar[i][j];
                for (int k = 0; k < strlen(prod); k++) {
                    char c = prod[k];
                    if (!isupper(c)) {
                        if (addToSet(first, i, c)) changed = 1;
                        break;
                    }
                    int idx = ntIndex(c);
                    for (int x = 0; first[idx][x] != '\0'; x++) {
                        if (first[idx][x] != '#') {
                            if (addToSet(first, i, first[idx][x])) changed = 1;
                        }
                    }
                    if (!contains(first, idx, '#')) break;
                    if (k == strlen(prod) - 1) {
                        if (addToSet(first, i, '#')) changed = 1;
                    }
                }
            }
        }
    } while (changed);
}

// Compute FOLLOW sets
void computeFollow() {
    addToSet(follow, ntIndex(startSymbol), '$');
    int changed;
    do {
        changed = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < prodCount[i]; j++) {
                char *prod = grammar[i][j];
                for (int k = 0; k < strlen(prod); k++) {
                    char c = prod[k];
                    if (isupper(c)) {
                        int idx = ntIndex(c);
                        int hasEpsilon = 1;
                        for (int l = k + 1; l < strlen(prod); l++) {
                            char next = prod[l];
                            if (!isupper(next)) {
                                if (addToSet(follow, idx, next)) changed = 1;
                                hasEpsilon = 0;
                                break;
                            }
                            int nextIdx = ntIndex(next);
                            for (int x = 0; first[nextIdx][x] != '\0'; x++) {
                                if (first[nextIdx][x] != '#') {
                                    if (addToSet(follow, idx, first[nextIdx][x])) changed = 1;
                                }
                            }
                            if (!contains(first, nextIdx, '#')) {
                                hasEpsilon = 0;
                                break;
                            }
                        }
                        if (hasEpsilon) {
                            for (int x = 0; follow[i][x] != '\0'; x++) {
                                if (addToSet(follow, idx, follow[i][x])) changed = 1;
                            }
                        }
                    }
                }
            }
        }
    } while (changed);
}

// Print FIRST sets
void printFirst() {
    printf("\nFIRST SETS:\n");
    for (int i = 0; i < n; i++) {
        printf("FIRST(%c) = { ", nonTerminals[i]);
        for (int j = 0; first[i][j] != '\0'; j++)
            printf("%c ", first[i][j]);
        printf("}\n");
    }
}

// Print FOLLOW sets
void printFollow() {
    printf("\nFOLLOW SETS:\n");
    for (int i = 0; i < n; i++) {
        printf("FOLLOW(%c) = { ", nonTerminals[i]);
        for (int j = 0; follow[i][j] != '\0'; j++)
            printf("%c ", follow[i][j]);
        printf("}\n");
    }
}

int main() {
    printf("Enter number of productions: ");
    scanf("%d", &n);
    getchar();

    printf("Enter productions (use # for epsilon):\n");
    for (int i = 0; i < n; i++) {
        char input[50];
        fgets(input, sizeof(input), stdin);

        char lhs = input[0];
        nonTerminals[i] = lhs;
        prodCount[i] = 0;

        char *rhs = strstr(input, "->") + 2;
        rhs[strcspn(rhs, "\n")] = 0;

        char *token = strtok(rhs, "|");
        while (token != NULL) {
            strcpy(grammar[i][prodCount[i]++], token);
            token = strtok(NULL, "|");
        }
    }

    startSymbol = nonTerminals[0];

    findTerminals();
    computeFirst();
    computeFollow();

    printFirst();
    printFollow();

    return 0;
}
