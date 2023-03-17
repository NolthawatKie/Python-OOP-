from employee import Employee

class Accounting(Employee):  # Inheritance
    __departmentName = 'Accountant'

    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        # add more parameter for this class
        self._age = age

    # Overriding
    def _showDetail(self) :
        super()._showDetail()
        print("Age = {}".format(self._age))

    def __str__(self):
        return (super().__str__()+", Age = {}, Total Salary = {}".format(self._age, super()._getIncome(10000,500)))