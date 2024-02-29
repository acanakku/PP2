#1
import os

def list_directories_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_contents = [content for content in os.listdir(path)]
    return directories, files, all_contents

#2
import os

def check_path_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

#3
import os

def path_info(path):
    exists = os.path.exists(path)
    if exists:
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return filename, directory
    else:
        return None, None

#4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

#5
def write_list_to_file(file_path, my_list):
    with open(file_path, 'w') as file:
        for item in my_list:
            file.write(str(item) + '\n')

#6
import string

for letter in string.ascii_uppercase:
    file_name = letter + ".txt"
    with open(file_name, 'w') as file:
        pass  
            
#7
def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source_file:
        with open(destination_path, 'w') as destination_file:
            for line in source_file:
                destination_file.write(line)
    
#8
import os

def delete_file(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"{file_path} deleted successfully.")
    else:
        print(f"Unable to delete {file_path}. File does not exist or access denied.")
                