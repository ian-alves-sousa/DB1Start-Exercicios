#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 7 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

try:
  n1 = int(input('Digite um número inteiro: '))
  n2 = int(input('Digite outro número inteiro: '))
  n3 = int(input('Digite mais um número inteiro: '))

  if n1 > n2 and n1 > n3:
    if n2 >= n3:
      print(f'Segue os números em ordem decrescente: {n1} {n2} {n3}')
    else:
      print(f'Segue os números em ordem decrescente: {n1} {n3} {n2}')
  elif n2 > n1 and n2 > n3:
    if n1 >= n3:
      print(f'Segue os números em ordem decrescente: {n2} {n1} {n3}')
    else:
      print(f'Segue os números em ordem decrescente: {n2} {n3} {n1}')
  else:
    if n1 >= n2:
      print(f'Segue os números em ordem decrescente: {n3} {n1} {n2}')
    else:
      print(f'Segue os números em ordem decrescente: {n3} {n2} {n1}')

    

except ValueError:
  print('Você não digitou um número inteiro. Tente novamente.')