# Official Python image as base image
FROM python:3.12

# Working directory
WORKDIR /webapp

# Copy requirements.txt file and install dependencies
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js for executing JavaScript code
RUN apt-get update && apt-get install -y nodejs npm

# Install GCC and G++ for C and C++ code execution
RUN apt-get install -y build-essential

# Copy all the code files
COPY . .

# Expose the port
EXPOSE 8000

# Set the working directory
WORKDIR /webapp/source

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]