from fastapi import APIRouter

from app.services.coefficient_service import (CoefficientService,)

router = APIRouter(prefix="/coefficients",tags=["Coefficients"],)

coefficient_service = CoefficientService()


@router.get("/")
def get_coefficients():

    return coefficient_service.load()