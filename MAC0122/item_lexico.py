# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
'''
   MAC0122 Principios de Desenvolvimento de Algoritmos
 
   NAO EDITE OU MODIFIQUE NADA QUE ESTA ESCRITO NESTE ARQUIVO
   
   Neste arquivo esta a classe Item. 
   Constantes que representam as possiveis categorias dos
   itens léxicos são importadas do arquivo constantes.py.
'''

# importa as constantes usadas pelo EP
from constantes import *

#===========================================================
#
# Classe Item: NÃO ALTERE ESSA CLASSE
#
#===========================================================
        
class Item:
    ''' 
    Classe utilizada para representar itens léxicos.

    Cada objeto desta classe tem dois atributos de estado, `lexema` e 
    e `tipo`: 

       - `lexema` (float ou str): é um float no caso do tipo do item ser 
             NUMERO e é um str em caso contrário (OPERADOR, VARIAVEL, ou
             BLOCO)
       - `tipo` (str): indica o a categoria a qual `lexema` pertence.
             Pode ser NUMERO, OPERADOR, VARIAVEL ou BLOCO.

    '''
    #----------------------------------------------------    
    def __init__(self, lexema = 0.0, tipo = NUMERO):
        '''(Item, int ou float ou str, str) -> None

        Chamado pelo construtor da classe.

        Recebe um referência `self` ao objeto que estão sendo criado
        e acrescenta a ele os seus atributos.

        Quando o cosntrutor é chamado sem argumentos, o lexema do objeto
        é 0.0 e o seu tipo é NUMERO (definido em constantes.py)

        Exemplos:

        >>> t1 = Item()
        >>> t1.lexema
        0.0
        >>> t1.tipo
        'NUM'
        >>> t2 = Item('+', OPERADOR)
        >>> t2.lexema
        '+'
        >>> t2.tipo
        'OP'
        >>> t3 = Item(3.14, NUMERO)
        >>> t3.lexema
        3.14
        >>> t3.tipo
        'NUM'
        >>>
        '''
        self.lexema = lexema
        self.tipo  = tipo

    #----------------------------------------------------    
    def __str__(self):
        '''(Item) -> str 

        Retorna uma referência a um objeto Item e retorna o string 
        que o representa. 

        Usando quando escrevemos print(Item) ou str(Item). 

        O string produzido deve ter o formato

             "'<lexema>' (<classe do lexema>): <tipo>" 
 
        O lexema de <tipo> pode ser "NUM", "OP" ou "VAR". 
        Veja a definição dessas contantes em constantes.py 

        Exemplos:

        >>> t1 = Item()
        >>> t2 = Item('+', OPERADOR)
        >>> str(t1)
        "0.0 (<class 'float'>): NUM"
        >>> str(t2)
        "'+' (<class 'str'>): OP"
        >>> print(t1)
        0.0 (<class 'float'>): NUM
        >>> print(t2)
        '+' (<class 'str'>): OP
        >>> t3 = Item(3.14, NUMERO)
        >>> str(t3)
        "3.14 (<class 'float'>): NUM"
        >>> 
        '''
        if self.tipo == NUMERO:
            s = str(self.lexema)
        else:
            s = "'%s'"%str(self.lexema) # apóstrofos em um string
        return s + " (%s): %s"%(str(type(self.lexema)), self.tipo)