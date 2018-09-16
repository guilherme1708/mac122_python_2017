# -*- coding: utf-8 -*-

#############################################################
#                                                           #
#  MAC0122 PrincÃ­pos de Desenvolvimento de Algoritmos       #
#                                                           #
#  MÃ“DULO console.py                                        #
#                                                           #
#  MÃ³dulo responsÃ¡vel pela animaÃ§Ã£o.                        #
#                                                           #
#  NÃ£o altere nada neste arquivo.                           #
#                                                           #
#  NÃ£o altere o nome do arquivo.                            #
#                                                           #     
#  A documentaÃ§Ã£o sobre "Turtle graphic for Tk" pode ser    #
#  vista em http://docs.python.org/3/library/turtle.html    #
#                                                           #
#############################################################

# mÃ³dulo responsÃ¡vel pela animaÃ§Ã£o
import turtle

#-------------------------------------------------------------
# constantes referentes aos pontos e linhas

# define a cor de cada ponto
COR_PONTO = "white"

# define o diÃ¢metro de cada ponto
DIAMETRO_PONTO = 3 # hmmm, este diÃ¢metro Ã© um chute.

# define a cor 'default' das linhas
COR_LINHA = "yellow"

# define cor de fundo da janela
COR_FUNDO = "black"

# tÃ­tulo da janela
TITULO = "MAC0122 2016 - Par Mais Próximo"

# parÃ¢metros para o tracer (sÃ£o chutes)
TRACER_RAPIDO  = 500
TRACER_DEFAULT = 3

# delay para desenhar
DELAY_DEFAULT = 5
DELAY_MIN = 1

