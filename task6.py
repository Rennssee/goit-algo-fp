def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item_name, item_info in sorted_items:
        if total_cost + item_info['cost'] <= budget:
            selected_items.append(item_name)
            total_cost += item_info['cost']
            total_calories += item_info['calories']
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    num_items = len(item_names)
    
    # Створюємо матрицю dp для збереження оптимальної кількості калорій для кожного підмножини
    dp = [[0] * (budget + 1) for _ in range(num_items + 1)]
    
    for i in range(1, num_items + 1):
        for j in range(budget + 1):
            current_item = items[item_names[i - 1]]
            if current_item['cost'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - current_item['cost']] + current_item['calories'])
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Відновлюємо оптимальний набір страв
    selected_items = []
    i, j = num_items, budget
    while i > 0 and j > 0:
        current_item = items[item_names[i - 1]]
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(item_names[i - 1])
            j -= current_item['cost']
        i -= 1
    
    selected_items.reverse()
    return selected_items, dp[num_items][budget]

# Задані дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Бюджет
budget = 80

# Виклик функцій
greedy_result = greedy_algorithm(items, budget)
dynamic_result = dynamic_programming(items, budget)

# Виведення результатів
print("Greedy Algorithm:")
print("Selected items:", greedy_result[0])
print("Total cost:", greedy_result[1])
print("Total calories:", greedy_result[2])
print()

print("Dynamic Programming:")
print("Selected items:", dynamic_result[0])
print("Total calories:", dynamic_result[1])
