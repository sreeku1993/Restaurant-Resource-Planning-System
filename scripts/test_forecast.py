from app.services.forecast_service import ForecastService

service = ForecastService()

prediction = service.predict(hour=19,day_of_week="saturday",weather="sunny",promotion=True,event=False,)

print(f"Predicted Covers: {prediction}")