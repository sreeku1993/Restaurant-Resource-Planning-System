from pydantic import BaseModel
from typing import Dict


class ResourcePlanResponse(BaseModel):

    predicted_covers: float

    staff_plan: Dict

    menu_orders: Dict

    ingredient_demand: Dict

    order_plan: Dict