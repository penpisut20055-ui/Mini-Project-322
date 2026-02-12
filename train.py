# train.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# -----------------------
# 1) สร้าง Dataset ตัวอย่าง
# -----------------------

np.random.seed(42)

n = 200

data = pd.DataFrame({
    "area": np.random.randint(30, 500, n),
    "bedrooms": np.random.randint(1, 5, n),
    "bathrooms": np.random.randint(1, 4, n),
    "age": np.random.randint(0, 30, n),
})

# สร้างราคาแบบสมการจำลอง
data["price"] = (
    50000
    + data["area"] * 3000
    + data["bedrooms"] * 50000
    + data["bathrooms"] * 30000
    - data["age"] * 2000
    + np.random.normal(0, 20000, n)
)

# -----------------------
# 2) Split Train/Test
# -----------------------

X = data[["area", "bedrooms", "bathrooms", "age"]]
y = data["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------
# 3) Train Model
# -----------------------

model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------
# 4) Evaluate Model
# -----------------------

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

# -----------------------
# 5) Save Model
# -----------------------

joblib.dump(model, "house_price_model.pkl")
print("Model saved successfully!")