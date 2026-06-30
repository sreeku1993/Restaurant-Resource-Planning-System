from pydantic import BaseModel


class ForecastRequest(BaseModel):

    hour: int

    day_of_week: str

    weather: str

    promotion: bool = False

    event: bool = False