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

from PIL import Image

## Use a sua implementação da classe Palete
from palete import Palete

#########################################################################
#
# Classe Nuvens
#
class Nuvens:
    '''
    Estrutura para auxiliar a construção de nuvens de pontos (cores)
    associadas a cada classe (uma cor na palete) para o algoritmo de
    k-médias.
    '''
    # ------------------------------------------------------------
    def __init__(self, palete):
        ''' (Nuvens, Palete) -> None
        O construtor de Nuvens recebe um objeto Palete que define os 
        k nomes de classes (cores) e cria um dicionário para armazenar as 
        "nuvens" a serem associadas a cada classe. 
        Nesse dicionário, a chave é o nome da cor (str) 
        e o valor é a lista de cores mais próximas (inicialmente vazia).
        '''

        self.nuvem = palete.get_cores()
        
        for i in self.nuvem:
            self.nuvem[i] = []

    # ------------------------------------------------------------
    def __str__(self):
        ''' (Nuvens) -> str
        Retorna um string com o estado (nome e tamanho) de cada nuvem.
        '''
        s= ''
        
        for k in self.nuvem:
            s += str(k) + ' : ' + str(len(self.nuvem[k])) + ' pixels' + '\n'
            
        return s
    # ------------------------------------------------------------
    def aglomere(self, img, palete):
        ''' (Nuvens, Image, Palete) -> None
        Recebe uma imagem img e classifica cada pixel de 
        img em uma nuvem usando a palete.
        Como resultado da classificação de um pixel, a sua
        cor deve ser inserida na nuvem de centroide mais próximo
        dessa cor.

        Você pode usar os seguintes métodos da classe Image:
        - img.size   ==> 2-tuple contendo a largura e altura da imagem
        - img.getpixel ((coluna, linha)) ==> retorna a cor RGB (3-tuple) 
        na posição (coluna, linha)
        '''
        
        dimc, diml = img.size
        
        for col in range(dimc):
            for lin in range(diml):
                r,g,b = img.getpixel((col,lin))
                cor = palete.mais_proxima((r,g,b))
                self.nuvem[cor].append((r,g,b))
        
    # ------------------------------------------------------------
    def calcule_centroides(self, palete):
        ''' (Nuvens, Palete) -> Palete
        Recebe a palete utilizada para calcular as nuvens e 
        retorna um objeto Palete com as novas cores refinadas, resultado do
        cálculo do centróide de cada nuvem.
        As nuvens devem ser re-inicializadas (esvaziadas) para uma próxima iteração. 
        Caso a nuvem de uma cor esteja vazia, o valor do centróide na palete de saida deve 
        ser igual à palete de entrada.
        '''
        a,b,c = 0,0,0
        
        for cor in self.nuvem:
            tam = (len(self.nuvem[cor]))
            for k in self.nuvem[cor]:
                    a += k[0]
                    b += k[1]
                    c += k[2]
                    
            if tam == 0:
                (a,b,c) = palete.cores[cor]
            else:
                (a,b,c) = ((a//tam,b//tam,c//tam))
        
            palete.cores[cor] = ((a,b,c))
            a,b,c = 0,0,0

        self.__init__(palete)
        
        return palete

#########################################################################
#########################################################################
#
#  Escreva a seguir outras funções  e classes que desejar. Você pode
#  inclusive mudar o testinho.
#
#########################################################################
#########################################################################

#########################################################################
#
#  Função para teste da classe Nuvens

def testinho_das_nuvens():
    ''' None -> None
    Função que executa testes da classe Nuvens.
    Execute esse programa em seu computador antes de submeter.

    Saída:

    Palete inicial:
    vermelho : (200, 0, 0)
    verde : (0, 200, 0)
    amarelo : (128, 128, 0)
    azul : (0, 0, 200)

    Nuvens inicial:
    vermelho : 0 pixels
    verde : 0 pixels
    amarelo : 0 pixels
    azul : 0 pixels

    Nuvens aglomeradas:
    vermelho : 1 pixels
    verde : 3 pixels
    amarelo : 2 pixels
    azul : 0 pixels

    Palete refinada:
    vermelho : (210, 12, 20)
    verde : (0, 210, 20)
    amarelo : (120, 90, 20)
    azul : (0, 0, 200)

    Nuvens limpas:
    vermelho : 0 pixels
    verde : 0 pixels
    amarelo : 0 pixels
    azul : 0 pixels
    
    '''

    # Cria uma Palete
    cores = {
        'vermelho':(200,0,0),
        'verde':(0,200,0),
        'amarelo':(128, 128, 0),
        'azul':(0,0,200)
        }
    palete = Palete(cores)
    print("Palete inicial:\n%s"%(str(palete)))
    
    # Cria uma imagem-zinha
    largura = 3
    altura = 2
    s = (largura, altura)
    img = Image.new('RGB', s)

    cores = [
        [(120, 100, 10), (120, 80, 30), (0, 210, 20)],
        [(0, 210, 20), (0, 210, 20), (210, 12, 20)]
        ]
    
    for col in range( largura ):
        for lin in range( altura ):
            img.putpixel( (col, lin), cores[lin][col] )
    
    # vamos testar...
    nuv = Nuvens(palete)
    print("Nuvens inicial:\n%s"%(str(nuv)))

    nuv.aglomere(img, palete)
    print("Nuvens aglomeradas:\n%s"%(str(nuv)))
    
    nova = nuv.calcule_centroides(palete)
    print("Palete refinada:\n%s"%(str(nova)))
    print("Nuvens limpas:\n%s"%(str(nuv)))
    

#########################################################################
#
#   FIM
#
#########################################################################


#########################################################################

if __name__ == "__main__":
    testinho_das_nuvens()
