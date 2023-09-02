from PyQt5.QtWidgets import QToolTip ,QMainWindow , QLabel ,QApplication , QPushButton , QWidget , QMenu , QLineEdit , QTextEdit , QGridLayout
from PyQt5 import QtCore, QtGui , QtWidgets
from PyQt5.QtWidgets import QGraphicsView , QGraphicsScene , QHBoxLayout
import sys
import sqlite3
from PyQt5.QtGui import QFont , QPixmap , QIcon , QIntValidator
from PyQt5.QtWidgets import QMessageBox
from illustration2 import Ui_Form
import numpy as np

class demo( QMainWindow , Ui_Form , QWidget):

    def __init__(self):
        super().__init__()
        ui = Ui_Form()
        ui.setupUi(self)
        
        self.setWindowTitle('圖鑑')
        self.setWindowIcon(QIcon('icons8-ios-photos-16'))
        
        ui.label.resize(200,20)
        ui.label.setText('請在此輸入：')
        
        self.lineEditt = ui.lineEdit
        tuuxtt = 'what do you want to find?\n1.monster\n2.item\n3.active skill\n4.pasive skill\n5.role\n'
        ui.textBrowser.append(tuuxtt)
        self.textbrows = ui.textBrowser
        
        self.okk = QPushButton('OK', self)
        self.cle = QPushButton('Clear',self)
        self.okk.move(590, 295)
        self.cle.move(695, 295)
        self.okk.clicked.connect(self.okBotton)
        self.cle.clicked.connect(self.cleBotton)
        
        pixmap1 = QPixmap('12')      #兩顆眼睛
        pixmap2 = QPixmap('123')        
        lab1 = QLabel(self)
        lab1.resize(200,200)
        lab1.setPixmap(pixmap1)
        lab2 = QLabel(self)
        lab2.resize(200,200)
        lab2.setPixmap(pixmap2)
        lab1.move(50,50)
        lab2.move(380,50)
        
        self.setFixedSize(self.width(), self.height());    #固定視窗大小
        self.show()
    
    def okBotton(self):
        a = str(self.lineEditt.text())
        self.lineEditt.clear()
        if  a=='item' or a=='2' :
            b='item'
            with sqlite3.connect('libary') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM {}".format(b))
                for item in c.fetchall():
                    ab = str(item[1])+' , '+str(item[2])+' , '+str(item[3])
                    self.textbrows.append(ab)
        
        else :
            abc = '\n can not find it , please do it again \n'
            self.textbrows.append(abc)
   
    def cleBotton(self):
        self.lineEditt.clear()
        self.textbrows.clear()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
    
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = demo()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    sys.exit(app.exec_())