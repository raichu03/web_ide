import os
import uuid

from . import run_python
from . import run_c
from . import run_cpp
from . import run_js

def convert_extention(extenction: str):
    """
    Converts the extention to the valid extention for the execution
    """
    if extenction == "python":
        return "py"
    elif extenction == "c":
        return "c"
    elif extenction == "cpp":
        return "cpp"
    elif extenction == "javascript":
        return "js"
    else:
        return None

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
    extention = convert_extention(extention)
    file_path = save_file(code, extention)
    timeout = 5
    
    if extention == "py":
        stdout, stderr, return_code = run_python.execute(file_path, timeout)
        return stdout, stderr, return_code
    
    elif extention == "c":
        stdout, stderr, return_code = run_c.execute(file_path, timeout)
        return stdout, stderr, return_code
    
    elif extention == "cpp":
        stdout, stderr, return_code = run_cpp.execute(file_path, timeout)
        return stdout, stderr, return_code
    
    elif extention == "js":
        stdout, stderr, return_code = run_js.execute(file_path, timeout)
        return stdout, stderr, return_code
    

        
    