from farmework.models import Model
import json

class Book(Model):
    file = 'books.json'

    def __init__(self, book_name, book_autor):

        data = self.get_file_data(self.file)
        if len(data) > 0:
            self.id = data[-1]['id'] + 1
        else:
            self.id = 1
        self.book_name = book_name
        self.book_autor = book_autor

    #думав зробити лист, але вирішив не змінювати
    @classmethod
    def get_all_books(cls):
        with open('database/'+cls.file, 'r') as file:
            books = json.loads(file.read())
            for book in books:
                print("Book #" + str(book['id']))
                print("First Name: " + book['book_name'])
                print("Last Name: " + book['book_autor'])
    @classmethod
    def search_by(cls, search_str, what_to_search):
        with open('database/' + cls.file, 'r') as file:
            books = json.loads(file.read())
            for book in books:
                    if str(book[what_to_search]).lower() == str(search_str).lower():
                        print("Book #" + str(book['id']))
                        print("First Name: " + book['book_name'])
                        print("Last Name: " + book['book_autor'])
                    else:
                        print('Not found')

    @classmethod
    def update_book(cls):
        file = open('database/'+cls.file, 'r')
        books = json.loads(file.read())
        file.close()
        id = int(input("Type id of book which you want to update: "))
        book_name = input("Book title: ")
        book_autor = input("Book autor: ")
        for book in books:
            if book['id'] == id:
                book['first_name'] = book_name
                book['last_name'] = book_autor

        with open('database/'+cls.file, 'w') as file:
            file.write(json.dumps(books))