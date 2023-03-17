# Aluno: Ian Alves Sousa
# DB1 Start - Tipos não primitivos
# Exercício 1 - Escreva um programa que some todos os itens de uma lista.

lista = []  # Cria uma lista vazia
for i in range(100):  # Define um número de iterações alto para que quem for testar não saia do for até chegar o break
    try:
        # Acrescenta o valor ao final da lista
        lista.append(float(input('Digite um valor (para parar a soma digite 0): ')))

        if lista[0] != 0:
          # Compara o valor colocado com 0, se for 0, o deleta, printa a lista a finaliza.
          if lista[len(lista)-1] == 0:
            del lista[len(lista)-1]
            print(f'A lista que você criou é: {lista}')
            break
        else: #Se o primeiro número for 0, precisa de outra entrada para parar a formação da lista.
            del lista[0]
            print('Você criou uma lista vazia, adicione um número para somar.')

    except ValueError:  # Se for digitado algum valor diferente de floar vai dar essa mensagem.
        print('Valor inválido. Tente novamente!')

soma = 0
for i in lista:  # Faz a quantidade de iterações do tamanho da lista e soma valor por valor.
    soma += i
print(f'Somando todos os itens dessa lista o valor final é: {soma}')
