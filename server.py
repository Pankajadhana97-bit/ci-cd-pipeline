from fastapi import FastAPI

app = FastAPI(
    title="FastAPI -(HashedIn University Revisit)",
    description="AI is future and kunal is certified Randi",
    contact={
        "name": "Somil Trader", "email": "pankajadhana97@gmail.com"
    },
    docs_url='/'
)


@app.get("/root")
async def root():
    return {"message": "Hello World from the amazon web services using dockerhub"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello world {name}  "}
