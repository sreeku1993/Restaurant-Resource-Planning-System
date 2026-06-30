import pandas as pd
import random
from datetime import datetime, timedelta

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

weather_options = ["Sunny", "Cloudy", "Rain"]

rows = []

current_date = start_date

while current_date <= end_date:

    day_of_week = current_date.strftime("%A")

    weather = random.choices(weather_options,weights=[0.5, 0.3, 0.2])[0]

    promotion = random.choice([0, 0, 0, 1])
    event = random.choice([0, 0, 0, 0, 1])

    for hour in range(24):
        covers = 5
        # Lunch rush
        if 12 <= hour <= 14:
            covers += 35
        # Dinner rush
        if 18 <= hour <= 21:
            covers += 55
        # Weekend boost
        if day_of_week in ["Saturday", "Sunday"]:
            covers += 20
        # Weather impact
        if weather == "Rain":
            covers *= 0.8
        elif weather == "Sunny":
            covers *= 1.1
        # Promotion impact
        if promotion:
            covers *= 1.2
        # Event impact
        if event:
            covers *= 1.3
        # Random variation
        covers += random.randint(-5, 5)
        covers = max(0, round(covers))
        rows.append([current_date.strftime("%Y-%m-%d"),hour,day_of_week,weather,promotion,event,covers,])

    current_date += timedelta(days=1)

df = pd.DataFrame(rows,columns=["date","hour","day_of_week","weather","promotion","event","covers",],)

df.to_csv("data/historical_sales.csv", index=False)

print(f"Generated {len(df)} rows")