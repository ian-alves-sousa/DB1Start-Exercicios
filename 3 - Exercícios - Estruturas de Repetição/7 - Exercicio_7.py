#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas de Repetição
#Exercício 7 - Faça um Programa que leia três números e mostre o maior e o menor deles.


x = 0
while x < 3:
  try: #Deixa as entradas em um loop, até a entrada não ser a correta, o sistema não pede a próxima
    if x == 0:
      maior = menor = n1 = float(input('Digite o primeiro número: ')) #Define o primeiro valor como o maior e menor valor
    elif x == 1:
      n2 = float(input('Digite o segundo número: '))
    else:
      n3 = float(input('Digite o terceiro número: '))
    x += 1
  except ValueError:
    print('Você não digitou um número.')

n_list = (n1, n2, n3)
for i in range(1,3): #Faz duas iterações e compara o valor do n1 com os outros 2
  if maior < n_list[i]:
    maior = n_list[i] #Substitui o valores do maior quando for maior.
  if menor > n_list[i]:
    menor = n_list[i] #Substitui o valores do menor quando for maior.
else:
  print(f'O maior número entre eles é o número {maior}.')
  print(f'O menor número entre eles é o número {menor}.')
  
