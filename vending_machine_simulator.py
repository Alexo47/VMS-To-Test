"""
Vending Machine Simulator - version 20240210 v09
=> This Module handles all classes/methods/attributes related to drink vending machines operations

It consists of the following elements:

### class MaterialsContainersDispenser:
	=> This class handles the coins_dispenser of containers where each container is associated to a
	specific material (~ingredient such as coffee, water, milk, ...)
	
	## attributes:
		materials_containers dictionary with the following structure:
		{'material name string':  {'capacity': value , 'volume': value}}
	
	## methods:
		def exist_material_container(self, material):
		def allocate_material_container(self, material, capacity)
		def get_capacity_material_container(self, material):
		def get_volume_material_container(self, material):
		def refill_material_container(self, material):

### class AcceptedCoinsDispenser:
	=> This class is related to the payment of drinks with coins (no credit cards in this version)
	
	## attributes:
		accepted coins with following structure:
		{coin_name string: coin_value float}
	
	## Methods
		def add_accepted_coin(self, coin, value):
		
### Class Drinks Menu
=> This class deals with the drink coins_dispenser OFFER that clients can purchase
	
	=> attributes:
		drinks_menu is a dictionary with the following structure:
		{drink string:
		{'price': cost of the drink in float,
		'bom': {material name (str): required volume (float), material_name (str): ....}}
		'command': keystrokes to order string}
	
	=> methods:
		def exist_drink(self, drink: str) -> bool:
		def add_drink(self, drink: str, price: float, bom: Dict[str, int], command: str) -> bool:
		def get_drink_price(self, drink: str) -> float:
		def get_drink_bom(self, drink: str) -> Dict[str, int]:
		def get_drink_command(self, drink: str) -> str:
		

### class VendingMachineOperations:
	=> This class manages customer orders, payments...cumulated revenue
	
	## attributes:
		uses objects defined in other classes namely:
		materials_dispenser, drinks_bom, drinks_menu, accepted_coins, business_cumulated_revenue
		
	=> methods:
		def check_drink_availability(self, drink):
		def update_drink_volume(self, drink):
		def reset_revenue(self):
		def add_revenue(self, amount):
		def drink_checkout(self, ordered_drink):
		def ask_user_drink(self):
		def make_drink(self, ordered_drink):
		
### class DrinksBusinessMaintenance:
	=> This class manages all maintenance operations
	it uses materials_dispenser from MaterialsContainersDispensers
	
	=> attributes:
		admin_maintenance_commands is a dictionary with the following structure
			{keystrokes (string): command message (string)}
			
	=> methods:
		def add_admin_command(self, control_command):
		def report_containers_levels(self):
		def refill_all_containers(self):
		
	
	
"""

from datetime import datetime
from typing import Dict, Union


def date_stamp():
	"""
	=> Returns date_stamp for prints
	:return: date_time
	"""
	now = datetime.now()
	date_time = now.strftime("%Y/%m/%d, %H:%M")
	return date_time

# ###################################################################################
# ## ===vending_machine_simulator=> MaterialsContainersDispenser
# ###################################################################################

