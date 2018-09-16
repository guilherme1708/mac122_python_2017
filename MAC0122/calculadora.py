# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
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
# importa todas as constantes: COMENTARIO, PARENTESES, BLOCO,...
from constantes import *

# importa a classe Item
from item_lexico import Item


#===========================================================
#
# Classe Calculadora
#
#===========================================================

class Calculadora:
    ''' 
    Classe utilizada para representar uma calculadora.

    Cada objeto desta classe tem dois atributos de estado: 

       `var` (list): é um lista em que cada posição é uma
             referência para um string que é o nome de uma variável.

       `val` (list): é uma lista em que cada posição é contém o valor 
             float da variável na posição correspondente na lista `var`. 
             Assim, val[i] é o valor de var[i].

    Em ciência da computação a coleção de pares "nome de variável", "valor" e 
    conhecida pelo nome de _dicionário_ ou _tabela de símbolos_.
    '''
    def __init__(self):
        '''(Calculatora) -> None

        Chamado pelo construtor da classe.

        Recebe uma referência `self` para um objeto da classe Calculadora e 
        acrescenta a esse objeto os atributos de estado `var` e `val`.

        Em outras palavras, __init__() cria o dicionário das variáveis da
        calculadora.        
        
        Exemplos
        
        >>> texas = Calculadora()
        >>> hp = Calculadora()
        >>> texas.var
        []
        >>> texas.val
        []
        >>> texas.var.append("soma")
        >>> texas.val.append(0)
        >>> texas.var
        ['soma']
        >>> texas.val
        [0]
        >>> hp.var
        []
        >>> hp.val
        []
        >>> 
        '''
        self.var = []
        self.val = []        
        
    #----------------------------------------------------------------
    def set_val(self, nome_var, valor):
        '''(Calculadora,str, float) ->  None
    
        Recebe uma referência `self` para uma Calculadora e um  
        string `nome_var` e um float `valor`. 
        O método insere o par `nome_var`, `valor` ao dicionário de 
        variáveis da calculadora. 
        Se a variável `nome_var` já está no dicionário o seu valor é 
        atualizado.

        Exemplos:

        >>> hp = Calculadora()
        >>> hp.var
        []
        >>> hp.val
        []
        >>> hp.set_val("soma", 0)
        >>> hp.set_val("n", 10)
        >>> hp.var
        ['soma', 'n']
        >>> hp.val
        [0, 10]
        >>> hp.set_val("n", 15.56)
        >>> hp.var
        ['soma', 'n']
        >>> hp.val
        [0, 15.56]        
        '''
        i = self.indice(nome_var)
        
        if nome_var in self.var:
            self.val[i] = valor

        else:
            self.var.append(nome_var)
            self.val.append(valor)

    #----------------------------------------------------------------
    def get_val(self, nome_var):
        '''(Calculadora, str) -> float ou None
    
        Recebe uma referência `self` para uma Calculadora e um  
        string `nome_var`. Retorna o valor da variável `nome_var` ou 
        None se a variável não foi definida.

        Exemplos:
    
        >>> hp = Calculadora()
        >>> hp.set_val("n", 10)
        >>> hp.set_val("pi", 3.14)
        >>> hp.get_val("n")
        10
        >>> hp.get_val("pi")
        3.14
        >>> hp.get_val("X")
        >>> a1 = hp.get_val("pi")
        >>> a1
        3.14
        >>> 
        '''
        i = self.indice(nome_var)
        
        if i != None:
            return self.val[i]
        return None
    #----------------------------------------------------------------
    def indice(self, var):
        '''(Calculadora, valor) -> int
        '''
        
        for i in range(len(self.var)):
            if var == self.var[i]:
                return i

    #----------------------------------------------------------------
    def clear(self):
        '''(Calculadora) -> None
    
        Recebe uma referência `self` para uma Calculadora e retorna o 
        estado (atributos de estado) ao original.

        Exemplos:

        >>> hp = Calculadora()
        >>> hp.set_val("n", 10)
        >>> hp.set_val("pi", 3.14)
        >>> hp.var
        ['n', 'pi']
        >>> hp.val
        [10, 3.14]
        >>> hp.clear()
        >>> hp.val
        []
        >>> hp.varhp.get_val("pi")
        []
        >>> 
        '''
        self.var = []
        self.val = []
    
    #----------------------------------------------------------------
    def lexer(self, exp = ''):
        ''' (Calculadora, str) -> list 

        Recebe um string `exp` representando uma expressão aritmética 
        e cria retorna uma lista de objetos Item. Essa lista é contém
        os itens léxicos que formam a expressão, na ordem que ocorrem na 
        expressão. 

        A classe Item está definida no módulo item-lexico.py. Antes
        de começar a escrever esse método, estude a especificação
        contida nesse módulo.

        A função ignora tudo que esta na exp apos o caractere
        COMENTARIO (= "#").

        Exemplos:

        >>> hp = Calculadora()
        >>> exp1 = "soma=soma + 2 # este é um comentario"
        >>> exp2 = "2+3- 123 *3.14 # uma conta"
        >>> itens1 = hp.lexer(exp1)
        >>> itens2 = hp.lexer(exp2)
        >>> type(itens1[0])
        <class 'item_lexico.Item'>
        >>> type(itens1[1])
        <class 'item_lexico.Item'>
        >>> itens1[0].lexema
        'soma'
        >>> itens1[0].tipo
        'VAR'
        >>> itens1[1].lexema
        '='
        >>> itens1[1].tipo
        'OP'
        >>> print(itens1[0])
        'soma' (<class 'str'>): VAR
        >>> print(itens1[1])
        '=' (<class 'str'>): OP
        >>> 
        >>> print(itens1[2])
        'soma' (<class 'str'>): VAR
        >>> print(itens1[3])
        '+' (<class 'str'>): OP
        >>> print(itens1[4])
        2.0 (<class 'float'>): NUM
        >>> print(itens1[5])
        Traceback (most recent call last):
        File "<pyshell#10>", line 1, in <module>
        print(itens1[5])
        IndexError: list index out of range
        >>> for item in itens1: print(item)

        'soma' (<class 'str'>): VAR
        '=' (<class 'str'>): OP
        'soma' (<class 'str'>): VAR
        '+' (<class 'str'>): OP
        2.0 (<class 'float'>): NUM
        >>> for item in itens2: print(item)

        2.0 (<class 'float'>): NUM
        '+' (<class 'str'>): OP
        3.0 (<class 'float'>): NUM
        '-' (<class 'str'>): OP
        123.0 (<class 'float'>): NUM
        '*' (<class 'str'>): OP
        3.14 (<class 'float'>): NUM
        
        >>> hp = Calculadora()
        >>> exp = "p1 + 2*(p2+p3)"
        >>> fila_infixa = hp.lexer(exp)
        >>> for item in fila_infixa: print(item)
        >>> 
        '''
        s = ''
        lf = []

        if exp == '':
            return lf
            
        if COMENTARIO in exp:
            indice = exp.index(COMENTARIO)
            novo = exp[:indice]
        else:
            novo = exp
        
        for car in novo:
            if car in LETRAS:
                s += car
            elif car in FLOATS:
                s += car
            elif car in PARENTESES:
                s += ' ' + car + ' '
            else:
                s+= ' ' + car + ' '
        print(s)
        lista = s.split()

        for i in range(len(lista)):
            if lista[i][0] in LETRAS:
                lf.append(Item(lista[i], VARIAVEL))
            elif lista[i][0] in FLOATS:
                lf.append(Item(float(lista[i]), NUMERO ))
            elif lista[i] in OPERADORES:
                lf.append(Item(lista[i], OPERADOR))
            elif lista[i] in PARENTESES:
                lf.append(Item(lista[i], BLOCO))
            
        return lf
            
            
    
