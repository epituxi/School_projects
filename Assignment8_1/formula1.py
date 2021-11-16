def main():
    name = input("Enter a filename:\n")
    laptimes = {}
    try:
        resultfile = open(name, "r")
        for line in resultfile:
            line = line.rstrip()
            parts = line.split(":")
            if len(parts) != 2:
                print("ERROR in line:", line)
            else:
                driver = parts[0]
                try:
                    time = float(parts[1])
                    # COMPLETE: update the dictionary laptimes when needed.
                    if driver in laptimes:
                        current_time = laptimes[driver]
                        if current_time <= time:
                            pass
                        else:
                            laptimes[driver] = time
                    else:
                        laptimes[driver] = time
                except ValueError:
                    print("ERROR: incorrect lap time:", parts[1])
        resultfile.close()
        # Output the best lap times.
        if laptimes == {}:
            print("The file did not contain any correct lap times.")
        else:
            print("Results")
            print("Driver                Time (s)")
            drivers = sorted(laptimes)
            for driver in drivers:
                #print(f'{driver:22}{laptimes[driver]:.3f}')
                print("{:22s}{:.3f}".format(driver, laptimes[driver]))

    except OSError:
        print("Error in reading file {:s}. Closing program.".format(name))

main()