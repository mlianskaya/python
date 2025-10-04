import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# === 0. Загрузка данных ===
# Подсказка: используйте pd.read_csv("carsharing.csv", parse_dates=["Date"])
data = pd.read_csv("carsharing.csv", parse_dates=["Date"])

# Добавьте новые колонки
# Profit = Revenue - Fuel_cost
# Avg_speed = Distance_km / (Duration_min/60)
data["Profit"] = data["Revenue"] - data["Fuel_cost"]
data["Avg_speed"] = data["Distance_km"] / (data["Duration_min"]/60)

# === 1. Предварительный анализ ===
# Найдите топ-5 автомобилей по выручке
top_cars = data.groupby("Car_ID")["Revenue"].sum().nlargest(5)
# Найдите 5 машин с наименьшей рентабельностью
low_profit_cars = data.groupby("Car_ID")["Profit"].mean().nsmallest(5)

print("Топ-5 автомобилей по выручке:\n", top_cars)
print("\n5 автомобилей с наименьшей рентабельностью:\n", low_profit_cars)

# === 2. Временные ряды ===
# Средняя выручка по дням
daily_revenue = data.groupby("Date")["Revenue"].mean()
# 7-дневное скользящее среднее
rolling_avg = daily_revenue.rolling(window=7).mean()

# Постройте график динамики
plt.figure(figsize=(10,5))
plt.plot(daily_revenue.index, daily_revenue.values, label="Средняя выручка")
plt.plot(rolling_avg.index, rolling_avg.values, label="7-дневное среднее")
plt.legend()
plt.xlabel("Дата")
plt.ylabel("Доход")
plt.title("Среднесуточный доход")
plt.show()

# === 3. Будни vs выходные ===
# Создайте колонку IsWeekend (True/False)
data["Weekday"] = data["Date"].dt.weekday
data["IsWeekend"] = data["Weekday"].isin([5, 6])

# Сравните средние значения
weekend_stats = data.groupby("IsWeekend")[["Duration_min", "Revenue", "Avg_speed"]].mean()
print("\nБудни vs выходные:\n", weekend_stats)

# Постройте график
weekend_stats.T.plot(kind="bar")
plt.ylabel("Сдредние значения")
plt.title("Weekday vs Weekend")
plt.show()

# === 4. Сравнительный анализ поездок ===
# Постройте гистограмму длительности поездок
plt.hist(data["Duration_min"], bins=30)
plt.xlabel("Продолжительность (min)")
plt.ylabel("Частота")
plt.title("Распределение продолжительности поездок")
plt.show()

# Найдите 95-й перцентиль и выделите аномальные поездки
threshold = np.percentile(data["Duration_min"], 95)
print("Аномальные поездки:\n", data[data["Duration_min"] > threshold])

# Постройте распределение средних скоростей
plt.hist(data["Avg_speed"], bins=25)
plt.xlabel("Средняя скорость (km/h)")
plt.ylabel("Частота")
plt.title("Распределение средних скоростей")
plt.show()

# === 5. Кластеризация автомобилей ===
# Рассчитайте средние показатели для каждого Car_ID
car_features = data.groupby("Car_ID")[["Revenue", "Duration_min", "Avg_speed"]].mean()

# Нормализация данных
scaled = StandardScaler().fit_transform(car_features)

# Кластеризация k-means
kmeans = KMeans(n_clusters=3, random_state=42,n_init = 10)
labels = kmeans.fit_predict(scaled)
car_features["Cluster"] = labels

# Постройте scatter plot
plt.scatter(car_features["Revenue"], car_features["Duration_min"], c=labels, cmap="viridis")
plt.xlabel("Средний доход")
plt.ylabel("Средняя продолжительность")
plt.title("Кластеризация автомобилей")
plt.show()

# === 6. Корреляции ===
corr = data[["Duration_min", "Distance_km", "Revenue", "Fuel_cost", "Avg_speed"]].corr()
plt.imshow(corr, cmap="coolwarm")
plt.colorbar()
plt.title("Матрица корреляции")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.show()

# === 7. Прогнозирование ===
# Создайте массив дней
days = np.arange(len(daily_revenue))

# Постройте полином (polyfit и poly1d)
coeffs = np.polyfit(days, daily_revenue.values, deg=3)
poly = np.poly1d(coeffs)

# Прогноз на 14 дней вперёд
future_days = np.arange(len(daily_revenue) + 14)
future_pred = poly(future_days)

# График прогноза
plt.plot(daily_revenue.index, daily_revenue.values, label="Фактическая выручка")
plt.plot(daily_revenue.index.union(pd.date_range(daily_revenue.index[-1] + pd.Timedelta(days=1), periods=14)), future_pred, label="Прогноз", linestyle="--")
plt.xlabel("Дата")
plt.ylabel("Доход")
plt.title("Прогноз дохода")
plt.legend()
plt.show()
