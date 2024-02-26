from fastapi import APIRouter

router = APIRouter(
    prefix='/portfolio',
    tags=['Portfolio'],
    responses={
      404 : {
        'description' : 'Requirred resource not found'
      }
    }
)

@router.get(path='/')
async def all_portfolios():
  try:
    return {
      'response' : 'This route will give you all the services that we offer'
    }
  except Exception as e:
    raise e


