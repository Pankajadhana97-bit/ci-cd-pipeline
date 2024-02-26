from fastapi import FastAPI
from .views import users,services,portfolio,company,contactus

app = FastAPI(
    title="kspinfotech - (Backend necessary endpoints to develop FE)",
    description="backend service for FE of kspinfotech.com",
    contact={
        "name": "Pankaj Adhana",
        "email": "pankajadhana97@gmail.com"
    },
    docs_url='/',
    version="1.1.0"
)

app.include_router(users.router)
app.include_router(services.router)
app.include_router(portfolio.router)
app.include_router(company.router)
app.include_router(contactus.router)


@app.get('/health', tags=['Health'])
async def root():
    try:
        return {
            "message" : "your application is working fine"
        }
    except Exception as e:
        raise e
    
