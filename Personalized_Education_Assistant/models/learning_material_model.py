from pydantic import BaseModel
from typing import List

class LearningMaterial(BaseModel):
    videos: List[str]
    articles: List[str]
    exercises: List[str]