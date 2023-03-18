# Aluno: Ian Alves Sousa
# DB1 Start - Classes
# Exercício 7 - Criar uma classe Triangulo, que receba no seu construtor 3 medidas de ângulos.
# Criar um método check_angulo que valide as informações dos 3 ângulos informados na criação da classe.
# Instanciar a classe Triangulo e imprimir os lados informados e imprimir se o triângulo é um triângulo ou não.
# O método check_angulo deverá retornar True se a soma dos valores for igual a 180 e False em qualquer outra possibilidade;

#Criação da classe
class Triangulo():
    """Classe para fazer a verificação de um triângulo através de suas medidas."""
    def __init__(self, angulo_1, angulo_2, angulo_3):
        self.__check_medidas(angulo_1, angulo_2, angulo_3)
        self.validacao = self.__check_angulo()
    
    def __check_medidas(self, angulo_1, angulo_2, angulo_3):
        """Faz a checagem se os ângulos de entrada são valores válidos."""
        if not (isinstance(angulo_1,int) or isinstance(angulo_1,float)):
            raise ValueError(f'O angulo {angulo_1} é inválido')
        elif not (isinstance(angulo_2,int) or isinstance(angulo_2,float)):
            raise ValueError(f'O angulo {angulo_2} é inválido')
        elif not (isinstance(angulo_3,int) or isinstance(angulo_3,float)):
            raise ValueError(f'O angulo {angulo_3} é inválido')
        else:
            self.angulo_1 = angulo_1
            self.angulo_2 = angulo_2
            self.angulo_3 = angulo_3
            
    def __check_angulo(self):
        """Faz a checagem se a soma dos ângulos do triângulo é 180°."""
        if (self.angulo_1 + self.angulo_2 + self.angulo_3 == 180):
            return True
        else:
            return False
            
    def __str__(self):
        self.__check_medidas(self.angulo_1, self.angulo_2, self.angulo_3)
        self.validacao = self.__check_angulo()
        if self.validacao == True:
            return f"""Os ângulos do triângulo são: {self.angulo_1}°, {self.angulo_2}° e {self.angulo_3}°.
E esse objeto é um triângulo!"""
        else:
            return f"""Os angulos do triângulo são: {self.angulo_1}°, {self.angulo_2}° e {self.angulo_3}°.
E esse objeto NÃO é um triângulo!"""
            
#Implementação da classe
t = Triangulo(5,59.5,60)
t.angulo_1 = 60.5
print(t)
        