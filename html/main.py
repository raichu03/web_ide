from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from codeRunner import Run

class my_data(BaseModel):
    language: str
    code: str

app = FastAPI()

app.add_middleware(
   CORSMiddleware,
   allow_origins= ["*"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)


@app.post("/test")
async def post_test(data: my_data):

    code = data.code
    language = data.language
    run_code = Run()
    output = run_code.codeRunner(language, code)
    return JSONResponse(content=output)
