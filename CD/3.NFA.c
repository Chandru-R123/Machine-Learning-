#include <stdio.h>
#include <ctype.h>
#include <string.h>

// Check Identifier
int isIdentifier(char str[]) {
    if (!isalpha(str[0]))
        return 0;

    for (int i = 1; str[i] != '\0'; i++) {
        if (!isalnum(str[i]))
            return 0;
    }
    return 1;
}

// Check Constant (Integer)
int isConstant(char str[]) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (!isdigit(str[i]))
            return 0;
    }
    return 1;
}

// Check Operator
int isOperator(char str[]) {
    if (strlen(str) == 1 && strchr("+-*/=<>", str[0]))
        return 1;
    return 0;
}

int main() {
    char input[50];

    printf("Enter a token: ");
    scanf("%s", input);

    if (isIdentifier(input)) {
        printf("'%s' is an Identifier\n", input);
    }
    else if (isConstant(input)) {
        printf("'%s' is a Constant\n", input);
    }
    else if (isOperator(input)) {
        printf("'%s' is an Operator\n", input);
    }
    else {
        printf("'%s' is NOT recognized\n", input);
    }

    return 0;
}
