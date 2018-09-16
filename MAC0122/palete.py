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
# Classe Palete
#


class Palete:
    '''
    Classe utilizada para representar paletes e suas operações.
    '''
    # ------------------------------------------------------------
    def __init__(self, cores):
        ''' (Palete, dict) -> None
        O construtor de Palete recebe um dicionário com as cores a
        serem armazenadas. Uma chave do dicionário é o nome (str) de uma
        cor e o valor do dicionário é uma cor RBG (3-tuple) associado ao 
        nome.

        Um objeto Palete deve fazer uma cópia de cores.
        '''
        self.cores = cores
        
    # ------------------------------------------------------------
    def __str__(self):
        ''' (Palete) -> str
        Retorna um string com os nomes e valores das cores armazenadas.
        '''
        s= ''
        
        for (k,v) in self.cores.items():
            s += str(k) + ' : ' + str(v) + '\n'
            
        return s
    # ------------------------------------------------------------
    def __eq__(self, other):
        ''' (Palete, Palete) -> Bool
        '''
        
        if self.cores == other.cores:
            return True
        return False
    # ------------------------------------------------------------
    def get_cores(self):
        ''' (Palete) -> dict
        Retorna uma cópia do dicionário contendo as cores armazenadas.
        '''
        copia = self.cores.copy()
        
        return copia
      
    # ------------------------------------------------------------
    def mais_proxima(self, cor):
        ''' (Palete, 3-tuple) -> str (nome de cor)
        Recebe uma cor RGB e retorna o nome da cor mais próxima
        armazenada na Palete.
        '''
        z = []
        dc = {}

        for rgb in self.cores:
            a = ((self.cores[rgb][0]-cor[0])**2 +(self.cores[rgb][1]-cor[1])**2 + (self.cores[rgb][2]-cor[2])**2)**(1/2)
            dc[a] = rgb
            z.append(a)
    
        m = min(z)
        
        for c in dc:
            if m == c:
                return dc[c]
        
    # ------------------------------------------------------------
    def converte_imagem(self, img):
        ''' (Palete, Image) -> Image
        Esse método recebe uma imagem img e retorna uma
        cópia dessa imagem onde cada cor foi convertida para 
        uma cor da palete atual (a mais próxima).
        Você pode usar os seguintes métodos da classe Image:
        - img.copy() ==> retorna uma cópia de img
        - img.size   ==> 2-tuple contendo a largura e altura da imagem
        - img.getpixel ((coluna, linha)) ==> retorna a cor RGB (3-tuple) na posição (coluna, linha)
        - img.putpixel ((coluna, linha), nova_cor_RBG) ==> altera a cor do pixel na 
        posição (coluna, linha) para o valor nova_cor_RGB.
        '''
        
        dimc,diml = img.size
        
        for col in range(dimc):
            for lin in range(diml):
                 r,g,b = img.getpixel((col,lin))
                 nova_cor = self.mais_proxima((r,g,b))
                 img.putpixel((col,lin), self.cores[nova_cor])
 
        
        return img

#########################################################################
#
#   Inclua a seguir outros métodos, classes e funções que você desejar
#
#   As funções "meus_testes()" e "pause()" são dadas abaixo free of charge.
#   Você pode modificá-las se desejar, para incluir outros testes, mas
#   teste o seu código antes de submetê-lo ao menos utilizando os testes
#   abaixo.
#
#   Não esqueça de documentar as suas funções e métodos usando docstrings. 
#
#########################################################################

#########################################################################
#
# meus_testes()

def meus_testes():
     ''' None -> None
     Função que executa testes da classe Palete
     Exemplo:
     >>> meus_testes()
     Palete: 
     vermelho : (128, 0, 0)
     verde : (0, 128, 0)
     amarelo : (128, 128, 0)
     azul : (0, 0, 128)
     cinza : (128, 128, 128)

     A cor mais proxima de (192, 168, 45) foi amarelo
     A cor mais proxima de (92, 10, 20) foi vermelho
     A cor mais proxima de (2, 168, 75) foi verde
     A cor mais proxima de (21, 178, 57) foi verde

     Digite o nome do arquivo contendo uma imagem: figs/ime.jpg
     Carreguei a imagem figs/ime.jpg que tem 160 linhas e 230 colunas
     >>> Aperte 'enter' para continuar...
     >>> Aperte 'enter' para continuar...
     A nova imagem foi salva em saida.jpg.
         FIM
     '''
    
     cores = {
            
        'vermelho':(128,0,0),
        'verde':(0,128,0),
        'amarelo':(128, 128, 0),
        'azul':(0,0,128),
        'cinza':(128, 128, 128)
        
        }
     
     palete = Palete(cores)
     print("Palete: ")
     print(palete)
     
     valores = [

          (128,1,2),(5,69,8),(192,36,85)
 
           ]
 

     for cor in valores:
         print("A cor mais proxima de %s foi %s"%(cor, palete.mais_proxima(cor)))
     print()

  #   teste da aplicação da palete
     nome_imagem = input("Digite o nome do arquivo contendo uma imagem: ")
        
     img = Image.open( nome_imagem )
     width, height = img.size
     print ("Carreguei a imagem %s que tem %d linhas e %d colunas"%(nome_imagem, height, width))
     img.show()
     pause()

     nova = palete.converte_imagem(img)
     nova.show()
     pause()
     nova.save("saida.jpg")
     print("A nova imagem foi salva em saida.jpg.\n    FIM")

#########################################################################
#
# Função main para teste da função k_medias
#    
    
def pause():
    '''
    '''
    input(">>> Aperte 'enter' para continuar...")


   
#########################################################################
#
#   FIM
#
#########################################################################


#########################################################################

if __name__ == "__main__":
    meus_testes()
