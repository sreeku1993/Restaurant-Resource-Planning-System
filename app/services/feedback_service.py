from app.services.coefficient_service import CoefficientService


class FeedbackService:

    def calculate_error(self,predicted: float,actual: float,):

        error = actual - predicted

        error_ratio = actual / predicted

        return {"error": round(error, 2), "error_ratio": round(error_ratio, 2),
        }
    
    def update_coefficient(self,reason,error_ratio):
        coefficient_service = CoefficientService()

        coefficients = coefficient_service.load()

        current_value = coefficients.get(reason,1.0)

        new_value = round((current_value + error_ratio) / 2, 2)

        coefficients[reason] = new_value

        coefficient_service.save(coefficients)

        return new_value