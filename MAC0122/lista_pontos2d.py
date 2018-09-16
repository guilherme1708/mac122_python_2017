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

# import classe Ponto2D
from ponto2d import Ponto2D

# contantes
INFINITO = float('inf')

#===========================================================
#
# Classe Lista_Pontos
#
#===========================================================

class Lista_Pontos2D:
    '''
    Classe que representa uma lista de pontos no plano representados por
    objetos da classe Ponto2D.
    
    Os atributos de estado desta classe serão `pts` e `n`:

       `pts` (list): lista de referências a objetos da classe Ponto2D e
       `n`   (int) : número de pontos em `pts`.
 
    '''
    
    #----------------------------------------------------    
    def __init__(self, pts):
        '''(Lista_Pontos2D, list) -> None

        Chamado pelo construtor da classe.

        Recebe um referência `self` ao objeto Lista_Pontos2D que está sendo 
        criado e uma lista `pts` de objetos da classe Ponto2D.

        Exemplos:

        >>> lista = [Ponto2D(), Ponto2D((1,1)), Ponto2D((0,1)), Ponto2D((1,1))]
        >>> lista[0]
        <ponto2d.Ponto2D object at 0x7f8cc526ada0>
        >>> print(lista[0])
        (0, 0)
        >>> print(lista[1])
        (1, 1)
        >>> type(lista[2])
        <class 'ponto2d.Ponto2D'>
        >>> pontos = Lista_Pontos2D(lista)
        >>> type(pontos)
        <class '__main__.Lista_Pontos2D'>
        >>> type(pontos.pts)
        <class 'list'>
        >>> for i in range(4):
                print(pontos.pts[i])

                
        (0, 0)
        (1, 1)
        (0, 1)
        (1, 1)
        >>>
        >>> pontos.n
        4
        >>> 
        '''
        laux = []
        for i in pts:
            laux.append(i)
        
        self.pts = laux
        self.n = len(self.pts)
        

    #----------------------------------------------------
    def __len__(self):
        '''(Lista_Pontos2D) -> int 

        Recebe uma referência `self` para um objeto Lista_Pontos2D e 
        retorna o número de pontos na lista representada por `self`.

        Usado pelo Python quando escrevemos "len(Lista_Pontos2D)".

        Exemplos:
        
        >>> lista = [Ponto2D(), Ponto2D((1,1)), Ponto2D((0,1)), Ponto2D((1,1))]
        >>> pontos = Lista_Pontos2D(lista)
        >>> type(pontos)
        <class '__main__.Lista_Pontos2D'>
        >>> len(pontos)
        4
        >>> pontos2 = Lista_Pontos2D([Ponto2D((1.2,3.4)), Ponto2D((1,2.7))])
        >>> len(pontos2)
        2        
        >>> 
        '''
        return len(self.pts)
    #----------------------------------------------------    
    def __str__(self):
        '''(Lista_Pontos2D) -> str

        Recebe uma referência a um objeto Lista_Pontos2D e retorna o string 
        que o representa. 

        Usando quando escrevemos "print(Lista_Pontos2D)" ou "str(Lista_Pontos2D)". 

        O formato do string deve ser: 

           "[str(Ponto2D), str(Ponto2D), ..., str(Ponto2D)]"
           
        Exemplos:

        >>> lista = [Ponto2D(), Ponto2D((1,1)), Ponto2D((0,1)), Ponto2D((1,1))]
        >>> pontos = Lista_Pontos2D(lista)
        >>> type(pontos)
        <class '__main__.Lista_Pontos2D'>        
        >>> str(pontos)
        '[(0, 0), (1, 1), (0, 1), (1, 1)]' 
        >>> print(pontos)
        [(0, 0), (1, 1), (0, 1), (1, 1)]
        >>> pontos2 = Lista_Pontos2D([Ponto2D((1.2,3.4)), Ponto2D((1,2.7))])
        >>> len(pontos2)
        2
        >>> str(pontos2)
        '[(1.2, 3.4), (1, 2.7)]'
        >>>         
        '''
        s = '['
        pts = ''
        
        if len(self.pts) == 0:
            return str([])
        
        for i in self.pts:
            pts += str(i)
        
        n = len(pts)
        i = 0
        
        while i < n-1:
            s += pts[i]
            if pts[i] == ')':
                s += ', '
            i += 1
        s += ')'
        s += ']'

        return s
        
    #----------------------------------------------------
    def forca_bruta(self, p, r):
        '''(Lista_Pontos2D, int, int) -> float, tuple

        Recebe 

            - uma referência `self` para um objeto Lista_Pontos2D e 
            - dois inteiros `p` e `r`. 

        O método calcula e retorna 

            - a menor distância d entre um par de pontos na lista 
              self.pts[p:r], e 

            - um tuple (pt0, pt1) de objetos da classe Ponto2D, sendo que 
              pt0 e pt1 são pontos em self.pts[p:r] que estão a distância d.

        Para calcular a distância entre dois pontos, digamos, pt0 e pt1 
        este método __deve__ utilizar os métodos Ponto2D.distancia() ou 
        Ponto2D.distancia2():

            pt0.distancia(pt1) == pt1.distancia(pt0) # distância entre pt0 e pt1
            pt0.distancia2(pt1) == pt1.distancia2(pt0) # quadrado da distância entre pt0 e pt1

        Se self.pts[p:r] não tem dois pontos a função __deve__ retornar None, ()

        Exemplos:

        >>> lista = [Ponto2D(), Ponto2D((1,0)), Ponto2D((0,1)), Ponto2D((1,1))]
        >>> pontos = Lista_Pontos2D(lista)
        >>> print(pontos)
        [(0, 0), (1, 0), (0, 1), (1, 1)]        
        >>> d, par = pontos.forca_bruta(0, len(pontos))
        >>> print("d =", d, "pts0=", par[0], "pts1=", par[1])
        d = 1 pts0= (0, 0) pts1= (1, 0)
        >>> d, par = pontos.forca_bruta(1, len(pontos))
        >>> print("d =", d, "pts0=", par[0], "pts1=", par[1])
        d = 1 pts0= (1, 0) pts1= (1, 1)
        >>> d, par = pontos.forca_bruta(2, len(pontos))
        >>> print("d =", d, "pts0=", par[0], "pts1=", par[1])
        d = 1 pts0= (0, 1) pts1= (1, 1)
        >>> d, par = pontos.forca_bruta(3, len(pontos))
        >>> d, par
        (None, ())
        >>> lista2 = [Ponto2D((0,0)), Ponto2D((0.5,0.5)), Ponto2D((0,2)), Ponto2D((2,3))]
        >>> pontos2 = Lista_Pontos2D(lista2)
        >>> d, par = pontos2.forca_bruta(0, 4)
        >>> print("d =", d, "pts0=", par[0], "pts1=", par[1])
        d = 0.7071067811865476 pts0= (0, 0) pts1= (0.5, 0.5)
        >>> d, par = pontos2.forca_bruta(0, 3)
        >>> print("d =", d, "pts0=", par[0], "pts1=", par[1])
        d = 0.7071067811865476 pts0= (0, 0) pts1= (0.5, 0.5)
        >>> d, par = pontos2.forca_bruta(1, 3)
        >>> print("d =", d, "pts0=", par[0], "pts1=", par[1])
        d = 1.5811388300841898 pts0= (0.5, 0.5) pts1= (0, 2)
        >>> lista3 = [Ponto2D((0,3)), Ponto2D((-1,-1)), Ponto2D(), Ponto2D((2,2)), Ponto2D((3,0))]
        >>> pontos3 = Lista_Pontos2D(lista3)
        >>> print(pontos3)
        [(0, 3), (-1, -1), (0, 0), (2, 2), (3, 0)]
        >>> d, par = pontos3.forca_bruta(0, 5)
        >>> print("d =", d, "pts0=", par[0], "pts1=", par[1])
        d = 1.4142135623730951 pts0= (-1, -1) pts1= (0, 0)
        >>> d, par = pontos3.forca_bruta(3, 5)
        >>> print("d =", d, "pts0=", par[0], "pts1=", par[1])
        d = 2.23606797749979 pts0= (2, 2) pts1= (3, 0)
        >>>  
        '''
        n = len(self.pts[p:r])
        dc = {}
        dist = 0 
        if n < 2:
            return None, ()
        
        i = p
        while i < r:
            j = p
            while j != i and i < r:
                dist = self.pts[i].distancia(self.pts[j])
                dc[dist] = (self.pts[j],self.pts[i])
                j += 1
            i += 1
        
        if self.pts[0] != self.pts[1]:
            d = min(num for num in dc if num != 0)
        else:
            d = min(num for num in dc if num == 0)
        
        return d,dc[d]
