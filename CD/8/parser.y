%{
#include <stdio.h>
#include <stdlib.h>
#include "parser.h"
%}

%union {
    ASTNode* node;
}

%token <node> ID NUM
%type <node> E T F

%%

stmt : ID '=' E ';'
      {
        printf("%c = ", $1->value);
        printAST($3);
        printf("\n");
      }
    ;

E : E '+' T { $$ = newNode('E','+',$1,$3,0); }
  | E '-' T { $$ = newNode('E','-',$1,$3,0); }
  | T       { $$ = $1; }
  ;

T : T '*' F { $$ = newNode('T','*',$1,$3,0); }
  | T '/' F { $$ = newNode('T','/',$1,$3,0); }
  | F       { $$ = $1; }
  ;

F : '(' E ')' { $$ = $2; }
  | ID       { $$ = $1; }
  | NUM      { $$ = $1; }
  ;

%%

ASTNode* newNode(char type, char op, ASTNode* left, ASTNode* right, char value) {
    ASTNode* node = (ASTNode*)malloc(sizeof(ASTNode));
    node->type = type;
    node->op = op;
    node->left = left;
    node->right = right;
    node->value = value;
    return node;
}

void printAST(ASTNode* node) {
    if (!node) return;
    if(node->left) printAST(node->left);
    if(node->right) printAST(node->right);
    if(node->op) printf("%c ", node->op);
    if(node->value) printf("%c ", node->value);
}

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}

int main() {
    printf("Enter statement:\n");
    yyparse();
    return 0;
}