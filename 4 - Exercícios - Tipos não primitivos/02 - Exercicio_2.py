# Aluno: Ian Alves Sousa
# DB1 Start - Tipos não primitivos
# Exercício 2 - Escreva um programa que multiplique todos os itens de uma lista.

lista = []  # Cria uma lista vazia
print('Vamos criar uma lista a multiplicar os seus valores! Digite 0 para parar a lista (Qualquer multiplicação por 0 tem o valor zerado também, por isso não vamos considerar essa multiplicação.)')
for i in range(100): #Define um número de iterações alto para que quem for testar não saia do for até chegar o break
    try:
        # Acrescenta o valor ao final da lista
        lista.append(float(input('Digite um valor (para parar a multiplicação digite 0): ')))

        if lista[0] != 0:
          # Compara o valor colocado com 0, se for 0, o deleta, printa a lista a finaliza.
          if lista[len(lista)-1] == 0:
            del lista[len(lista)-1]
            print(f'A lista que você criou é: {lista}')
            break
        else: #Se o primeiro número for 0, precisa de outra entrada para parar a formação da lista.
            del lista[0]
            print('Você criou uma lista vazia, adicione um número para multiplicar.')

    except ValueError:  # Se for digitado algum valor diferente de floar vai dar essa mensagem.
        print('Valor inválido. Tente novamente!')

multi = 1
for i in lista:  # Faz a quantidade de iterações do tamanho da lista e soma valor por valor.
    multi *= i
print(f'Multiplicando todos os itens dessa lista o valor final é: {multi}')