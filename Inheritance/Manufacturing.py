class Manufacturing:
	def __init__(self, raw_material_product_name, raw_material_ratio_quantity_value, finished_product_name):
		self.raw_material_product_name = raw_material_product_name
		self.raw_material_ratio_quantity_value = raw_material_ratio_quantity_value
		self.finished_product_name = finished_product_name
		self.available_raw_material = 0
		self.available_finished_product = 0

	# adds purchase quantity to available quantity
	def purchase_raw_material(self, purchase_quantity):
		self.available_raw_material += purchase_quantity
		print(f"Purchase complete. now you have {self.available_raw_material} {self.raw_material_product_name}.")

	# adds finished product quantity
	def produce(self, production_quantity):
		required_material = self.raw_material_ratio_quantity_value * production_quantity

		if required_material > self.available_raw_material:  # if raw material is not enough
			print(f"Not enough raw material available to produce the product, please do the purchase of raw material.")
			print(f"you have {self.available_raw_material} {self.raw_material_product_name} and still need {required_material-self.available_raw_material} more to produce a total of {production_quantity} {self.finished_product_name}.")
		else:
			self.available_finished_product += production_quantity  # increase finished product
			self.available_raw_material -= required_material  # decrease raw material
			print(f"Production Complete. now you have {self.available_finished_product} {self.finished_product_name}")
			if self.available_raw_material == 0:  # if raw material is finished
				print(f"You have used-up all raw material, please do purchase raw material.")
		print()

	# prints raw material stock
	def display_raw_material_stock(self):
		print()
		print("{:<10}{:<25}{:<25}".format('No.', 'Raw Material', 'Raw Material Quantity'))
		print('='*60)
		print("{:<10}{:<25}{:<25}".format('No.', self.raw_material_product_name, self.available_raw_material))
		print()

	# prints finished product stock
	def display_finished_product_stock(self):
		print()
		print("{:<10}{:<25}{:<25}".format('No.', 'Finished Product', 'Finished Product Quantity'))
		print('=' * 60)
		print("{:<10}{:<25}{:<25}".format('No.', self.finished_product_name, self.available_finished_product))
		print()
