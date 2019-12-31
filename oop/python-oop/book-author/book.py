from author import Author

class Book:
    def __init__(self,name,price,qty, bookAuthor):
        self.name = name
        self.obj_author = bookAuthor
        self.authors = [self.obj_author]
        self.price = price
        self.qty = qty

    def getName(self):
        return self.name

    def getAuthors(self):
        return [author.getName() for author in self.authors]

    def setAuthors(self,name,email,gender):
        author = Author(name,email,gender)
        self.authors.append(author)

    def getPrice(self):
        return self.price

    def setPrice(self,price):
        self.price = price
    
    def getQty(self):
        return self.qty

    def setQty(self,qty):
        self.qty = qty

    def toString(self):
        return f"Book {self.name}, Authors {self.getAuthors()},Price {self.price},Qty {self.qty}"

    def getAuthorsName(self):
        return [author.name for author in self.authors]
    
if __name__ == '__main__':
    bob = Author("bob","bob@gmail.com","Male")
    print(bob.name)
    book1 = Book("Crime and Punishment",15.20,1,bob)
    print(book1.toString())




