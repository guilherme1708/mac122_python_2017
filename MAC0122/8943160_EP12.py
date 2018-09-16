# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: 8943160
    NUSP: Guilherme Navarro

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
HASHTAG    = "#"
DOCSTRING1 = "'''"
DOCSTRING2 = '"""'
NEWLINE    = '\n'

# módulo utilizado para coletar os nomes de arquivos em um diretório
import glob

# inclua outros módulos padrão e qualquer outro que já vem junto do Anaconda.
# caso você necessite de outro módulo, é melhor perguntar no fórum antes de usar.

#########################################################################
#
# Programa 
#

def main():
    ''' 
    Esse é o programa principal. 
    Ele inicialmente lê um diretório dos arquivos.py a serem verificados
    utilizando o módulo glob, em seguida cria uma lista de tamanho n com os
    arquivos encontrados, logo após cria-se uma matriz M de tamanho n x n
    exatamente iniciada com valores 0, posteriormente verifica se um par de ep's   
    são iguais e substitui o valor do par de ep's associado M[lin][col] por 1.0,
    faz-se o mesmo e verifica se um par de ep's são iguais sem os comentários,
    e substitui o valor do par de ep's associado M[lin][col] por 2.0,
    por fim imprime todos os ep's que foram considerados plágio.

    Para usar esse exemplo, crie uma pasta chamada 'testes' no 
    mesmo diretório desse arquivo e coloque alguns arquivos com
    extensão .py dentro dessa pasta.
    '''
    nome_pasta = input("Onde estão os arquivos em Python: ")
    
    # *.py -> A estrela (*) equivale a procurar todos os arquivos .py na pasta
    procurar = nome_pasta + '/*.py'
    print("Onde e o que vou procurar: ", procurar)
    nomes_arquivos = glob.glob(procurar)
    
    n = len(nomes_arquivos)
    print("Achei %d arquivos com extensão .py"%n)
    
    for nome in nomes_arquivos:
        print (nome)

    lista = [] # Lista com os arquivos ja abertos
    lista_aux = [] # Lista com os aqruivos sem os comentários
    M = crie_matriz(n,n)
    cont = 0
    
    # Le todos os arquivos e armazena em uma lista
    for i in range(n):
        candidato = leia_arquivos(nomes_arquivos[i])
        lista.append(candidato)

    # Varre a matriz e verifica se um par de ep's são canditados a plágio
    # e compara se são exatamente iguais, caso mais simples possível de plágio
    for lin in range(n):
        for col in range(lin+1,n):
            candidato1 = lista[lin]
            candidato2 = lista[col]
            if candidato1 == candidato2:
                M[lin][col] = 1.0 
    
    # Le todos os arquivos remove os comntários e armazena em uma lista
    for i in range(n):
        candidato = remove_comentarios(lista[i])
        lista_aux.append(candidato)
        
    # Varre a matriz e verifica se um par de ep's são canditados a plágio
    # e compara se são exatamente iguais sem comentários
    for lin in range(n):
        for col in range(lin+1,n):
            if M[lin][col] != 1.0 :
                candidato1 = lista_aux[lin]
                candidato2 = lista_aux[col]
                if candidato1 == candidato2:
                    M[lin][col] = 2.0 
    
    # Imprime uma mensagem de quais foram os Ep's que foram considerados plágio
    for lin in range(n):
        for col in range(lin+1,n):
            if M[lin][col] != 0:
                cont += 1
                print("\nOs Ep's com plágio, são:",nomes_arquivos[lin],"e", nomes_arquivos[col], "com nível %d" %  M[lin][col])
                
    # Se caso não ter ep's plagiados, imprime uma mensagem       
    if cont == 0:
        print("Não existem Ep's com plágio")


#########################################################################
#
# Função e classes auxiliares
#    
#  Escreva a seguir as funções e classes auxiliares que desejar
#  usar em seu programa.
# ------------------------------------------------------------
def crie_matriz(n_linhas, n_colunas, valor = 0):
    ''' (int, int, valor) -> matriz 
	
    Recebe dois inteiros n_linhas >= 0 e n_colunas >= 0 
    e um valor inicialmente com 0, cria e retorna uma 
    matriz com n_linhas linhas e n_colunas colunas 
    em que cada elemento é igual ao valor dado.
    '''
     
    matriz = []
    
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(valor)
        matriz.append(linha)
        
    return matriz
# ------------------------------------------------------------
def leia_arquivos(nome_arq):
    ''' (arquivo.py) -> lista
    
    Recebe o nome de um aquivo nome_arq e retorna uma lista
    com strings de cada linha do arquivo.
    '''
    
    with open(nome_arq, 'r', encoding='utf-8') as candidato:
        return candidato.readlines()
    
# ------------------------------------------------------------
def remove_comentarios(candidato):
    ''' arquivo.py -> lista
    
    Recebe o nome de um aquivo candidato, cria manipula uma lista
    removendo todos os comentarios retornando uma lista contendo 
    só o código sem comentários.
    '''

    sem_comen = []
    
    # Remove todos os comentátios inicidados com HASHTAG
    for line in candidato:
        if HASHTAG in line:
            indice = line.index(HASHTAG)
            novo = line[:indice]
            if len(novo) < 1:
                continue
            else:
                sem_comen.append(novo + NEWLINE)
        else:
            sem_comen.append(line)

    return sem_comen
        

#########################################################################
#
#   FIM
#
#########################################################################


#########################################################################

if __name__ == "__main__":
    main()