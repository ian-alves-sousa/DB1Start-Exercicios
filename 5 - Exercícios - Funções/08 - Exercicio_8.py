# Aluno: Ian Alves Sousa
# DB1 Start - Funções
# Exercício 8 - Escreva um programa que execute uma função que receba um número informado no console como parâmetro e verifique se o número informado é primo ou não.
#Nota: Número primo é um número natural, maior que 1 e que não tenha outros divisores além do 1 e dele mesmo.

#A lógica para essa função é a seguinte, se o número é maior que 1, colocamos ele dentro de uma estrutura de repetição que vai de 1 até o número em questão e o código dentro fará com que verifiquemos se o número colocado é divisível por i, sendo i os números dessa sequência. O número primo só ode ser dividido por 1 e por ele mesmo, então, se a contagem for 2, é primo, se não for não é.
def primo(num: int) -> bool:
    """Função retorna true quano o número natual é primo."""
    cont = 0
    if num == 0:
        return False
    elif num == 1:
        return True
    else:
      for i in range(1,(num+1)):
          if (num % i) == 0:
              cont += 1
      else:
          if cont == 2:
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
def printPrimo(num : int,primo : bool):
    """Printa se o número é primo ou não"""
    if primo == True:
        print(f'\nO número {num} é um número primo.')
    else:
        print(f'\nO número {num} NÃO é um número primo.')


num = natural() #Chama a função de entrada do número natural
boleano = (primo(num)) #Guarda o resultado da verificação do número natural
printPrimo(num,boleano) #Printa o número com a sua devida verificação


