
import compile
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

class request_data(BaseModel):
    language: str
    code: str


app = FastAPI()

## this function compiles code written in C, C++ Javascript and Python
@app.post("/compile-code")
async def compile_code(data: request_data):
    code = data.code
    language = data.language

    final_output = compile.codeRun(language, code)
    return JSONResponse(content=final_output)
    
