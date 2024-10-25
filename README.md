# Algoritmo para validação do CNPJ alfanumérico

## Cálculo dos dígitos verificadores
O CNPJ alfanumérico é composto por doze caracteres alfanuméricos e dois dígitos veriﬁcadores
numéricos.
Os dígitos veriﬁ cadores (DV) são calculados a par r dos doze primeiros caracteres em duas
etapas, u lizando o módulo de divisão 11e pesos distribuídos de 2 a 9.

### Cálculo do primeiro dígito verificador
Para cada um dos caracteres do CNPJ, atribuir o valor da coluna “Valor para cálculo do DV”, conforme a tabela abaixo (ou subtrair 48 do “Valor ASCII”):

Exemplo

|**CNPJ**|1|2|A|B|C|3|4|5|0|1|D|E|
|--------|-|-|-|-|-|-|-|-|-|-|-|-|
|Valor|**1**|**2**|**17**|**18**|**19**|**3**|**4**|**5**|**0**|**1**|**20**|**21**|

a. Distribuir os pesos de 2 a 9 da direita para a esquerda (recomeçando depois do oitavo caracter), conforme o exemplo:


|**CNPJ**|1|2|A|B|C|3|4|5|0|1|D|E|
|--------|-|-|-|-|-|-|-|-|-|-|-|-|
|Valor|**1**|**2**|**17**|**18**|**19**|**3**|**4**|**5**|**0**|**1**|**20**|**21**|
|Peso|**5**|**4**|**3**|**2**|**9**|**8**|**7**|**6**|**5**|**4**|**3**|**2**|

b. Multiplicar o peso e o valor de cada coluna e somar todos os resultados:
|**CNPJ**|1|2|A|B|C|3|4|5|0|1|D|E|
|--------|-|-|-|-|-|-|-|-|-|-|-|-|
|Valor|**1**|**2**|**17**|**18**|**19**|**3**|**4**|**5**|**0**|**1**|**20**|**21**|
|Peso|**5**|**4**|**3**|**2**|**9**|**8**|**7**|**6**|**5**|**4**|**3**|**2**|
|Multiplicação|**5**|**8**|**51**|**36**|**171**|**24**|**28**|**30**|**0**|**4**|**60**|**42**|

**Somatória: (5+8+51+36+171+24+28+30+0+4+60+42) = 459**]

c. Obter o resto da divisão do somatório por 11.

Se o resto da divisão for igual a 1 ou 0, o primeiro dígito será igual a 0 (zero).
Senão, o primeiro dígito será igual ao resultado de 11– resto.

No exemplo:

Resto da divisão 459/11 = 8.

1º DV = 3 (resultado de 11-8)

### Cálculo do segundo dígito verificador
Para o cálculo do segundo dígito é necessário acrescentar o primeiro DV ao ﬁnal do CNPJ,
formando assim treze caracteres, e repe r os passos realizados para o primeiro dígito.
Assim, no exemplo, temos:

|**CNPJ**|1|2|A|B|C|3|4|5|0|1|D|E|**3**|
|--------|-|-|-|-|-|-|-|-|-|-|-|-|-|
|Valor|**1**|**2**|**17**|**18**|**19**|**3**|**4**|**5**|**0**|**1**|**20**|**21**|3|
|Peso|**6**|**5**|**4**|**3**|**2**|**9**|**8**|**7**|**6**|**5**|**4**|**3**|**2**|
|Multiplicação|**6**|**10**|**68**|**54**|**38**|**27**|**32**|**35**|**0**|**5**|**80**|**63**|**6**|

**Somatória: (6+10+68+54+38+27+32+35+0+5+80+63+6) = 424**]
Resto da divisão 424/11 = 6
2° DV = 5 (resultado de 11-6)

CNPJ completo:**12.ABC.345/01DE-35**
