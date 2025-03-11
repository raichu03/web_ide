from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from app import run_code

app = FastAPI()

app.mount("/static", StaticFiles(directory="web"), name="static")

class Code(BaseModel):
    code: str
    
    
@app.get("/", response_class=HTMLResponse)
def root():
    with open("web/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)
    
@app.post("/execute")
def execute(message: Code):
    print("success")
    result = run_code.save_file(message.code, "py")
    return {"message": "Hello, World!"}

    