from app.services.forecast_service import ForecastService
from app.services.staff_planner import StaffPlanner
from app.services.menu_mix_planner import MenuMixPlanner
from app.services.inventory_planner import InventoryPlanner


def main():

    # Step 1: Forecast covers
    forecast_service = ForecastService()

    predicted_covers = forecast_service.predict(hour=19,day_of_week="Saturday",weather="Sunny",promotion=True,event=False,)

    print("\n===== FORECAST =====")
    print(f"Predicted Covers: {predicted_covers}")

    # Step 2: Staff planning
    staff_planner = StaffPlanner()

    staff_plan = staff_planner.calculate_staff(predicted_covers)

    print("\n===== STAFF PLAN =====")
    print(staff_plan)

    # Step 3: Menu mix planning
    menu_mix_planner = MenuMixPlanner()

    menu_orders = menu_mix_planner.calculate_orders(predicted_covers)

    print("\n===== MENU ORDERS =====")
    print(menu_orders)

    # Step 4: Ingredient demand
    inventory_planner = InventoryPlanner()

    ingredient_demand = (inventory_planner.calculate_ingredient_demand(menu_orders))

    print("\n===== INGREDIENT DEMAND =====")
    print(ingredient_demand)

    # Step 5: Order recommendations
    order_plan = (inventory_planner.generate_order_plan(ingredient_demand))

    print("\n===== ORDER PLAN =====")
    print(order_plan)


if __name__ == "__main__":
    main()