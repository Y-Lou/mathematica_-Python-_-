"""
计算abg的模块
"""
ab = JS.Ab(Omega,1)
GabList = JS.Setprecision(JS.Extract(JS.quzhi_2(Gab,Vspc),ab),0,Myprecision)
LamabList = JS.Setprecision(JS.Extract(JS.quzhi_2(Lamab,Vspc),ab),0,Myprecision)
ea = JS.List_Add(JS.Setprecision(JS.quzhi_1(eNil,Vspc),0,Myprecision),JS.Total(JS.Setprecision(JS.quzhi_3(Lamab,Vspc,Lspc),1,Myprecision),0),0)
Gaa = JS.Setprecision(JS.quzhi_1(JS.Diagonal(Gab),Vspc),0,Myprecision)
print("GabList,LamabList,ea,Gaa set to Myprecision")
if calAbg is True:
    abg = JS.Abg(Omega)
    abg = np.array(abg).reshape(int(len(abg)/3),3)
    aInabg = JS.Ab_All_1(Omega)
    abAso = JS.Ab(Omega,1)
    abIX = JS.ABG_G_IX(abAso,abg,0,1)
    bgIX = JS.ABG_G_IX(abAso,abg,1,2)
    agIX = JS.ABG_G_IX(abAso,abg,0,2)
    print("abg,aInabg,bgIX finished.")
    keys = list(np.dot((np.array(abg)),np.array([Omega**2,Omega,1])) + 1) 
    key2IX = JS.SparseArray(list(keys),abg,Omega,1) 
    abAso = ()
    abg = []
    keys = []
    abAndg = JS.AbAndg(Omega)
    abAndg = JS.Sort(abAndg)
    keys = list(np.dot((np.array(abAndg)),np.array([Omega**2,Omega,1])) + 1) 
    abgIX = JS.quzhi_1(key2IX,(np.array(keys)-1))
    key2IX = []
    abAndg = []
    keys = []
    print("abgIX finished.")