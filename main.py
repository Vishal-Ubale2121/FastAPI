from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {
    "status": 200,
    "response": "Ok"
    "output": None
  }

