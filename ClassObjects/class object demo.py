class Animal:
	def walk(self):
		print("walking")

	def eat(self):
		print("eating")


class Dog(Animal):
	def __init__(self, name='Dog'):
		self.name = name

	def bark(self):
		print(f"{self.name} is barking")


obj = Animal()
obj.walk()

obj2 = Dog()
obj2.bark()

