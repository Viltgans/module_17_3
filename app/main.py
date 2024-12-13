from fastapi import FastAPI
from routers import task, user

app = FastAPI()

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)

## Запуск:
## 1. Переход в директорию: cd module_17/homework_17_1/app/
## 2. Сам запуск: uvicorn main:app --reload