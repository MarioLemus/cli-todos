import json
import os

script_dir = os.path.dirname(os.path.abspath('main.py'))
json_path = os.path.join(script_dir, 'db.json')

class DbEntityHandler:
    def write_db(self, todos_array):
        with open(json_path, 'w') as db:
            json.dump(todos_array, db, indent=4)


    def add_new_props_to_all_entities(self, currentDB, new_props_and_default_values):
        temp_db = []
        
        if len(new_props_and_default_values.keys()) == 0:
            print("To add new props to all existing objects in DB, they have to exist first")
            return


        if len(currentDB) == 0:
            print("Provide a valid DB list")
            return
        
        for todo in currentDB:
            # merge new props with old ones, this mutates the original dict
            new_todo = todo | new_props_and_default_values
            temp_db.append(new_todo)
        self.write_db(temp_db)
 
