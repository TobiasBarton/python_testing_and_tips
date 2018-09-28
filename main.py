from datetime import datetime
from pprint import pprint

from class_tips import Employee


emp1 = Employee('Ross', 'Miller', 1000000, 'Miner', datetime(2018, 1, 1))

print('Employee class 1')
print(emp1.__class__)
print(emp1.__dict__)
print(emp1.__doc__)

