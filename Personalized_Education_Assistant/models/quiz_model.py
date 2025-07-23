from pydantic import BaseModel
from typing import List

class Quiz(BaseModel):
    questions: List[str]
    answers: List[str]