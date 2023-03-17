#Aluno: Ian Alves Sousa
#DB1 Start
#Exercício 2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

#Corpo do código
try:
  n = int(input('Digite um número inteiro: '))
  print('O número informado foi', n)
except ValueError:
  print("Você não digitou um número inteiro :/")