import numpy as np
import matplotlib.pyplot as plt

#1
np.random.seed(42) 
products = np.random.normal(20000, 5000, 1000)
entertainment = np.random.normal(10000, 4000, 1000)
online = np.random.normal(15000, 7000, 1000)

#2
expenses_matrix = np.column_stack((products, entertainment, online))
total_expenses = np.sum(expenses_matrix, axis=1)  # axis=1 суммирует по строкам
correlation_matrix = np.corrcoef(expenses_matrix, rowvar=False)
print("Матрица корреляции:\n", correlation_matrix)

#3
top_5_percent_threshold = np.percentile(total_expenses, 95)
top_5_percent_indices = np.where(total_expenses >= top_5_percent_threshold)
top_5_percent_expenses = total_expenses[top_5_percent_indices]

total_expenses_all = np.sum(total_expenses)
total_expenses_top_5_percent = np.sum(top_5_percent_expenses)
percentage_of_total = (total_expenses_top_5_percent / total_expenses_all) * 100
print(f"Топ-5% клиентов формируют {percentage_of_total:.2f}% общих расходов.")

#4
plt.figure(figsize=(10, 6))
plt.boxplot([products, entertainment, online], labels=['Продукты', 'Развлечения', 'Онлайн-покупки'])
plt.ylabel('Расходы (руб)')
plt.title('Распределение расходов по категориям')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(products, online, alpha=0.5)
plt.xlabel('Продукты (руб)')
plt.ylabel('Онлайн-покупки (руб)')
plt.title('Зависимость расходов на продукты и онлайн-покупки')
plt.grid(True)
plt.show()