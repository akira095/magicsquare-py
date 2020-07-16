#!/usr/bin/python3

#  Autor: Artur Rabelo <artur.rabelo05@gmail.com>
#  Github: akira095

"""
    Um quadrado mágico é uma tabela quadrada de números de dimensão n² onde a soma das linhas,
    colunas e diagonais é sempre a mesma, aqui calculada por n*(n²+1)/2.

           0       1       2    (j)
       + ----- + ----- + ----- +        Sendo (i, j) a posição atual, posicionamos os números:
    0  | (0,0) | (0,1) | (0,2) |        - O primeiro número é posicionado em (n/2, n-1);
       + ----- + ----- + ----- +        - A próxima posição é calculada por (i-1, j+1).
    1  | (1,0) | (1,1) | (1,2) |        Condição 1: Se i = -1, então i = n-1;
       + ----- + ----- + ----- +        Condição 2: Se j = n, então j = 0;
    2  | (2,0) | (2,1) | (2,2) |        Condição 3: Se a célula já tem um número, então i = i+1 e j = j-2;
       + ----- + ----- + ----- +        Condição 4: Se i = -1 e j = n, a nova posição será (0, n-2).
   (i)
"""

class Magic:
    def __init__(self, size):

        self.size = size
        self.magicsum = (self.size * ((self.size**2) + 1)) // 2
        self.square = [[0 for x in range(self.size)]
                        for y in range(self.size)]

    def build(self):

        #  Iniciando a primeira posição
        i = self.size // 2
        j = self.size - 1

        aux = 1
        while aux <= self.size**2:

            #  Condição 4: i é menor que 0 e j é igual a n
            if i == -1 and j == self.size:
                i = 0
                j = self.size-2

            else:
                #  Condição 2: j é igual a n
                if j == self.size:
                    j = 0

                #  Condição 1: i é menor que 0
                if i < 0:
                    i = self.size-1

            #  Condição 3: célula já contém um número
            if self.square[int(i)][int(j)]:
                j -= 2
                i += 1
                continue

            else:
                #  A célula recebe o número e calculamos a próxima posição
                self.square[int(i)][int(j)] = aux
                aux += 1

            i -= 1
            j += 1
        
        return self.square

    def draw(self):

        square = self.build()
        print(f'Soma mágica: {self.magicsum}')
        
        for i in range(0, self.size):
            for j in range(0, self.size):
                print(f'{square[i][j]}', end=' ')
                if j == self.size - 1:
                    print()


num = int(input('Tamanho do quadrado: '))
if num % 2 != 0:
    square = Magic(num)
    square.draw()
else:
    print(f'Você deve inserir um número ímpar.')
