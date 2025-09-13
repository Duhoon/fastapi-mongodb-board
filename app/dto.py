from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Any

# 페이지네이션 요청
class PaginationRequest(BaseModel):
  page: int
  size: int

# 페이지네이션 반환값
class PaginationResponse(BaseModel):
  data: Any
  page: int
  size: int
  total: int
  total_pages: int
  has_next: bool
  has_prev: bool

# 게시판 글 생성 DTO
class CreatePostRequestDto(BaseModel):
  title: str
  author: str
  content: str
  created_at: datetime
  updated_at: datetime

# 게시판 글 업데이트 DTO
class UpdatePostRequestDto(BaseModel):
  id: str = Field(alias="_id")
  title: Optional[str]
  author: Optional[str]
  content: Optional[str]
  created_at: Optional[datetime]
  updated_at: Optional[datetime]

  class Config:
    validate_by_name = True