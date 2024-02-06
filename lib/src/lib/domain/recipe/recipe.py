from typing import List, Optional
from pydantic import BaseModel
from lib.infrastruture.openai_client import AzureOpenAIClient
import ulid


class Recipe(BaseModel):
    id : str
    name: str
    description: str
    steps: List[str]
    ingredients: List[str]
    def __init__(self,id:Optional[str],name: Optional[str], description: Optional[str],steps:Optional[List[str]],ingredients:Optional[List[str]]) -> None:
        id = id if id else str(ulid.new())
        name = name if name else ""
        description = description if description else ""
        steps = steps if steps else []
        ingredients = ingredients if ingredients else []
        super().__init__(
            id=id,
            name=name,
            description=description,
            steps=steps,
            ingredients=ingredients,
        )   

    def __str__(self) -> str:
        return f"Recipe(id={self.id}, name={self.name}, description={self.description}, ingredients={self.ingredients}, steps={self.steps})"

    def __repr__(self) -> str:
        return self.__str__()

    def fill_self(self, openai_client:AzureOpenAIClient):
        response = openai_client.fetch_recipe(self.description)
        self.name = response.name
        self.steps = response.steps
        self.ingredients = response.ingredients