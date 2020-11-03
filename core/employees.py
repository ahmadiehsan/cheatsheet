class Employee:
    def __init__(self, first_name, last_name, emails, username, is_active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.emails = emails
        self.username = username
        self.is_active = is_active

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name


class EmployeeManager:
    def __init__(self):
        self.employees = [
            Employee('علی', 'داود', ['alidavood.it@gmail.com'], 'ali_davood', False),
            Employee('میلاد', 'جلالی', ['milad.jalali@gmail.com'], 'milad_jalali', False),
            Employee('احسان', 'احمدی', ['1374ea@gmail.com'], 'ehsan_ahmadi'),
        ]

    def all(self):
        return self.employees

    def actives(self):
        rtn = []
        for employee in self.employees:
            if employee.is_active:
                rtn.append(employee)
        return rtn

    def de_actives(self):
        rtn = []
        for employee in self.employees:
            if not employee.is_active:
                rtn.append(employee)
        return rtn


EMPLOYEES = EmployeeManager()