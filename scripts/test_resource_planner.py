from app.services.resource_planner_service import (ResourcePlannerService)

planner = ResourcePlannerService()

result = planner.plan_resources(hour=19,day_of_week="Saturday",weather="Sunny",promotion=True,event=False,)

print(result)