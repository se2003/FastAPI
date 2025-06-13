from fastapi import FastAPI

app = FastAPI(root_path="/test1")  # Important if served at /test1

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}

