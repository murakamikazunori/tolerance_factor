import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import csv

x = np.arange(0.7, 1.5, 0.1) # x軸
y = np.arange(0.3, 1.1, 0.1) # y軸
X, Y = np.meshgrid(x, y)
Ro = 1.38#酸素は4配位

#pyrochloreを読み取る
Ra = []
Rb = []
path = "/mnt/c/Users/村上和則/Documents/000_reserch/pyrochlore_latticeparameter_2.csv"
with open(path) as f: 
    reader = csv.reader(f) 
    for row in csv.reader(f): 
        Ra.append(float(row[0])) 
        Rb.append(float(row[1]))


#層状ペロブスカイトを用意
#物質のリストのpath="/mnt/c/Users/村上和則/Documents/000_reserch/layer_perovskite/all.txt"
Ra_p = [1.16, 1.12, 1.26, 1.126, 1.109, 1.18, 1.26, 1.25, 1.143, 1.079, 1.066]
Rb_p = [0.605, 0.64, 0.64, 0.605, 0.605, 0.6, 0.64, 0.64, 0.605, 0.605, 0.605]

plt.subplots_adjust(wspace=0.5, hspace=0.6)


#1
plt.subplot(2,3,1)#縦横に何分割か、左上から何番目かをいれる、一桁の数字
Z1 = (3/math.sqrt(17))*((X + Ro)/(Y + Ro))
cont = plt.contourf(X,Y,Z1,cmap="rainbow", alpha=0.75, vmin=0.666,vmax=1.136)
cont.clabel(fmt='%1.1f', fontsize=0)
plt.xlabel('RA', fontsize=10)
plt.ylabel('RB', fontsize=10)
plt.title(r"$[1] \quad t = \frac{3(R_{A} + R_{O})}{\sqrt{17}(R_{B} + R_{O})}$", fontsize=10)
plt.gca().set_aspect('equal')
plt.xticks([0.8, 1.0, 1.2, 1.4, 1.6], fontsize = 8)#x軸目盛
plt.yticks([0.4, 0.6, 0.8, 1.0], fontsize = 8)#y軸目盛
plt.scatter(Ra, Rb, s=5, c='k', marker='+', alpha=0.75)
plt.scatter(Ra_p, Rb_p, s=5, c='r', marker='o', alpha=0.75)
plt.xlim(0.8, 1.4)
plt.ylim(0.4, 1.0)


#2
plt.subplot(2,3,2)
Z2 = -(1.43373-0.42931*((X + Ro) / (Y + Ro)))
cont = plt.contourf(X,Y,Z2,cmap="rainbow", alpha=0.75, vmin=-1.040,vmax=-0.763)
cont.clabel(fmt='%1.1f', fontsize=0)
plt.xlabel('RA', fontsize=10)
#plt.ylabel('RB', fontsize=10)
plt.title(r'$[2] \quad t = -1.4+0.4 \frac{(R_{A} + R_{O})}{(R_{B} + R_{O})}$', fontsize=10)
plt.gca().set_aspect('equal')
plt.xticks([0.8, 1.0, 1.2, 1.4, 1.6], fontsize = 8)#x軸目盛
plt.yticks([0.4, 0.6, 0.8, 1.0], fontsize = 8)#y軸目盛
plt.scatter(Ra, Rb, s=5, c='k', marker='+', alpha=0.75)
plt.xlim(0.8, 1.4)
plt.ylim(0.4, 1.0)




#3
plt.subplot(2,3,3)
Z3 = 0.866*((X + Ro) / (Y + Ro))
cont = plt.contourf(X,Y,Z3,cmap="rainbow", alpha=0.75, vmin=0.793,vmax=1.353)
cont.clabel(fmt='%1.1f', fontsize=0)
plt.xlabel('RA', fontsize=10)
#plt.ylabel('RB', fontsize=10)
plt.title(r'$[3] \quad t = 0.86 \frac{(R_{A} + R_{O})}{(R_{B} + R_{O})}$', fontsize=10)
plt.gca().set_aspect('equal')
plt.xticks([0.8, 1.0, 1.2, 1.4, 1.6], fontsize = 8)#x軸目盛
plt.yticks([0.4, 0.6, 0.8, 1.0], fontsize = 8)#y軸目盛
plt.scatter(Ra, Rb, s=5, c='k', marker='+', alpha=0.75)
plt.xlim(0.8, 1.4)
plt.ylim(0.4, 1.0)


