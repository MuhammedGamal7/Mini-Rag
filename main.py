from fastapi import FastAPI
app=FastAPI()

@app.get("/welcome")  #decorator
def welcome():
    return {
        "message" : "Hello World"
    }
