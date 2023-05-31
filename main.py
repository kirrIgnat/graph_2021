from PyQt5 import QtWidgets
import sys

from graphApp import UiGraphApp

app = QtWidgets.QApplication(sys.argv)
graphApp = QtWidgets.QMainWindow()
ui = UiGraphApp()
ui.setupUi(graphApp)
graphApp.show()
print(sys.executable)
sys.exit(app.exec_())