import random
import time
#text текст для обработки
#sm количество лживых шифров на шифр каждой буквы
#nrsh  номер реального шифра
#kshp количество реальных символов подряд
#sme= смещение шифров
# na переставление 1 и 0 наоборот местами
# pa переставление второго элемента на первое место первого на второе третьего на четвёртое чётвертое на третье последний нечётный элемент на месте

# f количество добавленных фейковых элементов в конец или начало
# k добовлять фей ковые элеметы в конец 1 в начало 0
# pz переворачивать значения 0 с начала 1 с конца
# kpz сколько значений перевернуть
# srm позизиция с которой будет добовляться рандомный текст
#srmd длинна рандомного текста
def sh(text, sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd):
    r = ""
    po = 0
    n = 0
    for i in range(sm*len(text)):
        if po == sm:
            po = 0
        if po == nrsh:
            r += text[n]
            n += 1
        else:
            r += str(random.randint(0, 1))
        po += 1
    c = ""
    for i in range(len(r)):
        if i + sme < len(r):
            c += r[i + sme]
        else:
            #c += r[-1*(sme - (i + sme)) - sme]
            c += r[(-1*(len(r)-i))+sme]
    r = c
    if na:
        nr = ""
        for i in range(len(r)):
            if r[i] == "1":
                nr += "0"
            else:
                nr += "1"
        r = nr
    if pa:
        py = ""
        l = 0
        for i in range(len(r)):
            if l == 0 and i == (len(r) - 1):
                py += r[i]
                break
            if l < 1:
                py += r[i + 1]
                l += 1
            else:
                py += r[i - 1]
                l = 0
        r = py
    if f:
        if k:
            for i in range(f):
                r += str(random.randint(0, 1))
        else:
            for i in range(f):
                r = str(random.randint(0, 1)) + r
    zi = ""
    if pz:
        for i in range(kpz):
            if r[i] == "0":
                zi += "1"
                # r[i] = "1"
            else:
                zi += "0"
                # r[i] = "1"
        r = zi + r[kpz::]
    else:
        for i in range(len(r)-1,len(r)-kpz-1,-1):
            if r[i] == "0":
                zi += "1"
                # r[i] = "1"
            else:
                zi += "0"
                # r[i] = "1"
        r = r[0:len(r) - kpz] + zi
    if srmd:
        ra = ""
        for i in range(srmd):
            ra += str(random.randint(0, 1))
        r = r[0:srm] + ra + r[srm::]
    return r
def dsh(r, sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd):
    if srmd:
        r = r[0:srm] + r[(srm + srmd)::]
    zi = ""
    if pz:
        for i in range(kpz):
            if r[i] == "0":
                zi += "1"
                # r[i] = "1"
            else:
                zi += "0"
                # r[i] = "1"
        r = zi + r[kpz::]
    else:
        for i in range(len(r)-1,len(r)-kpz-1,-1):
            if r[i] == "0":
                zi += "1"
                # r[i] = "1"
            else:
                zi += "0"
                # r[i] = "1"
        r = r[0:len(r) - kpz] + zi
    if f:
        if k:
            #print("ddd", r[0:len(r) - round(len(r)*(f/100))])
            r = r[0:len(r) - f]
        else:
            r = r[f::]
    if pa:
        dpy = ""
        l = 0
        for i in range(len(r)):
            if l == 0 and i == (len(r) - 1):
                dpy += r[i]
                break
            if l < 1:
                dpy += r[i + 1]
                l += 1
            else:
                dpy += r[i - 1]
                l = 0
        r = dpy
    if na:
        dnr = ""
        for i in range(len(r)):
            if r[i] == "0":
                dnr += "1"
            else:
                dnr += "0"
        r = dnr
    rc = ""
    for i in range(len(r)):
        if i - sme >= 0:
            rc += r[i - sme]
        else:
            #c += r[-1*(sme - (i + sme)) - sme]
            rc += r[((len(r)+i))-sme]
    r = rc
    d = ""
    po = 0
    for i in range(len(r)):
        if po == sm:
            po = 0
        if po == nrsh:
            d += r[i]
        po += 1
    return d
'''
r = sh("1010", 2, 1, 4, 1, 1, 1, False, 1, 4, 1, 5)
print(r)
print(dsh(r, 2, 1, 4, 1, 1, 1, False, 1, 4, 1, 5))
'''
def shf():
    with open("Андропов.jpg", "rb") as file:
        content: bytes = file.read()
    binary: str = "".join(map("{:08b}".format, content))
    r = sh(binary, 2, 1, 4, 1, 1, 1, False, 1, 4, 1, 5)
    contents = bytes(int(r[i: i + 8], 2) for i in range(0, len(r), 8))
    f = open("cop.jpg", "wb")
    f.write(contents)
def rshf():
    with open("cop.jpg", "rb") as file:
        content: bytes = file.read()
    r: str = "".join(map("{:08b}".format, content))
    d = dsh(r, 2, 1, 4, 1, 1, 1, False, 1, 4, 1, 5)
    content = bytes(int(d[i: i + 8], 2) for i in range(0, len(d), 8))
    f = open("copr.jpg", "wb")
    f.write(content)
start_time = time.time()
shf()
print(time.time() - start_time)
start_time = time.time()
rshf()
print(time.time() - start_time)
