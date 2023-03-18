# Aluno: Ian Alves Sousa
# DB1 Start - Classes
# Exercício 5 - Escreva uma classe em Python que receba como arqumentos um id, um nome e a classe de um estudante.
# Sendo que o nome e a classe não são obrigatórios no momento da instanciação da classe.
# Crie um método que imprima o id do aluno, e se houver nome, imprima o nome, e se houver classe, imprima a classe também.

#Criação da classe
class Aluno():
    """Classe para gerenciamento dos alunos."""
    def __init__(self,id:int,nome=None,classe=None):
        """Inicializa a classe e verifica os valores inseridos."""
        if not isinstance(id,int):
            raise ValueError(f'A id {id} é inválida.')
        elif not (isinstance(nome,str) or nome == None):
            raise ValueError(f'O nome {nome} é inválido.')
        elif not ((isinstance(classe,str) and (len(classe) == 2)) or classe == None) :
            raise ValueError(f'A classe {classe} é inválido.')    
        self._id = id
        self.nome = nome
        self.classe = classe
    
    def imprima(self):
        """Imprime as entradas, conforme foram colocadas."""
        if self.nome == None and self.classe == None:
            print(f'O aluno tem é id: {self._id}')
        elif self.classe == None:
            print(f'O aluno tem a id {self._id} e se chama {self.nome}.')
        elif self.nome == None:
            print(f'O aluno tem a id  {self._id} e pertence a classe {self.classe}.')
        else:
            print(f'O aluno tem a id {self._id}, se chama {self.nome} e pertence a classe {self.classe}.')
            
    def remove_nome(self):
        """Remove o nome e retorna ele a None."""
        self.nome = None
        
    def remove_classe(self):
        """Remove a classe e retorna ela a None."""
        self.classe = None
            
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,id):
        self._id = id
    
