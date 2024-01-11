from Inheritance.Manufacturing import Manufacturing

finished_product_name = 'Bicycle'  # input("Enter Finished Product Name: ")
raw_material_product = 'Wheels'  # input("Enter Raw Material Product Name: ")
raw_material_ratio_quantity = 2  # int(input(f"How many {raw_material_product} will need to make one {finished_product_name}: "))
print()
obj = Manufacturing(raw_material_product, raw_material_ratio_quantity, finished_product_name)

while True:
	print()
	print(f"{'-' * 35}Menu{'-' * 35}")
	print("1. Purchase Raw Material Product")
	print("2. Manufacture Finished Product")
	print("3. Show Raw Material Quantity")
	print("4. Show Finished Product Quantity")
	print("5. Exit")
	choise = input("Enter your choice: ")

	if choise == '1':
		purchase_quantity = int(input(f"How many {raw_material_product} you want to purchase: "))
		obj.purchase_raw_material(purchase_quantity)
	elif choise == '2':
		production_quantity = int(input(f"How many {finished_product_name} you want to produce: "))
		obj.produce(production_quantity)
	elif choise == '3':
		obj.display_raw_material_stock()
	elif choise == '4':
		obj.display_finished_product_stock()
	elif choise == '5':
		print("Thank you!")
		break
	else:
		print("Invalid input please try again")
