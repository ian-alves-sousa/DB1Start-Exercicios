#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 14 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

try:
  print('Vamos descobrir se esse ano é bissexto!')
  ano = int(input('Digite o ano:  '))
  
  if ano == 0:
    print(f'Você digitou {ano}, vamos tentar um ano um pouco maior.')
  elif ano > 0:
    if (ano % 4) == 0:
      print(f'Você digitou {ano}, e esse ano é bissexto!')
    else:
      print(f'Você digitou {ano}, mas esse ano não é bissexto!')
  else:
    print(f'Você digitou um ano negativo, tente novamente com números positivos.')
  
except ValueError:
  print('Você digitou um ano inválido. Tente novamente.')