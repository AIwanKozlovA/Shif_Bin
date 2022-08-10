import os
import sys, random,threading,webbrowser # sys нужен для передачи argv в QApplication
from ui12 import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox
from core12 import *
#pr()
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Dialog()
ui.setupUi(Form)
#ui.setFixedSize(16777215,16777215)
#QFileDialog.getOpenFileName(self.centralwidget)
def ob(n):
    if n == "" or int(n) < 0:
        return 0
    else:
        return int(n)
def shq(fil, sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd, pr):
    erd = False
    if fil[0] == "":
        #er(6)
        ui.mysignal.emit(6)
        #th = threading.Thread(target=er, args=(6,))
        #th.start()
        erd = True
        #QPainter.end()
    if erd == 0:
        with open(fil[0], "rb") as file:
            content: bytes = file.read()
        binary: str = "".join(map("{:08b}".format, content))
        # (text, sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd)
        dt = len(binary)
        if dt < sme:
            ui.mysignal.emit(3)
            erd = True
            #threading.Thread(target=er, args=(3,)).start()
        if kpz > dt:
            ui.mysignal.emit(4)
            erd = True
        if srm > dt - 1:
            ui.mysignal.emit(5)
            erd = True
    if erd == 0:
        if ui.checkBox_6.checkState():
            if dt < 820000:
                sm = random.randint(2, 20)
                #ui.lineEdit.setText(str(sm))
                nrsh = random.randint(1, sm-1)
                #ui.lineEdit_2.setText(str(nrsh))
            sme = random.randint(1, dt-1)
            #ui.lineEdit_3.setText(str(sme))
            na = random.randrange(0, 2)
            if na == 1:
                na = 2
            #ui.checkBox.setCheckState(na)
            pa = random.randrange(0, 2)
            if pa == 1:
                pa = 2
            #ui.checkBox_2.setCheckState(pa)
            f = random.randint(2, 10000)
            #ui.lineEdit_4.setText(str(f))
            k = random.randrange(0, 2)
            if k == 1:
                k = 2
            #ui.checkBox_3.setCheckState(k)
            pz = random.randrange(0, 2)
            if pz == 1:
                pz = 2
            #ui.checkBox_4.setCheckState(pz)
            if dt-1 > 100000:
                kpz = random.randint(1, 100000)
            else:
                kpz = random.randint(1, dt-1)
            #ui.lineEdit_6.setText(str(kpz))
            srm = random.randint(0, dt-1)
            #ui.lineEdit_7.setText(str(srm))
            srmd = random.randint(1, 10000)
            #ui.lineEdit_5.setText(str(srmd))
            pr = random.randint(1, 1000000000)
            #ui.lineEdit_8.setText(str(pr))
            ui.mysignal_set_gen_rand.emit(dt,sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd, pr)
        ma = [sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd, pr]
        if sum(ma) == 0:
            ui.mysignal.emit(8)
            erd = True
        #if y(1):
        #    return er(7)
        if erd == 0:
            ui.mysignal1.emit(1)
            r, o = sh(binary, sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd, pr)
            #ui.lineEdit_9.setText(str(o))
            ui.mysignal_o.emit(o)
            contents = bytes(int(r[i: i + 8], 2) for i in range(0, len(r), 8))
            if ui.checkBox_5.checkState() and ui.lineEdit_10.text() == "":
                f = open(fil[0], "wb")
                f.write(contents)
                ui.mysignal_end_sh.emit(1)
            elif ui.lineEdit_10.text() != "":
                f = open(fil[0][::-1].split("/",1)[1][::-1]+"/"+ui.lineEdit_10.text(), "wb")
                f.write(contents)
                if ui.checkBox_5.checkState():
                    os.remove(fil[0])
                ui.mysignal_end_sh.emit(2)
            else:
                f = open(fil[0].split(".")[0]+' зашифрованная копия.'+fil[0].split(".")[1] , "wb")
                f.write(contents)
                ui.mysignal_end_sh.emit(3)
