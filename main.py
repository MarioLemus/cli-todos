import sys
import os
from app import db_repo
from app.db_repo import DBRepo
from app.constants.available_user_options import AvailableUserOptions

AvailableOptions = AvailableUserOptions

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'db.json')


def show_all():
    if len(read_db()) == 0:
        print('\n No todos yet')
        return

    for index, todo in enumerate(read_db()):
        if todo['completed'] == True: continue
        print(f'[{'x' if todo['completed'] else ' '}] id: {f"0{index+1}" if index <=8 else index + 1} >  todo: {todo['todo']}')


def mark_as_completed(id):
    temp_db = []
    
    for index, todo in enumerate(read_db()):
        if index == (int(id) - 1):
            todo['completed'] = True
        temp_db.append(todo)
    rewrite_db(temp_db)


def display_todo_creation_rules():
    rules = [
        "No more than 5 todos can be available simoultaneously",
        "Addition of new todos is limited to max 5 per day (Mon to Fri)",
        "Todos must be well delimited and be specific (micro todos)",
        "Every starting todo should be short timed enough to do it even if you dont want\n"        
    ]

    for index, rule in enumerate(rules):
        print(f"{(index+1)}. {rule}")


def display_general_info():
    show_all()
    print("\nSee all the available \"weekly todos\"")
    print("-> other options: \n(c) mark as complete \n(a) add todos \n(d) delete todo \n(r) rules \n(q) quit")


def options_manager():
    display_general_info()
    user_selection = input('\n> ').strip().lower()
    print(user_selection)
    if user_selection == AvailableOptions.ADD.value:
        todo = input('\nTodo: ').strip().lower()
        print('')
        add(todo)
        options_manager()

    elif user_selection == AvailableOptions.DELETE.value:
        deletion_id = input('\nTodo ID: ').strip().lower()
        print('')
        delete(deletion_id)
        options_manager()

    elif user_selection == AvailableOptions.COMPLETED.value:
        completion_id = input('\nTodo ID: ').strip().lower()
        print('')
        mark_as_completed(completion_id)
        options_manager()
     
    elif user_selection == AvailableOptions.RULES.value:
        display_todo_creation_rules()
        options_manager()

    elif user_selection == AvailableOptions.QUIT.value:
        sys.exit(0)        
    
    else:
        print('\nInvalid option\n')


def main():
    db_repo = DBRepo()
    options_manager()


main()
