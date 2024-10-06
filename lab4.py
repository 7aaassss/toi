import random
import math


def init_temp():
    return 1000.0


def min_temp():
    return 0.001


def cooling_rate():
    return 0.99

# функция для вычисления вероятности перехода к новому состоянию
def prob(current_energy, new_energy, temperature):
    if new_energy < current_energy:
        return 1.0
    return math.exp((current_energy - new_energy) / temperature)

# функция для генерации случайного соседнего решения
def solution(current_solution):
    new_solution = current_solution[:]
    i = random.randint(0, len(new_solution) - 1)
    new_solution[i] = new_solution[i] + random.uniform(-1, 1)
    return new_solution

# основная функция для алгоритма отжига
def algh(initial_solution):
    current_solution = initial_solution
    current_energy = energy(current_solution)
    temp = init_temp()

    while temp > min_temp():
        new_solution = solution(current_solution)
        new_energy = energy(new_solution)

        # проверка вероятности принятия нового решения
        if prob(current_energy, new_energy, temp) > random.random():
            current_solution = new_solution
            current_energy = new_energy

        # охлаждение системы
        temp *= cooling_rate()

    return current_solution

# функция для вычисления энергии
def energy(solution):
    return sum([x**2 for x in solution])

initial_solution = [random.uniform(-10, 10) for _ in range(5)]
best_solution = algh(initial_solution)
print("Лучшее найденное решение:", best_solution)
