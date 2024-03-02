from fastapi import APIRouter

router = APIRouter(
    prefix='/contact',
    tags=['Contact Us'],
    responses={
        404: {
            'description': 'Required resource not found'
        }
    }
)


@router.post(path='/')
async def all_portfolios():
    try:
        return {
            'response': 'This route is used to send queries to server'
        }
    except Exception as e:
        raise e
