# TPC2: Conversor de MD para HTML

### Autor: Lingyun Zhu, 100820

Executar com:

- _python3 conversor.py ficheiro.md ficheiro.html_

A conversão dos elementos é feito de uma determinada ordem:

- h3 _(###)_ -> h2 _(##)_ -> h1 _(#)_
- bold _(\*\*)_ -> itálico _(\*)_
- imagem _(\!\[]\())_ -> link _(\[]\())_

Em relação às listas, através de uma variável bool _em_lista_ identificamos se a atual linha corresponde ao interior de uma lista, e consoante o resultado do _re.match_ realiza-se os passos necessários:

- iniciar uma lista (_em_lista == False_ e _re.match == False_);
- adicionar novo elemento à lista (_em_lista == True_ e _re.match == True_);
- fechar lista (_em_lista == True_ e _re.match == False_);
- nada (_em_lista == False_ e _re.match == False_).
