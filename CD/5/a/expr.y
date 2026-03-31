%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
int yyerror(const char *s);
%}

%token NUMBER
%left '+' '-'
%left '*' '/'

%%

S : E { printf("Valid Expression\n"); }
  ;

E : E '+' E
  | E '-' E
  | E '*' E
  | E '/' E
  | '(' E ')'
  | NUMBER
  ;

%%

int main() {
    printf("Enter expression:\n");
    yyparse();
    return 0;
}

int yyerror(const char *s) {
    printf("Invalid Expression\n");
    return 0;
}