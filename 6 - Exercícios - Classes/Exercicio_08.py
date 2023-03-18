# Aluno: Ian Alves Sousa
# DB1 Start - Classes
# Exercício 8 - Criar uma classe Musica, que deverá receber como parâmetro de criação uma lista de string com as estrofes de uma música. Esta classe deverá conter um método chamado cante_para_mim que imprima todas as estrofes, uma em cada linha.
# Para executar, instancie a classe e execute o método.

from time import sleep
#Criação da classe
class Musica():
    """Clase para cantar uma música."""
    def __init__(self, estrofes:list):
        """Inicializa a intância e salva a lista com as estrofes da música."""
        self.lista_estrofes = estrofes

    def cante_para_mim (self):
        """Método para cantar a música, printando cada estrofe depois de 6 segundos."""
        for i in self.lista_estrofes:
            print (f"\n{i}")
            sleep(6)


#Implementação da classe
#Criação da lista com a música a ser cantada
estrofes = ["""Eu sei estou mais forte
Mas se cheguei até aqui eu tive alguém para me ajudar
Eu agradeço e sei que juntos poderemos ganhar (hey!)""",
"""Todos juntos
Vamos juntos
Juntos iremos treinar""",
"""Todos juntos
Vamos juntos
Juntos para ganhar!""",
"""Levante a cabeça!""",
"""Uma muralha pela frente não assustará a gente
Sei que não estou sozinho
Nós jamais desistiremos de atingir o objetivo
Acredito na vitória, pois você está comigo""",
"""Nada é impossível se você acreditar
A minha alma Samurai é como um relâmpago
Desde que eu esteja junto com você
E que você esteja comigo, nada poderá nos abalar!""",
"""Saiba que qualquer batalha
Poderemos ganhar ou perder""",
"""Eu sei estou mais forte
Mas se cheguei até aqui eu tive alguém para me ajudar
Porque ninguém vence sozinho!
Mesmo se eu não puder
Eu estarei sempre para o que precisar
Nossa amizade para sempre sei que vai durar! (Hey!)""",
"""Todos juntos
Vamos juntos
Juntos iremos treinar""",
"""Todos juntos
Vamos juntos
Juntos para ganhar""",
"""Todos juntos
Vamos juntos
Juntos iremos treinar""",
"""Todos juntos
Vamos juntos
Juntos para ganhar"""]

super11 = Musica(estrofes)
super11.cante_para_mim()

#Ideia para continuar depois: Procurar como faz para pegar as estrofes de um arquivo ou site, colocar as estrofes na lista a assim assionar o cante_para_mim.