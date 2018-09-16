#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
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

def main():
    '''
    Este programa lê um inteiro `n` e imprime: 

        - uma estrela
        - uma borboleta e
        - um  diamante

    de ordem n.

    O objetivo desta função é apenas auxiliá-lo no desenvolvimento
    e teste das demais.

    A função main() não será corrigida.

    No momento, se você executar essa função, obterá o seguinte resultado:

    >>> main()
    Digite a ordem das figuras: 3
    Vixe! Ainda não fiz a função estrela()... :-(
    Vixe! Ainda não fiz a função borboleta()... :-(
    Vixe! Ainda não fiz a função diamante()... :-(

    Depois de fazer suas funções você deverá obter:

    >>> main()
    Digite a ordem das figuras: 3
    * . . . . . * 
    . * . . . * . 
    . . * . * . . 
    . . . * . . . 
    . . * . * . . 
    . * . . . * . 
    * . . . . . * 

    * . . . . . * 
    * * . . . * * 
    * * * . * * * 
    * * * * * * * 
    * * * . * * * 
    * * . . . * * 
    * . . . . . * 

    . . . * . . . 
    . . * * * . . 
    . * * * * * . 
    * * * * * * * 
    . * * * * * . 
    . . * * * . . 
    . . . * . . . 
    
    2*n+1 linhas
    4*n+1 colunas
 
    '''
    n = int(input('Digite a ordem das figuras: '))
    print(estrela(n))
    print(borboleta(n))
    print(diamante(n))

# ===============================================================
def estrela(n):
    ''' (int) -> str 
  
    Recebe um inteiro n >= 0 e retorna um string que representa
    uma "estrela" de ordem n.

    Exemplos:
    
    >>> estrela(1)
    '* . * \n. * . \n* . * \n' 0 4 9 14 18
    >>> estrela(2)
    '* . . . * \n. * . * . \n. . * . . \n. * . * . \n* . . . * \n'
    >>> s = estrela(1)
    >>> t = estrela(2)
    >>> len(s)
    21
    >>> len(t)
    55
    >>> print(s): ordem 1
    * . * 
    . * . 
    * . *

    >>> print(t): oredem 04 13 22 31 40
    * . . . * 
    . * . * . 
    . . * . . 
    . * . * . 
    * . . . * 
    
    >>> len(estrela(1))
    21
    >>> len(estrela(2))
    55
    >>> 
    '''
    nlin = ncol = 2*n+1
    
    e = ''
    
    for lin in range (nlin):
        for col in range (ncol): 
            if lin == col or -lin <= -2*n+col and not -lin < -2*n+col:
                e += '* '
            else:
                e += '. '
        e += '\n'

    return e
# ===============================================================
def borboleta(n):
    ''' (int) -> str 
  
    Recebe um inteiro n >= 0 e retorna um string que representa
    uma "borboleta" de ordem n.

    Exemplos:

    >>> borboleta(1)
    '* . * \n* * * \n* . * \n'
    >>> borboleta(2)
    '* . . . * \n* * . * * \n* * * * * \n* * . * * \n* . . . * \n'
    >>> len(borboleta(1))
    21
    >>> len(borboleta(2))
    55
    >>> print(borboleta(2))
    * . . . *   
    * * . * *   
    * * * * *  
    * * . * * 
    * . . . *   
    
    >>> print(borboleta(1))
    * . * 
    * * * 
    * . * 
    
    >>>
    '''
    nlin = ncol = 2*n+1
    
    b = ''
    
    for lin in range (nlin):
        for col in range (ncol): 
            if (-lin >= -col or lin <= 2*n-col) and (lin >= col or -lin <= -2*n+col):
                b += '* '
            else:
                b += '. '
        b += '\n'
    
    return b
# ===============================================================
def diamante(n):
    ''' (int) -> str 
  
    Recebe um inteiro n >= 0 e retorna um string que representa
    um "diamante" de ordem n.

    Exemplos:

    >>> diamante(1)
    '. * . \n* * * \n. * . \n'
    >>> diamante(2)
    '. . * . . \n. * * * . \n* * * * * \n. * * * . \n. . * . . \n'
    >>> len(diamante(2))
    55
    >>> print(diamante(2))
    . . * . . 
    . * * * . 
    * * * * * 
    . * * * . 
    . . * . . 
    
    >>> print(diamante(1))
    . * . 
    * * * 
    . * . 

    '''

    nlin = ncol = 2*n+1
    
    d = ''
    
    for lin in range (nlin):
        for col in range (ncol): 
            if lin >= n-col and lin <= n+col and -lin <= -col+n and -lin >= (-3*n)+col:
                d += '* '
            else:
                d += '. '
        d += '\n'
    
    return d
# ===============================================================
if __name__ == '__main__':
    main()
