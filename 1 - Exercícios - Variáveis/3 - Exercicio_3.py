#Aluno: Ian Alves Sousa
#DB1 Start
#Exercício 3 - Faça um Programa que peça dois números e imprima a soma.

try:
  n1 = int(input('Digite um número: '))
  n2 = int(input('Digite outro número: '))
  soma = n1 + n2
  print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
except ValueError:
  print('Digite um número inteiro')


