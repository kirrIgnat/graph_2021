import numpy as np


def xAngleCoord(width, length, angle):
    return int(width / 2 + length * np.cos(angle))


def yAngleCoord(height, length, angle):
    return int(height / 2 - length * np.sin(angle))


def coordList(width, height, radius, alpha, step, numVert, coords):
    for i in range(numVert):
        x = xAngleCoord(width, radius, alpha)
        y = yAngleCoord(height, radius, alpha)
        coords['x'].append(x)
        coords['y'].append(y)
        alpha = alpha - step


def arrayToMatrix(array,
                    nodes):  # array -- массив с данными для преобразования в матрицу, nodes -- числа для ребе квадратной матрицы
    mat = []
    for node in nodes:  # для каждого из чисел создается столбец и строка
        weights = {endnode: int(weight)
                   for w in array.get(node, {})
                   for endnode, weight in
                   w.items()}  # для каждого числа, записанного в массив пересчитываем переводим в инт и записываем в конец
        mat.append([weights.get(endnode, 0) for endnode in nodes])
    mat = np.array(mat)
    return mat  # чтобы вернуть симметричную матрицу --> mat + mat.transpose()
