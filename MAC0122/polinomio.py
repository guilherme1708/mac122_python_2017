class Polinomio:
	def __init__(self, grau, coef):
		self.grau = grau
		self.coef = coef[:]

	def __str__(self):
		'''(Polinomio) -> string'''
		texto, j = "", 0
		for i in range(self.grau + 1):
			if self.coef[i] == 0:
				continue
			j += 1
			if j > 1:
				if self.coef[i] < 0:
					texto += " - "
				else:
					texto += " + "
			elif self.coef[i] < 0:
				texto += "- "
			if i == 0:
				texto += "%.1f" %(abs(self.coef[i]))
			elif i == 1:
				texto += "%.1fx" %(abs(self.coef[i]))
			else:
				texto += "%.1fx^%d" %(abs(self.coef[i]), i)
		return texto

	def derive(self):
		'''(Polinomio) -> Polinomio'''
		lista = []
		for i in range(1, self.grau + 1):
			lista.append(self.coef[i]*i)
		return Polinomio(self.grau - 1, lista)

	def calc(self, x):
		'''(Polinomio) -> float'''
		y = 0
		for i in range(self.grau + 1):
			y += self.coef[i]*(x**i)
		return y

def main():
	#leia k e os k coeficientes
	k = int(input("Digite k: "))
	lista = []
	for i in range(k+1):
		lista.append(float(input("coeficiente a%d: "%(i))))
	
	p0 = Polinomio(k, lista)
	print("\nP(x) = ", p0)
	p1 = p0.derive()
	print("P'(x) = ", p1)
	p2 = p1.derive()
	print("P''(x) = ", p2)

	#leia n
	n = int(input("\nDigite n: "))
	for i in range(n):
		x = float(input("\nDigite x%d: "%(i)))
		print("P(%.1f) = %.2f"%(x, p0.calc(x)))
		print("P'(%.1f) = %.2f"%(x, p1.calc(x)))
		print("P''(%.1f) = %.2f"%(x, p2.calc(x)))

if __name__ == "__main__":
	main()