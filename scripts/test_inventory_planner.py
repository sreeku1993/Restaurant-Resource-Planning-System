import pandas as pd

from app.services.inventory_planner import InventoryPlanner

planner = InventoryPlanner()

orders = {"Beef Burger": 35,"Chicken Burger": 25,"French Fries": 25,"Soft Drink": 15,}

result = planner.calculate_ingredient_demand(orders)
plan = planner.generate_order_plan(result)

print(plan)
print(result)
inventory = pd.read_csv("data/inventory.csv")
recipes=pd.read_csv("data/recipes.csv")
print("inventory unique",inventory["ingredient"].unique())
print("recipes unique", recipes["ingredient"].unique())