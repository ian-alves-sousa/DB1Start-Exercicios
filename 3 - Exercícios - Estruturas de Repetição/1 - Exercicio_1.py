#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas de Repetição
#Exercício 1 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

try:
  for n in range(2): #Realiza apenas duas iterações, uma pedindo a primeira entrada e a segunda pedindo a segunda entrada
    if n == 0:
      hora = float(input('Informe quanto você ganha por hora: '))
    else:
      hmes = int(input('Informe agora o número de horas trabalhadas no mês: '))

#Cálculo é realizado e retornamos o valor do salário da pessoa depois de ter colocado as duas entradas.
  salario = hora * hmes
  print(f'O seu salário nesse mês será de: R$ {salario:.2f}')

except ValueError: #Se algum valor diferente do solicitado for inserido, o programa vai levar ao fim.
  print('Valor inserido é inválido. Lembre-se que o número de horas é um número inteiro.')
