#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 8 - Faça um Programa que pergunte em que turno você estuda

try:
  print('''Em qual turno você estuda?
  M - Manhã
  T - Tarde
  N - Noite''')
  turno = str(input('Digite o turno que você estuda: '))

  if turno == 'M' or turno == 'm':
    print('Que legal! Você estuda no turno da manhã!')
  elif turno == 'T' or turno == 't':
    print('Que legal! Você estuda no turno da tarde!')
  elif turno == 'N' or turno == 'n':
    print('Que legal! Você estuda no turno da noite!')
  else:
    print(f'Você não digitou um turno válido.')
  

except ValueError:
  print(f'Você não digitou um turno válido.')