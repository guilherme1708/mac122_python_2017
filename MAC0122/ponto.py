'''Questão 1 da lista 1 - MAC0122'''


class Ponto:
    
    def __init__(self, x= 0.0, y=0.0):
        
        self.x = x
        self.y = y
        
    def distancia_para_ponto(self,other):
        
        return ((self.x- other.x)**2 + (self.y - other.y)**2)**(1/2)
        
    def distancia_para_origem(self):
        
        return (self.x**2 + self.y**2)**(1/2)
        
    def inclinacao(self):
        
        if self.y != 0 and self.x != 0:
            return (self.y/self.x)
        
    def reta_para(self, other):

        a = ((other.y - self.y)/(other.x - self.x))    
        b = self.y - a*self.x
        
        return (a,b)
    
    def __str__(self):
        
        return '(%.2f,%.2f)' % (self.x, self.y)
        
    def __add__(self, other):
        
        soma_px = self.x + other.x
        soma_py = self.y + other.y

        return Ponto(soma_px, soma_py)
    
    def __sub__(self,other):
        
        sub_px = self.x - other.x
        sub_py = self.y - other.y

        return Ponto(sub_px, sub_py)
        
    def __eq__(self,other):
        
        if self.x == other.x and self.y == other.y:
            return True
        return False
        
    
    