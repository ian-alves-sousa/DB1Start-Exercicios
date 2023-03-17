# Aluno: Ian Alves Sousa
# DB1 Start - Tipos não primitivos
# Exercício 12 - Escreva um programa que verifique se uma lista está vazia ou não.

lista = []  # Cria uma lista vazia
for i in range(100):  # Define um número de iterações alto para que quem for testar não saia do for até chegar o break
    try:
        # Acrescenta o valor ao final da lista
        lista.append(float(input('Digite um valor (para parar a soma digite 0): ')))

        # Compara o valor colocado com 0, se for 0, o deleta, printa a lista a finaliza.
        if lista[len(lista)-1] == 0:
          del lista[len(lista)-1]
          break

    except ValueError:  # Se for digitado algum valor diferente de float vai dar essa mensagem.
        print('Valor inválido. Tente novamente!')

#Utilizando novamente o exercicio 1, comparamos agora a lista criada com uma lista vazia.
if lista == []:
  print('\nA lista está vazia!')
else:
  print(f'\nA lista que você criou é: {lista}')