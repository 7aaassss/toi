import random


# функция для оптимизации
def fitness_function(individual):
    return sum(individual)


# создание начальной популяции
def create_population(size, hromo_l):
    population = []
    for _ in range(size):
        individual = [random.randint(0, 1) for _ in range(hromo_l)]
        population.append(individual)
    return population


# отбор лучшего решения (селекция)
def selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual, fitness in zip(population, fitnesses):
        current += fitness
        if current > pick:
            return individual


# скрещивание (кроссовер) двух индивидов
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


# мутация индивида
def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # инвертировать бит


# основной цикл генетического алгоритма
def genetic_algorithm(pop_size, hromo_l, generations, mutation_rate):
    # шаг 1: инициализация популяции
    population = create_population(pop_size, hromo_l)

    for generation in range(generations):
        # шаг 2: оценка приспособленности (фитнес)
        fitnesses = [fitness_function(individual) for individual in population]

        # шаг 3: отбор родителей
        new_population = []
        for _ in range(pop_size // 2):
            parent1 = selection(population, fitnesses)
            parent2 = selection(population, fitnesses)

            # шаг 4: скрещивание
            child1, child2 = crossover(parent1, parent2)

            # шаг 5: мутация
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)

            new_population.extend([child1, child2])

        population = new_population

        # лучшая особь текущего поколения
        best_individual = max(population, key=fitness_function)
        best_fitness = fitness_function(best_individual)
        print(f"поколение {generation + 1}: лучшая приспособленность = {best_fitness}")

    # возврат лучшего решения
    best_individual = max(population, key=fitness_function)
    return best_individual


# параметры алгоритма
population_size = 10
hromo_l = 8
generations = 20
mutation_rate = 0.1

# запуск генетического алгоритма
best_solution = genetic_algorithm(population_size, hromo_l, generations, mutation_rate)
print("лучшее решение:", best_solution)