#--------------------------------------------------------------
class Console:
    #----------------------------------------------------------
    def __init__(self, pontos, cantos):
        '''(Console, Lista_Pontos2D, tuple) -> None

        Recebe uma referÃªncia `self` para um objeto Console, uma 
        referencia `pontos` a um objeto da classe Lista_Pontos2D e um tuple 
        `cantos` com as coordenadas de dois pontos.

        Cada ponto Ã© representado por um par (x,y) em que x e y
        sÃ£o nÃºmeros inteiros.

        Se cantos = ((x_min,y_min),(x_max,y_max)), entÃ£o (x_min,y_min] 
        Ã© a coordenada do ponto no canto inferior esquerdo e 
        (x_max,y_max) Ã© a coordenada do ponto superior direito 
        da regiÃ£o retangular do plano que contÃ©m os pontos em l_pontos.
        Desta forma, se pontos.pts[i] = (x,y), entÃ£o 

           x_min <= x < x_max   e   y_min <= y < y_max

        '''
        # crie o atributo de estado com os pontos
        # AVISO: self.l_pontos Ã© um apelido, nÃ£o um clone
        self.pontos = pontos

        # crie o atributo de estado com a dimensÃ£o da regiÃ£o
        # AVISO: self.cantos Ã© um apelido, nÃ£o um clone
        self.cantos = cantos

        # crie um contador para o nÃºmero de chamadas do mÃ©todo desenhe_linha
        self.no_linhas = 0

        # crie o atributo de estado do console
        self.canvas = turtle.Screen()

        # crie o atributo de estado com a 'pena' para desenharmos na janela
        self.pena = turtle.Turtle()

        # prepara a janela, pena, etc.
        self.setup()
        
        # desenhe os pontos
        self.desenhe_pontos()

    #----------------------------------------------------------
    def setup(self):
        '''(Console) -> None

        Recebe uma referÃªncia self para um objeto Console e faz as
        definiÃ§Ãµes iniciais da janela e pena.
        '''
        # apelidos
        cantos = self.cantos
        canvas = self.canvas
        pena   = self.pena

        # (volta) pena para valores default
        # necessÃ¡rio quando nÃ£o Ã© primeira chamada para setup() 
        pena.reset()
        
        # nÃ£o queremos que a tartaruga seja vista
        pena.hideturtle()        
        
        # defina a cor de fundo da janela
        canvas.bgcolor(COR_FUNDO)

        # coloque um tÃ­tulo na barra superior da janela
        canvas.title(TITULO)

        # a janela representarÃ¡ uma regiÃ£o retangular do plano cartesiano que
        # tem o canto inferior esquerdo na coordenada [x_min,y_min] e
        # tem o canto superior direito  na coordenada [x_max,y_max].
        x_min, y_min = cantos[0]
        x_max, y_max = cantos[1]

        # fixe a Ã¡rea do janela
        canvas.setworldcoordinates(x_min,y_min,x_max,y_max)

        # vamos agora diminuir o valor do argumento de tracer 
        canvas.tracer(TRACER_DEFAULT)

        # volte o delay para o default
        canvas.delay(DELAY_DEFAULT)

        # definimos o tamanho da janela em pixels?
        # hmmm, serÃ¡ que Ã© bom fixar?!
        # os valores default sÃ£o uma porcentagem da tela: 
        #
        #      width  == 0.5  que corresponde a 50% da largura da tela
        #      height == 0.75 que corresponde a 75% da altura  da tela
        # 
        # se os valores de width e height forem inteiros, entÃ£o 
        # eles sÃ£o considerados como sendo nÃºmero de pixels.
        # Por exemplo:
        # 
        #    width  = 800
        #    height = 675
        #
        # depois basta fazermos 
        #
        #    canvas.setup(width,height)
        #
        # hmmm, vamos deixar width e height variÃ¡veis em funÃ§Ã£o da tela 
        # do computador, ok?!
        # width  = canvas.window_width()
        # height = canvas.window_height()


    #----------------------------------------------------------
    def desenhe_pontos(self):
        '''(Console) -> None

        Recebe um referÃªncia self a um objeto Console e desenha 
        os pontos do console na janela.
        '''
        # apelidos 
        canvas = self.canvas   # janela e 
        pontos = self.pontos # lista de pontos
        pena   = self.pena     # pena

        # levante a pena para nÃ£o deixar rastros na janela
        pena.penup()  
        
        # delay para desenhar os pontos na janela mais rapidamente
        canvas.delay(DELAY_MIN)

        # aumentando o valor do argumento de tracer tornamos
        # o surgimento dos pontos na janela aparentemente instantÃ¢neo
        canvas.tracer(TRACER_RAPIDO)

        # pegue o nÃºmero de pontos na lista
        n = len(pontos)

        # desenhe os pontos
        for i in range(n):
            # pegue coordenadas do ponto i
            x, y = pontos.pts[i].x(), pontos.pts[i].y()
            
            # vÃ¡ para estÃ¡ a posiÃ§Ã£o do pontos 
            pena.setpos(x,y)

            # desenhe o ponto
            pena.dot(DIAMETRO_PONTO,COR_PONTO)

        # vamos agora diminuir o valor do argumento de tracer 
        canvas.tracer(TRACER_DEFAULT)

        # volte o delay para o default
        canvas.delay(DELAY_DEFAULT)

    #----------------------------------------------------------    
    def desenhe_linha(self, par_pontos, cor_linha = COR_LINHA):
        '''(Console, tuple, list) -> None

        Recebe uma referÃªncia `self` a um objeto Console e
        um tuple `par_pontos` com referÃªncia de dois pontos (Ponto2D).
        A funÃ§Ã£o desenha uma linha linha entre esses pontos.
        '''
        # caso o mÃ©todo seja chamado sem um par de pontos
        if par_pontos == (): return None
        
        # atualize contador
        self.no_linhas += 1
        
        # apelidos
        canvas = self.canvas
        pena   = self.pena

        # defina a cor da linha 
        pena.color(cor_linha)

        # levante a pena para nÃ£o deixar rastro na janela
        pena.penup()  

        # apelido para os dois pontos
        p0, p1 = par_pontos
        
        # leve a pena para o ponto p0
        pena.setposition((p0.x(), p0.y()))

        # baixe a pena
        pena.pendown()

        # leve a pena para o ponto p1
        pena.setposition((p1.x(), p1.y()))

        # levante a pena para terminar a linha
        pena.penup()  

    #----------------------------------------------------------    
    def no_call_dist(self):
        '''(Console) -> int

        Recebe uma referÃªncia `self` a um objeto Console e
        retorna o nÃºmero de chamadas feitas ao mÃ©todo 
        desenhe_linhas(). O nÃºmero de linhas deve ser o 
        nÃºmero de chamadas feitas Ã  funÃ§Ã£o distancia() do 
        mÃ³dulo NUSP_ep6.py.
        '''
        return self.no_linhas
    
    #----------------------------------------------------------    
    def exitonclick(self):
        '''(Console) -> None

        Recebe uma referÃªncia `self` e a um objeto Console e
        fecha a janela assim que seja feito um click sobre ela.
        '''
        print("\nClick na janela da animaÃ§Ã£o para fechÃ¡-la.")
        self.canvas.exitonclick()

    #----------------------------------------------------------    
    def reset(self):
        '''(Console) -> None

        Recebe uma referÃªncia `self` e a um objeto Console e
        fecha a janela assim que seja feito um click sobre ela.
        '''
        self.canvas.clear()
        self.setup()
        self.desenhe_pontos()