
from abc import ABC, abstractmethod
import json

class Model(ABC):
    file = 'default.json'

    @staticmethod
    def get_file_data(file_name):
        file = open('database/' + file_name, 'r')
        all_file_data_json = file.read()
        all_file_data = json.loads(all_file_data_json)
        file.close()
        print(all_file_data)
        return all_file_data

    def save(self):
        object_in_dict_format = self.__dict__
        all_file_data = self.get_file_data(self.file)
        all_file_data.append(object_in_dict_format)
        with open('database/'+self.file, 'w') as file:
            file.write(json.dumps(all_file_data))
        file.close()
