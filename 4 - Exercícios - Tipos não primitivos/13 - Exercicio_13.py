# Aluno: Ian Alves Sousa
# DB1 Start - Tipos não primitivos
# Exercício 13 - Escreva um programa que clone ou copie uma lista.
# Nesse caso, para mostrar o exemplo da copia eu quis solicitar quando a copia seria feita e não apenas copiar a lista no final, de qualquer forma, o intuito do exercício é fixar o conceito e os comandos para a cópia e por isso decidi fazer dessa forma.

lista = copiaLista = []  # Cria uma lista vazia
for i in range(5):  # Define um número de iterações alto para que quem for testar não saia do for até chegar o break
    try:
        # Acrescenta o valor ao final da lista
        lista.append(
            float(input('Digite um valor (para parar a soma digite 0): ')))

        # Compara o valor colocado com 0, se for 0, o deleta, printa a lista a finaliza.
        if lista[len(lista)-1] == 0:
            del lista[len(lista)-1]
            copiaLista = lista.copy()

    except ValueError:  # Se for digitado algum valor diferente de float vai dar essa mensagem.
        print('Valor inválido. Tente novamente!')

if copiaLista == []:
    print(f'A lista final é: {lista}.')
else:
    print(f'A lista copiada no momento da cópia foi: {copiaLista}.')
