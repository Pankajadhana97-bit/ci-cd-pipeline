from fastapi import FastAPI

app = FastAPI(
    title="FastAPI-(HashedIn University Revisit)",
    description="Let's create the crud applications which will work with the database of our application which is build over FastAPI",
    contact={
        "name": "Pankaj Adhana (Backend Developer)",
        "email": "pankajadhana97@gmail.com"
    },
    docs_url='/'
)


@app.get("/hello-world")
async def root():
    return {"message": "Hello World from the amazon web services using dockerhub"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello world {name}  "}
