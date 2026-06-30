import pandas as pd


class MenuMixPlanner:

    def __init__(self):
        self.menu_mix = pd.read_csv("data/menu_mix.csv")

    def calculate_orders(self,predicted_covers: float):

        orders = {}

        for _, row in self.menu_mix.iterrows():

            menu_item = row["menu_item"]
            percentage = row["percentage"]

            orders[menu_item] = round(predicted_covers * percentage)

        return orders