#4
plt.subplot(2,3,4)
x1 = 0.3125
Z4 = (math.sqrt((x1-(1/4))**2+(1/32)) / math.sqrt((x1-(1/2))**2+(1/32)))*((X + Ro)/(Y + Ro))
cont = plt.contourf(X,Y,Z4,cmap="rainbow", alpha=0.75, vmin=0.666,vmax=1.136)
cont.clabel(fmt='%1.1f', fontsize=0)
plt.xlabel('RA', fontsize=10)
plt.ylabel('RB', fontsize=10)
plt.title(r'$[4] \quad t_{1} =  \frac{[(x-\frac{1}{4})^{2}+\frac{1}{32}]^{\frac{1}{2}}(R_{A} + R_{O})}{[(x-\frac{1}{2})^{2}+\frac{1}{32}]^{\frac{1}{2}}(R_{B} + R_{O})} $'
          "\n" r"$x=0.3125$", fontsize=8)
plt.gca().set_aspect('equal')
plt.xticks([0.8, 1.0, 1.2, 1.4, 1.6], fontsize = 8)#x軸目盛
plt.yticks([0.4, 0.6, 0.8, 1.0], fontsize = 8)#y軸目盛
plt.scatter(Ra, Rb, s=5, c='k', marker='+', alpha=0.75)
plt.xlim(0.8, 1.4)
plt.ylim(0.4, 1.0)


#5
plt.subplot(2,3,5)
x2 = 0.375
Z5 = (math.sqrt((x2-(1/4))**2+(1/32)) / math.sqrt((x2-(1/2))**2+(1/32)))*((X + Ro)/(Y + Ro))
cont = plt.contourf(X,Y,Z5,cmap="rainbow", alpha=0.75, vmin=0.916,vmax=1.562)
cont.clabel(fmt='%1.1f', fontsize=0)
plt.xlabel('RA', fontsize=10)
plt.title(r'$[4] \quad t_{1} =  \frac{[(x-\frac{1}{4})^{2}+\frac{1}{32}]^{\frac{1}{2}}(R_{A} + R_{O})}{[(x-\frac{1}{2})^{2}+\frac{1}{32}]^{\frac{1}{2}}(R_{B} + R_{O})} $'
           "\n" r"$x=0.375$", fontsize=8)
plt.gca().set_aspect('equal')
plt.xticks([0.8, 1.0, 1.2, 1.4, 1.6], fontsize = 8)#x軸目盛
plt.yticks([0.4, 0.6, 0.8, 1.0], fontsize = 8)#y軸目盛
plt.scatter(Ra, Rb, s=5, c='k', marker='+', alpha=0.75)
plt.xlim(0.8, 1.4)
plt.ylim(0.4, 1.0)


#6
plt.subplot(2,3,6)
a=1.91712*(X + Ro) + 2.76428*(Y + Ro) + 0.04448
Z6 = -(a*(3*(3**(1/2))/8 / (X + Ro)))
cont = plt.contourf(X,Y,Z6,cmap="rainbow", alpha=0.75, vmin=-3.219,vmax=-2.405)
cont.clabel(fmt='%1.1f', fontsize=0)
plt.xlabel('RA', fontsize=10)
#plt.ylabel('RB', fontsize=10)
plt.title(r'$[4,5] \quad t_{2} = -{a \frac{3^(\frac{3}{2})}{8(R_{A} + R_{O})}}$', fontsize=10)
plt.gca().set_aspect('equal')
plt.xticks([0.8, 1.0, 1.2, 1.4, 1.6], fontsize = 8)#x軸目盛
plt.yticks([0.4, 0.6, 0.8, 1.0], fontsize = 8)#y軸目盛
plt.scatter(Ra, Rb, s=5, c='k', marker='+', alpha=0.75)
plt.xlim(0.8, 1.4)
plt.ylim(0.4, 1.0)


#引用
plt.text(-1.2,0.19,"[1] Z.Song and Q.Liu, $Inorg. Chem.$, 7, 1583(2020).[2] R.Mouta et al., $Act. Cryst. Sec. B$, 69, 439(2013).", fontsize=6)
#plt.text(-1,-0.55,"[2] R.Mouta et al., $Act. Cryst. Sec. B$, 69, 439(2013).", fontsize=10)
plt.text(-1.2,0.15,"[3] V.A.Isupov, $Kristallografiya$, 3, 99(1958).[4] Cai et al., $J. Mater. Chem.$, 21, 3611(2011).", fontsize=6)
#plt.text(-1,-0.85,"[4] Cai et al., $J. Mater. Chem.$, 21, 3611(2011).", fontsize=10)
plt.text(-1.2, 0.11, "[5] M.G.Brik and A.M.Srivastava, $J.Am.Ceram.Soc$, 95, 1454(2012).", fontsize = 6)
#plt.savefig("tolerance_factor.png")
plt.show()

