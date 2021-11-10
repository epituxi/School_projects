def get_file():
    file_name = input("Enter the name of the file containing your exercise diary:\n")
    return file_name

def open_file(file_name):
    try:
        tempfile = open(file_name, "r")
        return tempfile
    except:
        print(f"Error in reading the file '{file_name}'. Program ends.")


def main():

    x = False
    d = True

    minutes_spent = 0
    number_of_days = 0

    file_name = get_file()
    tempfile = open_file(file_name)
    if tempfile != None:
        sport = input("What sport are you interested in?\n")
        print("{:<11}{:<}".format("Day", "Time"))
        for i in tempfile:
            if sport in i:

                i = i.rstrip()
                current_line = i.split(",")

                try:
                    print("{:<11}{:<} min".format(current_line[0], int(current_line[2])))
                    x = True
                    d = True
                except ValueError:
                    print(f"Incorrect time in the file '{file_name}'. Program ends.")
                    x = False
                    d = False
                    break

                minutes_spent += int(current_line[2])
                number_of_days += 1
        if x == True:
            hours_spent = minutes_spent / 60
            hours = int(hours_spent)
            minutes = (minutes_spent) % 60
            print("-" * 31)
            print(f"Total exercise time: {hours} h {minutes} min")
            print(f"Number of exercise days: {number_of_days}")
        if x == False and d == True:
            print(f"The sport '{sport}' was not found in the file.")

main()
