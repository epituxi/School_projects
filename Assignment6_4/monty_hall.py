import random

def amount_of_doors():
    while True:
        number_of_doors = int(input("How many doors?\n"))
        if 3 <= number_of_doors <= 999:
            return number_of_doors
        print("The number of doors must be between 3-999!")

def door_choice(number_of_doors):
    print('')
    while True:
        choice = list(input(f"Choose a door 1-{number_of_doors}.\n"))
        y = "".join(choice)
        x = int(y)
        if 1 <= x <= number_of_doors:
            return choice
        

def initialize_doors(number_of_doors):
    # Implement your code here
    true_door = random.randint(0, number_of_doors - 1)

    boolean_list = [False for i in range(number_of_doors - 1)]
    boolean_list.insert(true_door, True)
    
    return boolean_list

def remove_wrong_doors(chosen_door, doors):
    # Implement your code here

    m = "".join(chosen_door)
    f = int(m)

    doors_list = [i + 1 for i in range(len(doors))]
    doors_dict = {doors_list[i]: doors[i] for i in range(len(doors))}
    chosen_value = doors_dict.get(f)
    if chosen_value == True:
        while True:
            x = [random.randint(1, len(doors))]
            if x != chosen_value:
                return x
            else:
                x = [random.randint(1, len(doors))]
    if chosen_value == False:
        chosen_door = [str(k) for k, v in doors_dict.items() if v == True]
        return chosen_door

def print_doors(doors, dont_open):
    # Implement your code here

    doors_list = [i + 1 for i in range(len(doors))]
    doors_dict = {doors_list[i]: doors[i] for i in range(len(doors))}
    chosen_door = [str(k) for k, v in doors_dict.items() if v == True]

    number_of_doors = len(doors)
    if len(dont_open) >= 2:
        w = int(dont_open[0])
        v = int(dont_open[1])
    elif len(dont_open) == 1:
        w = int(chosen_door[0])


    if len(dont_open) >= 3:
        print(" _  " * number_of_doors)
        print("| | " * number_of_doors)
        print("|_| " * number_of_doors)
        for i in range(number_of_doors):
            print("{:^3.0f} ".format(i + 1), end="")
    elif 3 > len(dont_open) >= 2:
        print(" _  " * number_of_doors)
        for i in range(1, number_of_doors + 1):
            if i == v:
                print("| | ", end="")
            elif i == w:
                print("| | ", end="")
            else:
                print("|G| ", end="")
        print("")
        print("|_| " * number_of_doors)
        for i in range(number_of_doors):
            print("{:^3.0f} ".format(i + 1), end="")
    else:
        c_temp = "".join(chosen_door)
        r_temp = int(c_temp)
        print(" _  " * number_of_doors)
        for i in range(1, number_of_doors + 1):
            if i == r_temp:
                print("|C| ", end="")
            else:
                print("|G| ", end="")
        print("")
        print("|_| " * number_of_doors)
        for i in range(number_of_doors):
            print("{:^3.0f} ".format(i + 1), end="")

def main():
    seed = int(input("Set seed:\n"))
    random.seed(seed)
    # Implement your code here

    number_of_doors = amount_of_doors()
    doors = initialize_doors(number_of_doors)

    dont_open = [i + 1 for i in range(len(doors))]

    print_doors(doors, dont_open)
    chosen_door = door_choice(number_of_doors)
    temp_number_f = "".join(chosen_door)
    temp_number = int(temp_number_f)
    print(f"You chose the door number {temp_number}.\n...")
    dont_open = remove_wrong_doors(chosen_door, doors)
    k = "".join(chosen_door)
    dont_open.append(k)
    q = int(dont_open[0])
    p = int(dont_open[1])
    print_doors(doors, dont_open)
    print(f"\n{len(doors) - 2} certainly wrong doors were opened. The door number {q} was left.")

    while True:
        dont_open = int(input(f"Choose {p} if you want to keep the door you first chose and choose {q} if you want to change the door.\n"))
        if p == dont_open or dont_open == q:
            trr = dont_open
            asddsa = str(dont_open)
            yeee = list(asddsa.split(" "))
            break

    print_doors(doors, yeee)

    doors_list = [i + 1 for i in range(len(doors))]
    doors_dict = {doors_list[i]: doors[i] for i in range(len(doors))}
    chosen_door = [str(k) for k, v in doors_dict.items() if v == True]
    i_j = "".join(chosen_door)
    int_i_j = int(i_j)

    if trr == int_i_j:
        print("\nCongratulations! The car was behind the door you chose!")
    else:
        print("\nA goat emerged from the door you chose! The car was behind the other door :(")

main()