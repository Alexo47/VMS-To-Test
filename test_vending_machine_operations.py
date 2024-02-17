import unittest
from unittest.mock import patch
from vending_machine_simulator import MaterialsContainersDispenser
from vending_machine_simulator import DrinksMenu
from vending_machine_simulator import VendingMachineOperations
import test_vending_machine_simulator_tests_datasets as data



class TestVendingMachineOperations(unittest.TestCase):

    def setUp(self) -> None:
        self.dispenser = MaterialsContainersDispenser()
        self.drinks_menu = DrinksMenu()
        self.vmo = VendingMachineOperations()

    def test_check_drink_availability(self):
        self.assertTrue(self.dispenser.allocate_material_container(data.mat1, data.mat1_capacity))
        self.assertTrue(self.dispenser.allocate_material_container(data.mat2, data.mat2_capacity))
        self.assertTrue(self.dispenser.allocate_material_container(data.mat3, data.mat3_capacity))
        self.assertTrue(
            self.drinks_menu.add_drink(
                data.drink1, data.drink1_price, data.drink1_bom, data.drink1_command_valid
            )
        )
        self.assertTrue(self.dispenser.refill_material_container(data.mat1))
        self.assertTrue(self.dispenser.refill_material_container(data.mat2))
        self.assertTrue(self.dispenser.refill_material_container(data.mat3))
        self.assertTrue(self.vmo.check_drink_availability(data.drink1))
        self.assertFalse(self.vmo.check_drink_availability(data.drink2))
        self.assertTrue(
            self.dispenser.takeout_material_container(data.mat1, data.drink1_bom[data.mat1])
        )
        self.assertTrue(
            self.dispenser.takeout_material_container(data.mat2, data.drink1_bom[data.mat2])
        )
        self.assertTrue(
            self.dispenser.takeout_material_container(data.mat3, data.drink1_bom[data.mat3])
        )
        self.assertEqual(
            self.dispenser.get_capacity_material_container(data.mat2), data.mat2_capacity
        )
        self.assertFalse(self.vmo.check_drink_availability(data.drink1))
    
    @patch(
        'builtins.input', side_effect=[data.drink1_command_valid]
    )  # Mock user input
    
    def test_ask_user_drink_valid(self, mocked_input):
        self.assertTrue(self.dispenser.allocate_material_container(data.mat1, data.mat1_capacity))
        self.assertTrue(self.dispenser.allocate_material_container(data.mat2, data.mat2_capacity))
        self.assertTrue(self.dispenser.allocate_material_container(data.mat3, data.mat3_capacity))
        self.assertTrue(
            self.drinks_menu.add_drink(
                data.drink1, data.drink1_price, data.drink1_bom, data.drink1_command_valid
            )
        )
        self.assertTrue(self.dispenser.refill_material_container(data.mat1))
        self.assertTrue(self.dispenser.refill_material_container(data.mat2))
        self.assertTrue(self.dispenser.refill_material_container(data.mat3))
        self.assertTrue(self.vmo.check_drink_availability(data.drink1))
        self.assertEqual(self.vmo.ask_user_drink(), data.drink1)
    
    @patch(
        'builtins.input', side_effect=[data.drink1_command_invalid]
    )  # Mock user input
    
    def test_ask_user_drink_invalid(self, mocked_input):
        self.assertTrue(self.dispenser.allocate_material_container(data.mat1, data.mat1_capacity))
        self.assertTrue(self.dispenser.allocate_material_container(data.mat2, data.mat2_capacity))
        self.assertTrue(self.dispenser.allocate_material_container(data.mat3, data.mat3_capacity))
        self.assertTrue(self.drinks_menu.add_drink(
            data.drink1, data.drink1_price, data.drink1_bom, data.drink1_command_valid)
        )
        self.assertTrue(self.dispenser.refill_material_container(data.mat1))
        self.assertTrue(self.dispenser.refill_material_container(data.mat2))
        self.assertTrue(self.dispenser.refill_material_container(data.mat3))
        self.assertTrue(self.vmo.check_drink_availability(data.drink1))
        self.assertNotEqual(self.vmo.ask_user_drink(), data.drink1)


if __name__ == '__main__':
    unittest.main()