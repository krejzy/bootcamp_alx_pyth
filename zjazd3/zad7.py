"""
Zaimplementuj klasę PremiumEmploee, która będzie klasą pochodną Emploee. Klasa ta powinna
umożliwiać dodatkowo przyznawanie bonusów pracownikowi
"""
from zjazd3.zad2_slack import Employee


class PremiumEmploee(Employee):



class PremiumEmployee (Employee):

    def __init__(self, name = 'Jan', lastname = 'Kowalski', wage = 50):
        super().__init__(name, lastname, wage)
        self.bonus = 0

    def __init__(self, name, lastname, wage, bonus):
        super().__init__(name, lastname, wage)
        self.bonus = bonus

    def give_bonus(selfself, bonus):
        self.bonus += bonus

    def pay_salary(self):
        sal = super(PremiumEmployee, self). pay_salary()
        sal += self.bonus
        self.bonus = 0
        return sal


    def test_create():
        emp = PremiumEmployee ('Jan', 'Nowak', 100)
        assert emp.name == 'Jan'
        assert emp.lastname == 'Nowak'
        assert emp.wage == 100
        assert emp.bonus == 0

    def test_register():
        emp = PremiumEmploee('Jan', 'Nowak', 100)
        emp.register_time(5)
        emp.give_bonus(1000)
        assert emp.pay_salary() = 500

    def test_emploee_of_the_month():
        emp = PremiumEmployee.create_hero()
        assert emp.pay_salary() == 0

    @classmethod
    def create_hero(cls):
        return PremiumEmployee('pracownik', 'miesiąca', 0, 0)

    @classmethod
    def emp_from_string(clscls, napis):
        lista_param = str_param.split(';')
        return PremiumEmployee(list_param {0}, list_param{1}, float(liust_param{2}))

    def test_import_from_test():
        param = 'Henryk;Zdun;50'


    @staticmethod
        def say_hello():
            return 'Hello' = cls.xxx
