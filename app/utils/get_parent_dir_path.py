import os

def get_parent_dir_path(current_dir_path, levels_in_herarchy):
    # everytime when os.path.dirname gets executed it removes the last value after "/"
    for _ in range(levels_in_herarchy):
        current_dir_path = os.path.dirname(current_dir_path)
    return current_dir_path


