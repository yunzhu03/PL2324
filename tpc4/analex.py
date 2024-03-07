import ply.lex as lex

# Lista do nome dos tokens
tokens = (
    'SELECT',
    'ID',
    'NOME',
    'SALARIO',
    'FROM',
    'EMPREGADOS',
    'WHERE',
    'SIMBOLO',
    'SBASE',
    'UNKNOWN',
)

# Expressões regulares dos tokens
t_SELECT = r'Select'
t_ID = r'id'
t_NOME = r'nome'
t_SALARIO = r'salario'
t_FROM = r'From'
t_EMPREGADOS = r'empregados'
t_WHERE = r'Where'
t_SIMBOLO = r'[<>]{1}[=]?'

def t_SBASE(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    r'[^\s]+'
    print("Unknown character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
    
def test(lexer, data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
             
def main():

    test(lexer, "Select id, nome, salario From empregados Where salario >= 820")
    return 0

if __name__ == "__main__":
    main()
