from fastapi import FastAPI, status
import uvicorn

app = FastAPI()

@app.get("/status")
async def alive():
  return status.HTTP_200_OK

if __name__ == "__main__":
  uvicorn.run(app="main:app", host="0.0.0.0", port=8080, reload=True)