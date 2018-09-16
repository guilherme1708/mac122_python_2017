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

# import classe Lista_Pontos2D
from lista_pontos2d import Lista_Pontos2D

# contantes
INFINITO = float('inf')

#===========================================================
#
# Classe Lista_Pontos
#
#===========================================================

class Par_Mais_Proximo(Lista_Pontos2D):
    '''
    Classe utilizada para representar uma lista de pontos plano. 
    Cada ponto é representado por um objeto Ponto2D.

    Está classe herda da classe Lista_Pontos todos os seus atributos.
    Os atributos herdados e que poderão ser uteis aqui são apenas:

      `pts` (list): lista de pontos (objetos da classe Ponto2D)
      `n`   (int) : número de pontos em `pts`
      __str__(self): recebe uma referência a um objeto Lista_Pontos2D e 
         retorna o string  que o representa. 
      __len__(self):  recebe uma referência `self` para um objeto 
         Lista_Pontos2D e retorna o número de pontos na lista 
         representada por `self`.
    '''
    
    #----------------------------------------------------    
    def __init__(self, pts):
        '''(Par_Mais_Proximo, list) -> None

        Chamado pelo construtor da classe.

        Recebe um referência `self` ao objeto Par_Mais_Proximo que está 
        sendo criado e uma lista `pts` de objetos da classe Ponto2D.

        Acrescenta a esse objeto todos os atributos herdados da classe 
        Lista_Pontos2D.

        Exemplos:

        >>> lista = [Ponto2D(), Ponto2D((1,1)), Ponto2D((0,1)), Ponto2D((1,1))]
        >>> type(lista[0])
        <class 'ponto2d.Ponto2D'>
        >>> print(lista[0])
        (0, 0)
        >>> print(lista[1])
        (1, 1)
        >>> type(lista[2])
        <class 'ponto2d.Ponto2D'>
        >>> pontos = Par_Mais_Proximo(lista)
        >>> type(pontos)
        <class '__main__.Par_Mais_Proximo'>
        >>> type(pontos.pts)
        <class 'list'>
        >>> type(pontos.pts[0])
        <class 'ponto2d.Ponto2D'>
        >>> print(pontos.pts[0])
        (0, 0)
        >>> for pt in pontos.pts: print(pt)

        (0, 0)
        (1, 1)
        (0, 1)
        (1, 1)
        >>> pontos.n
        4
        >>> len(pontos)
        4
        >>> 
        '''
        # acrescenta a self os atributos de Lista_Pontos2D:
        #     pts, n, __str__, __len__, forca_bruta()
        Lista_Pontos2D.__init__(self, pts)

    #-------------------------------------------------------------
    def faixa(self, d, p, q, r):
        '''(Par_Mais_Proximo, float, int, int, int) -> float, tuple

        Recebe 

            * uma referência `self` para um objeto Par_Mais_Proximo e 
            * um float `d`, 
            * inteiros `p`, `q` e `r` tais que 

                   0 <= p <= q <= r <= len(self).
 
        Os pontos em self.pts[p:r] então em __ordem crescente__ 
        em relação às suas abscissas. 

        O método retorna 

            - um float d_faixa e 
            - uma tupla (pt0_faixa, pt1_faixa)

        tais que

            - d_faixa é a menor distância entre dois pontos  
              pt0 e pt1 tais que:

                 (1) pt0 é um ponto em self.pts[p:q];
                 (2) pt1 é um ponto em self.pts[q:r]; e
                 (3) ambos os pontos estão na faixa de largura d_faixa
                     em relação a q;

            - a tupla pt0_faixa e pt1_faixa são pontos satisfazendo (1),
              (2) e (3) e a distãncia entre eles é d_faixa.

        Para calcular a distância entre dois pontos, digamos, pt0 e pt1 este 
        método __deve__ utilizar o método Ponto2D.distancia():

            pt0.distancia(pt1) == pt1.distancia(pt0) # distância entre pt0 e pt1

        Se a faixa de largura d em relação a q não possui pontos pt0 e pt1 
        satisfazendo (1), (2) e (3), então o método __deve__ retornar None, ()

        Exemplos:

        >>> lista = [(-4, 0), (-2, 0), (0, 3), (1, -1), (2, 2), (3, 2)]
        >>> pts = []
        >>> for pt in lista: pts.append(Ponto2D(pt))

        >>> type(pt)
        <class 'tuple'>
        >>> type(pt[0])
        <class 'int'>
        >>> type(pts)
        <class 'list'>
        >>> type(pts[0])
        <class 'ponto2d.Ponto2D'>
        >>> for p in pts: print(p)

        (-4, 0)
        (-2, 0)
        (0, 3)
        (1, -1)
        (2, 2)
        (3, 2)
        >>> pontos = Par_Mais_Proximo(pts)
        >>> len(pontos)
        6
        >>> pontos.n # herdado de Lista_Pontos2D
        6
        >>> type(pontos.pts)
        <class 'list'>
        >>> type(pontos.pts[0])
        <class 'ponto2d.Ponto2D'>
        >>> type(pontos.pts[1])
        <class 'ponto2d.Ponto2D'>
        >>> for p in pontos.pts: print(p)

        (-4, 0)
        (-2, 0)
        (0, 3)
        (1, -1)
        (2, 2)
        (3, 2)
        >>> d, par = pontos.faixa(6, 0, 3, 6)
        >>> print("d=", d, "pts0=", par[0], "pts1=", par[1])
        d= 2.23606797749979 pts0= (0, 3) pts1= (2, 2)
        >>> d, par = pontos.faixa(36, 0, 3, 6)
        >>> print("d=", d, "pts0=", par[0], "pts1=", par[1])
        d= 2.23606797749979 pts0= (0, 3) pts1= (2, 2)
        >>> d, par = pontos.faixa(1, 0, 3, 6)
        >>> print("d=", d, "par=", par)
        d= None par= ()
        >>> d, par = pontos.faixa(3, 0, 2, 6)
        >>> d, par = pontos.faixa(1, 0, 3, 6)
        >>> d, par = pontos.faixa(3, 0, 2, 6)
        >>> print("d=", d, "pts0=", par[0], "pts1=", par[1])
        d= 3.1622776601683795 pts0= (-2, 0) pts1= (1, -1)
        >>> d, par = pontos.faixa(3.5, 0, 2, 6)
        >>> print("d=", d, "pts0=", par[0], "pts1=", par[1])
        d= 3.1622776601683795 pts0= (-2, 0) pts1= (1, -1)
        >>> d, par = pontos.faixa(1.0, 1, 2, 6)
        >>> print("d=", d, "pts0=", par[0], "pts1=", par[1])
        Traceback (most recent call last):
          File "<pyshell#47>", line 1, in <module>
            print("d=", d, "pts0=", par[0], "pts1=", par[1])
        IndexError: tuple index out of range
        >>> print("d=", d, "par=", par)
        d= None par= ()
        >>> d, par = pontos.faixa(2.5, 1, 2, 6)
        >>> print("d=", d, "pts0=", par[0], "pts1=", par[1])
        d= 3.1622776601683795 pts0= (-2, 0) pts1= (1, -1)
        >>> d, par = pontos.faixa(2.0, 3, 4, 6)
        >>> print("d=", d, "pts0=", par[0], "pts1=", par[1])
        d= 3.1622776601683795 pts0= (1, -1) pts1= (2, 2)
        >>> d, par = pontos.faixa(2.0, 4, 5, 6)
        >>> print("d=", d, "pts0=", par[0], "pts1=", par[1])
        d= 1.0 pts0= (2, 2) pts1= (3, 2)
        >>> d, par = pontos.faixa(0.4, 4, 5, 6)
        >>> print("d=", d, "par=", par)
        d= None par= ()
        lista = [(-4, 0), (-2, 0), (0, 3), (1, -1), (2, 2), (3, 2)]
        d, par = pontos.faixa(6, 0, 3, 6)
        >>> 
        '''
        x = self.pts[q].x() # 1
        t = 0
        k = 0
        laux = []
        
        for i in range(p,q): #(0,3)
            m = abs(self.pts[i].x() - x)
            if m < d: # 5,3,1
                laux.append(m)
                t += 1
        mx = max(laux).index()
        
        for i in range(q+1,r): #(4,6)
            if abs(self.pts[i-1].x() - x) < d: # 0,1,2
                n = max(self.pts[i]).index()
                k += 1

        if t < 1 or k < 1:
            return None, ()
        
        for i in range(mx,q):
            for j in range(q,n):
                d_1 = self.pts[i].distancia(self.pts[j])
                if d_1 < d:
                    d = d_1
        
        return d
        
    #-------------------------------------------------------------
    def divisao_e_conquista(self, p, r):
        '''(Par_Mais_Proximo, int, int) -> float, tuple

        Recebe 

            - uma referência `self` para um objeto Par_Mais_Proximo e 
            - dois inteiros `p` e `r`. 

        Os pontos em self.pts[p:r] então em __ordem crescente__ em 
        relação às suas abscissas.

        O método calcula e retorna 

            - a menor distância d entre um par de pontos na lista 
              self.pts[p:r], e 

            - uma tupla (pt0, pt1) de pontos em self.pts[p:r] tais 
              que distância entre eles é d.

        Para calcular a distância entre dois pontos, digamos, pt0 e pt1 
        este método __deve__ utilizar os métodos Ponto2D.distancia():

            pt0.distancia(pt1) == pt1.distancia(pt0) # distância entre pt0 e pt1

        Se self.pts[p:r] não tem dois pontos a função __deve__ retornar None, ()

        Esta função deve ser uma implementação da simplificação do 
        algoritmo de Shamos e Hoey como descrito no enunciado do 
        exercício programa.


        Exemplos:

        >>> coords = [(-4, 0), (-2, 0), (0, 3), (1, -1), (2, 2), (3, 2)]
        >>> pts = []
        >>> for coord in coords: pts.append(Ponto2D(coord))

        >>> type(pts)
        <class 'list'>
        >>> type(pts[0])
        <class 'ponto2d.Ponto2D'>
        >>> len(pts)
        6
        >>> pontos = Par_Mais_Proximo(pts)
        >>> len(pontos)
        6
        >>> pontos.n
        6
        >>> for p in pontos.pts: print(p)

        (-4, 0)
        (-2, 0)
        (0, 3)
        (1, -1)
        (2, 2)
        (3, 2)
        >>> print(pontos)
        [(-4, 0), (-2, 0), (0, 3), (1, -1), (2, 2), (3, 2)]
        >>> d, par = pontos.divisao_e_conquista(0, 6)
        >>> print("d=", d, "pts0=", par[0], "pts1=", par[1])
        d= 1.0 pts0= (2, 2) pts1= (3, 2)
        >>> d, par = pontos.divisao_e_conquista(0, 3)
        >>> print("d=", d, "pts0=", par[0], "pts1=", par[1])
        d= 2.0 pts0= (-4, 0) pts1= (-2, 0)
        >>> d, par = pontos.divisao_e_conquista(3, 6)
        >>> print("d=", d, "pts0=", par[0], "pts1=", par[1])
        d= 1.0 pts0= (2, 2) pts1= (3, 2)
        >>> d, par = pontos.divisao_e_conquista(4, 6)
        >>> print("d=", d, "pts0=", par[0], "pts1=", par[1])
        d= 1.0 pts0= (2, 2) pts1= (3, 2)
        >>> d, par = pontos.divisao_e_conquista(3, 5)
        >>> print("d=", d, "pts0=", par[0], "pts1=", par[1])
        d= 3.1622776601683795 pts0= (1, -1) pts1= (2, 2)
        >>> d, par = pontos.divisao_e_conquista(4, 5)
        >>> d, par
        (None, ())
        >>> 
        '''
        n = r-p

        if n <= 1:
            return None, ()
        elif n == 2:
            pt0 = self.pts[p]
            pt1 = self.pts[r-1]
            d = pt0.distancia(pt1)
            return d,(pt0,pt1)
        
        q = (p+r)/2
        d_esq = self.divisao_e_conquista(p,q)
        d_dir = self.divisao_e_conquista(q,r)
        d = min(d_esq,d_dir)
        print('1',d_dir)
        print('2',d_esq)
        return self.faixa(d,p,q,r)

