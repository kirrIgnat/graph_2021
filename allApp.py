import cv2
import os
import numpy as np

from functions.drawDiffOblects import drawGraph
from functions.graph import arrayToMatrix, coordList

def createMatrix(numVert):

    graph = {'1': [{'2': '6'}, {'4': '7'}, {'5': '1'}],
             '2': [{'3': '5'}, {'4': '1'}, {'1': '9'}],
             '3': [{'4': '6'}, {'6': '7'}],
             '4': [{'5': '4'}, {'6': '4'}],
             '5': [{'3': '6'}, {'6': '8'}],
             '6': [{'1': '1'}],
             '7': [{'2': '9'}, {'4': '7'}, {'5': '1'}],
             '8': [{'3': '5'}, {'4': '1'}, {'1': '9'}],
             '9': [{'4': '6'}, {'6': '7'}],
             '10': [{'5': '4'}, {'6': '4'}],
             '11': [{'3': '6'}, {'6': '8'}],
             '12': [{'2': '9'}, {'4': '7'}, {'5': '1'}],
             '13': [{'3': '5'}, {'4': '1'}, {'1': '9'}],
             '14': [{'4': '6'}, {'6': '7'}],
             '15': [{'5': '4'}, {'6': '4'}],
             '16': [{'3': '6'}, {'6': '8'}],
             '17': [{'2': '9'}, {'4': '7'}, {'5': '1'}],
             '18': [{'3': '5'}, {'4': '1'}, {'1': '9'}],
             '19': [{'4': '6'}, {'6': '7'}],
             '20': [{'5': '4'}, {'6': '4'}],
             '21': [{'3': '6'}, {'6': '8'}],
             '22': [{'18': '7'}]}  # задание графа
    nodesInt = list(range(1, numVert + 1))  # массив со всеми ребрами графа в int
    nodes = list()
    for node in nodesInt:  # переводит массив int в массив str
        nodes.append(str(node))
    matrix = arrayToMatrix(graph, nodes)
    return matrix, nodes



def allApp(height, width, coords, matrix, nodes):
    img = np.zeros((height, width, 3), np.uint8)  # создает массив из единиц с размерами свыше (поже с помощью cv2 этот массив преобразуется в белый лист) (3 означает количество цвета(тип 3 rgb))
    img[:, 0:width] = (255, 255, 255)





    drawGraph(img, matrix, coords, nodes)

    print(matrix)
    pathToImg = os.path.abspath(os.path.dirname(__file__)) + '\Graph.png'
    print(pathToImg)
    cv2.imwrite(pathToImg, img)



