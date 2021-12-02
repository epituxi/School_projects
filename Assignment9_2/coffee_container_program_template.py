# Y1 AUTUMN 2021
# Basic Course in Programming Y1
# Author: Joel Lahenius, modified by Veera Laine
# Template for Exercise 9.2 Coffee containers

from container import LiquidContainer

def main():
    # Ask the names and volumes of the containers according to the example runs and
    # create three containers: large coffee cup, small coffee cup, and coffee jug.

    big_cup_input = input("Big coffee cup name and volume: ")
    big_cup_list = big_cup_input.split("/")
    description = big_cup_list[0]
    volume = float(big_cup_list[1])
    has_lid = False
    big_coffee_cup = LiquidContainer(description, volume, has_lid)
    
    small_cup_input = input("Small coffee cup name and volume: ")
    small_cup_list = small_cup_input.split("/")
    description = small_cup_list[0]
    volume = float(small_cup_list[1])
    has_lid = False
    small_coffee_cup = LiquidContainer(description, volume, has_lid)

    coffee_jug_input = input("Coffee jug name and volume: ")
    coffee_jug_list = coffee_jug_input.split("/")
    description = coffee_jug_list[0]
    volume = float(coffee_jug_list[1])
    has_lid = True
    coffee_jug = LiquidContainer(description, volume, has_lid)
 
    print("Created the following containers:")
    # Print here the statuse of the three created coffee containers
    print(f"{big_coffee_cup.get_name()} - Filled {big_coffee_cup.get_liquid_volume():.2f} out of {big_coffee_cup.get_total_volume():.2f} litres ({big_coffee_cup.get_fill_percentage():.0f} %)")
    print(f"{small_coffee_cup.get_name()} - Filled {small_coffee_cup.get_liquid_volume():.2f} out of {small_coffee_cup.get_total_volume():.2f} litres ({small_coffee_cup.get_fill_percentage():.0f} %)")
    print(f"{coffee_jug.get_name()} (lidded) - Filled {coffee_jug.get_liquid_volume():.2f} out of {coffee_jug.get_total_volume():.2f} litres ({coffee_jug.get_fill_percentage():.0f} %)")

    # Fill the format with the jug name" 
    print("\nFilling {:s}...".format(coffee_jug.get_name()))
    # Fill here the coffee jug
    
    coffee_jug.fill()
    
    print("Jug status after filling:")
    # Print here the status of the coffee jug

    print(f"{coffee_jug.get_name()} (lidded) - Filled {coffee_jug.get_liquid_volume():.2f} out of {coffee_jug.get_total_volume():.2f} litres ({coffee_jug.get_fill_percentage():.0f} %)")
    
    amount_to_be_served = float(input("\nHow many litres of coffee should be served?\n"))

    # Fill the format. Sould print "Trying to pour [amount to be served] litres from [jug name] into [big cup name] and [small cup name]"
    print("Trying to pour {} litres from {} into {} and {}".format(amount_to_be_served, coffee_jug.get_name(), big_coffee_cup.get_name(), small_coffee_cup.get_name())) 
    
    # Pour here the coffee from the jug first to the big cup and then to small cup

    b = coffee_jug.pour_to_another(big_coffee_cup, amount_to_be_served)
    second_serve = coffee_jug.pour_to_another(small_coffee_cup, amount_to_be_served)

    # Print the amounts of the coffee poured in each container, i.e., fill the format
    print("Managed to pour {} litres to {}".format(b, big_coffee_cup.get_name()))
    print("Managed to pour {} litres to {}".format(second_serve, small_coffee_cup.get_name()))
  
    print("\nCup and jug statuses after pouring:") 
    # Print here the statuses of the containers
    
    print(f"{big_coffee_cup.get_name()} - Filled {big_coffee_cup.get_liquid_volume():.2f} out of {big_coffee_cup.get_total_volume():.2f} litres ({big_coffee_cup.get_fill_percentage():.0f} %)")
    print(f"{small_coffee_cup.get_name()} - Filled {small_coffee_cup.get_liquid_volume():.2f} out of {small_coffee_cup.get_total_volume():.2f} litres ({small_coffee_cup.get_fill_percentage():.0f} %)")
    print(f"{coffee_jug.get_name()} (lidded) - Filled {coffee_jug.get_liquid_volume():.2f} out of {coffee_jug.get_total_volume():.2f} litres ({coffee_jug.get_fill_percentage():.0f} %)")
    

    # Check whether both cups got the same amount of coffee, i.e. fill the if clause
    if big_coffee_cup.get_liquid_volume() == small_coffee_cup.get_liquid_volume():
        print("\nBoth were happy for having the same amount of coffee and lived happily everafter.")
    else:
        # Fill the format with the name of the small cup.
        print("\nThe holder of {} became angry for having less coffee and flipped their coffee cup!".format(small_coffee_cup.get_name()))
        
        # Flip here the small cup
        small_coffee_cup.flip()

        print("\nThey also flipped the jug!")
        # Flip here the coffee jug
        coffee_jug.flip()
        
        print("However, it had a lid, so the liquid stayed inside:")
        # Print here the status of the coffee jug
        print(f"{coffee_jug.get_name()} (lidded) - Filled {coffee_jug.get_liquid_volume():.2f} out of {coffee_jug.get_total_volume():.2f} litres ({coffee_jug.get_fill_percentage():.0f} %)")

        print("\nSo they had to force flip to the jug!")
        # Force flip here the coffee jug
        coffee_jug.force_flip()
        
        print("Now it's empty and no longer has a lid:")
        # Print here the status of the coffee jug
        print(f"{coffee_jug.get_name()} - Filled {coffee_jug.get_liquid_volume():.2f} out of {coffee_jug.get_total_volume():.2f} litres ({coffee_jug.get_fill_percentage():.0f} %)")

        # Fill the format with the name of the big cup
        print("\nNext they got mad and nicked all the coffee they could from {}".format(big_coffee_cup.get_name()))

        # Pour here as much coffee as possible from the large cup to the small cup
        a = big_coffee_cup.pour_to_another(small_coffee_cup, small_coffee_cup.get_available_volume())

        # Fill the format with the stolen amount
        print("{} litres were stolen.".format(a))
       
        print("\nCup statuses after the theft:")
        # Print here the status of the big and small cup
        print(f"{big_coffee_cup.get_name()} - Filled {big_coffee_cup.get_liquid_volume():.2f} out of {big_coffee_cup.get_total_volume():.2f} litres ({big_coffee_cup.get_fill_percentage():.0f} %)")
        print(f"{small_coffee_cup.get_name()} - Filled {small_coffee_cup.get_liquid_volume():.2f} out of {small_coffee_cup.get_total_volume():.2f} litres ({small_coffee_cup.get_fill_percentage():.0f} %)")

        # Fill the format with the name of the small cup
        print("\nNow finally the holder of {} can drink their coffee:".format(small_coffee_cup.get_name()))
        # Empty here the small cup
        small_coffee_cup.flip()

        # Print here the status of the small cup
        print(f"{small_coffee_cup.get_name()} - Filled {small_coffee_cup.get_liquid_volume():.2f} out of {small_coffee_cup.get_total_volume():.2f} litres ({small_coffee_cup.get_fill_percentage():.0f} %)")
main()
