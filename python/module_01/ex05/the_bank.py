class Account:
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = Account.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0


class Bank:
    def __init__(self):
        self.accounts = []

    def add(self, acc):
        if not isinstance(acc, Account):
            return False
        self.accounts.append(acc)
        return True

    def transfer(self, origin, dest, amount):
        a = None
        b = None
        for acc in self.accounts:
            if acc.name == origin:
                a = acc
            if acc.name == dest:
                b = acc

        if not a or not b:
            return False
        if a.value < amount:
            return False

        a.value -= amount
        b.value += amount
        return True

    def fix_account(self, name):
        return True