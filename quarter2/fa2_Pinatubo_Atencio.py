class Patient:
    __name: str
    __bill_amount: float
    def __init__(self, name, bill_amount):
        self.set_name(name)
        self.__bill_amount = 0.0
        self.set_bill_amount(bill_amount)
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_bill_amount(self, bill_amount):
        if bill_amount > 0:
            self.__bill_amount = bill_amount
        else:
            print("Invalid Input! Please enter a positive number.")
    def get_bill_amount(self):
        return self.__bill_amount
    def calculate_bill(self):
        return self.get_bill_amount()

class SeniorPatient(Patient):
    __name: str
    __bill_amount: float
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

class PhilHealthPatient(Patient):
    __name: str
    __bill_amount: float
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85
