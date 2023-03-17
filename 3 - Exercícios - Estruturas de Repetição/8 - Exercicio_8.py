#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas de Repetição
#Exercício 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

#A dificuldade nesse programa foi quanto as condições dentro da estrutura de repetição para imprimir os valores repetidos ou não. Assim, para finalizar a lógica e deixar funcional, deixei com bastante explicações e pouco rebuscado. Pretendo voltar ao futuro para atualizar.

x = 0
print('Vamos te ajudar a decidir qual produto comprar, digite o valor dos produtos.')
while x < 3:
  try: #Deixa as entradas em um loop, até a entrada não ser a correta, o sistema não pede a próxima
    if x == 0:
      menor = n1 = n2 = n3 = float(input('Digite o valor do PRIMEIRO produto: ')) #Define o primeiro valor como o maior e valor
    elif x == 1:
      n2 = float(input('Digite o valor do SEGUNDO produto: '))
    else:
      n3 = float(input('Digite o valor do TERCEIRO produto: '))
    if n1 <= 0 or n2 <= 0 or n3 <= 0: #Caso alguém digitar um valor negativo, vai solicitar o valor novamente
      print('Você digitou um preço negativo, tente novamente.')
      continue
    x += 1
  except ValueError:
    print('Você não digitou um número.')

x = 1
n_list = (n1, n2, n3,None)
rep = 1
for i in range(1,3): #Faz duas iterações e compara o valor do n1 com os outros 2
  if menor > n_list[i]:
    menor = n_list[i] #Substitui o valores do menor quando for maior.
    x = i + 1

  if (n_list[i] == n_list[i - 1] or n_list[i-1] == n_list[i+1]) and menor >= n_list[i-1]: #A condição para somar rep são dois números serem iguais e o menor ser maior ou igual o anteior, isso faz com que quando a pessoa digitar dois números iguais e o menor ser um deles, o número de rep aumentar
    rep += 1
    if n_list[i-1] == n_list[i] > menor: #Contudo, o número também aumenta quando o menor não se repete, dessa forma, esse if tira a repetição antes colocada.
      rep -= 1
    elif i == 1 and (n_list[i-1] == n_list[i] > n_list[i+1]): #Em uma das condições que o menor não se repete, quando ao primeiro e o segundo são iguais e maiores que o menor, o número de repetições acresce devido, mas não se encaixa na anterior para retirar, e essa condição força que o número de rep volte a ser 1 para esse caso específico.
      rep -= 1
    
else: #Condições para diferentes tipos de entradas, com números iguais ou não
  if rep == 1:
    print(f'Você deve comprar o produto de número {x}, com o valor de R${menor:.2f}.')
  elif rep == 2:
    print(f'Você digitou dois valores iguais, então compre qualquer um dos produtos com o valor de R${menor:.2f}.')
  else:
    print(f'Você digitou três números com o mesmo valor, de R${menor:.2f}, então compre qualquer um deles.')