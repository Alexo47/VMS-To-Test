from vending_machine_simulator import MaterialsContainersDispenser
from vending_machine_simulator import DrinksMenu
from vending_machine_simulator import VendingMachineOperations
import test_vending_machine_simulator_tests_datasets as data

disp_flags = []
drink_flags = []
dispenser = MaterialsContainersDispenser()
drinks_menu = DrinksMenu()
vmo = VendingMachineOperations()


def test_check_drink_availability():
    disp_flags.append(dispenser.allocate_material_container(data.mat1, data.mat1_capacity))
    disp_flags.append(dispenser.allocate_material_container(data.mat2, data.mat2_capacity))
    disp_flags.append(dispenser.allocate_material_container(data.mat3, data.mat3_capacity))
    drink_flags.append(drinks_menu.add_drink(
            data.drink1, data.drink1_price, data.drink1_bom, data.drink1_command_valid
        )
    )
    disp_flags.append(dispenser.refill_material_container(data.mat1))
    disp_flags.append(dispenser.refill_material_container(data.mat2))
    disp_flags.append(dispenser.refill_material_container(data.mat3))
    drink_flags.append(vmo.check_drink_availability(data.drink1))
    drink_flags.append(vmo.check_drink_availability(data.drink2))
    disp_flags.append(dispenser.takeout_material_container(
        data.mat1, data.drink1_bom[data.mat1]
        )
    )

    disp_flags.append(
        dispenser.takeout_material_container(data.mat2, data.drink1_bom[data.mat2])
    )

    disp_flags.append(dispenser.takeout_material_container(
        data.mat3, data.drink1_bom[data.mat3])
    )
    capacity_mat2 = dispenser.get_capacity_material_container(data.mat2)
    drink_flags.append(vmo.check_drink_availability(data.drink1))
    
    print(f"\n===test_check_drink_availability=> dispenser related flags = {disp_flags}")
    print(f"\n===test_check_drink_availability=> drink related Flags = {drink_flags}")
    print(f"\n===test_check_drink_availability=> capacity_mat2 = {capacity_mat2}")
    
if __name__ == '__main__':
    test_check_drink_availability()
    