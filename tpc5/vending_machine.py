import re
import ply.lex as lex

class VendingMachine(object):
    
    tokens = (
       'LISTAR',
       'MOEDA',
       'SELECIONAR',
       'SAIR',
       'SALDO',
    )
    
    states = (
        ('inserir', 'inclusive'),
    )
    
    def __init__(self):
        self.saldo = 0
        print("Máquina Vending Machine")
        print("Escolha uma das seguintes opções:")
        print("LISTAR")
        print("MOEDA")
        print("SELECIONAR")
        print("SAIR")
        
    def t_LISTAR(self,t):
        r'LISTAR'
        t.lexer.begin('INITIAL')
        print("1 - água 50c")
        print("2 - bolo 60c")
        
    def t_MOEDA(self,t):
        r'MOEDA'
        t.lexer.begin('inserir')
        
        
    def t_SELECIONAR(self,t):
        r'SELECIONAR\s(\d)'
        t.lexer.begin('INITIAL')

        opt = re.match(r'SELECIONAR\s(\d)',t.value,re.I)
        
        if opt:
            match opt.group(1):
                case '1':
                    if self.saldo >= 50:
                        self.saldo -= 50
                        print("Operaão feita com sucesso.")
                case '2':
                    if self.saldo >= 60:
                        self.saldo -= 60
                        print("Operaão feita com sucesso.")                        
                case _:
                    print("Não existe essa opção.")
            
            print("Saldo: ", self.saldo, 'c')
            
        return t
        
    def t_SAIR(self,t):
        r'SAIR'
        print('Troco: ', self.saldo,'c')
        self.saldo = 0
       
    def t_SALDO(self,t):
        r'(\d+)c'
        pass
    
    def t_inserir_SALDO(self,t):
        r'(\d+)c'
        t.value = int(t.value[:-1]) 
        self.saldo += t.value  
        print('Saldo: ', self.saldo, 'c')  
        return t

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs,reflags=re.IGNORECASE |re.VERBOSE)

m = VendingMachine()
m.build()         

def main():
    
    while True:
        data = input("Escolha a opção:")
        m.lexer.input(data) 
        m.lexer.token()     

if __name__ == "__main__":   
    main()