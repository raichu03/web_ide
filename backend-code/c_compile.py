import os
import subprocess

def execute(filePath):
    """executes c file and returns the output"""
    compile_command = f"gcc {filePath} -o {filePath[:-2]}"

    try:
        subprocess.check_output(compile_command, shell=True, stderr=subprocess.STDOUT, text=True)
        if os.path.exists(filePath):
            os.remove(filePath)
        
    except subprocess.CalledProcessError as e:
        if os.path.exists(filePath):
            os.remove(filePath)
        return e.output
    
    run_command = None

    if os.name == "nt":
        run_command = f"{filePath[:-2]}.exe"
    elif os.name == "posix":
        run_command = f"./{filePath[:-2]}"
    else:
        return "OS not supported. Please run the program on Windows or Linux."

    try:
        output = subprocess.check_output(run_command, stderr=subprocess.STDOUT, text=True)
        if os.path.exists(filePath[:-2]):
            os.remove(filePath[:-2])
        return output
    except subprocess.CalledProcessError as e:
        if os.path.exists(filePath[:-2]):
            os.remove(filePath[:-2])
        return e.output
    
