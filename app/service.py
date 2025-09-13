from app.db import collection
from app.dto import (
  CreatePostRequestDto, 
  UpdatePostRequestDto, 
  PaginationResponse,
)
from datetime import datetime
from bson import ObjectId
from math import ceil

# 리스트 페이지 별 조회
def get_list(page: int, size: int):
  if size == 0:
    raise ZeroDivisionError()

  try :
    posts = []

    # 페이지네이션 메타데이터
    total = collection.count_documents({})
    total_pages = ceil(total / size)
    docs = (
      collection
        .find({}, {"content": False})
        .sort("created_at", -1)
        .skip((page - 1) * size)
        .limit(size)
    )
    has_next = total_pages > page
    has_prev = page > 1

    # content 필드 제외
    for post in docs:
      post["_id"] = str(post["_id"])
      posts.append(post)

    # 반환값 생성
    res = {
      "data": posts,
      "page": page,
      "size": size,
      "total": total,
      "total_pages": total_pages,
      "has_next": has_next,
      "has_prev": has_prev
    }

    return PaginationResponse(**res)
  except Exception as e:
    raise e

# 상세 조회
def get_detail(_id: str):
  try:
    post = collection.find_one({"_id": ObjectId(_id)})
    post["_id"] = str(post["_id"])

    return post
  except Exception as e:
    raise e

# 생성
def create_post(post: CreatePostRequestDto):
  post = post.model_dump()
  post = {
    **post,
    "created_at": datetime.now(),
    "updated_at": datetime.now(),
  }

  try : 
    id = str(collection.insert_one(post))
    return id
  except Exception as e:
    raise e

# 수정
def update_post(post: UpdatePostRequestDto):
  post_filtered = post.model_dump(exclude={"id"})
  post_filtered = {
    **post_filtered,
    "updated_at": datetime.now(),
  }

  try :
    collection.update_one({"_id", ObjectId(post.id)}, post_filtered)
  except Exception as e:
    raise e

# 삭제
def delete_post(id: str):
  try :
    return collection.delete_one({"_id": ObjectId(id)})

  except Exception as e:
    raise e

# test code
if __name__ == "__main__":
  current = datetime.now()
  post = CreatePostRequestDto(
    title="Hello World!",
    author="Kang Duhoon",
    content="How's the weahter today? It's sunny!",
    created_at=current,
    updated_at=current
  )

  post_created = create_post(post)
  inserted_id = post_created.inserted_id

  print(get_list())