#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas de Repetição
#Exercício 4 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre

n = 0
soma = 0
while n < 2: #Realiza a quantidade de iterações definida na entrada anterior
  try: #Faz o teste se o valor colocado é inteiro, se não ele não soma e continua no while, pedindo outro valor
    n1 = int(input('Digite um número inteiro: '))
    soma += n1
    n += 1
  except ValueError:
    print('Você não digirou um número inteiro.')
else:
  while n < 3:
    try:  #Faz o teste se o valor colocado é real, se não ele não soma e continua no while, pedindo outro valor
      n2 = float(input('Digite um número real: '))
      final = soma + n2
      print('A soma entre os valores é: {}'.format(round(final,2),))
      n += 1
    except ValueError:
      print('Você não digirou um número real.')
  

