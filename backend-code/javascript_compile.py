import os
import subprocess
import re

def execute(filePath):
    """executes javascript file and returns the output"""
    command = None
    if os.name == 'nt':
        command = ['node', filePath]
    elif os.name == 'posix':
        command = ['nodejs', filePath]
    else:
        return 'OS not supported. Please run the program on Windows or Linux.'
    
    if command != None:
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
            if os.path.exists(filePath):
                os.remove(filePath)
            return output
        
        except subprocess.CalledProcessError as e:
            result = re.sub('[a-zA-Z0-9\"/\-_\.,]*:', '', e.output)
            result = "line: " + result
            if os.path.exists(filePath):
                os.remove(filePath)
            return result
    else:
        return "Unknown error occurred. Please try again."


