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
from palete import Palete
from nuvens import Nuvens

#########################################################################
#
#  Função K médias

def k_medias(img, palete):
    '''
    (Image, Palete) -> lista de Paletes
    Recebe uma imagem (img) e um objeto Palete (palete) que contém a definição
    inicial das cores a serem classificadas (nomes e centróides). 
    A função k_medias refina as cores (centroides) da palete a partir
    dessa classificação inicial iterativamente usando o algoritmo de
    k-medias, até que o centroide de cada cor estabilize (ou seja, não sofra 
    mais mudanças).

    A função retorna a lista contendo todas as paletes utilizadas e calculadas, 
    desde a inicial até a estabilização. A última palete calculada, por ser igual
    a penúltima, não deve ser inserida na lista.
    
    '''
    paletes = []
    cp = palete.get_cores()
    paleteini = Palete(cp)
    paletes.append(paleteini)
    nuv = Nuvens(palete)
    nuv.aglomere(img, palete)
    paletefim = nuv.calcule_centroides(palete)
    paletes.append(paletefim)
    
    while paleteini != paletefim: 
        
        nuv = Nuvens(paletefim)
        nuv.aglomere(img, paletefim)
        nova = nuv.calcule_centroides(paletefim)
        paletes.append(nova)
        paleteini = nova
        paletefim = paleteini
        
  
    return paletes

#######################################################################
#######################################################################
#                                                                     #
#  Escreva a seguir outras funções  e classes que desejar. Você pode  #
#  inclusive mudar o testinho.                                        #
#                                                                     #
#######################################################################
#######################################################################

# Função para teste da função k_medias

def testinho_da_k_medias():
    """ 
    le uma imagem (de um arquivo) e usa uma palete dada para
    testar a função k_medias. Salva uma imagem transformada 
    com a palete mais refinada.

    OBS: altere a palete e veja como o resultado final pode mudar bastante.
    """
    cores = {
        'vermelho':(128,0,0),
        'verde':(0,128,0),
        'amarelo':(128, 128, 0),
        'azul':(0,0,128),
        'cinza':(128, 128, 128)
        }
     
    palete_inicial = Palete(cores)
    print("Palete:\n%s"%(str(palete_inicial)))

    nome_imagem = input("Digite o nome do arquivo contendo uma imagem: ")
        
    img = Image.open( nome_imagem )
    width, height = img.size
    print ("Carreguei a imagem %s que tem %d linhas e %d colunas"%(nome_imagem, height, width))
    img.show()

    paletes = k_medias(img, palete_inicial)

    n = len(paletes)
    print("O k-medias convergiu após %d iterações e as seguintes paletes:\n"%(n))
    
    # imprime as paletes
    for i in range(n):
        print("Palete[%2d]:\n%s"%( i, str(paletes[i])))
        
    # mostra as imagens convertidas usando a palete inicial
    print("Mostrando imagem convertida usando a primeira palete")
    img_ini = paletes[0].converte_imagem(img)
    img_ini.show()
    pause()

    # mostra as imagens convertidas usando a ultima palete
    print("Mostrando imagem convertida usando a última palete")
    img_fim = paletes[-1].converte_imagem(img)
    img_fim.show()

    nome_saida = 'saida.jpg'
    img_fim.save(nome_saida)
    print("Imagem convertida foi salva em ", nome_saida)

    print("Fim")
    
#########################################################################
#    
    
def pause():
    '''
    '''
    input(">>> Aperte 'enter' para continuar...")
    
#########################################################################
#
#

if __name__ == "__main__":
    testinho_da_k_medias()
