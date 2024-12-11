from enum import Enum
import sys
import json
import time


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


def format_id_user_readable(id):
    # 4 digits sets
    set_length = 4
    formatted_id = ''

    for index, letter in enumerate(f"{id}"):
        # check if index is a multiple of set_length
        if (index + 1) % set_length == 0:
            formatted_id += letter
            formatted_id += '-'
            continue
        formatted_id += letter
    
    return formatted_id


def transform_unformatted_id(id):
    return "".join(f"{id}".split('-'))


def show_all():
    if len(read_db()) == 0:
        print('\n No todos yet')
        return

    for todo in read_db():
        print(f'[{'x' if todo['completed'] else ' '}] id: {format_id_user_readable(todo['id'])} >  todo: {todo['todo']}')


def add(str):
    unique_id = int(time.time() * 1000)
    temp_db = []
    formatted_todo = {
        'id': unique_id,
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
    id = transform_unformatted_id(id)

    for todo in read_db():
        if todo['id'] != int(id):
            temp_db.append(todo)
    rewrite_db(temp_db)


def mark_as_completed(id):
    temp_db = []
    id = transform_unformatted_id(id)

    for todo in read_db():
        if todo['id'] == int(id):
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
        add(todo)
        options_manager()
    elif user_selection == AvailableOptions.DELETE.value:
        deletion_id = input('\nTodo ID: ').strip().lower()
        delete(deletion_id)
        options_manager()
    elif user_selection == AvailableOptions.COMPLETED.value:
        completion_id = input('\nTodo ID: ').strip().lower()
        mark_as_completed(completion_id)
        options_manager()
    elif user_selection == AvailableOptions.QUIT.value:
        sys.exit(0)        
    else:
        print('\nInvalid option')


def main():
    options_manager()


main()
