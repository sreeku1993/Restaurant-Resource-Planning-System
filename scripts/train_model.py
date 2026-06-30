import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
import joblib
from app.utils.constants import WEATHER_MAP, DAY_MAP
df = pd.read_csv("data/historical_sales.csv")


df["weather"] = df["weather"].map(WEATHER_MAP)
df["day_of_week"] = df["day_of_week"].map(DAY_MAP)
X = df[["hour","day_of_week","weather","promotion","event",]]
y = df["covers"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = XGBRegressor(n_estimators=100,max_depth=5,learning_rate=0.1)

model.fit(X_train, y_train)
joblib.dump(model, "app/models/forecast_model.pkl")
print("Model saved successfully")
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print(f"MAE: {mae:.2f}")