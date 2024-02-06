from typing import List
from openai import AzureOpenAI, BaseModel

class RecipeResponse(BaseModel):
    name: str
    description: str
    steps: List[str]
    ingredients: List[str]


class AzureOpenAIClient:

     
    def __init__(self, api_key: str,azure_endpoint:str,api_version:str) -> None:
        self.client = AzureOpenAI(
            azure_endpoint=azure_endpoint,
            api_version=api_version,
            api_key=api_key
        )

    def fetch_recipe(self, description:str) ->RecipeResponse:
        messages = [
            {
                "role": "system",
                "content": """
                    You are a chef and you are trying to make a recipe for a dish.
                    You are given a description of the dish and you need to come up with a recipe for it.
                    The output should include the ingredients and the steps to make the dish.
                    The output should be in the below format:
                    {
                        "name": "Dish Name",
                        "description": "Dish Description",
                        "steps": ["Step 1", "Step 2", "Step 3"],
                        "ingredients": ["Ingredient 1", "Ingredient 2", "Ingredient 3"]
                    }
                """
            },
            {
                "role": "user",
                "content": description
            }
        ]
        return RecipeResponse.model_validate_json(self._fetch_chat_completion(messages))

    def _fetch_chat_completion(self, messages)->str:
        response = self.client.chat.completions.create(model="gpt-35-turbo",messages=messages)
        return str(response.choices[0].message.content)

        
