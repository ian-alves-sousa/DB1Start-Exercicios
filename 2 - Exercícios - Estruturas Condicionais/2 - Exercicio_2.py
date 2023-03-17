#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

try:
  n1 = int(input('Digite um número inteiro: '))

  if n1 > 0:
    print(f'O número é {n1} é positivo.')
  elif n1 < 0:
    print(f'O número é {n1} é negativo.')
  else:
    print(f'Você digitou {n1} é ele é neutro.')

except ValueError:
  print('Você não digitou um número inteiro. Tente novamente.')