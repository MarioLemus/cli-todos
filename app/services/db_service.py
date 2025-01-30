import json
import os
from app.utils.db_entity_handler import DbEntityHandler
from app.utils.get_current_date_time_gmt_6 import current_date_time


script_dir = os.path.dirname(os.path.abspath('main.py'))
json_path = os.path.join(script_dir, 'db.json')


class DbService:
    def __init__(self):
        self.db_entity_handler = DbEntityHandler()

    def add_one(self, todo):
        temp_db = []
        formatted_todo = {
            'todo': todo, 
            'completed': False, 
            'completion_time': (current_date_time())['time'], 
            'completion_date': (current_date_time())['date']
        }

        temp_db.extend(self.get())
        temp_db.append(formatted_todo)

        try:
            self.db_entity_handler.write_db(temp_db)
            print('Added succesfully!\n')
        except Exception:
            print('Something went wrong while adding todo!\n')


    def update_one(self, id, newData):
        temp_db = []
     
        for index, todo in enumerate(self.get()):
            if index == (int(id) - 1):
                for field_to_update in newData.keys():
                    if field_to_update == ('id' or 'ID'):
                        continue

                    try:
                        if (type(todo[field_to_update]) != type(newData[field_to_update])):
                            print(f"'{field_to_update}' has to be of the same datatype")
                            break
                        if ((type(newData[field_to_update]) == 'str') and len(newData[field_to_update]) == 0):
                            continue
                        todo[field_to_update] = newData[field_to_update]
                    except:
                        print(f"'{field_to_update}' does not exists in 'todo' dict")
                
            temp_db.append(todo)
        
        self.db_entity_handler.write_db(temp_db)


    def delete_one(self, id):
        temp_db = []
        for index, todo in enumerate(self.get()):
            # exclude the coincidence
            if index != (int(id) - 1):
                temp_db.append(todo)

        try:
            self.db_entity_handler.write_db(temp_db)
            print("Deleted succesfully!\n")
        except Exception:
            print('Something went wrong while deleting todo!\n')


    def get(self):
        try:
            with open(json_path, 'r') as db:
                content = db.read().strip()  # Elimina espacios en blanco al inicio y fin

                if not content:
                    return []

                db_instance = json.loads(content)
                return db_instance

        except json.JSONDecodeError as e:
            print(f"Something went wrong while reading DB {e}")
            return []
       
    #def update_all():
    #def bulk_deletion():
    #def bulk_update():
