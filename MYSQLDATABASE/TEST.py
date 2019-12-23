from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox
import sys
import pymysql
from PyQt5.uic.properties import QtWidgets



from inicioSesion.py import *

class MainWindow(QtWidgets.QMainWindow):
   pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()