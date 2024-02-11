## TPC1: Análise de um dataset
### Autor: Lingyun Zhu, 100820

* Executar com:
    - *cat dataset.csv | python3 analise.py*
    - *python3 analise.py < dataset.py*

* A primeira linha (exemplo) é ultrapassada;

* O parse de cada linha:
    - separa os elementos pelas virgulas;
    - remove o '\n' no fim de cada linha.

* A lista das modalidades desportivas é inicialmente inserida num set de modo a evitar repetição;

* A faixa etária é guardada num dicionário através da sua divisão inteira com o intervalo.