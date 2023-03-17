#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 1 - Faça um Programa que peça dois números e imprima o maior deles.

try:
  n1 = int(input('Digite um número: '))
  n2 = int(input('Digite um segundo número: '))

  if n1 > n2:
    print(f'O maior número é {n1}.')
  elif n1 < n2:
    print(f'O maior número é {n2}.')
  else:
    print(f'Os números são iguais.')

except ValueError:
  print('Você digitou um valor inválido. Tente novamente.')