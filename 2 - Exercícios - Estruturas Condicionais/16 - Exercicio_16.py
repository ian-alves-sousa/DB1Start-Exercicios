#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 16 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

try:
  n = int(input('Digite um número inteiro menor que 1000: '))

  if n <= 1000 and n >= 0:
    centena = (n // 100)
    centenaResto = n % 100
    dezena = centenaResto // 10
    unidade = centenaResto % 10

    print(f'''O número que você digitou foi: {n}
    Esse número tem {centena} centenas
    Além disso, ele tem {dezena} dezenas
    E por fim, tem {unidade} unidades.''')
  
  else:
    print('Você digitou um número menor que 0 ou maior que 1000')
 

except ValueError:
  print('Você não digitou um número inteiro. Tente novamente.')