#---------------------------------------------------------------------
def unit_test():
    '''(None) -> None

    Função que pode ser usada para testar a sua classe Lista_Pontos2D
    interativamente.
    '''
    import util
    
    # deseja animação
    SIM = 's'
    NAO = 'n'

    # prompts usados pelo programa
    PROMPT_NO_PONTOS  = "no. de pontos >>> "
    PROMPT_SEMENTE    = "semente >>> "
    PROMPT_ANIMACAO   = "\nexecutar animação ('s' para sim) >>> "

    # mensagens de erro
    ERRO_PONTOS  = "ERRO >>> número de pontos deve ser um inteiro positivo > 1 ('%s')"
    ERRO_SEMENTE = "ERRO >>> semente deve ser um inteiro ('%s')"

    # leia o número de pontos
    n_str = input(PROMPT_NO_PONTOS)

    # verifique se n_str é um string representando um inteiro positivo
    try:
        n = int(n_str)
        if n <= 1: raise ValueError
    except ValueError:
        print(ERRO_PONTOS %n_str)
        return None

    # leia a semente
    semente_str = input(PROMPT_SEMENTE)
 
    # verifique se semente_str é um string representando um inteiro
    try:
        semente = int(semente_str)
    except ValueError:
        print(ERRO_SEMENTE %semente_str)
        return None
   
    # crie uma lista de n pontos (Ponto2D) aleatórios 
    pts = util.gere_pontos(n,semente)

    # crie um objetos Lista_Pontos2D
    pontos = Lista_Pontos2D(pts)
    
    # execute a função selecionada    
    util.execute(pontos)

    # pergunte se a animação deve ser executada
    opcao = input(PROMPT_ANIMACAO).strip()
    if opcao == SIM:
        # execute a animação
        util.animacao(pontos)

    # termino normal... vaze    
    print("Fui!")

if __name__ == "__main__":
    unit_test()
