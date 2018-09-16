# -*- coding: utf-8 -*-

#############################################################
#                                                           #
#  MAC0122 PrincÃ­pos de Desenvolvimento de Algoritmos       #
#                                                           #
#  MÓDULO util.py                                           #
#                                                           #
#  Contem funções auxiliares do EP                          #
#                                                           #
#  NÃo altere nada neste arquivo.                           #
#                                                           #
#  NÃo altere o nome do arquivo.                            #
#                                                           #     
#############################################################

# mÃ³dulo para geraÃ§Ã£o de nÃºmeros aleatÃ³rios
import random

# para cronometrar o tempo das funÃ§Ãµes
import time

# mÃ³dulo responsÃ¡vel pela animaÃ§Ã£o
from console import Console

# mÃ³duloe que implementa a classe Ponto2D
from ponto2d import Ponto2D

# constantes
# retÃ¢ngulo onde os pontos serÃ£o gerados Ã© definido por
#    - canto inferior esquerdo [X_MIN,Y_MIN] e
#    - canto superior direito  [X_MAX,Y_MAX].
X_MIN = -1024
Y_MIN = -1024
X_MAX =  1024
Y_MAX =  1024
CANTOS = ((X_MIN,Y_MIN),(X_MAX,Y_MAX))

# cada ponto Ã© representando por um par [x,y] 
X = 0 # abscissa do ponto Ã© valor na posiÃ§Ã£o 0 
Y = 1 # ordenada do ponto Ã© valor na posiÃ§Ã£o 1 

#-------------------------------------------------------------    
def gere_pontos(n, semente, cantos=CANTOS):
    '''(int, int, tuple) -> list

    Recebe um nÃºmero inteiro nÃ£o negativo `n`, um nÃºmero inteiro 
    `semente` e um tuple `cantos` com de pares de nÃºmeros inteiros 
    ((x_min,y_min),(x_max,y_max)) que definem uma regiÃ£o retangular do 
    plano cartesiano. 

    A funÃ§Ã£o cria e retorna uma lista de objetos Ponto2D gerados aleatoriamente 
    na regiÃ£o retangular.  Assim, para cada ponto `p` na lista retornada temos que:

        - x e y sÃ£o nÃºmeros inteiros;
        - x_min <= p.x() < x_max
        - y_min <= p.y()x < y_max

    O valor de semente Ã© usado para inicializar o gerador de nÃºmeros 
    aleatÃ³rios do Python.

    NÃ£o altere estÃ¡ funÃ§Ã£o.
    '''
    # avise que estamos trabalhando
    print("\ngere_pontos(): gerando %d pontos ..." %n)
    
    # crie a lista a ser retornada
    pontos = []
    
    # inicialize a semente do gerador 
    random.seed(semente)

    # cantos da regiÃ£o retangular
    x_min, y_min = cantos[0]
    x_max, y_max = cantos[1]

    # gere os pontos
    for i in range(n):
        # sorteie uma posiÃ§Ã£o no retÃ¢ngulo 
        x = random.randrange(x_min, x_max)
        y = random.randrange(y_min, y_max)

        # coloque o ponto na lista
        pontos.append(Ponto2D((x, y)))

    # avise que terminamos o serviÃ§o e estamos voltando
    print("gere_pontos(): pontos gerados.")
    
    return pontos
    
#------------------------------------------------------------
def execute(pontos, algoritmo = ''):
    '''(Lista_Pontos2D, str) -> None

    Recebe uma referÃªncia `pontos` para um objeto Lista_Pontos2D e
    um string `algoritmo` indicando o mÃ©todo que sera utilizado para
    encontrar um par de pontos em `pontos`. A funÃ§Ã£o mede o consumo 
    de tempo e imprime pequeno um pequeno relatÃ³rio referente
    a execuÃ§Ã£o da implementaÃ§Ã£o do algoritmo.

    Nota:

    https://docs.python.org/3.0/library/time.html#time.clock

    time.clock():

    On Unix, return the current processor time as a floating point
    number expressed in seconds. The precision, and in fact the very
    definition of the meaning of â€œprocessor timeâ€, depends on that of
    the C function of the same name, but in any case, this is the
    function to use for benchmarking Python or timing algorithms.

    On Windows, this function returns wall-clock seconds elapsed since
    the first call to this function, as a floating point number, based
    on the Win32 function QueryPerformanceCounter. The resolution is
    typically better than one microsecond.
    '''
    # comeÃ§e a cronometrar 
    start = time.clock()

    # execute a funÃ§Ã£o
    dist, par = pontos.forca_bruta(0, len(pontos))

    # trave o cronÃ´metro 
    end = time.clock()

    # calcule o tempo gasto
    elapsed = end - start

    print("\nResultado: ")

    # caso ainda nÃ£o tenha implementado a funÃ§Ã£o
    if dist == None:
        print("  par mais próximo  =", par)
        print("  menor distancia   = None")
    else:
        print("  par mais próximo  = (%s, %s))"%(str(par[0]),str(par[1])))
        print("  menor distancia   = %.2f" %dist)
    print("  tempo de execução = %.2fs" %elapsed)

#------------------------------------------------------------
def animacao(pontos, algoritmo = ''):
    '''(Lista_Pontos2D, str) -> None

    Recebe uma referÃªncia `pontos` para um objeto Lista_Pontos2D e
    um string `algoritmo` indicando o mÃ©todo que sera utilizado para
    encontrar um par de pontos em `pontos`.

    A funÃ§Ã£o apresenta uma pequena aninamaÃ§Ã£o da
    execuÃ§Ã£o da chamada do mÃ©todo referente ao algoritmo.
    '''
    #-----------------------------------
    # crie uma janela com os pontos
    janela = Console(pontos, CANTOS)

    # contemple os pontos
    pause()

    Ponto2D.animacao = True
    Ponto2D.linha = janela.desenhe_linha
    
    # determine o par mais prÃ³ximo
    print("\nVeja sua função em ação...")
    dist, par = pontos.forca_bruta(0,len(pontos))

    # contemple as linhas indicando chamadas Ã  funÃ§Ã£o distancia()
    pause()

    # mostre apenas um par mais prÃ³ximo
    janela.reset()
    janela.desenhe_linha(par)

    # mostre pequeno relatÃ³rio da execuÃ§Ã£o da funÃ§Ã£o
    no_chamadas_dist = janela.no_call_dist()
    print("\nResultado: ")
    # caso ainda nÃ£o tenha implementado a funÃ§Ã£o
    if dist == None:
        print("  par mais próximo  =", par)
        print("  menor distancia   = None")
    else:
        print("  par mais próximo  = (%s, %s))"%(str(par[0]),str(par[1])))
        print("  menor distancia   = %.2f" %dist)
                
    print("  no. chamadas da função distancia() = %d" %no_chamadas_dist)

    Ponto2D.animacao = False
    Ponto2D.linha = None
     
    # contemple um par mais prÃ³ximo antes de irmos embora
    janela.exitonclick()  

    
#------------------------------------------------------------
def pause(): 
    '''(None) -> None

    Para a execuÃ§Ã£o do programa atÃ© que um ENTER seja teclado.

    NÃ£o altere estÃ¡ funÃ§Ã£o
    '''
    input("\nPara continuar, tecle ENTER _nesta_ janela. ")