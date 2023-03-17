#Aluno: Ian Alves Sousa
#DB1 Start
#Exercício 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

try:
    raio = float(input('Digite o raio de um círculo em cm: '))
    area = math.pi*(raio**2)
    print('Em um círculo com o raio de {}cm, a área é de {}cm².'.format(raio,round(area, 2)))
except ValueError:
  print('Você não digitou um raio válido, digite um número!')