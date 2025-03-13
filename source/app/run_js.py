import subprocess
import re
import os

def execute(file_path: str, timeout: int = 10):
    """
    Executes the python code and returns the output
    """
    try:
        # Run the Python code using subprocess
        result = subprocess.run(
            ['node', file_path],
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
    
    stderr = re.sub(r'/.*.js:', '', stderr).strip()
    os.remove(file_path)
    return stdout, stderr, return_code