import uvicorn
from fastapi import FastAPI
from api import router


app = FastAPI()
app.include_router(router)


@app.get('/')
def root():
    return {'message': 'hello'}



if __name__ == '__main__':
    from settings import settings

    uvicorn.run(
        'app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True
    )
