from enum import Enum
import sys
import json


class AvailableOptions(Enum):
    COMPLETED = 'c'
    QUIT = 'q'
    ADD = 'a'
    DELETE = 'd'

# UTILS
def read_db():
    with open('db.json', 'r') as db:
        db_instance = json.load(db)
    return db_instance


def rewrite_db(todos_array):
    with open('db.json', 'w') as db:
        json.dump(todos_array, db, indent=4)


def show_all():
    if len(read_db()) == 0:
        print('\n No todos yet')
        return

    for index, todo in enumerate(read_db()):
        print(f'[{'x' if todo['completed'] else ' '}] id: {index + 1} >  todo: {todo['todo']}')


def add(str):
    temp_db = []
    formatted_todo = {
        'todo': str,
        'completed': False
    }

    temp_db.extend(read_db())
    temp_db.append(formatted_todo)

    try:
        rewrite_db(temp_db)
        print('Added succesfully!\n')
    except Exception:
        print('Something went wrong while adding todo!\n')

def delete(id):
    temp_db = []

    for index, todo in enumerate(read_db()):
        if index != (int(id) - 1) :
            temp_db.append(todo)
    rewrite_db(temp_db)


def mark_as_completed(id):
    temp_db = []
    
    for index, todo in enumerate(read_db()):
        if index == (int(id) - 1):
            todo['completed'] = True
        temp_db.append(todo)
    rewrite_db(temp_db)


def display_info():
    show_all()
    print("\nSee all the available \"weekly todos\"")
    print("-> other options: \n(c) mark as complete \n(a) add todos \n(d) delete todo \n(q) quit")


def options_manager():
    display_info()
    user_selection = input('\n> ').strip().lower()

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

    elif user_selection == AvailableOptions.QUIT.value:
        sys.exit(0)        
    else:
        print('\nInvalid option\n')


def main():
    options_manager()


main()
