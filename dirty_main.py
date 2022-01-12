from application.Salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    Employees.get_employees()
    print(datetime.today())
    Salary.calculate_salary()
    print(datetime.today())