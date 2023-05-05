import sys
sys.path.append('..')
from fastapi import APIRouter
from services.read_root import read_root_test

router = APIRouter()

@router.get("/")
async def read_root():
    return read_root_test()