def dshq(fil,sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd, pr, ost):
    erd = False
    if fil[0] == "":
        ui.mysignal.emit(6)
        erd = True
    if erd == False:
        with open(fil[0], "rb") as file:
            content: bytes = file.read()
        r: str = "".join(map("{:08b}".format, content))
        # (text, sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd)
        dt = len(r)
        if dt < sme:
            ui.mysignal.emit(3)
            erd = True
        if kpz > dt:
            ui.mysignal.emit(4)
            erd = True
        if srm > dt - 1:
            ui.mysignal.emit(5)
            erd = True
        ma = [sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd, pr]
        if sum(ma) == 0:
            ui.mysignal.emit(8)
            erd = True
        if erd == 0:
            ui.mysignal1.emit(2)
            d = dsh(r, sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd, pr, ost)
            contents = bytes(int(d[i: i + 8], 2) for i in range(0, len(d), 8))
            if ui.checkBox_5.checkState() and ui.lineEdit_10.text() == "":
                f = open(fil[0], "wb")
                f.write(contents)
                ui.mysignal_end_dsh.emit(1)
            elif ui.lineEdit_10.text() != "":
                f = open(fil[0][::-1].split("/",1)[1][::-1]+"/"+ui.lineEdit_10.text(), "wb")
                f.write(contents)
                if ui.checkBox_5.checkState():
                    os.remove(fil[0])
                ui.mysignal_end_dsh.emit(2)
            else:
                f = open(fil[0].split(".")[0] + ' расшифрованная копия.' + fil[0].split(".")[1], "wb")
                f.write(contents)
                ui.mysignal_end_dsh.emit(3)
def shqv():
    erd = True
    try:
        sm = ui.lineEdit.text()
        sm = ob(sm)
        nrsh = ui.lineEdit_2.text()
        nrsh = ob(nrsh)
        sme = ui.lineEdit_3.text()
        sme = ob(sme)
        na = ui.checkBox.checkState()
        pa = ui.checkBox_2.checkState()
        f = ui.lineEdit_4.text()
        f = ob(f)
        k = ui.checkBox_3.checkState()
        pz = ui.checkBox_4.checkState()
        kpz = ui.lineEdit_6.text()
        kpz = ob(kpz)
        srm = ui.lineEdit_7.text()
        srm = ob(srm)
        srmd = ui.lineEdit_5.text()
        srmd = ob(srmd)
        pr = ob(ui.lineEdit_8.text())
    except ValueError:
        ui.mysignal.emit(2)
        erd = False
    if sm < nrsh:
        ui.mysignal.emit(1)
        erd = False
    if erd:
        fil = QFileDialog.getOpenFileName()
        ths = threading.Thread(target=shq, args=(fil, sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd,pr),daemon=True)
        ths.start()
def dshqv():
    erd = True
    try:
        sm = ui.lineEdit.text()
        sm = ob(sm)
        nrsh = ui.lineEdit_2.text()
        nrsh = ob(nrsh)
        sme = ui.lineEdit_3.text()
        sme = ob(sme)
        na = ui.checkBox.checkState()
        pa = ui.checkBox_2.checkState()
        f = ui.lineEdit_4.text()
        f = ob(f)
        k = ui.checkBox_3.checkState()
        pz = ui.checkBox_4.checkState()
        kpz = ui.lineEdit_6.text()
        kpz = ob(kpz)
        srm = ui.lineEdit_7.text()
        srm = ob(srm)
        srmd = ui.lineEdit_5.text()
        srmd = ob(srmd)
        pr = ob(ui.lineEdit_8.text())
        ost = ob(ui.lineEdit_9.text())
    except ValueError:
        ui.mysignal.emit(2)
        erd = False
    if sm < nrsh:
        ui.mysignal.emit(1)
        erd = False
    if erd:
        fil = QFileDialog.getOpenFileName()
        thr = threading.Thread(target=dshq, args=(fil, sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd, pr, ost),daemon=True)
        thr.start()
