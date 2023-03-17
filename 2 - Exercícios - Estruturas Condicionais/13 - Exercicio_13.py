#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 13 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c

try:
  print('Vamos resolver uma equação do segundo grau, na forma ax² + bx + c')
  a = float(input('Digite o valor de a:  '))
  b = float(input('Digite o valor de b:  '))
  c = float(input('Digite o valor de b:  '))

  print(f'A equação de segunda grau ficou como: {a}x² + {b}x + {c}')

  delta = b**2 - 4*a*c
  x1 = (-b + delta**(1/2))/(2*a)
  x2 = (-b - delta**(1/2))/(2*a)
  if delta == 0:
    print(f'As raízes da função segundo grau são iguais: {x1}')
  elif delta > 0:
    print(f'As raízes da função segundo grau são: {x1:.2f}, {x2:.2f}')
  else:
    print(f'As raízes da função segundo grau tem parte imaginárias e são: {x1:.2f}, {x2:.2f}')

except ValueError:
  print('Você digitou um valor inválido. Tente novamente.')