from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/')
def root():
    #return {"message": "Hello world"}
    return RedirectResponse('/docs')

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True)