class MaterialsContainersDispenser:
	"""
	This class manages the materials (drink ingredients) containers of the vending machine
	Each container has a defined 'capacity' and is filled at 'volume' ranging [0:'capacity']
	
	acronym: 'mcd'  # will be used externally to reach it´s class methods
	
	attributes:
		materials_containers dictionary with the following structure:
		{'material name string':  {'capacity': value , 'volume': value}}
		materials_containers is encapsulated by getters methods described below
	
	methods:
		def exist_material_container(self, material):
		def allocate_material_container(self, material, capacity)
		def get_capacity_material_container(self, material):
		def get_volume_material_container(self, material):
		def refill_material_container(self, material):
		def takeout_material_container(self,material, volume):
		
	external methods: None
	
	"""
	
	def __init__(self) -> None:
		# Initialize the Materials dictionary
		self.materials_containers: Dict[str, Dict[str, Union[int, float]]] = {}
		
	
	
	def exist_material_container(self, material: str) -> bool:
		"""
		This method checks if there is a coins_dispenser allocated for a specific material.
		
		:param material: The name of the material to check.
		:return: True if a material_dispenser exists for the material, False otherwise.
		
		external calls:
			self.exist_material_container
		"""
		
		return material in self.materials_containers
	
	def allocate_material_container(self, material: str, capacity: int) -> bool:
		"""
		=> This method adds a new material container to the coins_dispenser
		It checks if the material container does not already exist
		If not it will add the new container with the capacity indicated and sets volume to 0
		
		:param material:  # kind of ingredient
		:param capacity:  # maximum volume container can be filled
		:return: True if container added - False if the material already has a container
		
		external calls:
			self.exist_material_container
		"""
		
		# Check if the material already exists
		if self.exist_material_container(material):
			return False
		# Add the material with the specified maximum quantity
		self.materials_containers[material] = {'capacity': capacity, 'volume': 0}
		return True
	
	def get_capacity_material_container(self, material: str) -> int:
		"""
		=> Get the capacity of the container allocated for a specific material.

		:param material:  # The name of the material to get the capacity of its container.
		:return capacity: # The capacity of the coins_dispenser allocated for the material.
		If the material container does not exist, returns a negative (-1) capacity value.
		
		external calls:
			self.exist_material_container
		"""
		
		if self.exist_material_container(material):
			capacity = self.materials_containers[material]['capacity']
		else:
			capacity = -1
		return capacity
	
	def get_volume_material_container(self, material: str) -> int:
		"""
		=> This method returns the volume of the container allocated for a specific material.
		
		:param material:
		:return volume: The volume of material available on it´s coins_dispenser - If the material does
		not have a coins_dispenser the volume returned is negative number -1
		
		external calls:
			self.exist_material_container
		"""
		
		if self.exist_material_container(material):
			volume = self.materials_containers[material]['volume']
		else:
			volume = -1
		return volume
	
	def refill_material_container(self, material: str) -> int:
		
		"""
		=> This method fills the container for a specified material (~ingredient)
		It does not manage any ingredient refill packs therefore the action is limited
		to set volume = capacity
		
		:param material: indicates what material (ingredient) is to be filled
		:return volume: True if refill operation achieved False otherwise
		
		external calls:
			self.exist_material_container
			self.get_capacity_material_container
		"""
		
		if self.exist_material_container(material):
			
			# the container exist so we set volume = capacity
			self.materials_containers[material]['volume'] = (
				self.get_capacity_material_container(material)
			)
			return True
		
		return False
	
	def takeout_material_container(self, material, draw_volume):
		"""
		Drink order consume materials - This method reduce the volume of a particular material
		:param material:
		:param draw_volume:
		:return: True if withdrawal possible False otherwise
		
		external calls:
			self.exist_material_container
			self.get_volume_material_container
		"""
		if self.exist_material_container(material):
			current_volume = self.get_volume_material_container(material)
			reduced_volume = current_volume - draw_volume
			if reduced_volume < 0:
				return False
			self.materials_containers[material]['volume'] = reduced_volume
			return True
		return False

# ###################################################################################
# ## ===vending_machine_simulator=> Accepted Coins Dispenser
# ###################################################################################

class AcceptedCoinsDispenser:
	"""
	=> This class is related to the payment of drinks with coins (no credit cards in this version)
	
	## attributes:
		accepted coins with following structure:
		{coin_name string: coin_value float}
	
	## Methods
		def exist_accepted_coin(self,coin: str) -> bool:
		def add_accepted_coin(self, coin: str, value: float) -> bool:
		def get_all_coins(self) -> list:
		def get_coin_value(self, coin: str) -> float:
	
	"""
	
	def __init__(self):
		# Initialize coins dictionary
		self.accepted_coins: Dict[str, float] = {}
	
	def exist_accepted_coins(self, coin: str) -> bool:
		"""
		Checks if a 'coin' is registered at the coins_dispenser
		:param coin:
		:return: True if coin is registered otherwise False
		"""
		return coin in self.accepted_coins
	
	def add_accepted_coins(self, coin: str, value: float) -> bool:
		"""
		=> This method adds a new accepted coin if the coin is not yet already accepted
		
		:param coin: name of the coin
		:param value: value in dollar/cents
		:return: True if coin is a new type False if coin already accepted by the coins_dispenser
		
		external calls:
			self.exist_accepted_coins:
		"""
		
		# Check if the coin already exists
		if self.exist_accepted_coins(coin):
			return False
		
		# Add the coin with the specified value
		self.accepted_coins[coin] = value
		return True

	def get_all_coins(self) -> list:
		"""
		Methods returns all the coins names (str) in a list structure
		:return coins_list
		"""
		coin_list = []
		for coin in self.accepted_coins:
			coin_list.append(coin)
		return coin_list


	def get_coin_value(self, coin: str) -> float:
		"""
		Returns value of a coin if the coin is registered otherwise returns -1
		:param coin:  # name of the coin
		:return:  # the value of coin if registered otherwise returns -1
		
		external calls:
			self.exist_accepted_coins:
		"""
		if self.exist_accepted_coins(coin):
			value = self.accepted_coins[coin]
		else:
			value = -1.
		return value
		
		
