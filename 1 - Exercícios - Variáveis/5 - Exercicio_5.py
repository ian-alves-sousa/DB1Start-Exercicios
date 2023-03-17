#Aluno: Ian Alves Sousa
#DB1 Start
#Exercício 5 - Faça um Programa que converta metros para centímetros.

try:
    metros = float(input('Digite a medida em metros: '))
    cent = metros*100
    print('A medida {}m convertida para centrímetros é {}cm.'.format(metros,cent))
except ValueError:
  print('Você não digitou uma medida válida, digite um número!')