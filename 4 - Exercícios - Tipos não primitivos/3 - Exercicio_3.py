# Aluno: Ian Alves Sousa
# DB1 Start - Tipos não primitivos
# Exercício 3 - Escreva um programa que retorne o maior e o menor número de uma lista.

lista = []  # Cria uma lista vazia
print('Vamos criar uma lista de 5 valores e mostrar qual deles é o menor e qual o maior.')
for i in range(100): #Define um número de iterações alto para que quem for testar não saia do for até chegar o break
  try:
    # Acrescenta o valor ao final da lista
    lista.append(float(input('Digite um valor: ')))
    if len(lista) == 5: #Quando a lista chegar a 5 itens, vai printar a lista e vai sair do for
      print(f'A lista que você criou é: {lista}')
      break

  except ValueError:  # Se for digitado algum valor diferente de floar vai dar essa mensagem.
    print('Valor inválido. Tente novamente!')

lista.sort() #Organiza a lista de números em ordem crescente para ficar mais fácil de encontrar o maior e o menor
print(f'O menor número da lista é {lista[0]} e o maior número é {lista[4]}.')

