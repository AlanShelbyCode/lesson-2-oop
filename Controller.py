from models.models import User, Car
class Сontroller:

    def __init__(self):
        pass
    def menu(self):
        while True:
            print("1. Add New User\n"
                   + "2. Get All Users\n"
                   + "3. Search\n"
                   + "4. Update User By Id\n"
                   + "5. Add car to User"
                  )
            menu_flag = int(input("Type your choose: "))
            if menu_flag == 1:
                self.add_user()
            elif menu_flag == 2:
                User.get_all_users()
            elif menu_flag == 3:
                what_to_search = input('By Which Parametr you want to search: ')
                search_str = input('Search: ')
                User.search_by(search_str, what_to_search)
            elif menu_flag == 4:
                User.update_user()
            elif menu_flag == 5:
                self.add_car_user()

    def add_user(self):
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        user = User(first_name, last_name, email)
        user.save()
    def add_car_user(self):
        car_user_id = input("User id to add car ")
        car_model = input("Car model: ")
        car_year = input("Car year: ")
        car_color = input("Car color: ")
        car = Car(car_user_id,car_model,car_year,car_color)
        car.save()
