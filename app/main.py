from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {"status": "Hello world! Todo api is raunning.."}
