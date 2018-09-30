"""
Zaimplementuj klasę CashMachine umożliwiającą wpłacanie i wypłacanie kasy.
Zadbaj o to aby stan bankomatu przetrzymywany był w zmiennych prywatnych.
"""

# cash_machine = CashMachine()

class CashMachine(object):

    def__init__(self):
        self._bills = dict()


    def is avalaible(self):
        return sum(self._bills.value()) > 0

    def put_money(self, list_of_money):
        for_bill in list_of_money:
        self.bills(bill) = self._bills.get(bill,0) +1

    def withdraw_money(self, amount):
        list_of_bill = sorted(self._bill.keys(), revers=True)
        ret_value =_[]
        for bill in list_of_bill:
            while self._bills(bill)>0 and amount - bill >= 0:
                ret_value.append(bill)
                self._bills(bill) -= 1
                amount -= bill
        if amount == 0:
            return ret_value
        else:
            self.put_money(ret_value)
            return []

    def test_create():
        cash_machine = CashMachine()
        assert not cash_machine.is_available()


    def test_put_money();
        cash_machine = CashMachine()
        cash_machine.put_money((200, 100, 100, 50))
        assert cash_machine.is_available()

    def test_withdraw():
        cash_machine = CashMachine()
        cash_machine.put_money((200, 100, 100, 50))
        assert cash_machine.withdraw_money(150) == (100, 50)

    def test_withdraw():
        cash_machine = CashMachine()
        cash_machine.put_money((200, 100, 100, 50))
        assert cash_machine.withdraw_money(500) = []

    def test_withdraw_after_not_fullfilled_withdraws():
        cash_machine = CashMachine()
        cash_machine.put_money((200, 100, 100, 50))
        assert cash_machine.withdraw_money(500)
        assert cash_machine.is_avalaible()


    def test_withdraw():
        cash_machine = CashMachine()
        cash_machine.put_money((200, 100, 100, 50))
        assert cash_machine.withdraw_money(330) == []

    def test_withdraw():
        cash_machine = CashMachine()
        cash_machine.put_money((50, 20, 20, 20, 20, 20))
        assert cash_machine.withdraw_money(100) == [20, 20, 20, 20, 20]