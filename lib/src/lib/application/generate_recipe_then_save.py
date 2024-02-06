



import os

from lib.domain.recipe.recipe import Recipe
from lib.infrastruture.openai_client import AzureOpenAIClient


def generate_recipe_then_save(description:str):
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    if not api_key:
        raise ValueError("AZURE_OPENAI_API_KEY is not set")
    azure_endpoint = os.getenv("AZURE_OPENAI_API_ENDPOINT")
    if not azure_endpoint:
        raise ValueError("AZURE_OPENAI_ENDPOINT is not set")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")
    if not api_version:
        raise ValueError("AZURE_OPENAI_API_VERSION is not set")
    openai_client = AzureOpenAIClient(
        api_key=api_key,
        azure_endpoint=azure_endpoint,
        api_version=api_version
    )
    recipe = Recipe(
        id=None,
        name=None,
        steps=None,
        ingredients=None,
        description=description,
    )
    recipe.fill_self(openai_client)
    return recipe