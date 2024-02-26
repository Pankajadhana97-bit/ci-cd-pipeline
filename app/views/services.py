from fastapi import APIRouter

router = APIRouter(
    prefix='/services',
    tags=['Services'],
    responses={
      404 : {
        'description' : 'Requirred resource not found'
      }
    }
)

@router.get(path='/')
async def all_services():
  try:
    return {
      'response' : 'This route will give you all the services that we offer'
    }
  except Exception as e:
    raise e


