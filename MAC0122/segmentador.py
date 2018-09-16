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

#########################################################################
#
# Classe segmentador
#
#########################################################################

class Segmentador:
  '''
  Estrutura para auxiliar a construção de regiões conexas
  associadas a cada pixel para o algoritmo recursivo de construção
  de regiões.
  '''
  # ------------------------------------------------------------
  def __init__(self):
    ''' (Segmentador) -> None
    O construtor cria um dionário para armazenar 
    os rótulos e suas listas de regiões conexas.
    '''
    self.rotulos = {}
    self.lista = []
    
    self.c = 0
    self.l = 0

  # ------------------------------------------------------------
  def limpa_rotulos(self):
    ''' (Segmentador) -> None
    Limpa (esvazia) o dcionário de regiões.
    '''
    self.rotulos = {}

  # ------------------------------------------------------------
  def get_rotulos(self):
    ''' (Segmentador) -> dict
    Retorna um dicionario com todas as regiões encontradas.
    A chave do dicionário deve ser uma coordenada (2-tuple) 
    que representa a semente utilizada, e seu valor
    associado deve ser a lista de pixels com vizinhança 4 
    que podem ser alcançados a partir da semente.
    Observe que a chave é também um valor da lista.
    '''
    return self.rotulos
 
  # ------------------------------------------------------------
  def agrupe_R(self, img, semente, visitei):
    ''' (Segmentador, Image, (col, lin), list) -> list
    Retorna a lista de pixeis de mesma cor da semente (agrupamento) e
    que define a região conexa que contem a semente. 
    visitei é uma matriz de boleanos que tem mesma dimensao 
    de img e indica os pixels já visitados.

    Esse método DEVE SER RECURSIVO.
    '''
    
    dimc,diml = img.size
    col = semente[0]
    lin = semente[1]

    if img.getpixel(semente) == img.getpixel((col,lin)):
        visitei[lin][col] = True
        self.lista.append(img.getpixel((col,lin))) 
        return self.lista 

    if lin+1 < diml and img.getpixel(semente) == img.getpixel((col,lin+1)) and visitei[lin+1][col] == False:
            visitei[lin+1][col] = True
            lin += 1
            self.lista.append(img.getpixel((col,lin+1))) 

            return self.agrupe_R(img, semente, visitei)
         
    if col+1 < dimc and img.getpixel(semente) == img.getpixel((col+1,lin)) and visitei[lin][col+1] == False:
            visitei[lin][col] = True
            self.lista.append(img.getpixel((col+1,lin))) 
            col += 1
            return self.agrupe_R(img, semente, visitei)
        
    if lin-1 >=0 and img.getpixel(semente) == img.getpixel((col,lin-1)) and visitei[lin][col] == False:
            visitei[lin-1][col] = True
            self.lista.append(img.getpixel((col,lin-1)))
            
            return self.agrupe_R(img, semente, visitei)
        
    if  col-1 >= 0 and img.getpixel(semente) == img.getpixel((col-1,lin)) and visitei[lin][col-1] == True:
            visitei[lin][col] = True
            self.lista.append(img.getpixel((col-1,lin)))
            col -= 1
            return self.agrupe_R(img, semente, visitei)
        

    
  # ------------------------------------------------------------
  def segmente(self, img):
    ''' (Segmentador, Image) -> None
    Monta o dicionário de rótulos que segmenta img em regiões conexas
    usando o método recursivo agrupe_R.
    '''
    
    dimc,diml = img.size
    visitei = self.crie_matriz(diml,dimc)
            
    for col in range(dimc):
        for lin in range(diml):
            rg = self.agrupe_R(img,(col,lin),visitei)
            px = img.getpixel((col, lin))
            if px in rg:
                self.rotulos[(lin,col)] = rg
 
            
  # ------------------------------------------------------------
  def crie_matriz(self,n_linhas, n_colunas, valor = False):
     ''' (int, int, valor) -> matriz 
	
	  Cria e retorna uma matriz com n_linhas linha e n_colunas
	  colunas em que cada elemento é igual ao valor dado.
	  '''
     
     matriz = []
     
     for i in range(n_linhas):
         linha = [] 
         for j in range(n_colunas):
             linha.append(valor)
         matriz.append(linha)
         
     return matriz
   

