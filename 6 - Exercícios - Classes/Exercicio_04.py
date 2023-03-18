# Aluno: Ian Alves Sousa
# DB1 Start - Classes
# Exercício 4 - Escreva uma classe em Python que possua 2 métodos, um chamado adicionar_string e outro chamado inverter_string. 
# O primeiro método deverá receber uma string como parâmetro e armazená-la em um array. 
# O segundo, deverá listar as strings invertidas no seu conteúdo e também, na sua ordem de inclusão.

#Criação da Classe
class ManipulaString():
    """Classe para fazer manipulações com strings."""
    def __init__(self):
        """Inicializa o objeto criando a array."""
        self._array = []
        
    def set_string(self,string:str):
        """Adiciona uma strins na lista do objeto."""
        self._array.append(string)
        self.__inverter_string(string)
        
    def del_string(self,string:str):
        """Verifica se a string está na lista, e deleta a mesma."""
        if string in self._array:
            self._array.remove(string)
            print(f'A string {string} foi deletada da lista.')
        else:
            raise ValueError(f'A string {string} não está na lista para poder ser deletada.')
        
    def __inverter_string(self,string:str) -> str:
        """Inverte a string."""
        s = ''
        return s.join(list(reversed(string)))
        
    def get_strings_invertidas(self):
        """Retorna uma lista de strings invertidas e em ordme invertida."""
        for i in range(len(self._array)-1,-1,-1):
            invertida = self.__inverter_string(self._array[i])
            print(f'A string de posiçao {i+1} invertida é {invertida}.')
        
    def __str__(self):
        return f'A lista criada é: {self._array}'
        
        
# Implementação da classe
string = ManipulaString()
string.set_string('Inverte')
string.set_string('Olá Mundão')
string.set_string('Hello')
string.set_string('Helo')
string.del_string('Helo')
string.set_string('Ousadia e Alegria')
string.get_strings_invertidas()