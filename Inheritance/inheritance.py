class Base:
	def greet(self):
		print("Hello this is base class")

	def hello(self):
		print("Hello, calling from child class using super")


class Child(Base):
	def greet(self):
		print("Hello this is child class")
		# calling super class
		super().hello()


obj1 = Base()
obj1.greet()
obj2 = Child()
obj2.greet()
