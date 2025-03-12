import os
import uuid

import run_python

def save_file(code: str, extection: str):
    """
    Saves the code file in the temp direcory for execution.
    Returns the file path 
    """
    directory_name = "temp/"
    file_name = f"{uuid.uuid4()}.{extection}"
    file_path = directory_name + file_name
    
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        
    with open(file_path, "w") as f:
        f.write(code)
        
    return file_path

def execute_code(code: str, extention: str):
    """
    Executes the code and returns the output
    """
    file_path = save_file(code, extention)
    
    if extention == "py":
        stdout, stderr, return_code = run_python.execute(file_path)
        return stdout, stderr, return_code

        
    