import random

# задаём параметры
num_ants = 10  # колво муравьев
num_cities = 5  # колво городов
max_iterations = 100  # итерации
alpha = 1.0  # влияние феромонов
beta = 2.0  # влияние эвристики
evaporation_rate = 0.5  # скорость испарения феромонов
pheromon = 100.0  # колво феромонов, выделяемых муравьем

# матрица расстояний
distances = [
    [0, 2, 9, 10, 7],
    [1, 0, 6, 4, 3],
    [15, 7, 0, 8, 3],
    [6, 3, 12, 0, 2],
    [9, 7, 5, 6, 0]
]

# инициализация феромонов
pheromones = [[1 for _ in range(num_cities)] for _ in range(num_cities)]


# расчет вероятности выбора следующего города
def calc_prob(ant, current_city):
    prob = []
    total_pheromone = 0.0

    # сумма вероятностей для доступных городов
    for city in range(num_cities):
        if city not in ant:
            tau = pheromones[current_city][city] ** alpha
            eta = (1.0 / distances[current_city][city]) ** beta
            total_pheromone += tau * eta
            prob.append(tau * eta)
        else:
            prob.append(0)  # город уже посещен муравьем

    # нормализация вероятностей
    probabilities = [prob / total_pheromone if total_pheromone > 0 else 0 for prob in prob]
    return probabilities


# выбор следующего города на основе вероятностей
def select_next_city(prob):
    r = random.random()
    total = 0
    for i, probability in enumerate(prob):
        total += prob
        if r <= total:
            return i
    return len(prob) - 1  # возвращаем последний город в случае ошибки


# обновление феромонов по всем муравьям
def update_phero(ants):
    # испарение феромонов
    for i in range(num_cities):
        for j in range(num_cities):
            pheromones[i][j] *= (1 - evaporation_rate)

    # выделение феромонов муравьями
    for ant in ants:
        length = calculate_path(ant)
        pheromone_addition = pheromon / length
        for i in range(len(ant) - 1):
            city_a = ant[i]
            city_b = ant[i + 1]
            pheromones[city_a][city_b] += pheromone_addition
            pheromones[city_b][city_a] += pheromone_addition


# расчет длины пути
def calculate_path(ant):
    length = 0
    for i in range(len(ant) - 1):
        length += distances[ant[i]][ant[i + 1]]
    length += distances[ant[-1]][ant[0]]  # возвращаемся в начальный город
    return length


# основной цикл муравьиного алгоритма
best_path = None
best_length = float('inf')

for iteration in range(max_iterations):
    ants = []

    # кпждый муравей строит свой путь
    for _ in range(num_ants):
        ant = [random.randint(0, num_cities - 1)]  # случайный стартовый город
        while len(ant) < num_cities:
            current_city = ant[-1]
            probabilities = calc_prob(ant, current_city)
            next_city = select_next_city(probabilities)
            ant.append(next_city)

        ants.append(ant)

    # обновляем феромоны
    update_phero(ants)

    # проверяем лучший путь
    for ant in ants:
        length = calculate_path(ant)
        if length < best_length:
            best_length = length
            best_path = ant

    print(f"Iteration {iteration + 1}, Best path length: {best_length}")

# вывод результатов
print("Лучший найденный путь:", best_path)
print("Длина пути:", best_length)
