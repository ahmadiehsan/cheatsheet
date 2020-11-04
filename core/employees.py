class Employee:
    def __init__(
            self,
            first_name,
            last_name,
            username,
            emails,
            rocket_chat_room_id,
            is_active=True
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.emails = emails
        self.rocket_chat_room_id = rocket_chat_room_id
        self.is_active = is_active

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name


class EmployeeManager:
    def __init__(self):
        self.employees = [
            Employee(
                'علی',
                'داود',
                'ali_davood',
                ['alidavood.it@gmail.com'],
                'oEzJbP4LP5jMktE3YxEao9bLuzxWERXRAN',
                False
            ),
            Employee(
                'میلاد',
                'جلالی',
                'milad_jalali',
                ['milad.jalali@gmail.com'],
                'WoXLXG5Xd3vnkWDf2oEzJbP4LP5jMktE3Y',
                False
            ),
            Employee(
                'احسان',
                'احمدی',
                'ehsan_ahmadi',
                ['1374ea@gmail.com'],
                'oEzJbP4LP5jMktE3YoEzJbP4LP5jMktE3Y'
            ),
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
