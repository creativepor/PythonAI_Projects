class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):

    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name) 
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):

    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name) 
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate


    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


if __name__ == "__main__":
    salary_emp = SalaryEmployee(1, "Priya", 13000)
    hourly_emp = HourlyEmployee(2, "Bob", 40, 13)

    print(salary_emp.calculate_payroll())
    print(hourly_emp.calculate_payroll())





