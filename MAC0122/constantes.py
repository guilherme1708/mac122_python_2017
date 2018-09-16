"""
   MAC0122 Principios de Desenvolvimento de Algoritmos
 
   NAO EDITE OU MODIFIQUE NADA QUE ESTA ESCRITO NESTE ARQUIVO
   
   Este arquivo contém apelidos para constantes que são usados 
   nos outros módulos.
"""

## Constantes que você DEVE utilizar em seu programa

# código a ser utilizado para as categorias/tipos de tokens
NUMERO      = 'NUM'
OPERADOR    = 'OP'
VARIAVEL    = 'VAR'

# caractere que indica comentário em expressão
COMENTARIO = '#'

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."

# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em identificadores ou nomes de variáveis
LETRAS  = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# caracteres usados em operadores
OPERADORES = "%*/+-^=" 

# 7 operadores aritméticos  
RESTO_DIVISAO  = "%"
MULTIPLICACAO  = "*"
DIVISAO        = "/"
ADICAO         = "+"
SUBTRACAO      = "-"
EXPONENCIACAO  = "^" # exponeciação

# atribuicao 
ATRIBUICAO     = "=" 

BLOCO       = 'BLC' # novo tipo/categoria

# parenteses são delimitadores de um BLOCO 
PARENTESES = "()" 

# parenteses: para expressões infixas 
ABRE_PARENTESES     = "(" 
FECHA_PARENTESES    = ")" 

# dicionário com a precedência de cada operador
PREC = {
    # 7 operadores aritmético
    EXPONENCIACAO: 5, # da DIREITA  para a ESQUERDA
    RESTO_DIVISAO: 3, # da ESQUERDA para a DIREITA
    MULTIPLICACAO: 3, # da ESQUERDA para a DIREITA
    DIVISAO:       3, # da ESQUERDA para a DIREITA
    ADICAO:        2, # da ESQUERDA para a DIREITA
    SUBTRACAO:     2, # da ESQUERDA para a DIREITA
    
    # atribuicao 
    ATRIBUICAO:    1,  # da DIREITA para a ESQUERDA

    ABRE_PARENTESES: 0 # pode ser conveniente
}