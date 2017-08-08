##Class Description: Stores Prospective Company Information.

class Company:

    def __init__(self, name, price, amount):

        self.__company_name = name
        self.__asking_price = price
        self.__desired_amount = amount

    ##accessors and mutators for attributes
    def get_company_name(self):
        return self.__company_name

    def set_asking_price(self, new_price):
        self.__asking_price = new_price
        
    def get_asking_price(self):
        return self.__asking_price

    def get_desired_amount(self):
        return self.__desired_amount

    def set_desired_amount(self, new_amount):
        self.__desired_amount = new_amount

    ##calculates price per item
    def calc_value(self):
        amount_desired = float(self.__desired_amount)
        
        asking_price = float(self.__asking_price)
        
        value = asking_price / amount_desired 
        
        return value
    
    def __str__(self):
        string = "Company Name: " + self.__company_name + " Price: " + str(self.__asking_price) + " Amount: " + str(self.__desired_amount)
        return string
        
