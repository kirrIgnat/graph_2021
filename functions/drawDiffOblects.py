import cv2


def drawCircle(img, matrix, coords, nodes):
    diam = 30  # задает диаметр вершины
    for i in range(len(nodes)):
        if any(matrix[i]) != 0:  # проверка на несуществующие вершины
            img = cv2.circle(img, (coords['x'][i], coords['y'][i]), diam, (0, 0, 0), -1)  # рисует все вершины в цикле
            if i + 1 >= 10:
                cv2.putText(img, str(i + 1), ((coords['x'][i] - 20), (coords['y'][i] + 10)), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 255, 255), 2)  # пишет номер вершины
            else:
                cv2.putText(img, str(i + 1), ((coords['x'][i] - 10), (coords['y'][i] + 10)), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 255, 255), 2)  # пишет номер вершины
    return img


def drawLine(img, matrix, coords, nodes):
    for i in range(len(nodes)):  # для  всего массива len(matrix)
        for j in range(len(nodes)):  # для  всего массива len(matrix[i])
            if matrix[i][j] != 0:  # проверяет и отсеивает несуществующие ребра графа
                xi = coords['x'][i]
                yi = coords['y'][i]
                xj = coords['x'][j]
                yj = coords['y'][j]
                # print(i, ' ', j)
                # print('xi = ', xi, ' yi = ', yi, ' xj = ', xj, ' yj = ', yj)
                img = cv2.line(img, (xi + 30, yi), (xj - 30, yj), (0, 0, 255), 2)  # рисует линию между 2 верцинами
                img = cv2.circle(img, (xj - 30, yj), 7, (0, 255, 0), -1)  # стрелочка(кружок) тип ориентированный граф

    return img


def textWeight(img, matrix, coords, nodes):
    for i in range(len(nodes)):  # для  всего массива len(matrix)
        for j in range(len(nodes)):  # для  всего массива len(matrix[i])
            if matrix[i][j] != 0:  # проверяет и отсеивает несуществующие ребра графа
                xi = coords['x'][i]
                yi = coords['y'][i]
                xj = coords['x'][j]
                yj = coords['y'][j]

                if xj > xi:  # рассчитывает приемлемое положения веса ребра
                    x_weight = xi + ((xj - xi) // 2)
                else:
                    x_weight = xj + ((xi - xj) // 2)
                if yj > yi:
                    y_weight = yi + ((yj - yi) // 2)
                else:
                    y_weight = yj + ((yi - yj) // 2)

                cv2.putText(img, matrix[i][j].astype(str), (x_weight - 5, y_weight + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                            (0, 0, 0), 2)  # подписывает вес к каждому нарисованному ребру
    return img


def drawGraph(img, matrix, coords, nodes):
    drawCircle(img, matrix, coords, nodes)
    drawLine(img, matrix, coords, nodes)
    textWeight(img, matrix, coords, nodes)
