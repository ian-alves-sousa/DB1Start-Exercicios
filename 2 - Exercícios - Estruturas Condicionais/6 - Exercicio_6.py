#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 6 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

try:
  print('Iremos te ajudar a escolher qual produto comprar!')
  v1 = float(input('Qual o valor do primeiro produto? '))
  v2 = float(input('Qual o valor do segundo produto? '))
  v3 = float(input('Qual o valor do terceiro produto? '))

  if v1 > 0 and v2 > 0 and v3 > 0:
    if v1 != v2 and v1 != v3 and v3 != v2:  
      if v1 < v2 and v1 < v3:
        print('Você deve comprar o primeiro produto pois ele é mais barato')
      elif v2 < v3:
        print('Você deve comprar o segundo produto pois ele é mais barato')
      else:
        print('Você deve comprar o terceiro produto pois ele é mais barato')
    elif v1 == v2 and v1 < v3:
      print('Os valores do primeiro e do segundo produtos são iguais, mas são os mais baratos, compre um deles.')
    elif v3 == v2 and v3 < v1:
      print('Os valores do segundo e do terceiro produtos são iguais, mas são os mais baratos, compre um deles.')
    elif v3 == v1 and v3 < v2:
      print('Os valores do primeiro e do terceiro produtos são iguais, mas são os mais baratos, compre um deles.')
    elif v1 == v2 and v1 > v3:
      print('Você deve comprar o terceiro produto pois ele é mais barato')
    elif v3 == v2 and v3 > v1:
      print('Você deve comprar o primeiro produto pois ele é mais barato')
    elif v3 == v1 and v3 > v2:
      print('Você deve comprar o segundo produto pois ele é mais barato')
    else:
      print('Os três produtos possuem os mesmos preços, compre qualquer um deles.')

  else:
    print('Você dogitou um preço negativo ou zerado. Tente novamente.')
except ValueError:
  print('Você não digitou um preço válido. Tente novamente.')