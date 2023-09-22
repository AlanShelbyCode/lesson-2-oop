import json

class User:

    def __init__(self, first_name, last_name, email):

        data = self.get_user_data()
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
        data = self.get_user_data()
        for user in data:
            if self.email == user['email']:
                return True
        return False

    @staticmethod
    def get_user_data():
        file = open('database/users.json', 'r')
        all_users_data_json = file.read()
        all_users_data = json.loads(all_users_data_json)
        file.close()
        return all_users_data

    # functions which used for adding users to user.json
    def save(self):
        user_in_dict_format = self.__dict__
        all_users_data = self.get_user_data()
        all_users_data.append(user_in_dict_format)
        with open('database/users.json', 'w') as file:
            file.write(json.dumps(all_users_data))
        file.close()

    #думав зробити лист, але вирішив не змінювати
    @classmethod
    def get_all(cls):
        with open('database/users.json', 'r') as file:
            users = json.loads(file.read())
            for user in users:
                print("User #" + str(user['id']))
                print("First Name: " + user['first_name'])
                print("Last Name: " + user['last_name'])
                print("Email: " + str(user['email']))

    @classmethod
    def search_by(cls, search_str, what_to_search):
        with open('database/users.json', 'r') as file:
            users = json.loads(file.read())
            for user in users:
                if str(user[what_to_search]).lower() == str(search_str).lower():
                    print("User #" + str(user['id']))
                    print("First Name: " + user['first_name'])
                    print("Last Name: " + user['last_name'])
                    print("Email: " + str(user['email']))

    @classmethod
    def update_user(cls):
        file = open('database/users.json', 'r')
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

        with open('database/users.json', 'w') as file:
            file.write(json.dumps(users))