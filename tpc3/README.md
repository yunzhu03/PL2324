# TPC3: Somador on/off

### Autor: Lingyun Zhu, 100820

Executar com:
```
$ python3 somador.py ficheiro.txt
```
Este programa consiste na separação das linhas do ficheiro através dos *on/off*s.
Com o resultado, verifica-se em cada linha o seu padrão inicial (*on*, *off* ou nenhum) para serem tratados adequadamente.

A cada linha *on* ou linha seguinte de tal, é chamado a função *soma* que recebe como parâmetro a linha correspondente para os somar e um acumulador para a impressão de eventuais *=*.

Relativamente às linhas *off* ou seguintes de tais, é chamada a função *not_soma* que recebe os mesmos parâmetros, contudo esta não produz a soma da linha, mas sim apenas a impressão do valor para a ocorrência de eventuais *=*.

Para a idenficação de linhas que não começam com *on* ou *off*, recorre-se a uma variável *last_is_on* que indica o estado do último switch.