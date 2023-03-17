#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas de Repetição
#Exercício 6 - Faça um Programa que leia três números e mostre o maior deles.

try: 
  maior = n1 = float(input('Digite um número: ')) #Define o primeiro valor como o maior valor
  n2 = float(input('Digite um número: '))
  n3 = float(input('Digite um número: '))
  n_list = (n1, n2, n3)

  for i in range(1,3): #Faz duas iterações e compara o valor do n1 com os outros 2
    if maior < n_list[i]:
      maior = n_list[i] #Substitui o valores do maior quando for maior.
  else:
    print(f'O maior número entre eles é o número {maior}.')
  
except ValueError:
  print('Você não digitou um número.')
