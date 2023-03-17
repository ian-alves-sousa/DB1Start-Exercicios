# Aluno: Ian Alves Sousa
# DB1 Start - Funções
# Exercício 4 - Escreva um programa que execute uma função que retorne o inverso de uma string passada por parâmetro.

#Essa função recebe uma string, a transforma de uma lista, depois inverte essa lista eu usa a função join() para juntar todos os parêmtros invertidos.
def inverteString(recebeString: str) -> str:
    """Recebe uma string e inverte a mesma."""
    listaString = list(recebeString)
    listaString.reverse()

    return ''.join(listaString) #A função join junta os componentes da lista, e os separa pelo parâmetro definido antes, como foi definido '', ou seja nada, ele junta todas as strings.

#O programa recebe uma string e a inverte, mesmo essa string sendo números, ou com espaços, letras maíusculas ou minúsculas, respeita todos os caracteres colocados, considerando como uma string.
recebeString = input('Digite uma string: ')
print(f'\n---A string passada por parâmetro foi: {recebeString}')
print(f'--A string invertida fica dessa forma: {inverteString(recebeString)}')