# ###################################################################################
# ## ===vending_machine_simulator=> Drinks Menu
# ###################################################################################


class DrinksMenu:

	"""
	=> This class deals with the drink coins_dispenser OFFER that clients can purchase
	
	=> attributes:
		drinks_menu is a dictionary with the following structure:
		{drink string:
		{'price': cost of the drink in float,
		'bom': {material name (str): required volume (float), material_name (str): ....}}
		'command': keystrokes to order string}
	
	=> methods:
		def exist_drink(self, drink: str) -> bool:
		def add_drink(
			self,
			drink: str,
			price: float,
			bom: Dict[str, int], command: str
		) -> bool:
		def get_all_drinks(self) -> list:
		def get_drink_price(self, drink: str) -> float:
		def get_drink_bom(self, drink: str) -> Dict[str, int]:
		def get_drink_command(self, drink: str) -> str:
		
	"""
	
	def __init__(self) -> None:
		"""
		Initializes the drinks drinks_menu with an empty dictionary.
		"""
		self.drinks_menu: Dict[str, Dict[str, Union[float, str, Dict[str, int]]]] = {}
	
	
	def exist_drink(self, drink: str) -> bool:
		"""
		Checks if a drink' figures in the drinks_menu

		:param drink: # The name of the drink to check in drinks_menu
		:return: True if 'drink' exists, False otherwise.
		"""
		
		return drink in self.drinks_menu
	
	
	def add_drink(self, drink: str, price: float, bom: Dict[str, int], command: str) -> bool:
		"""
		=> Adds a drink to the drinks_menu (a new drink offer for the customer)
		
		:param drink:  # name of the drink
		:param price: # cost of the drink
		:param bom:  # ingredients composition of the drink
		:param command: keystrokes to order the drink
		:return: True if drink added - False if drink already exists
		
		external calls:
			self.exist_drink:
		"""
		
		# Check if the drink already exists
		
		if self.exist_drink(drink):
			return False
		
		# Add the drink with the specified price, bom and command
		
		self.drinks_menu[drink] = {
			'price': price,
			'bom': bom,
			'command': command
		}
		return True
	
	def get_all_drinks(self) -> list:
		"""
		Methods returns all the drinks names (str) in a list structure
		:return: list of available drinks
		"""
		drink_list = []
		for drink in self.drinks_menu:
			drink_list.append(drink)
		return drink_list
	
	def get_drink_price(self, drink: str) -> float:
		"""
		This method returns the price value (float) of a specified drink.
		If drink not in drinks_menu returns -1
		:param drink:
		:return price:  # Price of the drink or -1 if drink not registered
		
		external calls:
			self.exist_drink:
		"""
		
		if self.exist_drink(drink):
			price = self.drinks_menu[drink]['price']
		else:
			price = -1.
		return price
		
	def get_drink_bom(self, drink: str) -> Dict[str, int]:
		"""
		This method returns the bom {ingredient: volume}  of a specified drink.
		If drink not in drinks_menu returns empty dictionary {}
		:param drink:
		:return bom:  # BOM of the drink or {} if drink not registered

		external calls:
			self.exist_drink:
		
		"""
		
		if self.exist_drink(drink):
			bom = self.drinks_menu[drink]['bom']
		else:
			bom = {}
		return bom
	
	def get_drink_command(self, drink: str) -> str:
		"""
		This method returns the command keystrokes (string) to launch the order
		If drink not in drinks_menu returns -1
		:param drink:
		:return command:  # keystrokes to command the drink or "#" if drink not registered
		
		external calls:
			self.exist_drink:
		"""
		
		if self.exist_drink(drink):
			command = self.drinks_menu[drink]['command']
		else:
			command = '#'
		return command



