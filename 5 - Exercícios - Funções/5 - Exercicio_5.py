# Aluno: Ian Alves Sousa
# DB1 Start - Funções
# Exercício 5 - Escreva um programa que execute uma função que calcule o fatorial de um número passado por parâmetro.

#Essa função recebe a entrada e faz alguns testes, se o número for 0, ele retorna 1, que é o fatorial de 0, se o número for negativo ele retorna uma resposta dizendo que é impossível calcular, e se o número for positivo entra em um uma estrutura de repetição e calcula o valor do fatorial.
def fatorial(inputFatorial : int) -> int :
    """Função recebe um número inteiro e retorna o fatorial."""
    num = 1
    if inputFatorial == 0 :
        return num
    elif inputFatorial < 0:
        return 'impossível de calcular, pois o número é negativo'
    else:
      for i in range(inputFatorial,1,-1): 
          #Inicia o for pelo valor de entrada e decresce até 2, pois num já está definido como 1 de default.
          num *= i
    return num

#O propósito dessa função é que a função fatorial receba apenas um número inteiro, e caso o cliente não digite o número inteiro de primeira, ele possa tentar novamente sem sair do programa, até que enfim ele digite um número inteiro, o range(100) foi definido para que haja 100 tentativas para digitar esse número.
def entrada () -> int :
    """Função define a entrada como um número inteiro"""
    for i in range(100):
      try:
        inteiro = int(input('\nDigite um número inteiro: '))
        return inteiro
      
      except ValueError:
        print('Valor inválido.')


inputFatorial = entrada() #Recebe a entrada como um número inteiro
print(f'\nO fatorial de {inputFatorial}! é {fatorial(inputFatorial)}.')