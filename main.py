from fastapi import FastAPI

app = FastAPI()


@app.get("/new_notification")
async def root(text: str):
    return {"message": text}
