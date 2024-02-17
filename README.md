# VendingMachineSimulator (VMS)

## Overview
The VendingMachineSimulator (VMS) project emulates a drink vending machine. It consists of one module (`vending_machine_simulator.py`) where all related classes, attributes, and methods are stored. Metaphorically, the module VMS can be considered as a "server". The classes included in the VMS are:

1. **MaterialsContainersDispenser**: Manages the materials (drink ingredients) containers of the vending machine.
2. **AcceptedCoinsDispenser**: Related to the payment of drinks with coins.
3. **DrinksMenu**: Deals with the drinks that clients can purchase through the vending machine.
4. **VendingMachineOperations**: Manages customer orders, payment checkout, making the drink, and takeout the ingredients consumed.
5. **VendingMachineFinancials**: Manages revenues and financial statistics.
6. **DrinksBusinessMaintenance**: Manages all background maintenance operations.

## Test Approach
The testing approach utilizes the Python `unittest` module, with a specific test file for each class of Module VMS. Metaphorically, each test file can be considered as a "client" of Module VMS, acting as a "server". To minimize "hard-coding", a module named `test_vending_machine_simulator_tests_datasets` was created, containing the real data for the variables used in the tests. This dataset module is imported in each test file.

Unitary tests for `MaterialsContainersDispenser`, `AcceptedCoinsDispenser`, and `DrinksMenu` passed without failures. The corresponding test files are available in this repository for reference.

## Test Failures
The `unittest` based test file `test_vending_machine_operations`, related to class `VendingMachineOperations`, systematically fails when the method `check_drink_availability` is invoked. To narrow the scope of the problem, the file `test_check_availability` was created, but the direct coding approach also fails.

## Investigation Findings
By setting breakpoints just before invoking `drink_check_availability` and another breakpoint at the beginning of the method, PyCharm provided a snapshot of the data structures. This information is stored in the file `VMS_test_check_availability_pycharm_snapshots.txt` also available in this repository. It shows that `test_check_availability` correctly fills the data structures, but they are lost (all the data structures are empty) at the `check_drink_availability` method.

> To check if PyCharm could interfere in this process, the tests were migrated to Visual Studio Code, but the `check_availability` test failures persisted. Further investigation is ongoing to identify the root cause of this issue.

## Test Setup

You just need to create a Python environment with the following three file .py files:
1. **`vending_machine_simulator.py`**
2. **`test_vending_machine_simulator_tests_datasets.py`**
3. **`test_check_availability.py`**
> Then run the test file to trigger the method.
