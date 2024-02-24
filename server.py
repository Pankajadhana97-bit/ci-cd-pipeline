from fastapi import FastAPI


app = FastAPI(
    title="FastAPI -(HashedIn University Revisit)",
    description="Performing the crud operations over the database and making it robust to handle the wide variety of "
                "the user load",
    contact={
        "name": "Pankaj Adhana", "email": "pankajadhana97@gmail.com"
    },
    docs_url='/'
)


@app.get("/root")
async def root():
    return {"message": "Hello World from the amazon web services"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello world {name} "}
