# Desafio 74: Maior e menor valores em tuplas
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

num = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(f'Os valores sorteados foram: ', end='')
for i in num:
    print(f'{i}', end=' ')

print(f'\nO maior: {max(num)}')
print(f'O menor: {min(num)}')
