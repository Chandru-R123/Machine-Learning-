%{
#include "parser.h"   // Must match your parser header
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%}

%%

[a-zA-Z]+      { yylval.str = strdup(yytext); return ID; }
[0-9]+         { yylval.str = strdup(yytext); return NUM; }
"+"            { return '+'; }
"-"            { return '-'; }
"*"            { return '*'; }
"/"            { return '/'; }
"="            { return '='; }
";"            { return ';'; }
[ \t\n]+       ;   // skip spaces, tabs, newlines

%%

int yywrap() { return 1; }