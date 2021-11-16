#global variable :D
BERRY_TYPES = ["blueberry", "lingonberry", "cloudberry", "cranberry", "raspberry", "strawberry"]

def input_data():
    berry_data = input("Enter the name of the file containing the berry data:\n")
    return berry_data

def input_price():
    berry_prices = input("Enter the name of the file containing the prices of the berries:\n")
    return berry_prices

def open_berry_data(berry_data):
    data_dict = {}
    try:
        file_open = open(berry_data, "r")
        for line in file_open:
            line = line.rstrip()
            try:
                parts = line.split(",")
                if len(parts) != 3 or parts[1] not in BERRY_TYPES:
                    #spaghetti code
                    if line == 'Date,Berry type,Amount of picked berries (kg)':
                        pass
                    #spaghetti code
                    elif line == '':
                        pass
                    else:
                        print(f"Invalid line: {line}")
                else:
                    berry_type = parts[1]
                    try:
                        amount = int(parts[2])
                        if berry_type in data_dict.keys():
                            current_value = data_dict.get(berry_type)
                            data_dict[berry_type] = amount + current_value
                        else:
                            data_dict[berry_type] = amount
                    except:
                        print(f"Invalid line: {line}")
            except:
                print(f"Invalid line: {line}")
    except:
        print(f"Invalid file: {berry_data}")
        return
    print('File read.')
    return data_dict

def open_berry_prices(berry_prices):
    price_dict = {}
    try:
        file_open = open(berry_prices, "r")
        for line in file_open:
            line = line.rstrip()
            try:
                parts = line.split(":")
                if len(parts) != 2 or parts[0] not in BERRY_TYPES:
                    #spaghetti speacial
                    if line == 'Berry type,Price per kg':
                        pass
                    #spaghetti speacial
                    elif line == '':
                        pass
                    else:
                        print(f"Invalid line: {line}")
                else:
                    berry_type = parts[0]
                    try:
                        price = float(parts[1])
                        price_dict[berry_type] = price
                    except:
                        print(f"Invalid line: {line}")
            except:
                print(f"Invalid line: {line}")
            
    except:
        print(f"Invalid file: {berry_prices}")
        return      
    print("File read.")

    return price_dict

def main():
    berry_data = input_data()
    data_file = open_berry_data(berry_data)
    

    if data_file != None:
        berry_prices = input_price()
        price_file = open_berry_prices(berry_prices)
        try:
            #mom's spaghetti
            data_file_key_lst = [*data_file]
            price_file_key_lst = [*price_file] 
            check = set(data_file_key_lst).issubset(price_file_key_lst)
            if check == False:
                print(f"Some of the berry prices are missing from the file '{berry_prices}'.")
                
        except:
            pass
        if price_file != None and check != False:
            earnings_lst = []
            kg_lst = [*data_file.values()]
            name_lst = [*data_file]
            for key, value in data_file.items():
                for key2, value2 in price_file.items():
                    if key == key2:
                        earnings_lst.append(value2 * value)
            print("Berry type   Picked berries (kg)   Money earned (eur)")
            print("-" * 53)
            for i in range(len([*data_file])):
                print("{:12s} {:>19.0f} {:>20.2f}".format(name_lst[i], kg_lst[i], earnings_lst[i]))
            print("-" * 53)
            print("{:12s} {:>19.0f} {:>20.2f}".format("Total", sum(kg_lst), sum(earnings_lst)))
    print("\nProgram ends.")
main()