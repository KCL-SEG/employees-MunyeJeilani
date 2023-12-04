class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0
        self.hourly_wage = 0
        self.hours_worked = 0
        self.bonus = 0
        self.commission = 0
        self.num_contracts = 0

    def set_monthly_salary(self, salary):
        self.salary = salary

    def set_hourly_wage(self, hourly_wage):
        self.hourly_wage = hourly_wage

    def set_hours_worked(self, hours):
        self.hours_worked = hours

    def set_bonus(self, bonus):
        self.bonus = bonus

    def set_commission(self, commission):
        self.commission = commission

    def set_num_contracts(self, num_contracts):
        self.num_contracts = num_contracts

    def get_pay(self):
        contract_pay = 0
        commission_pay = 0

        if self.salary > 0:
            contract_pay = self.salary
        elif self.hourly_wage > 0 and self.hours_worked > 0:
            contract_pay = self.hourly_wage * self.hours_worked

        if self.num_contracts > 0 and self.commission > 0:
            commission_pay = self.num_contracts * self.commission

        total_pay = contract_pay + commission_pay + self.bonus

        return total_pay

    def __str__(self):
        contract_info = ""
        if self.salary > 0:
            contract_info = f"monthly salary of {self.salary}"
        elif self.hourly_wage > 0 and self.hours_worked > 0:
            contract_info = (
                f"contract of {self.hours_worked} hours at {self.hourly_wage}/hour"
            )

        commission_info = ""
        if self.num_contracts > 0 and self.commission > 0:
            commission_info = f" and receives a commission for {self.num_contracts} contract(s) at {self.commission}/contract"

        bonus_info = ""
        if self.bonus > 0:
            bonus_info = f" and receives a bonus commission of {self.bonus}"

        return f"{self.name} works on a {contract_info}{commission_info}{bonus_info}. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie = Employee("Billie")
billie.set_monthly_salary(4000)

# Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.
charlie = Employee("Charlie")
charlie.set_hourly_wage(25)
charlie.set_hours_worked(100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.
renee = Employee("Renee")
renee.set_monthly_salary(3000)
renee.set_num_contracts(4)
renee.set_commission(200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.
jan = Employee("Jan")
jan.set_hourly_wage(25)
jan.set_hours_worked(150)
jan.set_num_contracts(3)
jan.set_commission(220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.
robbie = Employee("Robbie")
robbie.set_monthly_salary(2000)
robbie.set_bonus(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.
ariel = Employee("Ariel")
ariel.set_hourly_wage(30)
ariel.set_hours_worked(120)
ariel.set_bonus(600)
