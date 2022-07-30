import os
import sys, random,threading
def sh(text, sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd):
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
    return r
def dsh(r, sm, nrsh, sme, na, pa, f, k, pz, kpz, srm, srmd):
    d = ""
    po = 0
    for i in range(len(r)):
        if po == sm:
            po = 0
        if po == nrsh:
            d += r[i]
        po += 1
    r = d
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