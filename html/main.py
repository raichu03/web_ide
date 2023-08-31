from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from codeRunner import Run
from questions import Question
obj = Question()

class my_code(BaseModel):
    language: str
    code: str

class my_question(BaseModel):
    difficulty: str

app = FastAPI()

app.add_middleware(
   CORSMiddleware,
   allow_origins= ["*"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)


@app.post("/compile")
async def post_test(data: my_code):

    code = data.code
    language = data.language
    run_code = Run()
    output = run_code.codeRunner(language, code)
    return JSONResponse(content=output)


@app.post("/question")
async def post_question(data: my_question):
    question = data.difficulty
    output = None
    if question == "easy":
        output = obj.easyQuestion()
        
    elif question == "medium":
        output = obj.mediumQuestion()
    else :
        output = obj.hardQuestion()
        
    return JSONResponse(content=output)