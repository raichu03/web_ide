from datetime import datetime
import subprocess
import os

def filePathGen(fileName):
    """generates and returns filepath according to os to store code"""
    filepath = os.path.join("temp", fileName)
    return filepath


def codeGenerator(language, code):
    fileName = datetime.now().strftime("%d_%H_%M_%S") + "." + language
    filePath = filePathGen(fileName)

    try:
        with open(filePath, "w") as file:
            file.write(code)
        return filePath
    
    except FileNotFoundError:
        os.mkdir("temp")
        with open(filePath, "w") as file:
            file.write(code)
        return filePath
    
    except PermissionError:
        if os.name == "nt":
            print("Permission denied. Try running the program as administrator.")
            ## TODO: add code to run as administrator
        else:
            print("Permission denied. Try running the program as root.")
            ## TODO: add code to run as root
        return None
    
    except Exception as e:
        print("An error occured while creating file: " + str(e))
        ## TODO: add cod to write a log file and delete print statement
        return None


def runC(filePath):
    name = datetime.now().strftime("%d_%H_%M_%S")
    outputFile = os.join("temp", name)
    command = f"gcc {filePath} -o {outputFile}"

    try: 
        result = subprocess.run(command, shell=True, check=True, stderr=subprocess.PIPE, text=True)
    
    except subprocess.CalledProcessError as e:
        return e.stderr
    
    if result.returncode != 0:
        return result.stderr
    
    runCommand = f"{outputFile}"
    try:
        output = subprocess.check_output([runCommand], stderr=subprocess.STDOUT, text=True)
        return output
    
    except subprocess.CalledProcessError as e:
        return e.stderr

def runCpp(filePath):
    name = datetime.now().strftime("%d_%H_%M_%S")
    outputFile = os.join("temp", name)
    command = f"g++ {filePath} -o {outputFile}"

    try: 
        result = subprocess.run(command, shell=True, check=True, stderr=subprocess.PIPE, text=True)
    
    except subprocess.CalledProcessError as e:
        return e.stderr
    
    if result.returncode != 0:
        return result.stderr
    
    runCommand = f"{outputFile}"
    try:
        output = subprocess.check_output([runCommand], stderr=subprocess.STDOUT, text=True)
        return output
    
    except subprocess.CalledProcessError as e:
        return e.stderr
    
def runPy(filePath):
    command = None
    if os.name == "posix":
        command = f"python3 {filePath}"
    else:
        command = f"python {filePath}"

    if command == None:
        return None
    else:
        try:
            output = subprocess.check_output([command], stderr=subprocess.STDOUT, text=True)
            return output
        except subprocess.CalledProcessError as e:
            return e.stderr

def runJs(filePath):
    command = f"node {filePath}"
    try:
        output = subprocess.check_output([command], stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.stderr


def codeRun(language, code):
    filePath = codeGenerator(language, code)
    if filePath == None:
        return None
    
    if language == "c":
        result = runC(filePath)
        return result
    
    elif language == "cpp":
        result = runCpp(filePath)
        return result
    
    elif language == "py":
        result = runPy(filePath)
        return result
    elif language == "js":
        result = runJs(filePath)
        return result
    else:
        ## TODO: you can add support for other languages here
        result = "Language currently not supported"
        return result
    
    

