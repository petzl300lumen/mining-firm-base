from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Hello world"}
    return RedirectResponse('/docs')

@app.get('/users')
def get():
    return {"message": "def users"}

@app.get('/users/{user_id}/')
def get_user_id(user_id:int):
    return {
        "user":{
            "id": user_id,
        },
    }

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True)
    
    #http://127.0.0.1:8000/