from fastapi import APIRouter

router = APIRouter(
    prefix='/users',
    tags=['Users'],
    responses={
        404: {
            'description': 'Required resource not found'
        }
    }
)


@router.get(path='/')
async def all_users():
    try:
        return {
            'response': 'this route returns all users'
        }
    except Exception as e:
        raise e
