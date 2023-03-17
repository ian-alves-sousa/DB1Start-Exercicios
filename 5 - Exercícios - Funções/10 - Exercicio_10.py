# Aluno: Ian Alves Sousa
# DB1 Start - Funções
# Exercício 10 - Escreva uma função que imprima as primeiras n linhas do triângulo de pascal.
# Triângulo de pascal é uma figura aritmética e geométrica imaginada por Blaise Pascal. Cada número é a soma dos dois números diretamente acima.

#Essa função inicia-se criando uma lista 2 com todos os elementos da lista 1, que de default é [1], e printa todos os seus elelentos um do lado do outro e depois pula uma linha. A função é recursiva e faz as somas do triângulo de pascal usando a lista como base e coloca os resultados em l2, e enquando o número colocado não for do mesmo tamanho de l2, a recursividade continua.
def Pascal(num: int, lista: list):
    """Função retorna na tela um Triângulo de Pascal com n linhas."""
    l2 = [i for i in lista]
    for i in l2:
        print(i, end=' ')
    print('')
    if num == len(lista):
        return
    else:
        for i in range(len(lista)):
            if i > 0: #Condição para não somar o primeiro número com o último, pois lista[-1] é o último da lista
                l2[i] = lista[i-1] + lista[i]
            if i == (len(lista)-1):
                l2.append(1)        
    Pascal(num, l2)


# Função criada para verificar se o número da entrada é um número natural, e para dar uma outra chance ao usuário de colocar um número correto, caso a entrada não tenha sido satisfatória, e o programa não se encerrar e ter que rodar o mesmo novamente.
def natural() -> int:
    """Recebe um número natural."""
    for i in range(100):
        try:
            num = int(input('\nDigite um número natural: '))
            if num <= 0:
                print(f'{num} não é válido.')
            else:
                return num

        except ValueError:
            print('Valor inválido. Tente novamente.')


num = natural()  # Chama a função de entrada do número natural
lista = [1]
print(f'\nO Triângulo de Pascal com {num} linhas é:')
Pascal(num, lista)
