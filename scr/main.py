from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse
from users.routers import router as users_router

app = FastAPI()

app.include_router(users_router, prefix='/users') #main prefix

@app.get('/')
def root():
    return {"message": "Hello world"}
    return RedirectResponse('/docs')


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True)
    
    #http://127.0.0.1:8000/