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
# importa as constantes: NUMERO, OPERADOR, VARIAVEL, RESTO_DIVISÃO, ADICAO, ...
from constantes import *

# importa a classe Item
from item_lexico import Item

# importa a classe Calculadora que sera herdada por polonesa
from calculadora import Calculadora


#===========================================================
#
# Classe Calculadora
#
#===========================================================

class Polonesa(Calculadora):
    '''Classe utilizada para representar uma calculadora polonesa.

    Está classe herda da classe calculadora todos os seus atributos:

       var (list): é um lista em que cada posição é uma
           referência para um string que é o nome de uma variável.

       val (list): é uma lista em que cada posição é contém o valor 
           float da variável na posição correspondente na lista `var`. 
           Assim, val[i] é o valor de var[i].

       set_val(self, nome_var, valor): 

           Recebe uma referência `self` para uma Calculadora e um  
           string `nome_var` e um float `valor`. 

           O método insere o par `nome_var`, `valor` ao dicionário de
           variáveis da calculadora.

       get_val(self, nome_var):

           Recebe uma referência `self` para uma Calculadora e um  
           string `nome_var`. Retorna o valor da variável `nome_var` ou 
           None se a variável não foi definida.

       clear(self):

           Recebe uma referência `self` para uma Calculadora e retorna o
           estado (atributos de estado) ao original.
    '''
    def __init__(self):
        '''(Polonesa) -> None

        Chamado pelo construtor da classe.

        Recebe uma referência `self` para um objeto da classe Polonesa e 
        acrescenta a esse objeto os atributos de estado `var` e `val`
        que são herdados da classe Calculadora.

        Este método está completo. Não o altere.
        
        Exemplos
        
        >>> texas = Polonesa()
        >>> hp = Polonesa()
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
        Calculadora.__init__(self)

    #----------------------------------------------------------------    
    def __str__(self):
        ''' (Polonesa) -> str

        Recebe um objeto Polonesa referenciado por self e 
        retorna um string com o nome e conteúdo conteúdo das 
        variáveis da calculadora.

        Cada linha deve ter a forma:

            "<nome variável>: <valor variável>\n" 
 
        onde 
             <nome  variável>: é um string e
             <valor variável>: é um int se o valor for da classe int 
                               ou float se o valor é da classe float.

        Exemplos:

        >>> hp = Polonesa()
        >>> hp.set_val("e", 2.718281828459045)
        >>> hp.set_val("pi", 3.14)
        >>> hp.set_val("soma", 0)
        >>> str(hp)
        'e: 2.718281828459045\npi: 3.14\nsoma: 0\n'
        >>> print(hp)
        e: 2.718281828459045
        pi: 3.14
        soma: 0

        >>>          
        '''
        s = ''
        for i in self.var:
            s += str(i) + ': ' + str(self.get_val(i)) + '\n'

        return s
    #----------------------------------------------------
    def eval(self, fila_itens = []):
        '''(Polonesa, list) -> float ou None

        Recebe uma referencia `self` para um objeto polonesa e uma lista `fila_itens` de
        objetos Item representado uma expressão em notação posfixa.  
        O método calcula e retorna o valor da expressão. 

        Se o valor não puder ser calculado devido a algum erro na expressão 
        o método deve retornar None.

        A expressão pode conter variáveis, constantes int ou float
        e os operadores:

             ^ : exponenciação
             * : multiplicação
             / : divisão
             % : resto divisão
             + : adição
             - : subtração
             = : atribuição

        Exemplos:
       
        >>> hp = Polonesa()
        >>> exp1 = "12 2 + 3 -"
        >>> fila_itens1 = hp.lexer(exp1)
        >>> hp.eval(fila_itens1)
        11.0
        >>> exp2 = "var 2 3 + ="
        >>> fila_itens2 = hp.lexer(exp2)
        >>> hp.eval(fila_itens2)
        5.0
        >>> hp.eval([Item("var", VARIAVEL)])
        5.0
        >>> hp.eval("var")
        Traceback (most recent call last):
          File "<pyshell#7>", line 1, in <module>
            hp.eval("var")
          File "polonesa.py", line 242, in eval
            item   = fila_itens.pop(0)
        AttributeError: 'str' object has no attribute 'pop'
        >>> 
        '''
         
        pilha = []
       
        k = 0
        
        if len(fila_itens) == 1 and fila_itens[0].tipo == NUMERO:
            return fila_itens[0].lexema
        elif len(fila_itens) == 1 and fila_itens[0].tipo == VARIAVEL:
            return self.get_val(fila_itens[0].lexema)
        
        for i in range(len(fila_itens)):
            if fila_itens[i].tipo == VARIAVEL:
                valor = fila_itens[i].lexema
                pilha.append(valor)
            elif fila_itens[i].tipo == NUMERO:
                valor = fila_itens[i].lexema
                pilha.append(valor)
            elif fila_itens[i].tipo == OPERADOR and len(pilha) > 0:
                k += 1
                valor1 = pilha.pop()
                valor2 = pilha.pop()
                if fila_itens[i-1].tipo == VARIAVEL and fila_itens[i-2].tipo == VARIAVEL and fila_itens[i-3].tipo != VARIAVEL:
                    valor1 = self.get_val(valor2)
                    self.set_val(fila_itens[i-1].lexema,valor1)
                elif fila_itens[i].tipo == VARIAVEL or fila_itens[i-1].tipo == VARIAVEL:
                    valor1 = self.get_val(valor1)
                    valor2 = self.get_val(valor2)
                if fila_itens[i].lexema == ADICAO:
                    soma = valor2 + valor1
                    pilha.append(soma)
                elif fila_itens[i].lexema == RESTO_DIVISAO:
                    rest = valor2 % valor1
                    pilha.append(rest)
                elif fila_itens[i].lexema == MULTIPLICACAO:
                    mult = valor2 * valor1
                    pilha.append(mult)
                elif fila_itens[i].lexema == DIVISAO:
                    div = valor2 / valor1
                    pilha.append(div)
                elif fila_itens[i].lexema == SUBTRACAO:
                    sub = valor2 - valor1
                    pilha.append(sub)
                elif fila_itens[i].lexema == EXPONENCIACAO:
                    expo = valor2 ** valor1
                    pilha.append(expo)
                elif fila_itens[i].lexema == ATRIBUICAO:
                    if fila_itens[i-1].tipo == NUMERO and fila_itens[i-2].tipo == NUMERO:
                        return None 
                    self.set_val(valor2,valor1)
                    atrib = valor2 = valor1
                    pilha.append(atrib)
                    
                else:
                    pilha.append(float(i))
        
        if pilha != [] and k != 0:
            return pilha.pop()
            

#===========================================================
#
# para testar a classe Polonesa interativamente
#
#===========================================================

# constantes
PROMPT           = 'expr >>> '
QUIT             = 'qQxX'     # para sair tecle uma dessa letras
CLEAR            = 'clear'    # para limpar a memória da calculador
MOSTRE_VARIAVEIS = 'show'     # para mostras as variáveis

#------------------------------------------------------------
def unit_test():
    '''None -> None

    Função que lê do teclado expressões aritméticas 
    em notação posfixa e calcula e imprime seus valores.

    Pode ser usada para testar a classe Polonesa.
    Altere essa função como desejar. 
    Ela não será corrigida.

    Exemplo

    >>> unit_test()

    ==================================================
         C A L C U L A D O R A    P O L O N E S A     
    ==================================================

    expr >>> 2 3 4 5 * 5 6 * - + * # 2 * (3 + 4 * 5 - 5 * 6)
    -14.0
    expr >>> a 3 = # a = 3
    3.0
    expr >>> soma 4.3 = # soma = 4.3
    4.3
    expr >>> pi 3.1415926 = # pi = 3.1415926
    3.1415926
    expr >>> show
    a: 3.0
    soma: 4.3
    pi: 3.1415926

    expr >>> soma
    4.3
    expr >>> a
    3.0
    expr >>> pi
    3.1415926
    expr >>> soma a pi - = # soma = a = pi
    -0.14159260000000007
    expr >>> soma
    -0.14159260000000007
    expr >>> pi
    3.1415926
    expr >>> 2 3 # expressão errada
    None
    expr >>> 2 3= # expressão errada
    None
    expr >>> 
    expr >>> q # quit
    Curta a página de MAC0122 no feiçebuqui.
    '''
    print()
    print("==================================================")
    print("     C A L C U L A D O R A    P O L O N E S A     ")
    print("==================================================")
    print()    

    # crie calculadora para expressões polonesa
    hp = Polonesa()

    # interprete cada expressão ou comando
    expressao = input(PROMPT).strip()
    while expressao not in QUIT:
        if expressao == CLEAR:
            # limpe as variáveis na memória da calculadora
            hp.clear()
        elif expressao == MOSTRE_VARIAVEIS:
            # exiba as variáveis da calculadora
            print(hp)
        else:
            # calcule e exiba o valor da expressão
            print(hp.eval(expressao))

        # leia próxima expressão    
        expressao = input(PROMPT).strip()        

    print("Curta a página de MAC0122 no feiçebuqui.\n")
