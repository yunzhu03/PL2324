import sys
import re

def converte_headings(rascunho):
            
    rascunho = re.sub(r'^#{3}(.*)', r'<h3>\1 </h3>', rascunho)
    rascunho = re.sub(r'^#{2}(.*)', r'<h2>\1 </h2>', rascunho)
    rascunho = re.sub(r'^#{1}(.*)', r'<h1>\1 </h1>', rascunho)
    
    return rascunho

def converte_estilos(rascunho):
            
    rascunho = re.sub(r'\*{2}(.*)\*{2}', r'<b> \1 </b>', rascunho)
    rascunho = re.sub(r'\*{1}(.*)\*{1}', r'<i> \1 </i>', rascunho)
    
    return rascunho

def converte_links(rascunho):
    
    rascunho = re.sub(r'\[(.*)\]\((.*)\)',r'<a href="\2">\1</a>',rascunho)
    
    return rascunho

def converte_imagem(rascunho):
    
    rascunho = re.sub(r'!\[(.*)\]\((.*)\)',r'<img src="\2" alt="\1"/>',rascunho)
    
    return rascunho
    
def converte_elemento(rascunho):
    
    rascunho = re.sub(r'^\s*\d.(.*)',r'    <li>\1</li>', rascunho)
    
    return rascunho

def converte_inicio_lista(rascunho):
    
    rascunho = re.sub(r'^\s*\d.(.*)',r'<ol>\n    <li>\1</li>', rascunho)
    
    return rascunho

def converte_fim_lista(rascunho):
    
    rascunho = re.sub(r'(.*)$',r'\1</ol>\n', rascunho)
    
    return rascunho
  

def conversor(leitura, escrita):
    
    lines = leitura.readlines()
    
    em_lista = False
    
    for line in lines:
        
        rascunho = line

        rascunho = converte_headings(rascunho)
        rascunho = converte_estilos(rascunho)
        rascunho = converte_imagem(rascunho)
        rascunho = converte_links(rascunho)
        
        if (re.match(r'^\s*\d(.*)',rascunho)):  
            if em_lista:
                rascunho = converte_elemento(rascunho)
            else:
                em_lista = True
                rascunho = converte_inicio_lista(rascunho)
        
        else:
            if em_lista:
                rascunho = converte_fim_lista(rascunho)
                em_lista = False
                                    
        escrita.write(rascunho)
    
    return 0
    


def main():
    leitura = open(sys.argv[1], 'r')
    escrita = open(sys.argv[2], 'w')
    
    conversor(leitura, escrita)
    
    leitura.close()
    escrita.close()
    
    return 0

if __name__ == "__main__":
    main()