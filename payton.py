import random

class simuladordeDADOS:

    def __init__(self) :
        
        self. valor_minimo = 1
        self. valor_maximo = 6
        self. mensagem = 'vc gostaria de jogar novamente ?'

     
   def Iniciar (self): 

    resposta = input(self.mensagem) 

    if resposta == 'sim' :
     
     self.GerarValorDoDado(self) 

     print(random.randint(self.valor_maximo, self.valor_minimo))

     simulador = SimuladordeDADOS()
     simulador.Iniciar()
