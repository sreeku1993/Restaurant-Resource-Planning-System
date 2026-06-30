from math import ceil

from app.utils.staff_config import BARTENDER_CAPACITY, CHEF_CAPACITY, WAITER_CAPACITY


class StaffPlanner:

    def calculate_staff(self, predicted_covers: float):

        waiters = ceil(predicted_covers / WAITER_CAPACITY)

        chefs = ceil(predicted_covers / CHEF_CAPACITY)

        bartenders = ceil(predicted_covers / BARTENDER_CAPACITY)

        return {"waiters": waiters,"chefs": chefs,"bartenders": bartenders,}