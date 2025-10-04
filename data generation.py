import pandas as pd
import numpy as np

# Установите зерно генератора для воспроизводимости
np.random.seed(42)

# === Параметры генерации ===
num_days = 180          # количество дней (например, 180)
num_cars = 20          # количество машин (например, 20)
records_per_day = np.random.randint(5, 20, size=num_days)   # случайное количество поездок на день (используйте np.random.randint)

# Создайте список дат
dates = pd.date_range("2023-01-01", periods=num_days)

data = []

for i, date in enumerate(dates):
    for _ in range(records_per_day[i]):
        # Случайный ID автомобиля
        car_id = np.random.randint(1, num_cars + 1)
        
        # Сгенерируйте длительность поездки (15–180 минут)
        duration = np.random.randint(15, 181)
        
        # Дистанция примерно пропорциональна длительности, но добавьте шум
        distance = duration / 60 * 10 + np.random.normal(0, 2)
        distance = max(0, distance) # избегаем отрицательных значений
        
        # Доход зависит от дистанции (например, расстояние * коэффициент)
        revenue = distance * 15 + np.random.normal(0, 5)
        revenue = max(0, revenue)
        
        # Стоимость топлива также пропорциональна дистанции
        fuel_cost = distance * 3 + np.random.normal(0, 1)
        fuel_cost = max(0, fuel_cost)
        
        data.append([date, car_id, duration, distance, revenue, fuel_cost])

# Соберите DataFrame
df = pd.DataFrame(data, columns=["Date","Car_ID","Duration_min","Distance_km","Revenue","Fuel_cost"])

# Сохраните в CSV
df.to_csv("carsharing.csv", index=False, encoding="utf-8")

print("Файл carsharing.csv сгенерирован! Количество строк:", df.shape[0])
print(df.head())
