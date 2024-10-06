#узел дерева
class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    #обход дерева
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")



class Leaf:
    def __init__(self, char):
        self.char = char


    def walk(self, code, acc):
        code[self.char] = acc


# Подсчет частоты символов
def calc_freq(s):
    frequencies = {}
    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


# посторение дерева
def build_huffman_tree(s):
    frequencies = calc_freq(s)

    # список узлов
    nodes = [(freq, Leaf(char)) for char, freq in frequencies.items()]

    # поиск минимальных элементов
    def find_two_smallest(nodes):
        nodes.sort(key=lambda x: x[0])  #сортируем по частоте
        return nodes.pop(0), nodes.pop(0)  # берем два минимальных узла

    # объединяем два наименьших узла
    while len(nodes) > 1:
        (freq1, left), (freq2, right) = find_two_smallest(nodes)
        new_node = Node(left, right)  # создаем родительский узел
        nodes.append((freq1 + freq2, new_node))  # добавляем новый узел обратно

    return nodes[0][1]  # возвращаем корень дерева


# коды для символа
def huffman_code(tree):
    code = {}
    tree.walk(code, "")
    return code


# функция кодирования строки
def _encode(s, code):
    return "".join(code[char] for char in s)


# функция декодирования строки
def _decode(encoded_str, tree):
    decoded_str = []
    node = tree
    for bit in encoded_str:
        node = node.left if bit == "0" else node.right
        if isinstance(node, Leaf):
            decoded_str.append(node.char)
            node = tree
    return "".join(decoded_str)


# пример
s = "московский политех"


tree = build_huffman_tree(s)


code = huffman_code(tree)

# кодируем строку
encoded = _encode(s, code)

# декодируем строку
decoded = _decode(encoded, tree)

print(f"Оригинальная строка: {s}")
print(f"Коды символов: {code}")
print(f"Закодированная строка: {encoded}")
print(f"Декодированная строка: {decoded}")
