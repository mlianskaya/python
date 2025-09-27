import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

# ---------- СИМУЛЯЦИЯ ----------
mon_thu = np.random.normal(200, 40, 4)
fri = np.random.normal(150, 30, 1)
sat_sun = np.random.normal(300, 50, 2)

# Убедимся, что количество посетителей не отрицательное (в реальности может быть 0)
visitors = np.concatenate((np.maximum(0, mon_thu), np.maximum(0, fri), np.maximum(0, sat_sun)))

# ---------- АНАЛИЗ ----------
max_visitors_index = np.argmax(visitors)
day_with_max_visitors = days[max_visitors_index]
max_visitors_count = visitors[max_visitors_index]
print(f"День с максимальным количеством посетителей: {day_with_max_visitors} ({max_visitors_count:.0f} чел.)")

print(f"Общее число посетителей за неделю: {np.sum(visitors):.0f} чел.")
print(f"Среднее число посетителей в день: {np.mean(visitors):.2f} чел.")
print(f"Медиана числа посетителей в день: {np.median(visitors):.2f} чел.")

# ---------- ВИЗУАЛИЗАЦИЯ ----------
colors = ['skyblue'] * 5 + ['lightcoral'] * 2
plt.figure(figsize=(10,6))
plt.bar(days, visitors, color=colors)
plt.xlabel('День недели')
plt.ylabel('Количество посетителей')
plt.title('Распределение посещений спортзала по дням недели')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, count in enumerate(visitors):
    plt.text(i, count + 5, f"{count:.0f}", ha='center', va='bottom', fontsize=9)

plt.tight_layout() # Автоматически подгоняет параметры подложки, чтобы избежать обрезки
plt.show()