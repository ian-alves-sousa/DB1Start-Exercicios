# Aluno: Ian Alves Sousa
# DB1 Start - Funções
# Exercício 1 - Escreva um programa que execute uma função que encontre o maior número de uma lista passada por parâmetro.

#Essa função recebe uma lista de números, os organiza e inverte o valor, e retorna o primeiro número da lista, ou seja, o maior
def maiorNumero(lista : list) -> int:
  """Encontra o maior número de uma lista de números."""
  lista.sort(reverse=True)
  maior = lista[0]
  return maior

#Essa função solicita vários números como entradas e coloca eles em uma estrutura de repetição, quando o número for maior que o anterior, a variável local maior irá receber ele.
def maiorNumero2(*args : int) -> int:
  """Encontra o maior número entre vários números, e não dentro de uma lista, a entrada são vários argumentos."""
  maior = args[0]
  for i in range(1, len(args)):
    if args[i] > maior:
      maior = args[i]
  return maior

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
#Como criei duas formas de mostrar o maior número da lista, printei ambos.
print(f'O maior número dessa lista é {maiorNumero(lista)}')
print(f'O maior número dessa lista é {maiorNumero2(*lista)}')

