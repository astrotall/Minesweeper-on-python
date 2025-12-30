import random


def generate_sweeper_map(height, width, mine_probability):
    # Создаем пустую карту, заполняя ее нулями
    sweeper_map = [[0 for _ in range(width)] for _ in range(height)]
    mines_counter = 0
    # Заполняем карту минами на основе заданной вероятности
    for row in range(height):
        for col in range(width):
            if random.random() < mine_probability:
                sweeper_map[row][col] = 'm'  # 'm' представляет мины
                mines_counter += 1

    return sweeper_map, mines_counter


# Пример использования функции для создания карты 10x10 с вероятностью 0.2 для каждой клетки содержать мину
height = 15
width = 15
mine_probability = 0.2
sweeper_map, count = generate_sweeper_map(height, width, mine_probability)

# Выводим полученную карту
#for row in sweeper_map:
#    print(' '.join(map(str, row)))  # Выводим каждую строку карты
