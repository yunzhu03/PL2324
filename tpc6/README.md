# TPC6: Definição de Gramática Independente de Contexto

### Autor: Lingyun Zhu, 100820


## Axioma

```
P1: S -> '?' VAR
p2:   |  '!' EXP
p3:   |  VAR '=' EXP 

p4: EXP -> '(' EXP ')'
p5:     |  SIMB EXP2
p6:     |  VAR EXP
p7:     |  &

p8: SIMB -> '+'
p9:      |  '-'
p10:     |  'x'
p11:     |  '/'

p12: EXP2 -> VAR EXP
p13:      |  '(' EXP ')'
```

## Prioridades dos operadores

1. '?', '!', '='
2. '(', ')'
3. '+', '-', 'x', '/'


## LL(1): Cálculo dos LookAheads

```
p1: {'?'}
p2: {'!'}
p3: {VAR}
p4: {'('}
p5: {'+', '-', 'x', '/'}
p6: {VAR}
p7: {')'}
p8: {'+'}
p9: {'-'}
p10: {'x'}
p11: {'/'}
p12: {VAR}
p13: {'('}

