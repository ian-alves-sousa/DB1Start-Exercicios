#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas de Repetição
#Exercício 2 - Faça um Programa que peça dois números e imprima a soma.

try:
  valor = int(input('Digite quantas somas gostaria de realizar: '))
  for n in range(valor): #Realiza a quantidade de iterações definida na entrada anterior
    n1 = float(input('Informe o primeiro número: '))
    n2 = float(input('Informe o segundo número: '))
    soma = n1 + n2
    print('O valor entre a soma de {} com {} é: {}'.format(round(n1,2),round(n2,2),round(soma,2)))

except ValueError: #Se algum valor diferente do solicitado for inserido, o programa vai levar ao fim.
  print('Valor inserido é inválido. Você não digitou um número.')
 