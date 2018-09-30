Zadanie #11
Zaimplementuj klasy odpowiedzialne za tworzenie dokumenty w
składni MarkDown. Stwórz klase bazowa Element zawierajaca
podstawowa implementacje metody render() oraz kilka jej klas
pochodnych. Stwórz klase Document umozliwiajaca wyrendorowanie
dodanych elementów.
Przykład uzycia:
>>> document = Document()
>>> document.add_element(HeaderElement('Header'))
>>> document.add_element(LinkElement('ABC', 'abc.com'))
>>> document.add_element(Element('Simple'))
>>> document.render()
Header
======
(ABC)[http://abc.com]
Simple


class Document
    def __init__(self):
        self.container = []

    def add.element(self, element)
        self(cointainer.append.element)


    def render(self):
        output = ""
        for el in
        return self(text)


class Element
    def __init__ (self, text):
        self.text = text

    def render(self):
        return self(text)

class HeaderElement(Element)

class __init__(self, text, level=1):
    self.level = level
    super().__init__(text)


   def test_document():
    doc = Document()
        assert doc.container == []




