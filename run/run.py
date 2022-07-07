import os
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from src import band_fork, calculation, effectivemass, Mole_f_E_mass, Optical_absorption, Refractive_index
import numpy as np
import matplotlib.pyplot as plt
import math

x = float(input('조성비를 입력해주세요 : ' )) # 조성비


band_fork.band(x) # 밴드구조
Mole_f_E_mass.effective_mass() # 유효질량
Refractive_index.refractive_index(x) # 굴절률
Optical_absorption.absorption(x) # alpha 계산