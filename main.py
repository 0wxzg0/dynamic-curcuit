# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from select_page import *
from graf.graf1 import *
from graf.graf2 import *
from graf.graf3 import *
from graf.graf4 import *
from graf.graf5 import *
from graf.graf6 import *
from graf.graf7 import *
from scipy import linspace, exp
from scipy.integrate import odeint, solve_bvp, solve_ivp
import numpy as np
import math


class MyWindow1(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow1, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.main_page_1)
        self.pushButton_2.clicked.connect(self.main_page_2)
        self.pushButton_3.clicked.connect(self.main_page_3)
        self.pushButton_4.clicked.connect(self.main_page_6)
        self.pushButton_5.clicked.connect(self.main_page_5)
        self.pushButton_6.clicked.connect(self.main_page_4)
        self.pushButton_7.clicked.connect(self.main_page_7)

    def main_page_1(self):
        self.hide()
        self.s = input_window_1()
        self.s.show()

    def main_page_2(self):
        self.hide()
        self.s = input_window_2()
        self.s.show()

    def main_page_3(self):
        self.hide()
        self.s = input_window_3()
        self.s.show()

    def main_page_4(self):
        self.hide()
        self.s = input_window_4()
        self.s.show()

    def main_page_5(self):
        self.hide()
        self.s = input_window_5()
        self.s.show()

    def main_page_6(self):
        self.hide()
        self.s = input_window_6()
        self.s.show()

    def main_page_7(self):
        self.hide()
        self.s = input_window_7()
        self.s.show()


class input_window_1(QtWidgets.QWidget, Ui_Form_1):
    def __init__(self):
        super(input_window_1, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.back_to_select_page)
        self.pushButton.clicked.connect(self.draw_graf)
        self.pushButton_2.clicked.connect(self.clear_data)
        self.horizontalSlider.valueChanged.connect(self.get_num)

    def back_to_select_page(self):
        self.hide()
        self.f = MyWindow1()
        self.f.show()

    def get_num(self):
        self.lcdNumber.display(self.horizontalSlider.value()/10000)
        self.lcdNumber_2.display(self.u * math.exp(-1 / self.r / self.c * (self.horizontalSlider.value() / 10000)))

    def clear_data(self):
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.horizontalSlider.setValue(0)
        self.lcdNumber.display(0)
        self.lcdNumber_2.display(0)
        plt.delaxes()
        self.my_graf.draw()

    def draw_graf(self):
        self.u = float(self.lineEdit_1.text())
        self.r = float(self.lineEdit_2.text())
        self.c = float(self.lineEdit_3.text())
        self.nn = 6 * self.r * self.c
        self.t = np.linspace(0, self.nn, 100)
        self.y = []
        i = 0
        while i < 100:
            self.y.append(self.u * math.exp(-1 / self.r / self.c * self.t[i]))
            i = i + 1
        plt.plot(self.t, self.y)
        self.my_graf.draw()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(self.nn*10000)
        self.horizontalSlider.setSingleStep(1)


class input_window_2(QtWidgets.QWidget, Ui_Form_2):
    def __init__(self):
        super(input_window_2, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.back_to_select_page)
        self.pushButton.clicked.connect(self.draw_graf)
        self.pushButton_2.clicked.connect(self.clear_data)
        self.horizontalSlider.valueChanged.connect(self.get_num)

    def back_to_select_page(self):
        self.hide()
        self.f = MyWindow1()
        self.f.show()

    def get_num(self):
        self.lcdNumber.display(self.horizontalSlider.value() / 10000)
        self.lcdNumber_2.display(self.u * (1 - math.exp(-1 / self.r / self.c * (self.horizontalSlider.value() / 10000))))

    def clear_data(self):
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.horizontalSlider.setValue(0)
        self.lcdNumber.display(0)
        self.lcdNumber_2.display(0)
        plt.delaxes()
        self.my_graf.draw()

    def draw_graf(self):
        self.u = float(self.lineEdit_1.text())
        self.r = float(self.lineEdit_2.text())
        self.c = float(self.lineEdit_3.text())
        self.nn = 6 * self.r * self.c
        self.t = np.linspace(0, self.nn, 100)
        self.y = []
        i = 0
        while i < 100:
            self.y.append(self.u * (1 - math.exp(-1 / self.r / self.c * self.t[i])))
            i = i + 1
        plt.plot(self.t, self.y)
        self.my_graf.draw()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(self.nn * 10000)
        self.horizontalSlider.setSingleStep(1)


