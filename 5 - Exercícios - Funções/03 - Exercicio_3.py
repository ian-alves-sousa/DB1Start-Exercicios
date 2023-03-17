# Aluno: Ian Alves Sousa
# DB1 Start - Funções
# Exercício 3 - Escreva um programa que execute uma função que multiplique todos os números de uma lista passada por parâmetro.

#Essa função solicita uma lista e multiplica valor por valor, até o fim da mesma.
def multiLista(lista : list) -> int:
  """Multiplica os argumentos que estavam dentro da lista um por um."""
  total = 1
  for i in lista:
    total *= i
  return total

#Cria uma lista dentro de uma função, solicitando os números inteiros e adicionando um por um no final da lista, finalizando a mesma quando 0 for digitado.
def listCreate() -> list:
  """Função cria uma lista com números inteiros solicitados ao cliente."""
  lista = []
  for i in range(100):
    try:
      lista.append(int(input('\nDigite um número inteiro para a lista: ')))
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
print(f'\nA multiplicação total dessa lista é: {multiLista(lista)}')
