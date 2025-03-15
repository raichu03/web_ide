# Web based code editor
This is a web based code editor that allows you to write code in various languages like `python`, `javascript`, `c` and `c++`. It automatically runs the code in local machine without the need for downloading any application. It also provides a console to see the output of the code.

The editor was built using `FastAPI` and `HTML`, `CSS` and `Javascript` for the frontend. The code is run in a `docker` container and the output is displayed in the console.

## Installation
Clone the repository
```bash
git colne https://github.com/raichu03/web_ide.git
```

### Running locally
1. Install the dependencies(from the project directory)
```bash
pip install -r requirements.txt
```
2. Install the node, gcc and g++ compilers
``` bash
apt-get update && apt-get install -y nodejs npm
apt-get update && apt-get install -y build-essential
```
3. Run the application (from the `source` directory)
```bash
uvicorn main:app
```
This will run the application locally. You can access it by clicking on the link provided in the terminal.

### Running using docker
1. From the project directory, build the docker image
```bash
docker build -t app_name .
```
After the image is built, you can run the following command to start the application.

2. Run the docker container
```bash
 docker run -d -p 8000:8000 app_name
```
Now you can access the application by going to `http://localhost:8000` in your browser.


