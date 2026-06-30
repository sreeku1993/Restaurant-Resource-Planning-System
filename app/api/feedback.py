from fastapi import APIRouter

from app.models.feedback_request import (FeedbackRequest,)

from app.services.feedback_service import (FeedbackService,)

router = APIRouter( prefix="/feedback", tags=["Feedback"],)

feedback_service = FeedbackService()


@router.post("/")
def submit_feedback(request: FeedbackRequest,):

    result = feedback_service.calculate_error(predicted=request.predicted,actual=request.actual,)

    updated_coefficient = (feedback_service.update_coefficient(reason=request.reason,error_ratio=result["error_ratio"],))
       

    return {**result,"updated_coefficient": updated_coefficient,}