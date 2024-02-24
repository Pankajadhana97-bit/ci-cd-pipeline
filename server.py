from fastapi import FastAPI

app = FastAPI(
    title="FastAPI -(HashedIn University Revisit)",
    description="AWS connection practice and deploying Backend service which is built over FastAPI",
    contact={
        "name": "Kunal Randi", "email": "pankajadhana97@gmail.com"
    },
    docs_url='/'
)


@app.get("/root")
async def root():
    return {"message": "Hello World from the amazon web services using dockerhub"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello world {name}  "}
