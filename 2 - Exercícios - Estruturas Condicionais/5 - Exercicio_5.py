#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 5 - Faça um Programa que leia três números e mostre o maior e o menor deles.

try:
  n1 = int(input('Digite um número inteiro: '))
  n2 = int(input('Digite outro número inteiro: '))
  n3 = int(input('Digite mais um número inteiro: '))


  if n1 != n2 and n2 != n3 and n3 != n1:
    if n1 > n2 and n1 > n3:
      print(f'O número é {n1} é o maior número entre eles.')
      if n2 > n3:
        print(f'O número é {n3} é o menor número entre eles.')
      else:
        print(f'O número é {n2} é o menor número entre eles.')

    elif n2 > n1 and n2 > n3:
      print(f'O número é {n2} é o maior número entre eles.')
      if n1 > n3:
        print(f'O número é {n3} é o menor número entre eles.')
      else:
        print(f'O número é {n1} é o menor número entre eles.')

    elif n3 > n1 and n3 > n2:
      print(f'O número é {n3} é o maior número entre eles.')
      if n1 > n2:
        print(f'O número é {n2} é o menor número entre eles.')
      else:
        print(f'O número é {n1} é o menor número entre eles.')
  else:
      print(f'Você digitou dois ou mais números iguais')
    

except ValueError:
  print('Você não digitou um número inteiro. Tente novamente.')