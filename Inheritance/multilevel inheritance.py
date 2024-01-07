class A:
	def hello(self):
		print("Hello, I am from class A")


class B(A):
	def hello(self):
		print("Hello, I am from class B")


class C(B):
	def hello(self):
		print("Hello, I am from class C")
		print("calling super class method")
		super().hello()


class D(C):
	def hello(self):
		print("Hello, I am from class D")
		print("calling super class method")
		super().hello()


class E(D):
	def hello(self):
		print("Hello, I am from class E")
		print("calling super class method")
		super().hello()


obj = E()
obj.hello()
