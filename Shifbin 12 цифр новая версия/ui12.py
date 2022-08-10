from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Dialog(QtWidgets.QWidget):
    mysignal = QtCore.pyqtSignal(int)  # сигнал об ошибке
    mysignal1 = QtCore.pyqtSignal(int)  # сигнал об уведомлении
    mysignal_end_sh = QtCore.pyqtSignal(int)  # сигнал об уведомлении о шифровании
    mysignal_end_dsh = QtCore.pyqtSignal(int)  # сигнал об уведомлении о дешифровке
    mysignal_o = QtCore.pyqtSignal(int)  # сигнал об остатке
    mysignal_set_gen_rand = QtCore.pyqtSignal(int, int, int, int, int, int, int, int, int, int, int, int, int)
    def on_mysignal(self, id):
        msg = QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shifbin-iconka.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setWindowTitle("Ошибка!!!")
        if id == 1:
            msg.setText("Номер реального бита должен быть меньше количества лживых битов на шифр каждого бита!!!")
        elif id == 2:
            msg.setText("Вы ввели строку, а нужно ввести число в параметр шифра!!!")
        elif id == 3:
            msg.setText("Смещение битов превышает размер выбранного файла!!!")
        elif id == 4:
            msg.setText("Количество перевёрнутых бит должно быть меньше размера выбранного файла!!!")
        elif id == 5:
            msg.setText("Позизиция с которой будет добавляться рандомная последовательность больше размера выбранного файла")
        elif id == 6:
            msg.setText("Файл не выбран!!!")
        elif id == 7:
            msg.setText("Ошибка при чтении параметров щифра!!!")
        elif id == 8:
            msg.setText("Вы не задали парамет для шифра!!!")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
        #print(11)
    def on_mysignal1(self, id):
        msg = QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shifbin-iconka.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setWindowTitle("Процесс начался!!")
        if id == 1:
            msg.setText("Процесс шифрования файла начался. Если вы задали большие параметры для шифра, то процесс, может занять длительное время!!!\n Если вы используйте 12ую цифру(прибавленное число), то передадавайте параметр шифра после шифровки, так как часть параметра шифра(остаток) вычисляется и автоматически записывается после шифровки файла. О завершении процесса шифрования, эта программа уведомит вас.")
        elif id == 2:
            msg.setText("Процесс расшифровки файла начался. Если вы задали большие параметры для шифра, то процесс, может занять длительное время!!!\n О завершении процесса расшифровки, эта программа уведомит вас.")
        msg.setIcon(QMessageBox.Information)
        # msg.addButton("отмена", QMessageBox.NoRole)
        msg.exec_()
    def on_mysignal_end_sh(self, id):
        msg = QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shifbin-iconka.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setWindowTitle("Успех!!")
        if id == 1:
            msg.setText("Файл успешно зашифрован и записан поверх оригинала")
        elif id == 2:
            msg.setText("Файл успешно зашифрован и сохранён под указанным вами именем, в директории где располагался оригинал")
        elif id == 3:
            msg.setText("Файл успешно зашифрован и сохранён, в директории где располагается оригинал")
        elif id == 4:
            msg.setText("Парамет шифра(ключ) успешно сохранён!!!")
        elif id == 5:
            msg.setText("Парамет шифра(ключ) успешно считан!!!")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
    def set_o(self,o):
        self.lineEdit_9.setText(str(o))
    def on_mysignal_end_dsh(self, id):
        msg = QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shifbin-iconka.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setWindowTitle("Успех!!")
        if id == 1:
            msg.setText("Файл успешно расшифрован и записан поверх зашифрованного файла")
        elif id == 2:
            msg.setText("Файл успешно расшифрован и сохранён под указанным вами именем, в директории где располагался зашифрованный файл")
        elif id == 3:
            msg.setText("Файл успешно расшифрован и сохранён, в директории где располагается зашифрованный файл")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
    def set_gen_rand(self,dt,sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd, pr):
        if dt < 820000:
            self.lineEdit.setText(str(sm))
            self.lineEdit_2.setText(str(nrsh))
        else:
            self.lineEdit.setText("0")
            self.lineEdit_2.setText("0")
        self.lineEdit_3.setText(str(sme))
        self.checkBox.setCheckState(na)
        self.checkBox_2.setCheckState(pa)
        self.lineEdit_4.setText(str(f))
        self.checkBox_3.setCheckState(k)
        self.checkBox_4.setCheckState(pz)
        self.lineEdit_6.setText(str(kpz))
        self.lineEdit_7.setText(str(srm))
        self.lineEdit_5.setText(str(srmd))
        self.lineEdit_8.setText(str(pr))
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(1046, 719)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shifbin-iconka.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QWidget{\n"
"background-color:black;\n"
"color:white;\n"
"}\n"
"QLineEdit{\n"
"background-color:white;\n"
"color:black;\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(136, 138, 133);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(off.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(on.png);\n"
"}\n"
"")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 90, 501, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(930, 694, 51, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(510, 80, 530, 591))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(220, 50, 113, 25))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(990, 694, 41, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(460, 687, 121, 20))
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(0, 40, 221, 41))
        self.label_15.setObjectName("label_15")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 10, 111, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(530, 50, 151, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(800, 40, 331, 41))
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 101, 25))
        self.pushButton.setObjectName("pushButton")
        self.checkBox_6 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_6.setGeometry(QtCore.QRect(690, 50, 92, 23))
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_5 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_5.setGeometry(QtCore.QRect(420, 50, 92, 23))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(600, 10, 211, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(820, 10, 211, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.mysignal.connect(self.on_mysignal)
        self.mysignal1.connect(self.on_mysignal1)
        self.mysignal_end_sh.connect(self.on_mysignal_end_sh)
        self.mysignal_end_dsh.connect(self.on_mysignal_end_dsh)
        self.mysignal_o.connect(self.set_o)
        self.mysignal_set_gen_rand.connect(self.set_gen_rand)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Shifbin"))
        self.label.setText(_translate("Dialog", "количество лживых битов на шифр каждого бита"))
        self.label_2.setText(_translate("Dialog", "номер реального бита"))
        self.label_3.setText(_translate("Dialog", "смещение битов"))
        self.label_4.setText(_translate("Dialog", "инверсия битов (переставление 1 и 0 наоборот местами)"))
        self.label_5.setText(_translate("Dialog", "инверсия порядка битов"))
        self.label_6.setText(_translate("Dialog", "количество добавленных фейковых байт в конец или начало"))
        self.pushButton_4.setText(_translate("Dialog", "связь"))
        self.label_7.setText(_translate("Dialog", "добавлять фей ковые элеметы (в конец 1 в начало 0)"))
        self.label_14.setText(_translate("Dialog", "переворачивать значения (0 с начала 1 с конца)"))
        self.label_8.setText(_translate("Dialog", "сколько значений перевернуть"))
        self.label_9.setText(_translate("Dialog", "позизиция с которой будет добавляться рандомная последовательность"))
        self.label_10.setText(_translate("Dialog", "длинна рандомной последовательности"))
        self.label_16.setText(_translate("Dialog", "прибавленное число"))
        self.label_17.setText(_translate("Dialog", "остаток (нужен для расшифровки)"))
        self.pushButton_3.setText(_translate("Dialog", "?"))
        self.label_13.setText(_translate("Dialog", "© Иван КоZлоV"))
        self.label_15.setText(_translate("Dialog", "Имя файла после обработки"))
        self.pushButton_2.setText(_translate("Dialog", "Расшифровать"))
        self.label_11.setText(_translate("Dialog", "Удалить оригинал"))
        self.label_12.setText(_translate("Dialog", "Сгенерировать случайный\n"
"параметр шифра"))
        self.pushButton.setText(_translate("Dialog", "Зашифровать"))
        self.pushButton_5.setText(_translate("Dialog", "Сохранить параметр шифра"))
        self.pushButton_6.setText(_translate("Dialog", "Загрузить параметр шифра"))
