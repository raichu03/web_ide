from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from app import run_code

app = FastAPI()

app.mount("/static", StaticFiles(directory="web"), name="static")

class Code(BaseModel):
    code: str
    language: str
    
    
@app.get("/", response_class=HTMLResponse)
def root():
    with open("web/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)
    
@app.post("/execute")
def execute(message: Code):
    stdout, stderr, return_code = run_code.execute_code(message.code, message.language)
    return {"message": "Hello, World!"}

    