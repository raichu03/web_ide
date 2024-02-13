
import compile
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import get_question




class request_data(BaseModel):
    language: str
    code: str

class question_data(BaseModel):
    difficulty: str


app = FastAPI()

app.add_middleware(
   CORSMiddleware,
   allow_origins= ["*"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

## this function compiles code written in C, C++ Javascript and Python
@app.post("/compile-code")
async def compile_code(data: request_data):
    code = data.code
    language = data.language

    final_output = compile.codeRun(language, code)
    return JSONResponse(content=final_output)


## this function gets easy questions
@app.post("/questions")
async def questions(data: question_data):
    difficulty = data.difficulty
    question = get_question.questions(difficulty)
    return JSONResponse(content=question)
    
