from fastapi import FastAPI, status, Query
import uvicorn
from app.dto import CreatePostRequestDto, UpdatePostRequestDto, PaginationRequest
from app.service import get_detail, get_list, create_post, update_post, delete_post

app = FastAPI()

@app.get("/status")
async def alive():
  return status.HTTP_200_OK

@app.get("/posts")
async def list(page:int = Query(None), size:int = Query(10)):
  try:
    return get_list(page, size)
  except Exception as e :
    print(e)
    return status.HTTP_400_BAD_REQUEST

@app.get("/post/{_id}")
async def detail(_id: str):
  try :
    return get_detail(_id)
  except Exception as e :
    print(e)
    return status.HTTP_400_BAD_REQUEST

@app.post("/post")
async def create(post: CreatePostRequestDto):
  try : 
    return create_post(post)
  except Exception as e :
    print(e)
    return status.HTTP_400_BAD_REQUEST

@app.put("/post")
async def edit(post: UpdatePostRequestDto):
  try :
    return update_post(post)
  except Exception as e :
    print(e)
    return status.HTTP_400_BAD_REQUEST

@app.delete("/post/{_id}")
async def delete(_id: str):
  try :
    delete_post(_id)
  except Exception as e:
    print(e)
    return status.HTTP_400_BAD_REQUEST

if __name__ == "__main__":
  uvicorn.run(app="main:app", host="0.0.0.0", port=8080, reload=True)