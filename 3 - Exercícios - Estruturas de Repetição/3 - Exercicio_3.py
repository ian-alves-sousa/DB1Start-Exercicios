#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas de Repetição
#Exercício 3 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

try:
  soma = 0
  print('Digite a seguir as suas 4 notas bimestrais: ')
  n = 0  #Demonstração de como seria a lógica utilizando o while
  while n < 4:
    n1 = float(input(f'Informe a sua nota de número {(n+1)}: ')) #Solicita a nota de número índice+1
    if n1 > 10 or n1 < 0:
      print('Você digitou uma nota inválida, digite uma nota entre 0 a 10.')
      continue
    n += 1
    soma += n1
  else:
    media = soma/4
    print('A média final entre as suas notas é de {}.'.format(round(media,2)))
    if media >= 7:
      print('Aprovado!')
    else:
      print('Reprovado!')
  
  

except ValueError: #Se algum valor diferente do solicitado for inserido, o programa vai levar ao fim.
  print('Valor inserido é inválido. Você não digitou um número.')


  #for n in range(4): #Realiza a quantidade de iterações definida
    #n1 = float(input(f'Informe a sua nota de número {(n+1)}: ')) #Solicita a nota de número índice+1
    #if n1 > 10 or n1 < 0:
     # print('Você digitou uma nota inválida, digite uma nota entre 0 a 10.')
      #n -= 1
     # break
  #  soma += n1
 # else:
  #  media = soma/4
   # print('A média final entre as suas notas é de {}'.format(round(media,2)))
   # if media >= 7:
   #   print('Aprovado!')
   # else:
   #   print('Reprovado!') Final
  