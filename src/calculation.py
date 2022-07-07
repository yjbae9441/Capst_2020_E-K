import numpy as np
import matplotlib.pylab as plt
from . import effectivemass
from . import makematrix

def mobility_Si(N_A):
    x = 54.3+406.9/(1+(N_A/2.35e17)*0.88)
    return x

def mobility_SiGe(x): #[cm^2/Vs]
    y = mobility_Si(N_A)*(2.5*x+1)
    return y

def Soref_delta_alpha(N_h):
    x = 6.0e-18*N_h
    return x

def Soref_delta_n(N_h):
    x = (8.5e-18*(N_h)**0.8)
    return x

def Drude_delta_alpha(x,N_h): #단위 [1/cm]
    em_h = effectivemass.mass(x)[2]*m_e #em_h= effective mass of hole
    y = ((e**3*wavelength**2)/(4*np.pi**2*c**3*epsilon0*refractive_index(x)))*(N_h/(em_h**2*mobility_SiGe(x)))*1e8
    return y

def Drude_delta_n(x,N_h):
    em_h = effectivemass.mass(x)[2]*m_e #em_h= effective mass of hole
    y = -((e**2*wavelength**2)/(8*np.pi**2*c**2*epsilon0*refractive_index(x)))*(N_h/em_h)*1e4 
    return y

# 조성비에 따른 굴절률
def refractive_index(x):
    y = 3.42+0.37*x+0.22*x*x
    return y

#elementary charge[c]
e=1.602176462e-19
#speed of light in vacuum[cm/s]
c=3e10
#permittivity in vacuum[F/cm]
epsilon0=8.8541878176e-14
#wavelength[cm]
wavelength = 1.55e-4
#Acceptor density[cm^-3]
N_A=3e19
#electron mass[kg]
m_e = 9.10938188e-31