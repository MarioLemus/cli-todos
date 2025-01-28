import json
import os

script_dir = os.path.dirname(os.path.abspath('main.py'))
json_path = os.path.join(script_dir, 'db.json')

def write_db(todos_array):
    with open(json_path, 'w') as db:
        json.dump(todos_array, db, indent=4)



class DBRepo:
    #def update_one():
    def add_one(self, todo):
        temp_db = []
        formatted_todo = {'todo': todo,'completed': False}

        temp_db.extend(self.get())
        temp_db.append(formatted_todo)

        try:
            write_db(temp_db)
            print('Added succesfully!\n')
        except Exception:
            print('Something went wrong while adding todo!\n')


    def delete_one(self, id):
        temp_db = []
        for index, todo in enumerate(self.get()):
            # exclude the coincidence
            if index != (int(id) - 1):
                temp_db.append(todo)

        try:
            write_db(temp_db)
            print("Deleted succesfully!\n")
        except Exception:
            print('Something went wrong while deleting todo!\n')

    #def bulk_deletion():

    def get(self):
        with open(json_path, 'r') as db:
            db_instance = json.load(db)
        return db_instance

