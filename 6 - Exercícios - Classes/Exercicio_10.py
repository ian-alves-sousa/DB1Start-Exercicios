# Aluno: Ian Alves Sousa
# DB1 Start - Classes
# Exercício 10 - Criar uma classe que representará uma aeronave militar com o nome JatoMilitar1Lugar. O método construtor deverá receber duas informações iniciais: o modelo e a base onde a aeronave está; Crie um método chamado designar_piloto, que deverá receber o nome do piloto como parâmetro.
# Criar um método rebasear_aeronave, que deverá receber de parâmetro o nome da base para onde a aeronave deverá ser enviada. Antes de registrar, é necessário validar se o piloto foi designado para a aeronave, e somente se houver piloto, registrar a informação de rebaseamento, a data e hora que a movimentação foi realizada, deverá ser registrada também.
# Sobrescreva o métod __str__ da classe, para imprimir o seguinte conteúdo:
# Jato: <NOME DA AERONAVE>
# Base inicial: <NOME DA BASE DE ORIGEM>
# Piloto: <NOME DO PILOTO DESIGNADO>
# Histórico de transferências: <LISTAGEM DAS BASES PELAS QUAIS A
# AERONAVE PASSOU MOSTRANDO A DATA / HORA E BASE>

import datetime
# Criação da Classe

class JatoMilitar1Lugar():
    """Classe para criar um modelo e histórico de um Jato Militar de 1 lugar."""
    def __init__(self, modelo: str, base: str):
        """Inicializa a instância, faz a checagem das entradas e define o as variáveis de instância."""
        self.base = self.__check(base)
        self.modelo = self.__check(modelo)
        self._piloto = None
        self._new_base = None
        self._historico = []

    def __check(self, string: str) -> str:
        """Checa se a entrada é uma string."""
        check = string
        if not isinstance(string, str):
            raise ValueError(f'{string} não é uma string.')
        else:
            return check

    def designar_piloto(self, piloto: str):
        """Designa um piloto."""
        self._piloto = self.__check(piloto)

    def rebasear_aeronave(self, new_base: str):
        """Faz o rebaseamento da nave se tiver piloto e ciar um histórico de rebaseamento."""
        if not self._piloto == None:
            self._new_base = self.__check(new_base)
            self.momento = datetime.datetime.now().strftime('%d-%m-%Y - %I:%M:%S')
            self._historico.append((self._new_base, self.momento))
        else:
            print(f'Não é possível rebasear o jato sem definir um piloto primeiro.')

    @property
    def piloto(self):
        return self._piloto
    
    @piloto.setter
    def piloto(self, piloto):
        raise NotImplementedError(f'Não é possível setar o nome do piloto dessa forma, utilize o método designar_piloto.')

    def __str__(self) -> str:
        """Define o que será printado de acordo com as informações que já foram setadas."""
        if (self._piloto == None and self._new_base == None):
            return f"""Jato: {self.modelo}
Base inicial: {self.base}"""
        elif self._new_base == None:
            return f"""Jato: {self.modelo}
Base inicial: {self.base}
Piloto: {self._piloto}
Histórico de transferências: Não há históricos de transferências."""
        else:
            return f"""Jato: {self.modelo}
Base inicial: {self.base}
Piloto: {self._piloto}
Histórico de transferências: {self._historico}"""

