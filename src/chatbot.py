import os
from dotenv import load_dotenv
load_dotenv()
from google import genai
from pydantic import BaseModel
from typing import List
from google.genai import types
import json
class CaloriesCountPerDish(BaseModel):
    dish_name: str
    Calories:int
    carbohydrate: int
    fat: int
    protein: int

class CaloriesCountPerMeal(BaseModel):
     dishes: List[CaloriesCountPerDish]
     meal_name: str
     calories: int
     carbohydrate: int
     fat: int
     protein: int
     suggestions: str

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def ai_agent(user_input,is_image_exist=False):
    try:
        with open("saved_meal_images/meal.jpg", 'rb') as f:
            image_bytes = f.read()

        if is_image_exist:
            response =client.models.generate_content(
                    model='gemini-2.0-flash-001',
                    contents=[
                        'you are ai assistant, your job is measure calories, carbohydrate, protein and fat of each dish separate on the basis of image or user input. Also give suggestion on effect of meal on their health',
                        types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg'),
                        types.Content(
                            role='user',
                            parts=[types.Part.from_text(text=user_input)]
                        )
                    ],
                    config=types.GenerateContentConfig(
                        response_mime_type='application/json',
                        response_schema=CaloriesCountPerMeal,
                        temperature=0.0
                    )
            )
        else:
            response = client.models.generate_content(
                model='gemini-2.0-flash-001',
                contents=[
                    'you are ai assistant, your job is measure calories, carbohydrate, protein and fat of each dish separate on the basis of image or user input. Also give suggestion on effect of meal on their health',
                    types.Content(
                        role='user',
                        parts=[types.Part.from_text(text=user_input)]
                        )
                    ],
                config = types.GenerateContentConfig(
                    response_mime_type='application/json',
                    response_schema=CaloriesCountPerMeal,
                )
            )
        return json.loads(response.text)
    except Exception as e:
        return {"error": str(e)}