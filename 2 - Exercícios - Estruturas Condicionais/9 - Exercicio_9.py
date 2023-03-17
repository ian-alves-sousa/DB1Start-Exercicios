#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 9 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

try:
  print('Bem vindo às Organizações Tabajara, iremos reajustar o seu salário!')
  salario = float(input('Digite o valor do seu salário: '))

  if salario <= 1500:
    reajuste = salario * 1.20
  elif 1500 < salario <= 2000:
    reajuste = salario * 1.15
  elif 2000 < salario <= 2500:
    reajuste = salario * 1.10
  else:
    reajuste = salario * 1.05
  
  print('O seu salário reajustado é de R${:.2f}'.format(reajuste))
  
except ValueError:
  print('Você não digitou um salário válido. Tente novamente ou ficará sem reajuste.')