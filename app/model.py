from pydantic import BaseModel
from datetime import datetime

class Post(BaseModel):
  title: str
  author: str
  content: str
  created_at: datetime
  updated_at: datetime

