from farmework.models import Model
import json

class User(Model):
    file = 'users.json'

    def __init__(self, first_name, last_name, email):

        data = self.get_file_data(self.file)
        if len(data) > 0:
            self.id = data[-1]['id'] + 1
        else:
            self.id = 1
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if self.check_email() == True:
            print('User with this email already exist!!!')
            self.email = None

    def check_email(self):
        data = self.get_file_data(self.file)
        for user in data:
            if self.email == user['email']:
                return True
        return False

    #думав зробити лист, але вирішив не змінювати
    @classmethod
    def get_all_users(cls):
        with open('database/'+cls.file, 'r') as file:
            users = json.loads(file.read())
            for user in users:
                print("User #" + str(user['id']))
                print("First Name: " + user['first_name'])
                print("Last Name: " + user['last_name'])
                print("Email: " + str(user['email']))

    @classmethod
    def search_by(cls, search_str, what_to_search):
             with open('database/'+cls.file, 'r') as file:
                users = json.loads(file.read())
                for user in users:
                    if str(user[what_to_search]).lower() == str(search_str).lower():
                        print("User #" + str(user['id']))
                        print("First Name: " + user['first_name'])
                        print("Last Name: " + user['last_name'])
                        print("Email: " + str(user['email']))
                    else:
                        print('Not found')

    @classmethod
    def update_user(cls):
        file = open('database/'+cls.file, 'r')
        users = json.loads(file.read())
        file.close()
        id = int(input("Type id of user which you want to update: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        for user in users:
            if user['id'] == id:
                user['first_name'] = first_name
                user['last_name'] = last_name
                user['email'] = email

        with open('database/'+cls.file, 'w') as file:
            file.write(json.dumps(users))