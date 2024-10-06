print("Введите строку для арифметического кодирования")
s = input()

#тестовая строка
#s = "алгоритм_кодирования"


def otr(stroka: str) -> dict:
    d = {}
    for i in set(stroka):
        d[i] = stroka.count(i) / len(stroka)


    return d

x = otr(s)

def create_int(d: dict):
    intervals = {}
    lower_bound = 0

    for symbol, probability in d.items():
        upper_bound = lower_bound + probability  # верхняя граница = нижняя граница + вероятность символа
        intervals[symbol] = (lower_bound, upper_bound)
        lower_bound = upper_bound  # обновляем нижнюю границу для следующего символа

    return intervals




def _encode(s: str, intervals: dict):
    lower_bound = 0.0
    upper_bound = 1.0


    for symbol in s:

        symbol_interval = intervals[symbol]

        # обновляем границы интервала
        range_width = upper_bound - lower_bound
        new_lower_bound = lower_bound + range_width * symbol_interval[0]
        new_upper_bound = lower_bound + range_width * symbol_interval[1]

        # обновляем границы
        lower_bound = new_lower_bound
        upper_bound = new_upper_bound


    return (lower_bound + upper_bound) / 2

def _decode(encoded_string: float, intervals: dict, message_length: int):

    lower_bound = 0.0
    upper_bound = 1.0
    decoded_message = ""

    # ищем символы один за другим
    for _ in range(message_length):
        # текущее значение в диапазоне
        range_width = upper_bound - lower_bound
        value_in_range = (encoded_string - lower_bound) / range_width


        for symbol, (symbol_lower, symbol_upper) in intervals.items():
            if symbol_lower <= value_in_range < symbol_upper:
                decoded_message += symbol
                new_lower_bound = lower_bound + range_width * symbol_lower
                new_upper_bound = lower_bound + range_width * symbol_upper
                lower_bound = new_lower_bound
                upper_bound = new_upper_bound
                break

    return decoded_message


# вероятности символов
probabilities = otr(s)

# интервалы символов
intervals = create_int(probabilities)

# строка для кодирования
encoded_string = _encode(s, intervals)

print(f"Закодированное значение для строки '{s}': {encoded_string}")

decoded_message = _decode(encoded_string, intervals, len(s))
print(f"Декодированная строка: {decoded_message}")