#---------------------------------------------------------------------
def unit_test():
    '''(None) -> None

    Função que pode ser usada para testar a sua classe Lista_Pontos2D
    interativamente.
    '''
    import util

    #
    FORCA_BRUTA         = 'f'
    DIVISAO_E_CONQUISTA = 'd'
    # deseja animação
    SIM = 's'
    NAO = 'n'
    
    # prompts usados pelo programa
    PROMPT_NO_PONTOS  = "no. de pontos >>> "
    PROMPT_SEMENTE    = "semente >>> "
    PROMPT_ANIMACAO   = "\nexecutar animação ('s' para sim) >>> "
    PROMPT_ALGORITMO  = "algoritmo ('%s' para forçao-bruta, '%s' para divisão-e-conquista) >>> "\
                        %(FORCA_BRUTA,DIVISAO_E_CONQUISTA)

    # mensagens de erro
    ERRO_PONTOS  = "ERRO >>> número de pontos deve ser um inteiro positivo > 1 ('%s')"
    ERRO_SEMENTE = "ERRO >>> semente deve ser um inteiro ('%s')"
    ERRO_OPCAO   = "ERRO >>> opção inválida ('%s')"

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
    
    # crie um objeto Par_Mais_Proximo2D
    pontos = Par_Mais_Proximo(pts)

    # escolha o algoritmo 
    opcao = input(PROMPT_ALGORITMO).strip()
    if   opcao == FORCA_BRUTA:
        algoritmo = pontos.forca_bruta
        ordene_x  = False
    elif opcao == DIVISAO_E_CONQUISTA:
        algoritmo = pontos.divisao_e_conquista
        ordene_x  = True
    else:
        print(ERRO_OPCAO %opcao)
        return None

    # execute o algoritmo
    util.execute(pontos, algoritmo, ordene_x)
            
    # pergunte se a animação deve ser executada
    opcao = input(PROMPT_ANIMACAO).strip()
    if opcao == SIM:
        # execute a animação
        util.animacao(pontos, algoritmo)

    # termino normal... vaze    
    print("Fui!")
     
