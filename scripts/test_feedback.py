from app.services.feedback_service import FeedbackService

service = FeedbackService()

result = service.calculate_error(predicted=120,actual=85,)

print(result)
ratio = 0.71

updated = service.update_coefficient(reason="Rain",error_ratio=ratio)

print(updated)