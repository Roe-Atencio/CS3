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
    def display_patient_type(self):
        return "Regular Patient"

class SeniorPatient(Patient):
    __name: str
    __bill_amount: float
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80
    def display_patient_type(self):
        return "Senior Citizen"

class PhilHealthPatient(Patient):
    __name: str
    __bill_amount: float
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85
    def display_patient_type(self):
        return "PhilHealth Member"

print("Hospital Billing System\n-----------------------")
regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
phil_health_patient = PhilHealthPatient("Pedro Reyes", 15000)
patients = [regular_patient, senior_patient, phil_health_patient]
for patient in patients:
    print(f"Patient: {patient.get_name()}\nPatient Type: {patient.display_patient_type()}\nOriginal Bill: {patient.get_bill_amount()}\nFinal Bill: {patient.calculate_bill()}")
