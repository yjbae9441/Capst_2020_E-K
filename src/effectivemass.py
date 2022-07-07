from . import makematrix
from matplotlib import pyplot as plt
import numpy as np

#Valence band calculation of SiGe on Si by k-p
def mass(x):
    #Plank constant / 2pi [Js]
    HBAR = 1.054571596e-34

    #electron mass [kg]
    EM0 = 9.10938188e-31

    #elementary charge [C]
    EL = 1.602176462e-19

    #unit of energy [eV]
    e_unit = HBAR**2*1e20/(2*EM0*EL)

    Number = 100

    wavenumber= np.linspace(0,0.1,Number)

    energy1 = []
    energy2 = []
    energy3 = []

    for i in range(0,Number): 
        kx = wavenumber[i]
        ky = 0
        kz = 0
        A = makematrix.MakeMatrix(x, kx, ky, kz)
        w,v = np.linalg.eig(A)
        w.sort()
        eigenvalue = np.diag(w) #이유? - 

        energy1.append(-e_unit * eigenvalue[0][0]) #HH, LH ,SO
        energy2.append(-e_unit * eigenvalue[2][2])
        energy3.append(-e_unit * eigenvalue[4][4])

        k_test = []
        energy_HH =[]
        energy_LH = []

    for i in range(0,10): 
        k_test.append(wavenumber[i])
        energy_HH.append(energy1[i])
        energy_LH.append(energy2[i])

    p_HH = np.polyfit(k_test,energy_HH,2)
    p_LH = np.polyfit(k_test,energy_LH,2)

    #Heavy Hole
    mass_HH = HBAR*HBAR*1.0e20/2.0/EL/EM0/abs(p_HH[0])
    #Light Hole
    mass_LH = HBAR*HBAR*1.0e20/2.0/EL/EM0/abs(p_LH[0])
    #m_star
    effective_mass = (mass_HH**(3/2)+mass_LH**(3/2))/(mass_HH**(1/2)+mass_LH**(1/2))

    return mass_HH,mass_LH, effective_mass , energy1, energy2, energy3 
