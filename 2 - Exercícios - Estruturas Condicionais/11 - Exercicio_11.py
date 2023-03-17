#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 11 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

try:
  print('''Qual é o dia da semana?
  1 - Domingo
  2 - Segunda
  3 - Terça
  4 - Quarta
  5 - Quinta
  6 - Sexta
  7 - Sábado''')
  dia = int(input('Digite o número que corresponde ao dia da semana: '))

  if dia == 1:
    print('Estamos no DOMINGO, espera que esteja descansando, essa semana será puxada!')
  elif dia == 2:
    print('Estamos na SEGUNDA, enfrente essa batalha e sairá vencedor!')
  elif dia == 3:
    print('Estamos na TERÇA, falta muito pra acabar a semana?')
  elif dia == 4:
    print('Estamos na QUARTA, já estamos na metade da semana, aguente firme!')
  elif dia == 5:
    print('Estamos na QUINTA, já é quase sexta.')
  elif dia == 6:
    print('Estamos na SEXTA, FINALMENTE!.')
  elif dia == 7:
    print('Estamos no SÁBADO, tu batalhou muito pra esse cia chegar, aproveite.')
  else:
    print(f'Você não digitou um número válido.')
  

except ValueError:
  print(f'Você não digitou um número válido.')