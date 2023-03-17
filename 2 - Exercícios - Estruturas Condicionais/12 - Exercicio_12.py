#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 12 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.

try:
  print('Digite os valores das duas notas para calcular sua média. (Valores de 0 a 10)')
  n1 = float(input('Digite sua primeira nota:  '))
  n2 = float(input('Digite sua segunda nota:  '))

  if n1 >=0 and  n2 >=0:
    if n1 <= 10 and n2 <= 10:
      media = (n1 + n2) / 2
      print(f'A sua média é {media:.1f}.')

      if media >= 6:
        print(f'E com essa média você está APROVADO.')
      else:
        print(f'E com essa média você está REPROVADO.')
    else:
      print('Você digitou uma nota maior que 10.')
  else:
    print('Você digitou uma nota negativa.')

except ValueError:
  print('Você digitou um valor inválido. Tente novamente.')