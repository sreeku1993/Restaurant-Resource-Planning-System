from pydantic import BaseModel


class FeedbackRequest(BaseModel):

    predicted: float

    actual: float

    reason: str