class input_window_3(QtWidgets.QWidget, Ui_Form_3):
    def __init__(self):
        super(input_window_3, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.back_to_select_page)
        self.pushButton.clicked.connect(self.draw_graf)
        self.pushButton_2.clicked.connect(self.clear_data)
        self.horizontalSlider.valueChanged.connect(self.get_num)

    def back_to_select_page(self):
        self.hide()
        self.f = MyWindow1()
        self.f.show()

    def get_num(self):
        self.lcdNumber.display(self.horizontalSlider.value() / 10000)
        tmp = self.horizontalSlider.value() / 10000
        self.lcdNumber_2.display(self.us * (1 - math.exp(-1 / self.r / self.c * tmp))
                          + self.u * math.exp(-1 / self.r / self.c * tmp))

    def clear_data(self):
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.horizontalSlider.setValue(0)
        self.lcdNumber.display(0)
        self.lcdNumber_2.display(0)
        plt.delaxes()
        self.my_graf.draw()

    def draw_graf(self):
        self.u = float(self.lineEdit_1.text())
        self.r = float(self.lineEdit_2.text())
        self.c = float(self.lineEdit_3.text())
        self.us = float(self.lineEdit_4.text())
        self.nn = 6 * self.r * self.c
        self.t = np.linspace(0, self.nn, 100)
        self.y = []
        i = 0
        while i < 100:
            self.y.append(self.us * (1 - math.exp(-1 / self.r / self.c * self.t[i]))
                          + self.u * math.exp(-1 / self.r / self.c * self.t[i]))
            i = i + 1
        plt.plot(self.t, self.y)
        self.my_graf.draw()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(self.nn * 10000)
        self.horizontalSlider.setSingleStep(1)


class input_window_4(QtWidgets.QWidget, Ui_Form_4):
    def __init__(self):
        super(input_window_4, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.back_to_select_page)
        self.pushButton.clicked.connect(self.draw_graf)
        self.pushButton_2.clicked.connect(self.clear_data)
        self.horizontalSlider.valueChanged.connect(self.get_num)

    def back_to_select_page(self):
        self.hide()
        self.f = MyWindow1()
        self.f.show()

    def get_num(self):
        self.lcdNumber.display(self.horizontalSlider.value() / 10000)
        tmp = self.horizontalSlider.value() / 10000
        self.lcdNumber_2.display(self.i * math.exp(-1 * self.r / self.l * tmp))

    def clear_data(self):
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.horizontalSlider.setValue(0)
        self.lcdNumber.display(0)
        self.lcdNumber_2.display(0)
        plt.delaxes()
        self.my_graf.draw()

    def draw_graf(self):
        self.i = float(self.lineEdit_1.text())
        self.r = float(self.lineEdit_2.text())
        self.l = float(self.lineEdit_3.text())
        self.nn = 6 * (self.l / self.r)
        self.t = np.linspace(0, self.nn, 100)
        self.y = []
        i = 0
        while i < 100:
            self.y.append(self.i * math.exp(-1 * self.r / self.l * self.t[i]))
            i = i + 1
        plt.plot(self.t, self.y)
        self.my_graf.draw()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(self.nn * 10000)
        self.horizontalSlider.setSingleStep(1)


class input_window_5(QtWidgets.QWidget, Ui_Form_5):
    def __init__(self):
        super(input_window_5, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.back_to_select_page)
        self.pushButton.clicked.connect(self.draw_graf)
        self.pushButton_2.clicked.connect(self.clear_data)
        self.horizontalSlider.valueChanged.connect(self.get_num)

    def back_to_select_page(self):
        self.hide()
        self.f = MyWindow1()
        self.f.show()

    def get_num(self):
        tmp = self.horizontalSlider.value() / 10000
        self.lcdNumber.display(tmp)
        self.lcdNumber_2.display(self.i * (1 - math.exp(-1 * self.r / self.l * tmp)))

    def clear_data(self):
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.horizontalSlider.setValue(0)
        self.lcdNumber.display(0)
        self.lcdNumber_2.display(0)
        plt.delaxes()
        self.my_graf.draw()

    def draw_graf(self):
        self.i = float(self.lineEdit_1.text())
        self.r = float(self.lineEdit_2.text())
        self.l = float(self.lineEdit_3.text())
        self.nn = 6 * (self.l / self.r)
        self.t = np.linspace(0, self.nn, 100)
        self.y = []
        i = 0
        while i < 100:
            self.y.append(self.i * (1 - math.exp(-1 * self.r / self.l * self.t[i])))
            i = i + 1
        plt.plot(self.t, self.y)
        self.my_graf.draw()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(self.nn * 10000)
        self.horizontalSlider.setSingleStep(1)


