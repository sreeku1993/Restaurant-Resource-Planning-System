import pandas as pd


class InventoryPlanner:

    def __init__(self):

        self.recipes = pd.read_csv("data/recipes.csv")

    def calculate_ingredient_demand(self,menu_orders: dict):

        ingredient_demand = {}

        for menu_item, order_count in menu_orders.items():

            recipe_rows = self.recipes[self.recipes["menu_item"] == menu_item]

            for _, row in recipe_rows.iterrows():

                ingredient = row["ingredient"]
                quantity = row["quantity"]

                required_qty = (order_count * quantity)

                ingredient_demand[ingredient] = (ingredient_demand.get(ingredient,0)+ required_qty)

        return ingredient_demand
    
    def generate_order_plan(self,ingredient_demand: dict):
        inventory = pd.read_csv("data/inventory.csv")
        suppliers = pd.read_csv("data/suppliers.csv")
        order_plan = {}

        for ingredient, demand in ingredient_demand.items():

            stock_row = inventory[inventory["ingredient"] == ingredient]

            if stock_row.empty:
                continue

            current_stock = int(stock_row.iloc[0]["current_stock"])
            shelf_life_days = int(stock_row.iloc[0]["shelf_life_days"])
            shortage = float(max(0,demand - current_stock))
            supplier_row = suppliers[suppliers["ingredient"] == ingredient]

            lead_time_days = int(supplier_row.iloc[0]["lead_time_days"])
            order_plan[ingredient] = {"required": demand,"in_stock": current_stock,
                "shelf_life_days": shelf_life_days,"lead_time_days": lead_time_days,
                "to_order": shortage
            }
            

        return order_plan