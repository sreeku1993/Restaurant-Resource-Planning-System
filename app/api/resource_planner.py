from fastapi import APIRouter

from app.models.forecast_request import (ForecastRequest,)

from app.models.resource_plan_response import (ResourcePlanResponse,)

from app.services.resource_planner_service import (ResourcePlannerService,)

router = APIRouter(prefix="/planner",tags=["Resource Planner"],)

planner_service = ResourcePlannerService()


@router.post("/plan-resources",response_model=ResourcePlanResponse,)
def plan_resources(request: ForecastRequest,):

    result = planner_service.plan_resources(hour=request.hour,day_of_week=request.day_of_week,
        weather=request.weather,promotion=request.promotion,event=request.event,)

    return result