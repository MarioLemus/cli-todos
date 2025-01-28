from enum import Enum

class AvailableUserOptions(Enum):
    COMPLETED = 'c'
    QUIT = 'q'
    ADD = 'a'
    RULES = 'r'
    DELETE = 'd'
    # list description for available options
    HELP = '-h'
    # nested options DELETE
    # dg: delete group
    BULK_DELETION = 'dg'
    TOTAL_DELETION = 'td'



