%{
#include "parser.h"
#include <stdio.h>
#include <stdlib.h>
%}

%%

[ \t\n]+       ;      // ignore whitespace

[a-zA-Z]       { 
                    ASTNode* node = (ASTNode*)malloc(sizeof(ASTNode));
                    node->type='F'; node->op=0; node->left=NULL; node->right=NULL; node->value=yytext[0];
                    yylval.node = node; 
                    return ID; 
                }

[0-9]          { 
                    ASTNode* node = (ASTNode*)malloc(sizeof(ASTNode));
                    node->type='F'; node->op=0; node->left=NULL; node->right=NULL; node->value=yytext[0];
                    yylval.node = node; 
                    return NUM; 
                }

"+"             { return '+'; }
"-"             { return '-'; }
"*"             { return '*'; }
"/"             { return '/'; }
"="             { return '='; }
";"             { return ';'; }
"("             { return '('; }
")"             { return ')'; }

.               { return yytext[0]; }

%%

int yywrap() { return 1; }