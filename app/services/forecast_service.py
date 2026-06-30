import joblib
import pandas as pd

from app.services.coefficient_service import CoefficientService
from app.utils.constants import WEATHER_MAP, DAY_MAP


class ForecastService:

    def __init__(self):
        self.model = joblib.load("app/models/forecast_model.pkl")

    def predict(self,hour: int,day_of_week: str,weather: str,promotion: bool,event: bool,):
        weather = weather.strip().title()
        day_of_week = day_of_week.strip().title()
        weather_code = WEATHER_MAP[weather]
        day_code = DAY_MAP[day_of_week]
        data = pd.DataFrame(
            [{"hour": hour,"day_of_week": day_code,"weather": weather_code,"promotion": promotion,
                    "event": event,}])

        prediction = self.model.predict(data)
        coefficient_service = CoefficientService()

        coefficients = coefficient_service.load()
        factor = coefficients.get(weather, 1.0)
        adjusted_prediction = (prediction[0] * factor)
        return round(float(adjusted_prediction),2)