# ###################################################################################
# ## ===vending_machine_simulator=> Vending Machines Operations
# ###################################################################################

class VendingMachineOperations:
	"""
	This class manages customer orders, payment checkout, making the drink takeout ingredients
	
	attributes:
	
	methods:
		def check_drink_availability(self, drink):
		def ask_user_drink(self):
		def drink_checkout(self, ordered_drink):
		def make_drink(self, ordered_drink):
		
	external methods activated:
		drinks_menu.exist_drink
		drinks_menu.get_drink_price
		drinks_menu.get_drink_bom
		materials_dispenser.exist_material_container
		materials_dispenser.get_volume_material_container
		accepted_coins.get_all_coins
		accepted_coins.get_coin_value
		
		
		
	"""
	
	
	def __init__(self) -> None:
		# Create instances of other classes
		self.materials_dispenser = MaterialsContainersDispenser()
		self.drinks_menu = DrinksMenu()
		self.accepted_coins = AcceptedCoinsDispenser()

	
	def check_drink_availability(self, ordered_drink: str) -> bool:
		"""
		Checks if all ingredients are available to make the ordered_drink
		:param ordered_drink:
		:return: True if the ordered_drink can be made False otherwise
		
		external methods activated:
			drinks_menu.exist_drink
			drinks_menu.get_drink_bom
			materials_dispenser.exist_material_container
			materials_dispenser.get_volume_material_container

		"""
		count_ok = 0
		

		if self.drinks_menu.exist_drink(ordered_drink):
			drink_bom = self.drinks_menu.get_drink_bom(ordered_drink)
			for ingr in drink_bom:
				vol_required = drink_bom[ingr]
				if self.materials_dispenser.exist_material_container(ingr):
					# The ingredient has a container in the dispenser - check volume
					
					vol_available = self.materials_dispenser.get_volume_material_container(ingr)
					if vol_available >= vol_required:
						count_ok += 1
			
			if count_ok == len(drink_bom):
				return True
		return False
	
	def ask_user_drink(self):
		"""
		Scans the Drinks Menu - If drink can be made displays menu choice: price & command
		:return:
		
		external methods activated:
			drinks_menu.get_all_drinks
			drinks_menu.exist_drink
			drinks_menu.get_drink_price
			drinks_menu.get_drink_command
			materials_dispenser.exist_material_container
			materials_dispenser.get_volume_material_container
		"""
		
		drinks_in_menu = self.drinks_menu.get_all_drinks()
		for drink in drinks_in_menu:
			if self.check_drink_availability(drink):
				drink_price = self.drinks_menu.get_drink_price(drink)
				drink_command = self.drinks_menu.get_drink_command(drink)
				print(
					f"Want {drink} for {drink_price} US$?"
					f"then type: {drink_command}"
				)
		user_choice = input("So what is your choice? =?> ")
		print(f"\n===vending_machine_simulator=> You ordered {user_choice}")
		for drink in drinks_in_menu:
			drink_command = self.drinks_menu.get_drink_command(drink)
			if user_choice == drink_command:
				return drink
		# user choice unrecognizable
		drink = '#'
		return drink
	
	def drink_checkout(self, ordered_drink):
		"""

		:param ordered_drink:
		:return:
		
		external methods activated:
			drinks_menu.get_drink_price
			accepted_coins.get_all_coins
			accepted_coins.get_coin_value
			
		"""
		
		drink_price = self.drinks_menu.get_drink_price()
		current_payment = 0
		coins_accepted = self.accepted_coins.get_all_coins()
		for coin in coins_accepted:
			number_coins = int(input(f" <{coin}> : How many?"))
			coin_value = self.accepted_coins.get_coin_value(coin)
			current_payment += coin_value * number_coins
			if drink_price <= current_payment:
				change = current_payment - drink_price
				print(f" You are all set for your <{ordered_drink}> and your change is <{change}>")
				return True
		
		# at this level the user introduced an insufficient amount to pay for his ordered_drink
		change = current_payment
		print(
			f" {current_payment} is insufficient for your"
			f"<{ordered_drink}> that costs: <{drink_price}"
			f" Here is your change: {change}"
		)
		return False
	
	def make_drink(self, ordered_drink):
		"""
		Drink consumption requires ingredients, this method reduces volume accordingly to drink_bom
		:param ordered_drink:
		:return:
		
		external methods activated:
			drinks_menu.exist_drink
			drinks_menu.get_drink_price
			drinks_menu.get_drink_bom
			materials_dispenser.exist_material_container
			materials_dispenser.takeout_material_container
		"""
		if self.drinks_menu.exist_drink(ordered_drink):
			drink_bom = self.drinks_menu.get_drink_bom(ordered_drink)
			for ingr in drink_bom:
				vol_required = drink_bom[ingr]
				if self.materials_dispenser.exist_material_container(ingr):
					# The ingredient has a container in the dispenser - check volume
					new_volume = self.materials_dispenser.takeout_material_container(
						ingr, vol_required
					)
					if new_volume < 0:  # program error make_drink should not have been activated
						return False
			return True
		return False
	
	# ###################################################################################
	# ## ===vending_machine_simulator=> Vending Machines Financials
	# ###################################################################################
	
