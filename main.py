#!/usr/bin/python3
import sys
from app.services.db_service import DbService
from app.constants.available_user_options import AvailableUserOptions
from app.utils.get_current_date_time_gmt_6 import current_date_time


db_service = DbService()

def show_all():
    if len(db_service.get()) == 0:
        print('\n No todos yet')
        return

    for index, todo in enumerate(db_service.get()):
        if todo['completion_date'] < current_date_time()['date'] and todo['completed'] == True:
            continue
        
        if todo['completed']:
            print(f"[x] id: {index + 1} > todo: {todo['todo']}")
            continue
        elif index <= 8:
            print(f"[ ] id: 0{index + 1} > todo: {todo['todo']}")
        else:
            print(f"[ ] id: {index + 1} > todo: {todo['todo']}")


def mark_as_completed(id):
    db_service.update_one(id, {"completed": True})


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
    if user_selection == AvailableUserOptions.ADD.value:
        todo = input('\nTodo: ').strip().lower()
        print('')
        db_service.add_one(todo)
        options_manager()

    elif user_selection == AvailableUserOptions.DELETE.value:
        deletion_id = input('\nTodo ID: ').strip().lower()
        print('')
        db_service.delete_one(deletion_id)
        options_manager()

    elif user_selection == AvailableUserOptions.COMPLETED.value:
        completion_id = input('\nTodo ID: ').strip().lower()
        print('')
        mark_as_completed(completion_id)
        options_manager()
     
    elif user_selection == AvailableUserOptions.RULES.value:
        display_todo_creation_rules()
        options_manager()

    elif user_selection == AvailableUserOptions.QUIT.value:
        sys.exit(0)
    
    else:
        print('\nInvalid option\n')
        options_manager()


def main():
    options_manager()


main()
