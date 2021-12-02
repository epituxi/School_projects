class RentApartment:

    RENTAL_SERVICE_FEE = 100 # eur per month
    STUDIO_SIZE_LIMIT = 32 # m2
    ONE_BEDROOOM_SIZE_LIMIT = 45 # m2
    STUDIO_PRICE_LEVEL = 25 # eur/m2
    ONE_BEDROOOM_PRICE_LEVEL = 20 # eur/m2
    LARGE_PRICE_LEVEL = 18 # eur/m2
    TRANSFER_TAX = 0.02


    def __init__(self, address, rent, maintenance_charge, size, free_of_debt_price):
        self.__address = address
        self.__rent = rent
        self.__maintenance_charge = maintenance_charge
        self.__size = size 
        self.__free_of_debt_price = free_of_debt_price
        self.__rental_service = False
        self.__renovation_costs = 0
        

    def get_address(self):
        return self.__address

    def get_rent(self):
        return self.__rent

    def get_maintenance_charge(self):
        return self.__maintenance_charge

    def get_size(self):
        return self.__size

    def get_price(self):
        return self.__free_of_debt_price

    def get_renovation_costs(self):
        return self.__renovation_costs

    def update_rental_service(self):
        if self.__rental_service == True:
            self.__rental_service = False
            return False
        else:
            self.__rental_service = True
            return True

    def increase_rent(self, new_rent):
        if self.__rent < new_rent:
            self.__rent = new_rent
            return True
        else:
            return False

    def add_renovation_costs(self, costs):
        self.__renovation_costs += costs

    def calculate_square_meter_rent(self):
        return self.__rent / self.__size

    def calculate_rental_income(self):
        monthly_expenses = self.__maintenance_charge
        if self.__rental_service == True:
            monthly_expenses = self.__maintenance_charge + RentApartment.RENTAL_SERVICE_FEE
        return (self.__rent - monthly_expenses) * 12 / (self.__free_of_debt_price + (self.__free_of_debt_price * RentApartment.TRANSFER_TAX) + self.__renovation_costs) * 100

    def compare_rental_incomes(self, other):

        first_rental_income = self.calculate_rental_income()

        monthly_expenses = other.__maintenance_charge
        if other.__rental_service == True:
            monthly_expenses = other.__maintenance_charge + RentApartment.RENTAL_SERVICE_FEE
        second_rental_income = (other.__rent - monthly_expenses) * 12 / (other.__free_of_debt_price + (other.__free_of_debt_price * RentApartment.TRANSFER_TAX) + other.__renovation_costs) * 100

        if first_rental_income > second_rental_income:
            return 1
        elif second_rental_income > first_rental_income:
            return -1
        else:
            return 0


    def calculate_return_on_equity(self, down_payment, loan_interest):
        monthly_expenses = 0
        if self.__rental_service == True:
            monthly_expenses = self.__maintenance_charge + RentApartment.RENTAL_SERVICE_FEE
        else:
            monthly_expenses = self.__maintenance_charge

        return (self.__rent - monthly_expenses - loan_interest) * 12 / down_payment * 100

    def check_price_level(self):
        if self.__size < RentApartment.STUDIO_SIZE_LIMIT:
            sqm_rent = self.calculate_square_meter_rent()
            if sqm_rent < RentApartment.STUDIO_PRICE_LEVEL:
                return False
            else:
                return True
        elif RentApartment.ONE_BEDROOOM_SIZE_LIMIT > self.__size >= RentApartment.STUDIO_SIZE_LIMIT:
            sqm_rent = self.calculate_square_meter_rent()
            if sqm_rent < RentApartment.ONE_BEDROOOM_PRICE_LEVEL:
                return False
            else:
                return True 
        else:
            sqm_rent = self.calculate_square_meter_rent()
            if sqm_rent < RentApartment.LARGE_PRICE_LEVEL:
                return False
            else:
                return True

    def __str__(self):
        service = "in use"
        if self.__rental_service == False:
            service = "not in use"
        return f"Address: {self.get_address()}\nMaintenance charge: {self.get_maintenance_charge()} eur\nSize: {self.get_size()} m2\nRent: {self.get_rent()} eur\nRental service: {service}"
