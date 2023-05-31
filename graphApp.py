from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
import numpy as np
import cv2

from allApp import allApp, createMatrix
from functions.graph import coordList


class UiGraphApp(object):
    width = 800  # ширина картинки
    height = 800  # длина картинки
    numVert = None
    matrix = None
    nodes = None
    radius = 350
    alpha = 60  # угол между вершинами
    step = 10  # шаг угла
    img_step = None
    coords = {'x': [], 'y': []}  # координаты вершин

    def setupUi(self, graphApp):
        graphApp.setObjectName("graphApp")
        graphApp.resize(802, 861)
        self.centralWidget = QtWidgets.QWidget(graphApp)
        self.centralWidget.setObjectName("centralWidget")
        self.tabs = QtWidgets.QTabWidget(self.centralWidget)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 801, 821))
        self.tabs.setObjectName("tabs")
        self.serValue = QtWidgets.QWidget()
        self.serValue.setObjectName("serValue")

        self.showConnections = QtWidgets.QTableWidget(self.serValue)
        self.showConnections.setGeometry(QtCore.QRect(0, 471, 791, 321))
        self.showConnections.setObjectName("showConnections")
        self.showConnections.setColumnCount(4)
        self.showConnections.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.showConnections.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.showConnections.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.showConnections.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.showConnections.setHorizontalHeaderItem(3, item)

        self.setAllTable = QtWidgets.QTableWidget(self.serValue)
        self.setAllTable.setGeometry(QtCore.QRect(275, 0, 521, 441))
        self.setAllTable.setObjectName("setAllTable")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.serValue)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 121, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.numVerVertGrid = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.numVerVertGrid.setContentsMargins(0, 0, 0, 0)
        self.numVerVertGrid.setObjectName("numVerVertGrid")
        self.verCountBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.verCountBox.setObjectName("verCountBox")
        for i in range(23):
            self.verCountBox.addItem("")
        self.numVerVertGrid.addWidget(self.verCountBox)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.serValue)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 180, 121, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.weightVertGrid = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.weightVertGrid.setContentsMargins(0, 0, 0, 0)
        self.weightVertGrid.setObjectName("weightVertGrid")
        self.randomWeightBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.randomWeightBtn.setObjectName("randomWeightBtn")
        self.weightVertGrid.addWidget(self.randomWeightBtn)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.serValue)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 385, 121, 61))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.coordsVertGrid = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.coordsVertGrid.setContentsMargins(0, 0, 0, 0)
        self.coordsVertGrid.setObjectName("coordsVertGrid")
        self.circleDotCoordsBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.circleDotCoordsBtn.setObjectName("circleDotCoordsBtn")

        self.circleDotCoordsBtn.clicked.connect(self.pressedCircleDotCoordsBtn)

        self.coordsVertGrid.addWidget(self.circleDotCoordsBtn)
        self.usrDotCordsBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.usrDotCordsBtn.setObjectName("usrDotCordsBtn")
        self.coordsVertGrid.addWidget(self.usrDotCordsBtn)

        self.usrDotCordsBtn.clicked.connect(self.pressedUsrDotCordsBtn)

        self.createAllGraphBtn = QtWidgets.QPushButton(self.serValue)
        self.createAllGraphBtn.setGeometry(QtCore.QRect(180, 210, 91, 23))
        self.createAllGraphBtn.setObjectName("createAllGraphBtn")

        self.createAllGraphBtn.clicked.connect(self.pressedCreateAllGraphBtn)

        self.setNumVerBtn = QtWidgets.QPushButton(self.serValue)
        self.setNumVerBtn.setGeometry(QtCore.QRect(180, 15, 91, 23))
        self.setNumVerBtn.setObjectName("setNumVerBtn")

        self.setNumVerBtn.clicked.connect(self.pressedSetNumVerBtn)

        self.tabs.addTab(self.serValue, "")
        self.showGraph = QtWidgets.QWidget()
        self.showGraph.setObjectName("showGraph")
        self.graphPic = QtWidgets.QLabel(self.showGraph)
        self.graphPic.setGeometry(QtCore.QRect(0, 0, 801, 801))
        self.graphPic.setText("")
        self.graphPic.setPixmap(QtGui.QPixmap("Graph.png"))
        self.graphPic.setObjectName("graphPic")
        self.tabs.addTab(self.showGraph, "")
        graphApp.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(graphApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        graphApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(graphApp)
        self.statusbar.setObjectName("statusbar")
        graphApp.setStatusBar(self.statusbar)

        self.retranslateUi(graphApp)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(graphApp)

    def retranslateUi(self, graphApp):
        _translate = QtCore.QCoreApplication.translate
        graphApp.setWindowTitle(_translate("graphApp", "MainWindow"))

        self.verCountBox.setItemText(0, _translate("graphApp", "Количество ребер"))
        for i in range(22):
            self.verCountBox.setItemText(i + 1, _translate("graphApp", str(i + 1)))
        self.randomWeightBtn.setText(_translate("graphApp", "Случайные веса"))
        self.circleDotCoordsBtn.setText(_translate("graphApp", "Вершины по кругу"))
        self.usrDotCordsBtn.setText(_translate("graphApp", "Пользоват. вершины"))
        self.createAllGraphBtn.setText(_translate("graphApp", "Построить граф"))
        self.setNumVerBtn.setText(_translate("graphApp", "кол-во вершин"))
        self.tabs.setTabText(self.tabs.indexOf(self.serValue), _translate("graphApp", "set value"))
        self.tabs.setTabText(self.tabs.indexOf(self.showGraph), _translate("graphApp", "show graph"))

    def pressedSetNumVerBtn(self):

        self.numVert = int(self.verCountBox.currentText())
        self.setAllTable.setColumnCount(self.numVert)
        self.setAllTable.setRowCount(self.numVert)

        array_with_matrix_and_nodes = createMatrix(self.numVert)
        self.matrix = array_with_matrix_and_nodes[0]
        self.nodes = array_with_matrix_and_nodes[1]
        print(self.setAllTable)
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                self.setAllTable.setItem(i, j, QTableWidgetItem(str(self.matrix[i][j])))

    def pressedCircleDotCoordsBtn(self):
        _translate = QtCore.QCoreApplication.translate
        coordList(self.width, self.height, self.radius, self.alpha, self.step, self.numVert, self.coords)
        print(self.coords)

        #item = self.showConnections.horizontalHeaderItem(0)
        #item.setText(_translate("graphApp", "num"))
        item = self.showConnections.horizontalHeaderItem(0)
        item.setText(_translate("graphApp", "x"))
        item = self.showConnections.horizontalHeaderItem(1)
        item.setText(_translate("graphApp", "y"))
        item = self.showConnections.horizontalHeaderItem(2)
        item.setText(_translate("graphApp", "Connection"))
        self.showConnections.setRowCount(self.numVert)


        for i in range(len(self.nodes)):

            #self.showConnections.setItem(i, 0, QTableWidgetItem(str(i+1)))
            self.showConnections.setItem(i, 0, QTableWidgetItem(str(self.coords['x'][i])))
            self.showConnections.setItem(i, 1, QTableWidgetItem(str(self.coords['y'][i])))

            connect = {}
            for j in range(len(self.nodes)):
                if self.matrix[i][j] != 0:
                    connect.update({j+1: self.matrix[i][j]})

            self.showConnections.setItem(i, 2, QTableWidgetItem(str(connect)))




        allApp(self.height, self.width, self.coords, self.matrix, self.nodes)

        self.showGraphPic()


    def pressedUsrDotCordsBtn(self):
        def click_event(event, x, y, flags, params):

            if self.img_step < self.numVert:
                if event == cv2.EVENT_LBUTTONDOWN:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(imeg, str(self.img_step + 1) , (x, y), font,         1, (255, 0, 0), 2)
                    cv2.imshow('image', imeg)
                    self.coords['x'].append(x)
                    self.coords['y'].append(y)
                    self.img_step += 1



        self.img_step = 0
        imeg = np.zeros((self.height, self.width, 3),
                       np.uint8)  # создает массив из единиц с размерами свыше (поже с помощью cv2 этот массив преобразуется в белый лист) (3 означает количество цвета(тип 3 rgb))
        imeg[:, 0:self.width] = (255, 255, 255)
        cv2.imshow('image', imeg)
        cv2.setMouseCallback('image', click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(self.coords)

        _translate = QtCore.QCoreApplication.translate
        coordList(self.width, self.height, self.radius, self.alpha, self.step, self.numVert, self.coords)
        print(self.coords)

        #item = self.showConnections.horizontalHeaderItem(0)
        #item.setText(_translate("graphApp", "num"))
        item = self.showConnections.horizontalHeaderItem(0)
        item.setText(_translate("graphApp", "x"))
        item = self.showConnections.horizontalHeaderItem(1)
        item.setText(_translate("graphApp", "y"))
        item = self.showConnections.horizontalHeaderItem(2)
        item.setText(_translate("graphApp", "Connection"))
        self.showConnections.setRowCount(self.numVert)

        for i in range(len(self.nodes)):

            #self.showConnections.setItem(i, 0, QTableWidgetItem(str(i+1)))
            self.showConnections.setItem(i, 0, QTableWidgetItem(str(self.coords['x'][i])))
            self.showConnections.setItem(i, 1, QTableWidgetItem(str(self.coords['y'][i])))

            connect = {}
            for j in range(len(self.nodes)):
                if self.matrix[i][j] != 0:
                    connect.update({j+1: self.matrix[i][j]})

            self.showConnections.setItem(i, 2, QTableWidgetItem(str(connect)))




        allApp(self.height, self.width, self.coords, self.matrix, self.nodes)

        self.showGraphPic()



    def pressedCreateAllGraphBtn(self):
        print("a")

    def showGraphPic(self):
        self.graphPic = QtWidgets.QLabel(self.showGraph)
        self.graphPic.setGeometry(QtCore.QRect(0, 0, 801, 801))
        self.graphPic.setText("")
        self.graphPic.setPixmap(QtGui.QPixmap("Graph.png"))
        self.graphPic.setObjectName("graphPic")
