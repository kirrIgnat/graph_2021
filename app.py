# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_graphApp(object):
    def setupUi(self, graphApp):
        graphApp.setObjectName("graphApp")
        graphApp.resize(802, 861)
        self.centralwidget = QtWidgets.QWidget(graphApp)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 801, 821))
        self.tabs.setObjectName("tabs")
        self.serValue = QtWidgets.QWidget()
        self.serValue.setObjectName("serValue")
        self.sohwConnections = QtWidgets.QTableWidget(self.serValue)
        self.sohwConnections.setGeometry(QtCore.QRect(0, 471, 791, 321))
        self.sohwConnections.setObjectName("sohwConnections")
        self.sohwConnections.setColumnCount(4)
        self.sohwConnections.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sohwConnections.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sohwConnections.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sohwConnections.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sohwConnections.setHorizontalHeaderItem(3, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.serValue)
        self.tableWidget_2.setGeometry(QtCore.QRect(275, 0, 521, 441))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
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
        self.coordsVertGrid.addWidget(self.circleDotCoordsBtn)
        self.usrDotCordsBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.usrDotCordsBtn.setObjectName("usrDotCordsBtn")
        self.coordsVertGrid.addWidget(self.usrDotCordsBtn)
        self.pushButton = QtWidgets.QPushButton(self.serValue)
        self.pushButton.setGeometry(QtCore.QRect(180, 210, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.tabs.addTab(self.serValue, "")
        self.showGraph = QtWidgets.QWidget()
        self.showGraph.setObjectName("showGraph")
        self.graphPic = QtWidgets.QLabel(self.showGraph)
        self.graphPic.setGeometry(QtCore.QRect(0, 0, 801, 801))
        self.graphPic.setText("")
        self.graphPic.setPixmap(QtGui.QPixmap("Graph.png"))
        self.graphPic.setObjectName("graphPic")
        self.tabs.addTab(self.showGraph, "")
        graphApp.setCentralWidget(self.centralwidget)
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
        item = self.sohwConnections.horizontalHeaderItem(0)
        item.setText(_translate("graphApp", "num"))
        item = self.sohwConnections.horizontalHeaderItem(1)
        item.setText(_translate("graphApp", "x"))
        item = self.sohwConnections.horizontalHeaderItem(2)
        item.setText(_translate("graphApp", "y"))
        item = self.sohwConnections.horizontalHeaderItem(3)
        item.setText(_translate("graphApp", "Connection"))
        for i in range(22):
            self.verCountBox.setItemText(i + 1, _translate("graphApp", str(i + 1)))
        self.randomWeightBtn.setText(_translate("graphApp", "Случайные веса"))
        self.circleDotCoordsBtn.setText(_translate("graphApp", "Вершины по кругу"))
        self.usrDotCordsBtn.setText(_translate("graphApp", "Пользоват. вершины"))
        self.pushButton.setText(_translate("graphApp", "Построить граф"))
        self.tabs.setTabText(self.tabs.indexOf(self.serValue), _translate("graphApp", "set value"))
        self.tabs.setTabText(self.tabs.indexOf(self.showGraph), _translate("graphApp", "show graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graphApp = QtWidgets.QMainWindow()
    ui = Ui_graphApp()
    ui.setupUi(graphApp)
    graphApp.show()
    sys.exit(app.exec_())
