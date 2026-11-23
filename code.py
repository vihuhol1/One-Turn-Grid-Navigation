# Roman's One-Turn Grid Navigation Method
# Автор: Роман Подковыркин
# Дата: 07.06.2026
def find_route(A, B):
    """
    Построение маршрута между двумя точками
    на свободной прямоугольной сетке.
    """
    # 1. Получаем координаты точек
    x1, y1 = A
    x2, y2 = B
    # 2. Строим вертикальную линию через A
    vertical_line = [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    # 3. Строим горизонтальную линию через B
    horizontal_line = [(x, y2) for x in range(min(x1, x2), max(x1, x2) + 1)]
    # 4. Находим пересечение двух линий
    intersection = set(vertical_line) & set(horizontal_line)
    # 5. Получаем точку поворота
    P = intersection.pop()
    # 6. Формируем маршрут
    return [A, P, B]
# Пример работы
A = (0, 0)
B = (2, 1)
route = find_route(A, B)
print("Начальная точка:", A)
print("Конечная точка:", B)
print("Маршрут:", route)