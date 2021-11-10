def get_input():
    name = input("Enter the name of the file containing wind velocities.\n")
    return name

def file_check(file_name):
    try:
        tempfile = open(file_name, "r")
        return tempfile
    except:
        print(f"\nError while reading the '{file_name}' file. Program ends.")

def vel_lst(tempfile):

    velocities_lst = []

    for i in tempfile:
        i = i.rstrip()
        current_line = i.split(",")

        try:
            if current_line[5] in current_line:
                try:
                    add = float(current_line[5])
                    velocities_lst.append(add)
                except:
                    continue
        except:
            continue

    return velocities_lst

def calculate_powers(velocities_list):

    power_lst = []
    p_max = 3450000

    for i in range(len(velocities_list)):
        if 3 <= velocities_list[i] <= 25:
            v = velocities_list[i]
        else:
            v = 0
        p = 8/27 * 1.225 * v ** 3 * 8659
        p = float(p) / 1000
        power_lst.append(p)

    return power_lst

def calculate_capacity_factor(power_list):
    sum_kwh = sum(power_list)
    max_kwh = 3450 * 24
    n_hours = len(power_list)
    day_sum_kwh = (sum_kwh / n_hours) * 24

    net_capacity_multiplier = day_sum_kwh / max_kwh


    return net_capacity_multiplier



def main():

    file_name = get_input()
    tempfile = file_check(file_name)

    if tempfile != None:
        velocities_list = vel_lst(tempfile)
        power_list = calculate_powers(velocities_list)
        net_capacity_multiplier = calculate_capacity_factor(power_list)
        max_power_list = max(power_list)
        sum_power_list = sum(power_list)
        
        print("\nThe maximum power of the wind turbine was %.1f kW." % max_power_list)
        print("The wind turbine generated %.1f kWh of electricity." % sum_power_list)
        print("The capacity factor of the wind turbine was %.3f." % net_capacity_multiplier)
        
main()