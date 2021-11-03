import random

def amount_of_doors():
    while True:
        number_of_doors = int(input("How many doors?\n"))
        if 3 <= number_of_doors <= 999:
            return number_of_doors
        print("The number of doors must be between 3-999!")

def door_choice(number_of_doors):
    while True:
        choice = int(input(f"\nChoose a door 1-{number_of_doors}.\n"))
        if 1 <= choice <= number_of_doors:
            return choice
        

def initialize_doors(number_of_doors):
    # Implement your code here
    true_door = random.randint(0, number_of_doors - 1)

    boolean_list = [False for i in range(number_of_doors - 1)]
    boolean_list.insert(true_door, True)
    
    return boolean_list

def remove_wrong_doors(chosen_door, doors):
    # Implement your code here
    pass

def print_doors(doors, dont_open):
    # Implement your code here
    number_of_doors = len(doors)
    door_number_list = [n for n in range(1, number_of_doors + 1)]
    print(" _  " * number_of_doors)
    print("| | " * number_of_doors)
    print("|_| " * number_of_doors)
    for i in range(number_of_doors):
        print("{:^3.0f} ".format(i + 1), end="")
    pass

def main():
    seed = int(input("Set seed:\n"))
    random.seed(seed)
    # Implement your code here
    dont_open = 0
    number_of_doors = amount_of_doors()
    doors = initialize_doors(number_of_doors)
    door_printer = print_doors(doors, dont_open)
    chosen_door = door_choice(number_of_doors)
    print(f"You chose the door number {chosen_door}.\n...")


main()
