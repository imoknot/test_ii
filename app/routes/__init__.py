from fastapi import APIRouter

from . import ii_test, main


router = APIRouter()
router.include_router(main.router)
router.include_router(ii_test.router)
