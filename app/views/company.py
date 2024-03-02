from fastapi import APIRouter

router = APIRouter(
    prefix='/company',
    tags=['Company'],
    responses={
        404: {
            'description': 'Required resource not found'
        }
    }
)


@router.get(path='/')
async def all_portfolios():
    try:
        return {
            'response': 'This route will give all the details regarding the company'
        }
    except Exception as e:
        raise e
