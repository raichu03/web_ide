import os
import subprocess
import re


def execute(filePath):
    """executes python file and returns the output"""
    command = None
    if os.name == "nt":
        command = ["python", filePath]
    elif os.name == "posix":
        command = ["python3", filePath]
    else:
        return "OS not supported. Please run the program on Windows or Linux."

    if command != None:
        try:

            output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
            if os.path.exists(filePath):
                os.remove(filePath)
            return output
                
        except subprocess.CalledProcessError as e:

            result = re.sub("File [a-zA-Z0-9\"/\-_\.,]*", "", e.output)
            if os.path.exists(filePath):
                os.remove(filePath)
            return result
    else:
        return "Unknown error occurred. Please try again."
