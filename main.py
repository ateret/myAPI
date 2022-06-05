from fastapi import FastAPI
import scrapper

app = FastAPI()

@app.get("/")
async def root(url:str):

    statistics = scrapper.get_statistics(url)
    return statistics



