from random import *
from threading import Thread,Lock

lock=Lock()
Pr = [100, 50, 90, 1000, 70, 2000]
Po = [100, 300, 120, 10, 230, 1]
Pmax = 20000

def calculerPoids(X):
    global Po
    S = 0
    for i in range(len(X)):
        S += X[i] * Po[i]

    if S <= Pmax:
        return S
    else:
        return 0


def calculerPrixs(X):
    global Pr
    S = 0
    for i in range(len(X)):
        S += X[i] * Pr[i]

    return S


def f(po, pr):
    return float(po) / float(pr)





def calculerX(num):
    global   Pr,Po,Pmax,lock
    T = []
    k = 150

    Xi = [randint(0, 30), randint(0, 30), randint(0, 30), randint(0, 30), randint(0, 30), randint(0, 30)]
    sac = Xi


    t = 0



    while t < 2000:
        tPo = []
        tPr = []
        tX = []

        for i1 in range(-1, 2):
            for i2 in range(-1, 2):
                for i3 in range(-1, 2):
                    for i4 in range(-1, 2):
                        for i5 in range(-1, 2):
                            for i6 in range(-1, 2):
                                if Xi[0] + i1 >= 0 and Xi[1] + i2 >= 0 and Xi[2] + i3 >= 0 and Xi[3] + i4 >= 0 and Xi[
                                    4] + i5 >= 0 and Xi[5] + i6 >= 0:
                                    X = []
                                    X.append(Xi[0] + i1)
                                    X.append(Xi[1] + i2)
                                    X.append(Xi[2] + i3)
                                    X.append(Xi[3] + i4)
                                    X.append(Xi[4] + i5)
                                    X.append(Xi[5] + i6)

                                    if not (X in T):
                                        tX.append(X)
                                        tPo.append(calculerPoids(X))
                                        tPr.append(calculerPrixs(X))

        po = tPo[0]
        i = 0
        pr = tPr[i]
        for j in range(len(tPo)):
            if pr != 0 and tPr[j] != 0:
                if (f(po,pr)) < (f(tPo[j],tPr[j])):
                    po = tPo[j]
                    pr = tPr[j]
                    i = j
        Xi = tX[i]
        T.append(Xi)
        if len(T) > k:
            del T[0]
        if float(calculerPrixs(sac)) != 0 and float(calculerPrixs(tX[i])) != 0:
            if (f(calculerPoids(sac),calculerPrixs(sac))) < (
                f(calculerPoids(tX[i]),calculerPrixs(tX[i]))):
                sac = Xi

        t += 1
    with lock:
        print
        print
        print("Thread: %s" % num)
        print("Profit: %s" % (f(calculerPoids(sac),calculerPrixs(sac))))
        print("X*: %s" % sac)
        print("Poids: %s Kg" % (calculerPoids(sac) * 1. / 1000 * 1.))
        print("Prix: %s DA" % calculerPrixs(sac))
    



for i in range(10):
    th=Thread(target=calculerX,args=( i,))
    th.start()
