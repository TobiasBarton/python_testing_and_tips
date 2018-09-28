from datetime import datetime

class Sample:

    def __init__(self, test_var):
        self.test_var = test_var


class Employee:
    """
    A simple employee class to demonstrate how classes/objects work in Python
    """

    def __init__(self, first_name, last_name, salary, position, begin_date):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.position = position
        self.begin_date = begin_date


if __name__ == "__main__":
    emp = Employee('Ross', 'Miller', 1000000, 'Miner', datetime(2018, 1, 1))

    print('Employee class/instance data')
    # Will print out a type object with some class info
    print(emp.__class__)
    # Will just print out the name of the class
    print(emp.__class__.__name__)
    print(emp.__dict__)
