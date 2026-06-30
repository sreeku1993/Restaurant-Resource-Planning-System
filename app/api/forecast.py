from fastapi import APIRouter
from app.services.forecast_service import ForecastService

router = APIRouter()

forecast_service = ForecastService()


@router.post("/forecast")
def forecast(hour: int,day_of_week: str,weather: str,promotion: bool,):
    prediction = forecast_service.predict(hour=hour,day_of_week=day_of_week,weather=weather,promotion=promotion,event=event,)

    return {"predicted_covers": prediction}