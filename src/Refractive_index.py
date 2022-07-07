import numpy as np
import matplotlib.pylab as plt
from . import calculation as cal

def refractive_index(x):
    # list setting
    Soref_Refraction_index = []
    Si_Refraction_index = []
    SiGe_Refraction_index = []
    holedensity = []

    # Refractive index change
    for i in np.linspace(17,20,40):
        N_h = 10**i
        Soref_Refraction_index.append(cal.Soref_delta_n(N_h))
        Si_Refraction_index.append(-cal.Drude_delta_n(0,N_h))
        SiGe_Refraction_index.append(-cal.Drude_delta_n(x,N_h))
        holedensity.append(N_h)

    # graph plot
    plt.plot(holedensity,Soref_Refraction_index, label = "Si(soref)")
    plt.plot(holedensity,Si_Refraction_index, label = "Si")
    plt.plot(holedensity,SiGe_Refraction_index, label = r'$Si_{1-x}Ge_{x}$')
    plt.xlabel("hole density [$cm^{-3}$]")
    plt.ylabel("Refractive index change")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlim(1e17,1e20)
    plt.ylim(0.0001,1)
    plt.legend()
    plt.show()