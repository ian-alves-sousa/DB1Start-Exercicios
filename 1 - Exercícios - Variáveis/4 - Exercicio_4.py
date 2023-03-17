#Aluno: Ian Alves Sousa
#DB1 Start
#Exercício 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

try:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segundo nota: '))
    n3 = float(input('Digite a terceira nota: '))
    n4 = float(input('Digite a média nota: '))
    media = (n1 + n2 + n3 + n4) / 4
    print('A média do bimestre é {}'.format(media))
except ValueError:
  print('Você não digitou uma nota válida, digite um número')