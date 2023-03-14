class Employee:
    # Class Variable
    __minSalary = 23000
    __maxSalary = 50000
    _companyName = 'dotdotdot Co., Ltd'

    def __init__(self, name, salary, department):
        self._name = name
        self._salary = salary
        self._department = department

    def _showDetail(self):
        print("Name = {}".format(self._name))
        print("Salary = {}".format(self._salary))
        print("Department = {}".format(self._department))

    # Become overloading
    def _getIncome(self, bonus=0, overtime=0):
        return (self._salary * 12) +bonus + overtime

    def __str__(self):
        return ("Name = {}, Department = {}, Salary = {}".format(self._name, self._department, self._salary))