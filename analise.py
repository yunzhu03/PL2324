import sys
def main():
    
    # coleção para evitar elementos repetidos
    modalidades = set()
    
    # contador de cidadãos aptos
    aptos = 0
    
    # número de analises/pessoas
    tamanho = 0
    
    # guardar número de elementos em cada faixa etária
    faixa_etaria = {}
    
    f = sys.stdin
    # saltar a primeira linha correspndente ao exemplo
    next(f)
    
    for line in f:
        
        tamanho += 1
        
        # separar cada linha em tokens e remover o \n 
        tokens = line.rstrip().split(",")
        
        # modalidade encontra-se no índice 8
        modalidades.add(tokens[8]) 
        
        # resultado no indíce 12 (true/false)
        if (tokens[12] == "true"):
            aptos += 1
            
        # idade no indice 5
        if (int(tokens[5])//5) in faixa_etaria.keys():
            faixa_etaria[int(tokens[5])//5] += 1
        else:
            faixa_etaria[int(tokens[5])//5] = 1
           
    modalidades_ordenadas = list(modalidades)           
    modalidades_ordenadas.sort()
    
    print("\nModalidades ordenadas alfabeticamente:")  
    print(modalidades_ordenadas)
    
    if (tamanho > 0):
        print("\nPercentagem de atletas aptos: {valor}%".format(valor=aptos*100/tamanho))
        print("Percentagem de atletas inaptos: {valor}%\n".format(valor=100-(aptos*100/tamanho)))
        
    for faixa, quantidade in faixa_etaria.items():
        intervalo = [faixa*5,faixa*5+4]
        print("A faixa etária {faixa} corresponde a {porcentagem} da população.".format(faixa=intervalo,porcentagem=quantidade*100/tamanho))
    
    f.close()
 
if __name__ == "__main__":
    main()    
