from Exercicio_05 import Aluno
#Implementação da classe           
aluno_1 = Aluno(123,'João','7A')
aluno_2 = Aluno(124,'Marcos')
aluno_3 = Aluno(125,'7B')
aluno_4 = Aluno(123,'Pedro','9A')
grupo = [aluno_1,aluno_2,aluno_3,aluno_4]
for i in grupo:
    i.imprima()