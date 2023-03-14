from accounting import Accounting
from sales import Sales

obj1 = Accounting("A1", 25000,2)
print(obj1.__str__())

obj2 = Sales("A2", 28000, "Bangkok")
print(obj2.__str__())