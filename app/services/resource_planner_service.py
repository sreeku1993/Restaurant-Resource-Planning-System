from app.services.forecast_service import ForecastService
from app.services.staff_planner import StaffPlanner
from app.services.menu_mix_planner import MenuMixPlanner
from app.services.inventory_planner import InventoryPlanner


class ResourcePlannerService:

    def __init__(self):

        self.forecast_service = ForecastService()

        self.staff_planner = StaffPlanner()

        self.menu_mix_planner = MenuMixPlanner()

        self.inventory_planner = InventoryPlanner()

    def plan_resources(self,hour: int,day_of_week: str,weather: str,promotion: bool,event: bool,):

        # Step 1: Forecast covers
        predicted_covers = self.forecast_service.predict(
            hour=hour,
            day_of_week=day_of_week,
            weather=weather,
            promotion=promotion,
            event=event,
        )

        # Step 2: Staff planning
        staff_plan = self.staff_planner.calculate_staff(predicted_covers)

        # Step 3: Menu mix planning
        menu_orders = (self.menu_mix_planner.calculate_orders(predicted_covers))
            

        # Step 4: Ingredient demand
        ingredient_demand = (self.inventory_planner.calculate_ingredient_demand(menu_orders))
          

        # Step 5: Inventory planning
        order_plan = (self.inventory_planner.generate_order_plan(ingredient_demand))
        

        return {"predicted_covers": predicted_covers,"staff_plan": staff_plan,"menu_orders": menu_orders, "ingredient_demand": ingredient_demand,"order_plan": order_plan,}