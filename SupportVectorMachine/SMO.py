import numpy as np
import math
import os
class Train:
    def _init_(kwargs ):
        os.path.exists("../Sample_Data")

def select_Rand(i,m):
    b = i
    if(b == i):
        b = math.random(0,m)
        return b
def clipAlpha(low,high,alp):
    if(alp>high):
        alp = high
    if (alp<low):
        alp = low
    return alp

def simpleSMO(data,label,C,toler,maxIter):
    b = 0
    data = mat(data)
    labelMat = mat(label).transpose()
    m,n = shape(data)
    alphas = mat(zeros((m,1)))
    while (iter < maxIter):
        changed = 0
        for i in range(m):
            pred = float(multiply(alphas,labelMat).T*(data*data[i,:].T)) + b
            # calculate
            Ei = fxi - float(labelMat[i])
            if ((labelMat[i]*Ei< -toler) and (alphas[i]<C)) or ((labelMat[i]*Ei >toler) and (alphas[i] > 0)):
                j = select_Rand(i,m)
                fxj = float(multiply(alphas,labelMat).T*(data*data[j,:].T)) + b
                Ej = fXj -float(labelMat[j])
                oldi = alphas[i].copy()
                oldj = alphas[j].copy()
                if(labelMat[i] != labelMat[j]):
                    L = max(0,alphas[j] - alphas[i])
                    H = min(C,C+alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                if L == H:
                    print("L==H")
                    continue
                curbest = 2.0 * data[i,:]*data[j,:].T - data[i,:]*data[i,:].T - data[j,:].T*data[j,:].T
                if curbest >= 0:
                    print("curbest>=0")
                    continue
                alphas[j] = alphas[j] - labelMat[j]*(Ei-Ej)/curbest
                alphas[j] = clipAlpha(alphas[j],H,L)
                if(abs(alphas[j]-oldj<0.00001)):
                    print("not changed enough")
                    continue

            if (alp > 0):

                return

            return