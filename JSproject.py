'''
mathematica
数据取值，精度改变，运算
'''
import numpy as np
from decimal import *
def Ab_All_1(Omega): #ab[[all,1]]
    a = []
    for i in range(Omega):
        a.extend([i]*(Omega-(i+1)))
    return a

def Ab_All_2(Omega): #ab[[all,2]]
    a = []
    for i in range(Omega):#(N+1)
        a.extend(range(Omega)[i+1:])
    return a

def Ab(Omega,Choose): #ab
    a = []
    d = Choose
    for i in range(Omega):
        b = i
        for j in range(Omega)[i+1:]:
            a.extend([b,j])    
    e = np.array(a).reshape(int(len(a)//2),2)
    c = tuple(map(tuple, e))
    if d == 0:
        return a
    elif d == 1:    
        return c

def ABG_G_IX(abAso,abg,x,y): #abIX(0,1) bgIX(1,2) agIX(0,2)
    a = abAso
    b = []
    tu = dict(zip(a,list(range(len(a)))))
    ta = abg
    x = x
    y = y
    c = tuple(map(tuple,np.array(ta)[:,(x,y)]))
    for i in range(len(ta)):
        if c[i] in tu:
            b.append(tu.get(c[i]))
        else:
            b.append("None")
    return b

def AbAndg(Omega): #abAndg
    a=[]
    for i in range(int(Omega-1)):
        b = i
        for k in range(int(Omega-1))[i:]:
            d = k+1
            for j in range(Omega):
                a.extend([b,d,j])
    a = np.array(a).reshape(int(len(a)/3),3)
    return a

def Abg(Omega): #abg
    a = []
    c = list(range(Omega))
    for i in range(Omega-1):
        b = i
        for k in range(Omega-1)[i:]:
            d = k+1
            for j in range(Omega)[d+1:]:
                a.extend([b,d,c[j]])
    return a

def Diagonal(data): #主对角线元素列表
    a = data
    b = []
    for i in range(len(a)):
        b.append(a[i][i])
    return b

def Extract(data,data1): #Extract(提取)
    a = data
    b = data1
    c = []
    for i,j in b:
        c.append(a[i][j])
    return c

def FoldList(data,Omega,Nval,Myprecision): #Mathematica 取值方法
    a = Nval+1
    vi = np.array(data).reshape(Omega).tolist()
    v2i = np.ones((Omega),dtype = np.int).tolist()
    vi2 = np.ones((Omega),dtype = np.int)
    chiM = np.ones((Omega),dtype = np.int).tolist()
    chiMp1a = np.ones((Omega),dtype = np.int).tolist()
    sum_vc = Decimal('0')
    getcontext().prec = Myprecision
    for q in range(Omega):
        v2i[q] = Decimal(str(vi[q]))*Decimal(str(vi[q]))
    for i in range(a)[1:]:
        for j in range(Omega):
            sum_vc += Decimal(i)*Decimal(str(v2i[j]))*Decimal(str(chiM[j]))
        for k in range(Omega):
            chiM[k] = sum_vc-(Decimal(i)*Decimal(i))*Decimal(str(v2i[k]))*Decimal(str(chiM[k]))
            chiMp1a.append(chiM[k])
        sum_vc = Decimal('0')
    chiMp1a = np.array(chiMp1a).reshape(a, Omega).tolist()
    return v2i,chiMp1a

def List_Add(data,data1,Choose): #加
    a = data
    b = data1
    c = Choose
    d = []
    if c == 0: #向量与向量相加
        aa = 0
        for i in range(int(len(a))):
            aa = a[i]+b[i]
            d.append(aa)
        return d
    elif c == 1: #向量与数值相加
        for i in range(int(len(a))):
            d.append(a[i]+b)
        return d
    elif c == 2: #两矩阵相加
        e = np.zeros((len(data),len(data)),dtype = np.int).tolist()
        for i in range(int(len(a))):
            for j in range(int(len(a))):
                e[i][j] += (a[i][j]+b[i][j])
        return e

def List_CP(data,data1,Choose): #叉乘
    a = data
    b = data1
    c = []
    d = Choose
    if d == 0: #向量与数值叉乘
        for i in range(int(len(a))):
            c.append(a[i]*b)
        return c
    elif d == 1: #向量与向量叉乘
        for i in range(int(len(a))):
            c.append(a[i]*b[i])
        return c

def List_D(data,data1,Choose): #除
    a = data
    b = data1
    c = []
    d = Choose
    if d == 0: #向量与数值除
        for i in range(int(len(a))):
            c.append(a[i]/b)
        return c
    elif d == 1: #向量与向量除
        for i in range(int(len(a))):
            c.append(a[i]/b[i])
        return c
    elif d == 2: #数值与向量除
        for i in range(int(len(a))):
            c.append(b/a[i])
        return c 

def List_DM(data,data1,Choose): #点乘
    a = data
    b = data1
    d = Choose
    e =[]
    if d == 0: #向量与向量点乘
        c = 0
        for i in range(int(len(a))):
            f = a[i]*b[i]
            c += f
        return c
    elif d == 1: #矩阵与向量点乘
        for i in range(int(len(a))):
            h = 0
            for j in range(int(np.size(a)/len(a))):
                l = a[i][j]*b[j]
                h += l
            e.append(h)
        return e
    elif d == 2: #
        for i in range(int(np.size(a)/len(a))):
            h = 0
            for j in range(int(int(len(a)))):
                l = a[j][i]*b[j]
                h += l
            e.append(h) 
        return e

def List_Sub(data,data1,Choose): #减
    a = data
    b = data1
    c = []
    d = Choose
    if d == 0: #向量与向量减
        for i in range(int(len(a))):
            c.append(a[i]-b[i])
        return c
    elif d == 1: #向量与数值减
        for i in range(int(len(a))):
            c.append(a[i]-b)
        return c
    elif d == 2: #数值与向量减
        for i in range(int(len(b))):
            c.append(a-b[i])
        return c    

def Ordering(data):
    a = data
    b = np.argsort(a)
    return b

def Position(data,data1,Choose): #位置选取
    a = data
    b = data1
    c = []
    d = Choose
    if d == 0: #大于
        for i in range(int(len(a))):
            if a[i] > b:
                c.append(i)
    elif d == 1: #取真
        for i in range(int(len(a))):
            if a[i] == True:
                c.append(i)
    elif d == 2: #小于
        for i in range(int(len(a))):
            if a[i] < b:
                c.append(i)   
    return c

def Position1(data,data1,data2): #位置选取，大于且小于
    a = data
    b = []
    c = data1                    # data1<data2!
    d = data2
    for i in range(int(len(a))):
        if d > a[i] > c:
            b.append(i)  
    return b 

def Position2(data,data1): #位置选取，由向量关系决定
    a = data
    b = data1
    c = []
    for j in range(len(a)):
        if b == a[j]:
            c.append(a.index(b))
    return c

def Positions(data,data1):
    a = data
    b = data1
    c = []
    for i in range(len(b)):
        if b[i] in a:
            c.append(a.index(b[i]))
    return c

def quzhi_1(data,data1): #向量取值
    a = data
    b = data1
    c = []
    for i in b:
        c.append(a[i])
    return c

def quzhi_2(data,data1): #向量取值
    a = data
    b = data1
    c = []
    for i in b:
        for j in b:
            c.append(a[i][j])
    c = np.array(c).reshape((len(b),len(b)))
    return c

def quzhi_3(data,data1,data2):
    a = data
    b = data1
    c = data2
    d = []
    if c is not True:
        return np.array([0]*len(b)*len(c)).reshape((len(b),len(c)))
    else:
        for i in b:
            for j in c:
                d.append(a[i][j])
        d = np.array(d).reshape((len(b),len(c)))
        return d

def Replace(data,data1,data2,Choose): #向量中元素替换
    a = data
    b = data1
    c = data2
    d = Choose
    if d == 0:
        for i in c:
            a[i] = b[i]
        return a
    elif d == 1:
        k = 0
        for j in c:
            a[j] = b[k]
            k +=1
        return a

def Setprecision(data,Choose,Myprecision): #精度设定
    getcontext().prec = Myprecision
    a = np.array(data).tolist()
    d = Choose
    if d == 0:
        for i in range(int(len(a))):#d = 0
            a[i] = Decimal(str(a[i]))
        return a
    elif d == 1:
        for i in range(int(len(data))):#d = 1
            for j in range(int(np.size(data)/len(data))):
                a[i][j] = Decimal(str(a[i][j]))
        return a

def Sort(data): #排序
    a = data
    for i in range(int(len(a))):
        a[i,:].sort()
    return a

def SparseArray(data,data1,Omega,Choose): #建立稀疏矩阵
    d = Choose
    if d == 0:
        a = data
        b = data1
        c = np.zeros([Omega,Omega]).astype(int).tolist() #Omega
        i = 0
        for k,z in a:
            c[k][z] += b[i]
            i += 1
        return c
    elif d == 1:
        a = data
        b = list(range(len(data1)+1)[1:])
        c = list(np.ones(Omega**3,dtype = np.int)*(len(data1)+1)) #Omega
        e = 0
        for i in a:
            c[i-1] = b[e]
            e += 1
        return c

def Total(data,Choose): #总计
    a = data
    b = []
    c = 0
    d = Choose
    if d == 0:
        for i in range(len(a)):
            for j in range(int(np.size(a)/len(a))):
                c += a[i][j]
            b.append(c)
            c = 0
        return b
    elif d == 1:
        for i in range(len(a)):
            c += a[i]
        return c