def vop():
    msg = QMessageBox()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("shifbin-iconka.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msg.setWindowIcon(icon)
    msg.setWindowTitle("Объяснение")
    msg.setText("Программа 'Shifbin' написана для того, чтобы пользователи могли надёжно шифровать свои файлы (любого формата), через программу с открытым исходным кодом.\n Чтобы задать парамет шифра нужно ввести в поля ввода цифры(соответствующие требованию программы) или же перед шифровкой файла включить  опцию 'Сгенерировать случайный параметр шифра'. Параметр шифра(ключ) вы божете передать в любом формате. Для вашего удобства его можно записать в файл нажав кнопку 'Сохранить параметр шифра' задав файлу любое имя и расширение.\n Также параметр шифра(ключ) можно считать из файла, для этого нужно нажать на кнопку 'Загрузить параметр шифра'.\n Чтобы зашифровать файл нужно придумать параметр шифра(соответсвующий требованию программы)(ключ) и нажать на кнопку 'Зашифровать', далее программа попросит выбрать файл для шифровки и процесс начнётся.\n Чтобы расшифровать файл нужно знать параметр шифра(ключ) и не ошибиться при его вводе!!!\n Также вы можете удалить оригинал файла, который вы зашифровали или расшифровали, для этого нужно перед нажатием на кнопку 'Зашифровать' или 'Расшифровать' включить опцию 'Удалить оригинал'.\nТакже вы можете дать зашифрованному или расшифрованному файлу имя, под которым он сохранится после обработки. Для этого нужно указать имя файла(желательно с расширением) в поле 'Имя файла после обработки' до шифровки или расшифровки файла.\nВ новой версии этой программы  добавлена 12ая цифра(прибавленное число), которая многократно усложняет дешифровку. Но также после шифрования записывается остаток, который также нужно передать, для расшифровки, в случае использовании 12ой цифры!!! Остаток появляется после шифрования файла!!!\nТребования программы к параметру шифра:\n1) Номер реального бита не может быть больше количество лживых битов на шифр каждого бита.\n2) Смещение битов не может быть больше размера выбранного файла\n3) Количество перевёрнутых бит должно быть меньше размера выбранного файла\n4) Позизиция с которой будет добавляться рандомная последовательность не может быть больше размера выбранного файла")
    #msg.addButton("нет", QMessageBox.ResetRole)
    #msg.setIcon(QMessageBox.Information)
    msg.exec_()
    #print(thr.isAlive())
def save_shif():
    file = QFileDialog.getSaveFileName()
    if file[0] != "":
        f = open(file[0], "w")
        fi = open(file[0], "a")
        m = [ui.lineEdit.text(), ui.lineEdit_2.text(), ui.lineEdit_3.text(), ui.checkBox.checkState(), ui.checkBox_2.checkState(), ui.lineEdit_4.text(),ui.checkBox_3.checkState(), ui.checkBox_4.checkState(), ui.lineEdit_6.text(), ui.lineEdit_7.text(), ui.lineEdit_5.text(), ui.lineEdit_8.text(), ui.lineEdit_9.text()]
        fi.write(ui.lineEdit_10.text()+"\n")
        for i in m:
            fi.write(str(ob(i))+"\n")
        ui.on_mysignal_end_sh(4)
def open_shif():
    file = QFileDialog.getOpenFileName()
    if file[0] != "":
        fi = open(file[0], "r")
        try:
            ui.lineEdit_10.setText(str(fi.readline().replace("\n","")))
            ui.lineEdit.setText(str(int(fi.readline())))
            ui.lineEdit_2.setText(str(int(fi.readline())))
            ui.lineEdit_3.setText(str(int(fi.readline())))
            ui.checkBox.setCheckState(int(fi.readline()))
            ui.checkBox_2.setCheckState(int(fi.readline()))
            ui.lineEdit_4.setText(str(int(fi.readline())))
            ui.checkBox_3.setCheckState(int(fi.readline()))
            ui.checkBox_4.setCheckState(int(fi.readline()))
            ui.lineEdit_6.setText(str(int(fi.readline())))
            ui.lineEdit_7.setText(str(int(fi.readline())))
            ui.lineEdit_5.setText(str(int(fi.readline())))
            ui.lineEdit_8.setText(str(int(fi.readline())))
            ui.lineEdit_9.setText(str(int(fi.readline())))
            ui.on_mysignal_end_sh(5)
        except:
            ui.mysignal.emit(7)
def cv():
    webbrowser.open_new_tab("https://vk.com/ivan___kozlov")
ui.pushButton.clicked.connect(shqv)
ui.pushButton_2.clicked.connect(dshqv)
ui.pushButton_3.clicked.connect(vop)
ui.pushButton_5.clicked.connect(save_shif)
ui.pushButton_6.clicked.connect(open_shif)
ui.pushButton_4.clicked.connect(cv)
Form.show()
sys.exit(app.exec_())
