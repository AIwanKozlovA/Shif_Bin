import os
import sys, random,time
# na переставление 1 и 0 наоборот местами
# pa переставление второго элемента на первое место первого на второе третьего на четвёртое чётвертое на третье последний нечётный элемент на месте

# f количество добавленных фейковых элементов в конец или начало
# k добовлять фей ковые элеметы в конец 1 в начало 0
# pz переворачивать значения 0 с начала 1 с конца
# kpz сколько значений перевернуть
# srm позизиция с которой будет добовляться рандомный текст
#srmd длинна рандомного текста
#pr какое число прибавить к последовательности преобразовозованной в 10чную систему счисления прибавленное число
def sh(text, sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd, pr):
    r = text
    c = ""
    dt = len(r)#длина текста
    for i in range(dt):
        if i + sme < dt:
            c += r[i + sme]
        else:
            #c += r[-1*(sme - (i + sme)) - sme]
            c += r[(-1*(dt-i))+sme]
    r = c
    if na:
        nr = ""
        for i in range(dt):
            if r[i] == "1":
                nr += "0"
            else:
                nr += "1"
        r = nr
    if pa:
        py = ""
        l = 0
        for i in range(dt):
            if l == 0 and i == (dt - 1):
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
            for i in range(f * 8):
                r += str(random.randint(0, 1))
        else:
            for i in range(f * 8):
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
        ldt = len(r)# локальная длина текста
        for i in range(ldt-1,ldt - kpz-1,-1):
            if r[i] == "0":
                zi += "1"
                # r[i] = "1"
            else:
                zi += "0"
                # r[i] = "1"
        r = r[0:ldt - kpz] + zi
    if srmd:
        ra = ""
        for i in range(srmd * 8):
            ra += str(random.randint(0, 1))
        r = r[0:srm] + ra + r[srm::]
    if pr:
        r = bin(int("1" + r, 2) + pr)[2::]
        #if r % 8 != 0:
        #    r = r + ("0" * (8 - (r % 8)))
    if sm:
        po = 0
        n = 0
        text = r
        r = ''
        for i in range(sm * len(text)):
            if po == sm:
                po = 0
            if po == nrsh:
                r += text[n]
                n += 1
            else:
                r += str(random.randint(0, 1))
            po += 1
    #r +="0"*10
    ost = len(r) % 8
    if ost != 0:
        r += "0"*(8 - ost)
    return r, ost
def dsh(r, sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd, pr,ost):
    if ost != 0:
        r = r[0:len(r)-(8 - ost)]
    if sm:
        d = ""
        po = 0
        for i in range(len(r)):
            if po == sm:
                po = 0
            if po == nrsh:
                d += r[i]
            po += 1
        r = d
    if pr:
        # print(r)
        r = bin(int(r, 2) - pr)[2::]
        r = r[1::]
    if srmd:
        r = r[0:srm] + r[(srm + srmd*8)::]
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
        ldt = len(r)  # локальная длина текста
        for i in range(ldt-1,ldt-kpz-1,-1):
            if r[i] == "0":
                zi += "1"
                # r[i] = "1"
            else:
                zi += "0"
                # r[i] = "1"
        r = r[0:ldt - kpz] + zi
    if f:
        if k:
            #print("ddd", r[0:len(r) - round(len(r)*(f/100))])
            r = r[0:len(r) - f * 8]
        else:
            r = r[f * 8::]
    dt = len(r)  # длина текста
    if pa:
        dpy = ""
        l = 0
        for i in range(dt):
            if l == 0 and i == (dt - 1):
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
        for i in range(dt):
            if r[i] == "0":
                dnr += "1"
            else:
                dnr += "0"
        r = dnr
    rc = ""
    for i in range(dt):
        if i - sme >= 0:
            rc += r[i - sme]
        else:
            #c += r[-1*(sme - (i + sme)) - sme]
            rc += r[((dt + i))-sme]
    r = rc
    return r
'''
r,o = sh("10101010", 2, 1, 4, 1, 1, 2, True, 3, 1, 1, 1,1000)
print(r, len(r) % 8)
print(dsh(r, 2, 1, 4, 1, 1, 2, True, 3, 1, 1, 1,1000,o))
'''

