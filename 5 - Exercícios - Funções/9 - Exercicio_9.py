# Aluno: Ian Alves Sousa
# DB1 Start - Funções
# Exercício 9 - Escreva um programa que execute uma função que valide se o número informado é um número perfeito ou não.
#Nota: De acordo com a Wikipedia, um número perfeito é um número inteiro, positivo que seja igual à soma de todos os seus divisores positivos excluindo o próprio número. Equivalente a isto, um número perfeito é a metade da soma de todos os seus divisores positivos, incluindo o próprio número.

#Função recebe um número natural, e coloca ele em uma estrutura de repetição, dividindo ele por todos os números menores que ele. Os valores que dividem o número de entrada são somados, inclusive o 1 e o ele próprio. Após isso é verificado se essa contagem é metade do número entrada, se for, o número é perfeito, se não, não é.
def perfeito(num: int) -> bool:
    """Função verifica se o número natural é perfeito."""
    cont = 0
    for i in range(1,num+1):
        if (num % i) == 0:
            cont += i
    if (cont/2) == num:
        return True
    return False
    

#Função criada para verificar se o número da entrada é um número natural, e para dar uma outra chance ao usuário de colocar um número correto, caso a entrada não tenha sido satisfatória, e o programa não se encerrar e ter que rodar o mesmo novamente.
def natural() -> int:
    """Recebe um número natural."""
    for i in range(100):
        try:
            num = int(input('\nDigite um número natural: '))
            if num < 0:
                print(f'{num} não é um número natural.')
            else:
                return num

        except ValueError:
            print('Valor inválido. Tente novamente.')

#Função recebe o número natural e a verificação se é primo ou não e printa a veredito final.
def printPerfeito(num : int,pfct : bool):
    """Printa se o número é primo ou não"""
    if pfct == True:
        print(f'O número {num} é um número perfeito.')
    else:
        print(f'O número {num} NÃO é um número perfeito.')


num = natural() #Chama a função de entrada do número natural
printPerfeito(num,(perfeito(num))) #Printa o número com a sua devida verificação