VITAMIN_DICTIONARY = {'A': 800, 'B1': 1200, 'B2': 1300, 'B3': 15000, 'B5': 5000,'B6': 1500, 'B12': 2.0, 'C': 75000, 'D': 10, 'E': 9000}

def vit_input():
    #Input of wanted vitamin.
    desired_vitamin = input("Enter the vitamin.\n")
    
    return desired_vitamin

def get_input():
    #Input of file name
    food_file = input("Enter the name of the food file.\n")

    return food_file

def main():
    food_file = get_input()
    food = food_file.replace('.txt', '')
    vitamin_values = {}
    #File readability check
    try:
        temp_file = open(food_file, "r")
        #Creates a dictionary of all the vitamins in the file with error checks
        for line in temp_file: 
            line = line.rstrip()

            try:
                parts = line.split(" ")

            except:
                pass

            if len(parts) != 2:
                pass

            else:
                vitamin_type = parts[0]

                try:
                    amount = float(parts[1])
                    vitamin_values[vitamin_type] = amount

                except:
                    print(f"Invalid amount of vitamin {vitamin_type}.")

        desired_vitamin = vit_input()
        #Checks if vitamin is valid
        if desired_vitamin in vitamin_values.keys() and desired_vitamin in VITAMIN_DICTIONARY.keys():
            for i in vitamin_values.keys():
                #Checks if current key in dictionary is desired vitamin
                if i == desired_vitamin:
                    grams = VITAMIN_DICTIONARY[i] / vitamin_values[i] * 100
                    if grams < 1000:
                        print("You have to eat {:s} {:.1f} grams to reach the daily recommendation of the vitamin {:s}.".format(food, grams, desired_vitamin))
                    else:
                        kilos = grams / 1000
                        print("You have to eat {:s} {:.1f} kilos to reach the daily recommendation of the vitamin {:s}.".format(food, kilos, desired_vitamin))

        elif desired_vitamin not in VITAMIN_DICTIONARY.keys():
            print(f"{desired_vitamin} is an unknown vitamin.")

        else:
            print(f"{food} does not contain any vitamin {desired_vitamin}")

    except:
        print(f"Error in reading {food_file} file.")

main()