#########################################################################
#  ESCREVA AQUI SUAS PROPRIAS FUNÇÕES E CLASSES, SE DESEJAR
#########################################################################


#########################################################################
#
#   FIM
#
#########################################################################

#########################################################################    
# FUNÇÕES PARA TESTE DA CLASSE SEGMENTADOR
#########################################################################    
def pause():
    '''
    '''
    input(">>> Aperte 'enter' para continuar...")

import random
import sys
sys.setrecursionlimit(1000)

def teste_pinta_imagem():
  ''' Use essa função para testar o segmentador com imagens resultantes do EP08.
  Use imagens pequenas e paletes pequenas, e salve a imagem refinada em PNG.
  Cuidado: imagens com regiões muito grandes podem estourar a pilha de recursão
  do Python. Você pode alterar o limite de recursao modificando a linha 
  sys.setrecursionlimit se desejar.
  '''
  random.seed(0)
  # Carrega o arquivo
  nome_imagem = input("Digite o nome do arquivo contendo uma imagem: ")
  img = Image.open( nome_imagem )

  # Imprime o tamanho da imagem
  width, height = img.size
  print ("Carreguei a imagem %s que tem %d linhas e %d colunas"%(nome_imagem, height, width))
  img.show()
  # pause()

  seg = Segmentador()
  seg.segmente(img)

  regiao = seg.get_rotulos()

  print("Achei %d regiões"%len(regiao))
  for rot in regiao:
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    
    for pix in regiao[rot]:
      img.putpixel( pix, (R,G,B) )
    print("\nSemente: ", rot)
    print("Regiao: ", regiao[rot])
  img.show()
  # pause()


def testinho():
  # Cria uma imagem-zinha e imprime a rotulação obtida.
  # saída esperada (os números podem ser diferentes, mas
  # devem representar as mesmas regioes):
  # Achei 8 regiões
  #Segmentação:
  #  1   6   6   6   6 
  #  1   6   1   1   1 
  #  1   6   1   0   5 
  #  1   1   1   0   5 
  #  3   3   3   7   7 
  #  2   3   3   7   4 

  # Primeiro vamos criar uma imagem-zinha
  c = [ (0, 0, 0), (64, 64, 64), (128,128,128), (255,255,255) ]

  cores = [
    [ c[0], c[1], c[1], c[1], c[1] ],
    [ c[0], c[1], c[0], c[0], c[0] ],
    [ c[0], c[1], c[0], c[2], c[3] ],
    [ c[0], c[0], c[0], c[2], c[3] ],
    [ c[1], c[1], c[1], c[0], c[0] ],
    [ c[2], c[1], c[1], c[0], c[3] ]
  ]
  
  altura = len(cores)
  largura = len(cores[0])
  s = (largura, altura)
  img = Image.new('RGB', s)

  for col in range( largura ):
    for lin in range( altura ):
      img.putpixel( (col, lin), cores[lin][col] )

  # Agora vamos testar o Segmentador
  seg = Segmentador()
#  seg.segmente(img)

  dimc,diml = img.size
  a = (0,0)
  visitei = seg.crie_matriz(diml,dimc) 
  a = seg.agrupe_R(img,a,visitei)
  print(a)
'''
  regiao = seg.get_rotulos()
  print("Achei %d regiões"%len(regiao))

  # e ver os resultados na forma de matriz
  # --- criando e convertendo regioes para matriz
  rotulos = []
  for i in range(altura):
    rotulos.append( largura*[0] )

  i = 0
  for rot in regiao:    
    for pix in regiao[rot]:
      col, lin = pix
      rotulos[lin][col] = i
    i += 1
  # ---- mostrando a matriz
  print("Segmentação:")
  for lin in range (altura):
    for col in range (largura):
      print("%3d"%rotulos[lin][col], end=' ')
    print()
'''
if __name__ == "__main__":
  # teste_pinta_imagem()
  testinho()