class input_window_6(QtWidgets.QWidget, Ui_Form_6):
    def __init__(self):
        super(input_window_6, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.back_to_select_page)
        self.pushButton.clicked.connect(self.draw_graf)
        self.pushButton_2.clicked.connect(self.clear_data)
        self.horizontalSlider.valueChanged.connect(self.get_num)

    def back_to_select_page(self):
        self.hide()
        self.f = MyWindow1()
        self.f.show()

    def get_num(self):
        tmp = self.horizontalSlider.value() / 10000
        self.lcdNumber.display(tmp)
        self.lcdNumber_2.display(self.ics * (1 - math.exp(-1 * self.r / self.l * tmp))
                          + self.i * math.exp(-1 * self.r / self.l * tmp))

    def clear_data(self):
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.horizontalSlider.setValue(0)
        self.lcdNumber.display(0)
        self.lcdNumber_2.display(0)
        plt.delaxes()
        self.my_graf.draw()

    def draw_graf(self):
        self.i = float(self.lineEdit_1.text())
        self.r = float(self.lineEdit_2.text())
        self.l = float(self.lineEdit_3.text())
        self.ics = float(self.lineEdit_4.text())
        self.nn = 6 * (self.l / self.r)
        self.t = np.linspace(0, self.nn, 100)
        self.y = []
        i = 0
        while i < 100:
            self.y.append(self.ics * (1 - math.exp(-1 * self.r / self.l * self.t[i]))
                          + self.i * math.exp(-1 * self.r / self.l * self.t[i]))
            i = i + 1
        plt.plot(self.t, self.y)
        self.my_graf.draw()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(self.nn * 10000)
        self.horizontalSlider.setSingleStep(1)


class input_window_7(QtWidgets.QWidget, Ui_Form_7):
    def __init__(self):
        super(input_window_7, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.back_to_select_page)
        self.pushButton.clicked.connect(self.draw_graf)
        self.pushButton_2.clicked.connect(self.clear_data)
        self.horizontalSlider.valueChanged.connect(self.get_num)

    def back_to_select_page(self):
        self.hide()
        self.f = MyWindow1()
        self.f.show()

    def get_num(self):
        self.lcdNumber.display(self.t2[self.horizontalSlider.value()])
        self.lcdNumber_2.display(self.y[self.horizontalSlider.value(), 0])

    def clear_data(self):
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.horizontalSlider.setValue(0)
        self.lcdNumber.display(0)
        self.lcdNumber_2.display(0)
        plt.delaxes()
        self.my_graf.draw()

    def draw_graf(self):
        self.uc = float(self.lineEdit_1.text())
        self.r = float(self.lineEdit_2.text())
        self.c = float(self.lineEdit_3.text())
        self.l = float(self.lineEdit_5.text())
        self.us = float(self.lineEdit_4.text())
        self.il = float(self.lineEdit_6.text())
        hh=self.c*self.r*20
        self.t2 = linspace(0, hh, 1000)
        self.y0 = [self.uc, self.il / self.c]
        self.y = odeint(self.fvdp1, self.y0, self.t2, tfirst=True)
        y1, = plt.plot(self.t2, self.y[:, 0], label='Uc')
        #y1_1, = plt.plot(self.t2, self.y[:, 1], label='dUc/dt')
        #plt.legend(handles=[y1, y1_1])

        self.my_graf.draw()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(1000-1)
        self.horizontalSlider.setSingleStep(1)


    def fvdp1(self, t, y):
        dy1 = y[1]  # y[1]=dy/dt，一阶导
        dy2 = -(self.r / self.l) * y[1] - (1 / self.l / self.c) * y[0] + self.us / self.l / self.c
        return [dy1, dy2]


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow1()
    myWin.show()
    sys.exit(app.exec_())