# IDE for Website
This fullstack website can be deployed to run on a local machine or on a server. The website was built to fulfill the basic immediate need. It was made for sole purpose of holding coding competation among students of a college during annual tech event. 

The website is built using the following technologies:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Jquery](https://jquery.com/)
- [Python](https://www.python.org/)

Due to limited time, we could not implement the database system, and automated answer checking system but in future we will try to implement these features. The website can be easily scaled and expanded to add more features. Feel free to use the code for your own purpose or to contribute to the project. Currently it uses python dictionary to store and fetch the questions.

This code was made to run in linux system and runs without problem, but it can be easily modified to run on windows system. You just have to change the path of the files in the code. To increase the number of languages supported, you just have to add the language in the code and add the compiler for that language in the system. You would also need to add the path of the compiler in the code as we have done for the other languages.

It uses uvicorn server to host the api and all the requirements are mentioned in the requirements.txt file. You can install all the requirements using the following command:

``` pip install -r requirements.txt ```

To run the server in localhost, you can use the following command:

``` uvicorn main:app --reload ```

or you can use  the following command to run in different address:

``` uvicorn main:app --host [ip address] --port [port number] -reload```

