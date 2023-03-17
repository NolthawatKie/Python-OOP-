from employee import Employee

class Sales(Employee):  # Inheritance
    __departmentName = 'Sales'

    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self._area = area
    
    def _showDetail(self):
        super()._showDetail()
        print("Area = {}".format(self._area))

    def __str__(self):
        return (super().__str__() + ", Area = {}, Total Salary = {}".format(self._area, super()._getIncome(overtime=600)))