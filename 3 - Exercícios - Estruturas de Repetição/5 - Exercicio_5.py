#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas de Repetição
#Exercício 5 - Faça um Programa que peça dois números e imprima o maior deles.

n = 0
soma = 0
while n < 2: #Realiza a quantidade de iterações definida na entrada anterior
  try: #Faz o teste se o valor colocado é real, se não ele não soma e continua no while, pedindo outro valor
    n1 = float(input('Digite um número: '))
    soma += n1
    n += 1
  except ValueError:
    print('Você não digitou um número.')
else: # A lógica para quando sai do while é se a soma é maior que duas vezes o último valor inserido, então o primeiro valor inserido é o meior. Se a soma for menor que duas vezes o valor inserido, então o segundo valor inserido é o maior, e se nada disso for verdadeiro, então os valores são iguais.
  if soma > (2*n1): 
    print(f'O número {(soma-n1)} é maior que o número {n1}.')
  elif soma < (2*n1):
    print(f'O número {(n1)} é maior que o número {(soma-n1)}.')
  else:
    print(f'Os números digitados são iguais e são o número {n1}.')