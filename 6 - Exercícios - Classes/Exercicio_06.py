# Aluno: Ian Alves Sousa
# DB1 Start - Classes
# Exercício 6 - Utilizando a classe criada no exercício 5
# Imprima o tipo da classe, as chaves e valores do atributo __dict__.

from Exercicio_05 import Aluno
#Tipo da classe
print(type(Aluno))
#Dicionário da classe
print(f'\n{Aluno.__dict__}')
#Diretório da classe
print(f'\n{dir(Aluno)}')