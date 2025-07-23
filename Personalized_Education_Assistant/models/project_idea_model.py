from pydantic import BaseModel
from typing import List

class ProjectIdea(BaseModel):
    ideas: List[str]