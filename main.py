from application.Salary import Salary
from application.db.people import Employees
from datetime import datetime

if __name__ == '__main__':
    Employees.get_employees()
    print(datetime.today())
    Salary.calculate_salary()
    print(datetime.today())
    print("That's All, Folks!")