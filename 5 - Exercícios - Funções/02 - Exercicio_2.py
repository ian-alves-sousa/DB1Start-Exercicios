# Aluno: Ian Alves Sousa
# DB1 Start - Funções
# Exercício 2 - Escreva um programa que execute uma função que some todos os itens de uma lista passada por parâmetro.

#Essa função recebe uma lista de números, e os soma utilizando a função sum().
def somaLista(lista : list) -> int:
  """Soma os valores utilizando a função sum()."""
  total = sum(lista)
  return total

#Essa função solicita vários números como entradas e coloca eles em uma estrutura de repetição, e os soma.
def somaLista2(*args : int) -> int:
  """Soma os argumentos que estavam dentro da lista um por um."""
  total = 0
  for i in range(len(args)):
    total += args[i]
  return total

#Cria uma lista dentro de uma função, solicitando os números inteiros e adicionando um por um no final da lista, finalizando a mesma quando 0 for digitado.
def listCreate() -> list:
  """Função cria uma lista com números inteiros solicitados ao cliente."""
  lista = []
  for i in range(100):
    try:
      lista.append(int(input('Digite um número inteiro para a lista: ')))
      if lista[0] == 0:
        del lista[0]
        print ('Não deixe sua lista vazia, digite um valor.')
      else:
        if lista[len(lista)-1] == 0:
          del lista[len(lista)-1]
          print(f'A lista foi finalizada: {lista}')
          return lista

    except ValueError:
      print('Valor inválido. Tente novamente!')


lista = listCreate() #Chama a função que cria a lista
#Como criei duas formas de somar os valores da lista, printei ambos.
print(f'\nA soma total dessa lista é: {somaLista(lista)}')
print(f'A soma total dessa lista é: {somaLista2(*lista)}')