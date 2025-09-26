import numpy as np
import matplotlib.pyplot as plt

# 1. генерация выборки
np.random.seed(42)

informatics = np.random.normal(3.5, 1.5, 250)
economics = np.random.normal(2.5, 1.0, 250)
philology = np.random.normal(2.0, 0.8, 250)

# 2. Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(informatics, bins=20, alpha=0.5, label='Информатика')
plt.hist(economics, bins=20, alpha=0.5, label='Экономика')
plt.hist(philology, bins=20, alpha=0.5, label='Филология')
plt.xlabel('Время в соцсетях (часы)')
plt.ylabel('Количество студентов')
plt.title('Распределение времени в соцсетях по факультетам')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

# 3. Построение boxplot
plt.figure(figsize=(8, 6))
plt.boxplot([informatics, economics, philology], labels=['Информатика', 'Экономика', 'Филология'])
plt.ylabel('Время в соцсетях (часы)')
plt.title('Сравнение времени в соцсетях по факультетам (Boxplot)')
plt.grid(True)
plt.show()

# 4. Рассчет статистики
faculties = {
    'Информатика': informatics,
    'Экономика': economics,
    'Филология': philology
}

for name, data in faculties.items():
    mean = np.mean(data)
    median = np.median(data)
    std = np.std(data)
    over_4_hours = np.sum(data > 4) / len(data) * 100

    print(f"Факультет: {name}")
    print(f"  Среднее: {mean:.2f}")
    print(f"  Медиана: {median:.2f}")
    print(f"  Стандартное отклонение: {std:.2f}")
    print(f"  Процент студентов > 4 часов: {over_4_hours:.2f}%")
    print()
