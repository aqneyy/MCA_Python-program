
class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        print("Publisher:", self.name)
        print("Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price):
        super().__init__(name, title, author)
        self.price = price

    def display(self):
        super().display()
        print("Price:", self.price)


b = Python("Tech Publications", "Python Programming",
           "John Smith", 450)
b.display()
