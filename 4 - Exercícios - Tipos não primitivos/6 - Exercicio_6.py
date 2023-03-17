# Aluno: Ian Alves Sousa
# DB1 Start - Tipos não primitivos
# Exercício 6 - Escreva um programa que ordene em ordem crescente uma lista de tuplas informadas, pelo último item da tupla (Exemplo de lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Resultado esperado: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] )

print('Me ajude a criar 5 tuplas com números inteiros e vamos ordena-las pelo último item informado.')
lista = []
listaFinal = []
for i in range(6): #Define 5 tuplas a serem completadas
  for j in range(100): #Cria um número alto de iterações para que quando digitarem um valor não inteiro não encerre a contagem e sim peça um novo valor, não considerando o não válido
    try:
      #Adiciona um valor a tupla i+1
      lista.append(int(input('Digite um número inteiro(Para finalizar a tupla figite 0): ')))

      if lista[0] == 0: #Se o primeiro valor da tupla for 0 ele pede um novo valor e deleta o 0
        del lista[0]
        print('Digite um número diferente de 0 para completar a tupla.')
      else:
        if lista[len(lista)-1] == 0: #Quando o 0 é digitado o mesmo é deletado, a lista criado é tranformada em tupla, e essa tupla adiciona em um outra lista, e a lista anterior é limpa para receber novos valores
          del lista[len(lista)-1]
          tupla = tuple(lista)
          listaFinal.append(tupla)
          lista.clear()
          print(f'\nTupla {i+1} finalizada: {tupla}')
          break

    except ValueError:
      print('Digite uma tupla com números inteiros.')

listaFinal.sort(key=lambda x: x[len(x)-1]) #Ordena a lista em função de um lambda onde ele manda ordenar pelo último valor dos itens da lista
print(f'\nA lista final de tuplas ordenadas é: {listaFinal}')