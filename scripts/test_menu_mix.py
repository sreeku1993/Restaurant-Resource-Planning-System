from app.services.menu_mix_planner import MenuMixPlanner

planner = MenuMixPlanner()

orders = planner.calculate_orders(predicted_covers=100)

print(orders)