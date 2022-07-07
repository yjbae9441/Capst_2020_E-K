from . import effectivemass as e_mass
from matplotlib import pyplot as plt
import numpy as np


def effective_mass():
    Number = 100
    x_list= np.linspace(0,1,Number)
    mass_HH_list = []
    mass_LH_list = []
    effective_mass_list = []
    for i in x_list:
        mass_HH_list.append(e_mass.mass(i)[0])
        mass_LH_list.append(e_mass.mass(i)[1])
        effective_mass_list.append(e_mass.mass(i)[2])
    # # graph plot
    # plt.plot(x_list,mass_HH_list,'o',label=r'$m_{LH}$')
    # plt.plot(x_list,mass_LH_list,'o', label =r'$m_{HH}$')
    plt.plot(x_list,effective_mass_list,'o', label = r'$m^{*}$')
    plt.xlabel('x')
    plt.ylabel('Conductiviy Effective Mass')
    plt.legend()
    plt.show()
    plt.show()
