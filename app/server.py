from fastapi import FastAPI

app = FastAPI(
    title="FastAPI -(Crud Application with JWT support)",
    description="applying the concepts which we learnt in space of FastAPI",
    contact={
        "name": "Pankaj Adhana",
        "email": "pankajadhana97@gmail.com"
    },
    docs_url='/',
    version="1.0.0"
)


@app.get('/health', tags=['Health'])
async def health():
    try:
        return {
            "message" : "your application is working fine"
        }
    except Exception as e:
        raise e
    

@app.get('/hello-world',tags=['Health'])
async def hello_world():
    try:
        return {
            'message' : "Hello world"
        }
    except Exception as e:
        raise e