class Complex():
	def __init__(self,real,imaginary):
		self.real = real
		self.imaginary = imaginary
		
	def __add__(self,other):
		real_sum = self.real + other.real
		imaginary_sum = self.imaginary + other.imaginary
		return Complex(real_sum,imaginary_sum)
	
	def __str__(self):
			return f"{self.real} + i{self.imaginary}"


a,b,c,d = map(int,input().split())
		
complex1 = Complex(a,b)
complex2 = Complex(c,d)
		
sum_result = complex1 + complex2
print(sum_result)