import random
from collections import Counter

def monte_carlo_simulation(num_trials):
    results = Counter()

    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        results[total] += 1

    probabilities = {key: value / num_trials * 100 for key, value in results.items()}
    return probabilities

def print_table(probabilities):
    print("Сума\tІмовірність")
    for key in range(2, 13):
        probability = probabilities.get(key, 0)
        print(f"{key}\t{probability:.2f}%")

def main():
    num_trials = 1000000  # Бажана кількість імітацій
    probabilities = monte_carlo_simulation(num_trials)
    print_table(probabilities)

if __name__ == "__main__":
    main()
