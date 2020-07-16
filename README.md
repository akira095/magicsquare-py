###  Nota:
Na versão atual, o programa segue o algoritmo à risca, gerando sempre o mesmo quadrado, e só funciona quando o número n de linhas e colunas é ímpar.

###  A fazer:
- Posicionar números aleatoriamente para gerar quadrados diferentes.
- Implementar backtracking para construir o quadrado como uma pessoa faria (?).

### A mágica do quadrado
Um quadrado mágico é uma tabela quadrada de números de dimensão n² onde a soma das linhas, colunas e diagonais é sempre a mesma.

Eu encontrei diversas formas para construir quadrados mágicos, e esta é somente uma delas. Não me aprofundei muito no assunto, mas seu conceito é muito interessante.

               0       1       2    (j)
           + ----- + ----- + ----- +
        0  | (0,0) | (0,1) | (0,2) |
           + ----- + ----- + ----- +
        1  | (1,0) | (1,1) | (1,2) |
           + ----- + ----- + ----- +
        2  | (2,0) | (2,1) | (2,2) |
           + ----- + ----- + ----- +
       (i)

    Sendo (i, j) a posição atual, posicionamos os números:
    - O primeiro número é posicionado em (n/2, n-1);
    - A próxima posição é calculada por (i-1, j+1).
    Condição 1: Se i = -1, então i = n-1;
    Condição 2: Se j = n, então j = 0;
    Condição 3: Se a célula já tem um número, então i = i+1 e j = j-2;
    Condição 4: Se i = -1 e j = n, a nova posição será (0, n-2).
