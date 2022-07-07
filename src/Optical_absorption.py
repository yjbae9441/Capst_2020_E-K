import numpy as np
from . import calculation as cal
import matplotlib.pylab as plt

def absorption(x):
    # list setting
    holedensity = []
    Soref_absorption = []
    Si_absorption = []
    SiGe_absorption = []

    # Optical absorption change
    for i in np.linspace(17,20,40):
        N_h = 10**i
        Soref_absorption.append(cal.Soref_delta_alpha(N_h))
        Si_absorption.append(cal.Drude_delta_alpha(0,N_h))
        SiGe_absorption.append(cal.Drude_delta_alpha(x,N_h))
        holedensity.append(N_h)

    # graph plot
    plt.plot(holedensity,Soref_absorption,'--',c='k', label="Si(soref)")
    plt.plot(holedensity,Si_absorption,c='y', label = "Si")
    plt.plot(holedensity,SiGe_absorption, label = r'$Si_{1-x}Ge_{x}$')
    plt.xlabel("hole density [$cm^{-3}$]")
    plt.ylabel("Optical absorption change [1/cm]")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlim(1e17,1e20)
    plt.ylim(1e-1,1e4)
    plt.legend()
    plt.show()