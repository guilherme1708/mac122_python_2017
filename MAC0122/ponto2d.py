# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Guilherme Navarro
    NUSP: 8943160

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

'''

# math.sqrt()
import math

# constantes
X = 0  # abscissa
Y = 1  # ordenada

#===========================================================
#
# Classe Ponto2D
#
#===========================================================
        
class Ponto2D:
    ''' 
    Classe utilizada para representar pontos no plano euclidiano.
    Um ponto será representado através de coordenadas cartesianas.

    Cada objeto desta classe tem apenas o atributo de estado `coord` que 
    uma tuple de comprimento 2:

       - `coord[X]`: número representando a abscissa do ponto
       - `coord[Y]`: número representando a ordenada do ponto

    '''
    animacao = False # ignore
    linha = None     # ignore
    
    #----------------------------------------------------    
    def __init__(self, pt = (0,0)):
        '''(Ponto2D, tuple) -> None

        Chamado pelo construtor da classe.

        Recebe um referência `self` ao objeto Ponto2D que está sendo criado
        e as coordenadas do ponto através do tuple `pt`.

        Quando o construtor é chamado sem argumentos, o ponto representado será 
        a origem do plano cartesiano.

        Exemplos:

        >>> orig = Ponto2D()
        >>> orig.coord
        (0, 0)
        >>> p1 = Ponto2D((1,1))
        >>> p1.coord
        (1, 1)
        >>> p2 = Ponto2D((0.5,1))
        >>> p2.coord
        (0.5, 1)
        >>> 
        '''
        self.coord = pt    
        
    #----------------------------------------------------    
    def __str__(self):
        '''(Ponto2D) -> str 

        Recebe uma referência a um objeto Ponto2D e retorna o string 
        que o representa. 

        Usando quando escrevemos "print(Ponto2D)" ou "str(Ponto2D)". 

        O formato do string deve ser: "(abscissa, ordenada)"
           
        Exemplo:

        >>> p2 = Ponto2D((0.5,1))
        >>> str(p2)
        '(0.5, 1)'
        >>> print(p2)
        (0.5, 1)
        >>>         
        '''
        return str(self.coord)  
        
    #----------------------------------------------------    
    def __eq__(self, other):
        '''(Ponto2D, Ponto2D) -> bool

        Recebe referências `self` e `other` a objetos Ponto2D e  
        retorna True se `self` e `other` representam o mesmo ponto.

        Usando quando escrevemos "Ponto2D == Ponto2D"

        Exemplos:

        >>> orig = Ponto2D()
        >>> p1 = Ponto2D((1,1))
        >>> p2 = Ponto2D((0.5,1))
        >>> p3 = Ponto2D((1,1))
        >>> p1 == orig
        False
        >>> p1 == p1
        True
        >>> p1 == p2
        False
        >>> p1 == p3
        True
        >>>         
        '''
        if self.coord == other.coord:
            return True
        return False
    
    #----------------------------------------------------    
    def __ne__(self, other):
        '''(Ponto2D, Ponto2D) -> bool

        Recebe referências `self` e `other` a objetos Ponto2D e  
        retorna True se `self` e `other` representam pontos diferente.

        Usando quando escrevemos "Ponto2D != Ponto2D"

        Exemplos:

        >>> orig = Ponto2D()
        >>> p1 = Ponto2D((1,1))
        >>> p2 = Ponto2D((0.5,1))
        >>> p3 = Ponto2D((1,1))
        >>> p1 != orig
        True
        >>> p1 != p1
        False
        >>> p1 != p2
        True
        >>> p1 != p3
        False
        >>>         
        '''
        if self.coord != other.coord:
            return True
        return False

    #----------------------------------------------------    
    def __lt__(self, other):
        '''(Ponto2D, Ponto2D) -> bool

        Recebe referências `self` e `other` a objetos Ponto2D e  
        retorna True se a abscissa do ponto representado 
        por `self` e menor que a abscissa do ponto representado 
        por `other`.

        Usando quando escrevemos "Ponto2D < Ponto2D"

        Exemplos:

        >>> orig = Ponto2D()
        >>> p1 = Ponto2D((1,1))
        >>> p2 = Ponto2D((0.5,1))
        >>> p3 = Ponto2D((1,1))
        >>> p1 < orig
        False
        >>> orig < p1
        True
        >>> p1 < p2
        False
        >>> p1 < p3
        False
        >>>         
        '''
        if self.coord[0] < other.coord[0]:
            return True
        return False
    
    #----------------------------------------------------    
    def __ge__(self, other):
        '''(Ponto2D, Ponto2D) -> bool

        Recebe referências `self` e `other` a objetos Ponto2D e  
        retorna True se a abscissa do ponto representado 
        por `self` e maior ou igual a abscissa do ponto representado 
        por `other`.

        Usando quando escrevemos "Ponto2D >= Ponto2D"

        Exemplos:

        >>> orig = Ponto2D()
        >>> p1 = Ponto2D((1,1))
        >>> p2 = Ponto2D((0.5,1))
        >>> p3 = Ponto2D((1,1))
        >>> p1 >= orig
        True
        >>> orig >= p1
        False
        >>> p1 >= p2
        True
        >>> p1 >= p3
        True
        >>>     
        '''
        if self.coord[0] >= other.coord[0]:
            return True
        return False

    #----------------------------------------------------    
    def __gt__(self, other):
        '''(Ponto2D, Ponto2D) -> bool

        Recebe referências `self` e `other` a objetos Ponto2D e  
        retorna True se a abscissa do ponto representado 
        por `self` e maior que a abscissa do ponto representado 
        por `other`.

        Usando quando escrevemos "Ponto2D > Ponto2D"

        Exemplos:

        >>> orig = Ponto2D()
        >>> p1 = Ponto2D((1,1))
        >>> p2 = Ponto2D((0.5,1))
        >>> p3 = Ponto2D((1,1))
        >>> p1 > orig
        True
        >>> orig > p1
        False
        >>> p1 > p2
        True
        >>> p1 > p3
        False
        >>>       
        '''
        if self.coord[0] > other.coord[0]:
            return True
        return False


    #----------------------------------------------------    
    def __le__(self, other):
        '''(Ponto2D, Ponto2D) -> bool

        Recebe referências `self` e `other` a objetos Ponto2D e  
        retorna True se a abscissa do ponto representado 
        por `self` é menor ou igual a abscissa do ponto 
        representado por `other`.

        Usando quando escrevemos "Ponto2D <= Ponto2D"

        Exemplos:

        >>> orig = Ponto2D()
        >>> p1 = Ponto2D((1,1))
        >>> p2 = Ponto2D((0.5,1))
        >>> p3 = Ponto2D((1,1))
        >>> p1 <= orig
        False
        >>> orig <= p1
        True
        >>> p1 <= p2
        False
        >>> p1 <= p3
        True
        >>>                 
        '''
        if self.coord[0] <= other.coord[0]:
            return True
        return False

    #----------------------------------------------------
    def x(self):
        '''(Ponto2D) -> int|float

        Retorna a abscissa do ponto `self`.
        
        Exemplo:

        >>> orig = Ponto2D()
        >>> p1 = Ponto2D((1,1))
        >>> p2 = Ponto2D((0.5,1))
        >>> p3 = Ponto2D((1,1))
        >>> orig.x()
        0
        >>> p1.x()
        1
        >>> p2.x()
        0.5
        >>> p3.x()
        1
        >>>         
        '''
        return self.coord[0]
    
    #----------------------------------------------------
    def y(self):
        '''(Ponto2D) -> int|float

        Retorna a abscissa do ponto `self`.
        
        Exemplo:

        >>> orig = Ponto2D()
        >>> p1 = Ponto2D((1,1))
        >>> p2 = Ponto2D((0.5,1))
        >>> p3 = Ponto2D((1,1))
        >>> orig.y()
        0
        >>> p1.y()
        1
        >>> p2.y()
        1
        >>> p3.y()
        1
        >>>        
        '''
        return self.coord[1]
        
    #----------------------------------------------------    
    def distancia(self, other):
        '''(Ponto2D, Ponto2D) -> float

        Recebe referências `self` e `other` a objetos Ponto2D e  
        retorna a distância euclidiana entre os pontos representados 
        por `self` e `other`.

        Exemplos:

        >>> orig = Ponto2D()
        >>> p1 = Ponto2D((1,1))
        >>> p2 = Ponto2D((0.5,1))
        >>> p3 = Ponto2D((1,1))
        >>> orig.distancia(p1)
        1.4142135623730951
        >>> orig.distancia(p2)
        1.118033988749895
        >>> p1.distancia(p2)
        0.5
        >>> p1.distancia(p3)
        0.0
        >>> 
        '''
        # ignore e não apague a próxima linha
        if Ponto2D.animacao: Ponto2D.linha((self, other))
        # escreva seu método a partir da próxima linha
        
        return math.sqrt((self.coord[0] - other.coord[0])**2 + (self.coord[1] - other.coord[1])**2)
    
     
