# Aluno: Ian Alves Sousa
# DB1 Start - Funções
# Exercício 6 - Escreva um programa que execute uma função que conte o número de letras maiúsculas e minúsculas de um texto e que ao final, chame outra função para imprimir o resultado.

#Essa função recebe como argumento uma string, e dela cria diversas listas, sempre filtrando o que deseja, para filtrar a lista utilizei duas formas, uma usando a função filter() e outra com comprehension list, além disso, quando o caractere não é minústulo, maísculo, número  ou espaço, o consideramos um caractere especial.
def qtde (string : str) -> tuple :
    """Função recebe uma string e retorna a quantidade de letras maísculas, minúsculas, números, espaços e caracteres especiais."""
    minuscula = len(list(filter(lambda x: x.islower(), string)))
    maiuscula = len([x for x in string if x.isupper()])
    num = len(list(filter(lambda x: x.isnumeric(), string)))
    space = len([x for x in string if x.isspace()])
    special = len(string) - minuscula - maiuscula - num - space
    return minuscula,maiuscula,num,space,special

#Essa função relaciona a quantidade de caracteres com a sua quantidade através de uma estrutura de repetição em dois tipos não primitivos diferentes.
def printQtde(tupla : tuple):
    """Função para printar os valores obtidos na função qtde(), de acordo com seu tipo de caractere."""
    tipos = ['minúsculo', 'maiúsculo', 'numeral', 'espaço', 'especial']
    for i in range(5):
        if tupla[i] == 0:
            print(f'Essa string não tem caractere do tipo {tipos[i]}.')
        elif tupla[i] == 1:
            print(f'Essa string tem 1 caractere do tipo {tipos[i]}.')
        else:
          print(f'Essa string tem {tupla[i]} caracteres do tipo {tipos[i]}.')

string = input('Digite uma string:')
printQtde(qtde(string)) #Chama a função para encontrar a quantidade de cada tipo de caractere dentro de uma função para imprimir essas quantidades