class VendingMachineFinancials:
	"""
	Manages revenues and financial statistics
	attributes:
		vending_machine_revenue  # float value of cumulated payments of drinks ordered
	methods:
		def reset_revenue(self):
		def add_revenue(self, amount: float):
		def get_current_revenue(self) -> float:
	"""
	
	def __init__(self):
		self.vending_machine_revenue: float = 0.0
	
	
	def reset_revenue(self):
		"""
		Starts Vending Machine new business cycle
		"""
		self.vending_machine_revenue = 0
	
	def add_revenue(self, amount: float):
		"""
		User consumed a drink - the payment is added to the vending_machine_revenue
		:param amount:  # it corresponds to the drink price the user order
		"""
		self.vending_machine_revenue += amount
		
	def get_current_revenue(self) -> float:
		return self.vending_machine_revenue
	
		
	
	
	
	
	
# ###################################################################################
# ## ===vending_machine_simulator=> Drinks Business Maintenance
# ###################################################################################


class DrinksBusinessMaintenance:
	# TODO Fully encapsulate DrinksBusinessMaintenance Class
	"""
	=> This class manages all maintenance operations
	it uses materials_dispenser from MaterialsContainersDispensers
	
	=> attributes:
		admin_maintenance_commands is a dictionary with the following structure
			{keystrokes (string): command message (string)}
			
	=> methods:
		def add_admin_command(self, control_command):
		def report_containers_levels(self):
		def refill_all_containers(self):
			
	"""
	
	def __init__(
			self,
			materials_dispenser
	):
		self.admin_maintenance_commands = {}
		self.materials_dispenser = materials_dispenser
	
	def add_admin_command(self, control_command):
		"""
		
		:param control_command:
		:return:
		"""
		control_command_keystroke, control_command_message = list(control_command.items())[0]
		# print(
		# 	f"\n===DrinksBusinessMaintenance/add_admin_command=> @ {date_stamp()}"
		# 	f"\n parameter control_command: <{control_command}>"
		# 	f"\n variable control_command_keystroke: <{control_command_keystroke} ")

		
		for command in self.admin_maintenance_commands:
			if command == control_command_keystroke:
				print(
					f"\n===DrinksBusinessMaintenance/add_admin_command=> {date_stamp()}"
					f"{control_command_keystroke} already configured in the ContainerDispenser"
				)
				return False
		self.admin_maintenance_commands[control_command_keystroke] = control_command_message
		return True
	
	def report_containers_levels(self):
		"""
		
		:return:
		"""
		time_stamp = date_stamp()
		print(
			f"At this point of time: {time_stamp}"
			f"The Containers are in the following status:"
		)
		for material in self.materials_dispenser:
			material_capacity = self.materials_dispenser[material]['capacity']
			material_volume = self.materials_dispenser[material]['volume']
			# material = materials_available.key()
			# filled = materials_available.value()
			print(
				f" Container of: <{material}> with total capacity of {material_capacity}"
				f" is currently filled at {material_volume} level"
			)
	
	def refill_all_containers(self):
		"""
		
		:return:
		"""
		materials_volume = {}
		for material in self.materials_dispenser.materials_containers:
			volume = self.materials_dispenser.refill_material_container(material)
			materials_volume[material] = volume
		return materials_volume


print(f"\n===vending_machine_simulator=> Class/Methods/Attributes <20240210-v09> @ {date_stamp()}")
