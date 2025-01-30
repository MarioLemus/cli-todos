import os
from app.utils.get_parent_dir_path import get_parent_dir_path

_script_dir = os.path.dirname(os.path.abspath(__file__))
json_db_abs_path = os.path.join(get_parent_dir_path(_script_dir, 2), 'db.json')


