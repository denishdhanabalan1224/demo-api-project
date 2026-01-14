from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/messages")
def get_messages():
    return {"messages": ["Hello", "Welcome"]}
