class Author:
    def __init__(self,name,email,gender):
        self.name = name
        self.email = email
        self.gender = gender

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def setEmail(self,email):
        self.email = email

    def getGender(self):
        return self.gender

    def toString(self):
        return f"Author[{self.name},{self.email},{self.gender}]"

if __name__ == '__main__':
    pass