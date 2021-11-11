from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):           # abstract class that has atleast one abstract method
    def __init__(self,title,author):             # constructor
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass                          # the abstract method

#Write MyBook class
class MyBook(Book):                              # extending the abstract class

    def __init__(self,title,author,price):       # constructor
        self.title = title
        self.author = author
        self.price = price

    def display(self):                            # must implement the abstract method!
        print('Title:', self.title)
        print('Author:', self.author)
        print('Price:', self.price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
