from models.models import Book
class Сontroller:

    def __init__(self):
        pass
    def menu(self):
        while True:
            print("1. Add New Book\n"
                   + "2. Get All Books\n"
                   + "3. Search Book by\n"
                   + "4. Update Book By Id"
                  )
            menu_flag = int(input("Type your choose: "))
            if menu_flag == 1:
                self.add_book()
            elif menu_flag == 2:
                Book.get_all_books()
            elif menu_flag == 3:
                what_to_search = input('By Which Parametr you want to search '
                                       '(id/book_name/book_autor): ')
                search_str = input('Search: ')
                Book.search_by(search_str, what_to_search)
            elif menu_flag == 4:
                Book.update_book()

    def add_book(self):
        book_name = input("Title of book: ")
        book_autor = input("Last name: ")
        book = Book(book_name,book_autor)
        book.save()
