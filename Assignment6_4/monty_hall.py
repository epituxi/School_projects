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
    doors_list = [i + 1 for i in range(len(doors))]
    doors_dict = {doors_list[i]: doors[i] for i in range(len(doors))}
    chosen_value = doors_dict.get(chosen_door)
    if chosen_value == True:
        while True:
            x = random.randint(1, len(doors))
            if x != chosen_value:
                return x
            else:
                 x = random.randint(1, len(doors))
    if chosen_value == False:
        i = [str(k) for k, v in doors_dict.items() if v == True]
        a = "".join(i)
        b = int(a)
        return b

def print_doors(doors, dont_open):
    # Implement your code here
    number_of_doors = len(doors)
    if dont_open == 0:
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
    chosen_door = 0
    number_of_doors = amount_of_doors()
    doors = initialize_doors(number_of_doors)
    print_doors(doors, chosen_door)
    chosen_door = door_choice(number_of_doors)
    print(f"You chose the door number {chosen_door}.\n")
    wrong_door = remove_wrong_doors(chosen_door, doors)
    print(wrong_door)



main()
