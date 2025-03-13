import subprocess
import re
import os

def execute(file_path: str, timeout: int = 10):
    """
    Executes the python code and returns the output
    """
    
    executable_path = file_path.replace('.cpp', '')
    try:
        # Run the C code using subprocess
        compile_result = subprocess.run(
            ['g++', '-o', executable_path, file_path],
            text=True,
            capture_output=True,
            timeout=timeout,
            check=True
        )
        
        result = subprocess.run(
            [f'./{executable_path}'] if os.name != 'nt' else [executable_path],
            text=True,
            capture_output=True,
            timeout=timeout,
            check=True
        )
        
        #Capture standard output and standard error
        stdout = result.stdout
        stderr = result.stderr
        return_code = result.returncode
        
    except subprocess.TimeoutExpired:
        # Handle timeout
        stdout = ""
        stderr = f"Process timed out after {timeout} seconds"
        return_code = -1
    except subprocess.CalledProcessError as e:
        # Handle non-zero exit code
        stdout = e.stdout
        stderr = e.stderr
        return_code = -1
    except Exception as e:
        # Handle other exceptions
        stdout = ""
        stderr = str(e)
        return_code = -1
    
    file_pattern = re.escape(file_path) + r":"
    stderr = re.sub(file_pattern, '', stderr).strip()
    
    os.remove(executable_path)
    os.remove(file_path)
    return stdout, stderr, return_code
    