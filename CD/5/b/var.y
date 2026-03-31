%{
#include <stdio.h>

int yylex();
int yyerror(const char *s);
%}

%token ID

%%

S : ID { printf("Valid Variable\n"); }
  ;

%%

int main() {
    printf("Enter variable:\n");
    yyparse();
    return 0;
}

int yyerror(const char *s) {
    printf("Invalid Variable\n");
    return 0;
}