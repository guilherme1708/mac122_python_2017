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

class Horario:
    '''Classe utilizada para representar um horário.

    Um horário é representado por três números inteiros maiores ou iguais
    a zero. Assim, cada objeto dessa classe terá três atributos de estado:
 
       * `h`: um número inteiro entre 0 e 23 que indica horas
       * `m`: um número inteiro entre 0 e 59 que indica minutos
       * `s`: um número inteiro entre 0 e 59 que indica segundos
 
    Você deverá escrever os métodos sugeridos a seguir.
    '''

    #------------------------------------------------------------------------------
    def __init__(self, horas = 0, minutos = 0, segundos = 0):
        '''(Horario, int, int, int) -> None

        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e inteiros não negativos
        
             `horas`, `minutos` e `segundos` que

        indicam um horário a ser representado.

        Exemplos:

        >>> inicio = Horario() # construtor chama __init__()
        >>> inicio.h
        0
        >>> inicio.m
        0
        >>> inicio.s
        0
        >>> t1 = Horario(9)
        >>> print(t1.h, t1.m, t1.s)
        9 0 0
        >>> t2 = Horario(9,40)
        >>> print(t2.h, t2.m, t2.s)
        9 40 0 
        >>> t3 = Horario(9,40,48)
        >>> print(t3.h, t3.m, t3.s)
        9 40 48
        >>> t4 = Horario(24,10,10)
        >>> print(t4.h, t4.m, t4.s)
        0 10 10
        >>> t5 = Horario(25,10,15)
        >>> print(t5.h, t5.m, t5.s)
        1 10 15
        >>> t6 = Horario(0,0,3600)
        >>> print(t6.h, t6.m, t6.s)
        1 0 0
        >>> 
        '''
        self.h = horas
        self.m = minutos
        self.s = segundos
        
        if self.s >= 60:
            minu = self.s // 60
            self.s = self.s % 60          
            if self.s == 0:
                self.m += minu
        if self.m >= 60:
            hora = self.m // 60
            self.m = self.m % 60
            self.h += hora
        if self.h == 24:
            self.h = 0
       
            
        
    #------------------------------------------------------------------------------        
    def __str__(self):
        '''(Horario) -> str

        Recebe uma referencia `self` a um objeto da classe Horario e
        crie e retorna o string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna o string criado pelo métod __str__() da classe  

        Exemplos:

        >>> inicio_aula = Horario(8)
        >>> fim_aula = Horario(9, 40)
        >>> fim_aula.__str__()
        '09:40:00'
        >>> inicio_aula.__str__()# chamada do método __str__()
        '08:00:00'
        >>> str(inicio_aula) # função str() exibe o string criado por __str__()
        '08:00:00'
        >>> fim_aula.__str__()# chamada do método __str__()
        '09:40:00'
        >>> print(inicio_aula) # exibe o string criado por __str__()
        08:00:00
        >>> print(fim_aula)
        09:40:00
        >>>         
        '''
        s = ''
        
        if self.h < 10:
            s += '0%d:'%(self.h)
        else:
            s += '%d:'%(self.h)
        if self.m < 10:
             s += '0%d:'%(self.m)
        else:
            s += '%d:'%(self.m)
        if self.s < 10:
             s += '0%d'%(self.s)
        else:
            s += '%d'%(self.s)
            
        return s
    #------------------------------------------------------------------------------                
    def __eq__(self, other):
        '''(Horario, Horario) -> Horario

        Recebe referencias `self` e `other` a objetos da classe Horario.

        Retorna True se o horário `self` é igual ao horário `other` e
        retorna False em caso contrário.
        
        Este método é utilizado pelo Python quando escrevemos "Horario == Horario".

        Exemplos:
        
        >>> t1 = Horario(8,1,59)
        >>> t2 = Horario(8,1,59)
        >>> print(t1)
        08:01:59
        >>> print(t2)
        08:01:59
        >>> t1.__eq__(t2) # chamada explicita do método __eq__()
        True
        >>> t1 == t2 # python chama __eq__() para testar "=="
        True
        >>> t3 = Horario(8,1,58)
        >>> t1 == t3
        False
        >>> t2 == t3if self.h >= other.h and self.m >= other.m and self.s >= other.s:
            return True
        return False
        False     
        '''
        if self.h == other.h and self.m == other.m and self.s == other.s:
            return True
        return False
    
    #------------------------------------------------------------------------------                
    def __ge__(self, other):
        '''(Horario, Horario) -> Horario

        Recebe referencias `self` e `other` a objetos da classe Horario.

        Retorna True se o horário `self` é igual ou depois do horário `other` e
        retorna False em caso contrário.

        Este método é utilizado pelo Python quando escrevemos "Horario >= Horario".

        Exemplos:

        >>> t1 = Horario(8)
        >>> t2 = Horario(8)
        >>> t3 = Horario(8,0,1)
        >>> print(t1)
        08:00:00
        >>> print(t2)
        08:00:00
        >>> print(t3)
        08:00:01
        >>> t1.__ge__(t2) # chamada explicita do método __ge__()
        True
        >>> t1 >= t2 # Python chama o método __ge__() para testar ">="
        True
        >>> t2 >= t1
        True
        >>> t1 >= t3
        False
        '''
        if self.h >= other.h and self.m >= other.m and self.s >= other.s:
            return True
        return False

    #------------------------------------------------------------------------------                
    def __gt__(self, other):
        '''(Horario, Horario) -> Horario

        Recebe referencias `self` e `other` a objetos da classe Horario.

        Retorna True se o horário `self` é depois do horário representado por `other` e
        retorna False em caso contrário.

        Este método é utilizado pelo Python quando escrevemos "Horario > Horario".

        Exemplos:
        
        >>> t1 = Horario(8)
        >>> t2 = Horario(8)
        >>> t3 = Horario(8,0,1)
        >>> t1 > t2
        False
        >>> t2 > t1
        False
        >>> t1 > t3
        False
        >>> t3 > t1
        True
        >>>         
        '''
        if self.h > other.h:
            return True
        elif self.h == other.h and self.m > other.m:
            return True
        elif self.h == other.h and self.m == other.m and self.s > other.s:
            return True
        return False

    #------------------------------------------------------------------------------                
    def __le__(self, other):
        '''(Horario, Horario) -> Horario

        Recebe referencias `self` e `other` a objetos da classe Horario.

        Retorna True se o horário por `self` é igual ou antes do horário `other` e
        retorna False em caso contrário.

        Este método é utilizado pelo Python quando escrevemos "Horario <= Horario".

        Exemplos:
        
        >>> t1 = Horario(8)
        >>> t2 = Horario(8)
        >>> t3 = Horario(8,0,1)
        >>> t1 <= t2
        True
        >>> t1 <= t3
        True
        >>> t3 <= t1
        False
        >>>         
        '''
        if self.h <= other.h and self.m <= other.m and self.s <= other.s:
            return True
        return False
        
    #------------------------------------------------------------------------------                
    def __lt__(self, other):
        '''(Horario, Horario) -> Horario

        Recebe referencias `self` e `other` a objetos da classe Horario.

        O método retorna True se o horário `self` é antes do horário `other` e
        retorna False em caso contrário.

        Este método é utilizado pelo Python quando escrevemos "Horario < Horario".

        Exemplos:

        >>> t1 = Horario(8)
        >>> t2 = Horario(8)
        >>> t3 = Horario(8,0,1)
        >>> t1 < t2
        False
        >>> t2 < t1
        False
        >>> t1 < t3
        True
        >>>
        '''
        if self.h < other.h:
            return True
        elif self.h == other.h and self.m < other.m:
            return True
        elif self.h == other.h and self.m == other.m and self.s < other.s:
            return True
        return False
        
    #------------------------------------------------------------------------------        
    def __add__(self, other):
        '''(Horario, Horario) -> Horario

        Recebe referencias `self` e `other` a objetos da classe Horario e
        constroi e retorna o horário que é a soma de `self` e `other`.

        Este método é utilizado pelo Python quando escrevemos "Horario + Horario".

        Exemplos:

        >>> t1 = Horario(8,0,0)
        >>> t2 = Horario(1,40)
        >>> print(t1)
        08:00:00
        >>> print(t2)
        01:40:00
        >>> t3 = t1 + t2
        >>> print(t3)
        09:40:00
        >>> t4 = t1 + Horario(0,100)
        >>> print(t4)
        09:40:00
        >>> t5 = Horario(23,59,59)
        >>> t6 = Horario(0,0,1)
        >>> t7 = t5 + t6
        >>> print(t7)
        00:00:00
        >>> t8 = t5.__add__(t6) # chamada explícita ao método __add__()
        >>> print(t8)
        00:00:00
        >>>        
        '''
        soma_s = self.s + other.s
        soma_m = self.m + other.m
        soma_h = self.h + other.h
        
        if soma_s >= 60:
            soma_s -= 60
            soma_m = soma_m + 1
           
        if soma_m >= 60:
            soma_m -= 60
            soma_h = soma_h + 1

        
        soma = Horario(soma_h, soma_m, soma_s)

        return soma
            
    #------------------------------------------------------------------------------                
    def __sub__(self, other):
        '''(Horario, Horario) -> Horario

        Recebe referencias `self` e `other` a objetos da classe Horario e
        constroi e retorna o horário que é a diferença de `self` e `other`.

        Este método é utilizado pelo Python quando escrevemos "Horario - Horario".

        Pré-condição: esse método supõe que o horário `self` é igual ou 
                      depois do horário `other.

        Exemplos:

        >>> t1 = Horario(9,40)
        >>> t2 = Horario(8)
        >>> t1 > t2
        True
        >>> t3 = t1 - t2
        >>> print(t3)
        01:40:00
        >>> t4 = t1.__sub__(t2) # chamada explicita do método __sub__()
        >>> print(t3)
        01:40:00
        >>>         
        '''
        if self.h == 0:
            self.h = 24 
            
        sub_s = self.s - other.s
        sub_m = self.m - other.m
        sub_h = self.h - other.h
            
        if sub_h < 0:
            sub_h = -sub_h
            
        if sub_s < 0:
            sub_s = -sub_s
            sub_m -= 1 
            if self.s == 0:
                sub_s = 60 - other.s
           
        if sub_m < 0:
            sub_m = -sub_m
            sub_h -= 1
        
        sub = Horario(sub_h, sub_m, sub_s)

        return sub
        
    #----------------------------------------------------------------------------
    #
    # Se desejar, você pode escrever métodos auxiliares.
    # Coloque esses métodos a seguir
    #
    #----------------------------------------------------------------------------

