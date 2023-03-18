# Aluno: Ian Alves Sousa
# DB1 Start - Classes
# Exercício 9 - Criar uma classe chamada Ponto3D que herde de Object. Na classe Ponto3D, crie um construtor que receba 3 numeros, e armezene-os em 3 variáveis. Crie uma forma para que ao exibir o conteúdo da instancia, a informação apresenta seja: (<num1>; <num2> , <num3>)
# Uso:
# ponto = Ponto3D(1, 2, 3)
# Print(ponto) => (1, 2, 3)

# Criação da classe
class Ponto3D(object):
    """Classe que exite o conteúdo da instância."""
    def __init__(self, num1, num2, num3):
        """Inicializa a instância e chega seus parâmetros"""
        self.__check(num1, num2, num3)

    def __check(self, num1, num2, num3):
        """Faz a checagem se as entradas do Ponto3D são inteiros ou decimais."""
        if not (isinstance(num1, int) or isinstance(num1, float)):
            raise ValueError(f'O valor {num1} é inválido.')
        elif not (isinstance(num2, int) or isinstance(num2, float)):
            raise ValueError(f'O valor {num2} é inválido.')
        elif not (isinstance(num3, int) or isinstance(num3, float)):
            raise ValueError(f'O valor {num3} é inválido.')
        else:
            self.num1 = num1
            self.num2 = num2
            self.num3 = num3

    def __str__(self):
        """Define a saída quando for printado."""
        return f"({self.num1},{self.num2},{self.num3})"

    def __repr__(self):
        """Define a saída quando for representado"""
        return f'<num1 : {str(self.num1)}> <num2 : {str(self.num2)}> <num3 : {str(self.num3)}>'


# Implementação da classe
ponto = Ponto3D(1, 2, 3)
print(ponto)
print(repr(ponto))
