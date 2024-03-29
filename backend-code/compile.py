from datetime import datetime
import subprocess
import os
import python_compile
import javascript_compile
import c_compile
import cpp_compiler

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
    result = c_compile.execute(filePath)
    return result

def runCpp(filePath):
    result = cpp_compiler.execute(filePath)
    return result
    
def runPy(filePath):
    result = python_compile.execute(filePath)
    return result

def runJs(filePath):
    result = javascript_compile.execute(filePath)
    return result


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
    
    

