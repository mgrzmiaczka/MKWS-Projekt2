
import numpy as np
from cantera import *
from SDToolbox import *

from matplotlib.pylab import *

# Ethylene-Oxygen
Tmin = 300
Tmax = 800
Pmin = 101325
Pmax = 405300
fimin = float(0.2)
fimax = float(1.5)

q = 'C2H4:1 O2:3';
mech = 'gri30_highT.cti';

# Number of iterations
npoints = 20

Ti = np.zeros(npoints, 'd')
Pi = np.zeros(npoints, 'd')
fi = np.zeros(npoints, 'd')
Tcj = np.zeros(npoints, 'd')
s = np.zeros(npoints, 'd')
Pcj = np.zeros(npoints, 'd')
vcj = np.zeros(npoints, 'd')


#######################Temperature function###############
for i in range(npoints):
    Ti[i] = Tmin + (Tmax - Tmin) * i / (npoints - 1)
    [cj_speed, R2] = CJspeed(101325, Ti[i], q, mech, 0)
    gas = PostShock_eq(cj_speed, 101325, Ti[i], q, mech)
    vcj[i] = gas.density
    Pcj[i] = gas.P / 100000
    Tcj[i] = gas.T
    s[i] = cj_speed
    print 'CJ Speed is %.2f m/s' % s[i]

# create plot T
plot(Ti,s, '-', color = 'green')
xlabel(r'Temp [K]', fontsize=20)
ylabel("S [m\s]")
title(r'CJ speed (Ti)',
fontsize=22,horizontalalignment='center')
axis([300,800,2300,2400])
grid()
#show()
savefig('CJ_T.png', bbox_inches='tight')

# create plot Tcj
plot(Ti,Tcj, '-', color = 'green')
xlabel(r'Temp [K]', fontsize=20)
ylabel("Tcj [K]")
title(r'Tcj (Ti)',
fontsize=22,horizontalalignment='center')
axis([300,800,3700,4000])
grid()
#show()
savefig('CJ_Tcj.png', bbox_inches='tight')

# create plot Pcj
plot(Ti,Pcj, '-', color = 'green')
xlabel(r'Temp [K]', fontsize=20)
ylabel("Pcj [bar]")
title(r'Pcj (Ti)',
fontsize=22,horizontalalignment='center')
axis([300,800,10,35])
grid()
#show()
savefig('CJ_Pcj.png', bbox_inches='tight')

# create plot vcj
plot(Ti,vcj, '-', color = 'green')
xlabel(r'Temp [K]', fontsize=20)
ylabel("rocj [kg/m3]")
title(r'rocj (Ti)',
fontsize=22,horizontalalignment='center')
axis([300,800,0.5,2.5])
grid()
#show()
savefig('CJ_rocj.png', bbox_inches='tight')

for i in range(npoints):
    Pi[i] = Pmin + (Pmax - Pmin) * i / (npoints - 1)
    [cj_speed, R2] = CJspeed(Pi[i], 300, q, mech, 0)
    gas = PostShock_eq(cj_speed, Pi[i], 300, q, mech)
    vcj[i] = gas.density
    Pcj[i] = gas.P / 100000
    Tcj[i] = gas.T
    s[i] = cj_speed
    print 'CJ Speed is %.2f m/s' % s[i]

# create plot P
plot(Pi,s, '-', color = 'green')
xlabel(r'Pi [Pa]', fontsize=20)
ylabel("S [m\s]")
title(r'CJ speed (P)',
fontsize=22,horizontalalignment='center')
axis([100000,406000,2300,2500])
grid()
#show()
savefig('CJ_P.png', bbox_inches='tight')

# create plot Tcj
plot(Pi,Tcj, '-', color = 'green')
xlabel(r'Pi [Pa]]', fontsize=20)
ylabel("Tcj [K]")
title(r'Tcj (Pi)',
fontsize=22,horizontalalignment='center')
axis([100000,406000,3800,4400])
grid()
#show()
savefig('CJ_Tcj2.png', bbox_inches='tight')

# create plot Pcj
plot(Pi,Pcj, '-', color = 'green')
xlabel(r'Pi [Pa]', fontsize=20)
ylabel("Pcj [bar]")
title(r'Pcj (Pi)',
fontsize=22,horizontalalignment='center')
axis([100000,406000,20,150])
grid()
#show()
savefig('CJ_Pcj2.png', bbox_inches='tight')

# create plot vcj
plot(Pi,vcj, '-', color = 'green')
xlabel(r'Pi [Pa]', fontsize=20)
ylabel("rocj [kg/m3]")
title(r'rocj (Pi)',
fontsize=22,horizontalalignment='center')
axis([100000,406000,1,11])
grid()
#show()
savefig('CJ_rocj2.png', bbox_inches='tight')
#######################Fi function###############
for i in range(npoints):
    fi[i] = fimin + (fimax - fimin) * i / (npoints - 1)
    no = float(2 / fi[i])  # Number of O2 moles
    q = 'CH4:1 O2:' + str(no)
    [cj_speed, R2] = CJspeed(101325, 300, q, mech, 0)
    gas = PostShock_eq(cj_speed, 101325, 300, q, mech)
    vcj[i] = gas.density
    Pcj[i] = gas.P / 100000
    Tcj[i] = gas.T
    s[i] = cj_speed
    print 'CJ Speed is %.2f m/s' % s[i]

# create plot P
plot(fi,s, '-', color = 'green')
xlabel(r'fi [-]', fontsize=20)
ylabel("S [m\s]")
title(r'CJ speed (fi)',
fontsize=22,horizontalalignment='center')
axis([float(0.2),float(1.5),1600,2800])
grid()
#show()
savefig('CJ_fi.png', bbox_inches='tight')

# create plot Tcj
plot(fi,Tcj, '-', color = 'green')
xlabel(r'fi [-]', fontsize=20)
ylabel("Tcj [K]")
title(r'Tcj(fi)',
fontsize=22,horizontalalignment='center')
axis([float(0.2),float(1.5),2000,4000])
grid()
#show()
savefig('CJ_Tcj4.png', bbox_inches='tight')

# create plot Pcj
plot(fi,Pcj, '-', color = 'green')
xlabel(r'fi [-]', fontsize=20)
ylabel("Pcj [bar]")
title(r'Pcj(fi)',
fontsize=22,horizontalalignment='center')
axis([float(0.2),float(1.5),15,35])
grid()
#show()
savefig('CJ_Pcj3.png', bbox_inches='tight')

# create plot rocj
plot(fi,vcj, '-', color = 'green')
xlabel(r'fi [-]', fontsize=20)
ylabel("rocj [kg/m3]")
title(r'rocj (fi)',
fontsize=22,horizontalalignment='center')
axis([float(0.2),float(1.5),1,2.5])
grid()
#show()
savefig('CJ_rocj3.png', bbox_inches='tight')

