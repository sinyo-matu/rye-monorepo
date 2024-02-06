## a fastapi app

import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from lib.application.generate_recipe_then_save import generate_recipe_then_save

load_dotenv()

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

class GetNewRecipeBody(BaseModel):
    description:str

@app.post("/get_new_recipe")
async def get_new_recipe(body: GetNewRecipeBody):
    recipe = generate_recipe_then_save(body.description)
    return JSONResponse(content=recipe.model_dump())
