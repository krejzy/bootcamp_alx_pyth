"""
Zaimplementuj klasę Basket umożliwiającą dodawanie produktów w określonej liczbie do koszyka.
 Zaiplementuj metodę obliczającą całkowitą wartość koszyka oraz wypisującą informację o zawartości.
 Dodanie dwa razy tego samego produktu do koszyka powinna stworzyć tylko jedną pozycję.
"""

class Baskett:
      def __init__(self):
            self.koszyk = []

        def dodaj(self, obiekt):
            self.koszyk.append(obiekt)

        def rozmiar(self):
            return len(self.koszyk)



    def__init__(self, id, name, price):
    self.id = id
    self.name = name
    self.product = product

def print_info(self):
    print(f'"(self.name)", id: (self.id), cena:(self.price) PLN')

# wersja prowadzący

class Products:
    def__init__(self, id, name, price):
    self.id = id
    self.name = name
    self.product = product


class Basket:
    basket = Basket()

def test_basket_initialization():
    basket = Basket()
    assert basket.entries == []

def test_basket_add_product():
    basket = Basket()
    product = Product (1. 'Piwo',10)
    basket.add_product(product, 5)
    assert len(basket.entries)

class basket.generate_report

def print_info(self):
    print(f'"(self.name)", id: (self.id), cena:(self.price) PLN')

def __str__(self):
    return f"{self.id} | {self.name} | {self.price}"

def test_basket.generate_report_initialization():
    expected = """Produkty w koszyku:
    - Woda, 
    """
    assert basket.generate_report == []

def test_basket_add_product():
    basket = Basket()
    product = Product(1, 'Piwo', 10)
    basket.add_product(product, 5)
    assert len(basket.entries) == 1