import math
import numpy

def MakeMatrix(x,kx,ky,kz):
  A = [[0 for j in range(6)] for i in range(6)]

  # x는 Ge의 몰 분율!
  # 허수 정의 
  I = 1j

  # Plank constant / 2pi [Js]
  HBAR = 1.054571596e-34

  # electron mass [kg]
  EM0 = 9.10938188e-31

  # elementary charge [C]
  EL = 1.602176462e-19

  # valence band parameters

  # Fischetti JAP, v80, n4, 15, 1996.
  L_Si = -5.53
  L_Ge = -30.5
  L = L_Si + (L_Ge - L_Si) * x
  M_Si = -3.64
  M_Ge = -4.64
  M = M_Si + (M_Ge - M_Si) * x
  N_Si = -8.32
  N_Ge = -33.64
  N = N_Si + (N_Ge - N_Si) * x

  # Rieger & Vogl, PRB 48, 14275, 1993.
  # alpha = 6.7064
  # beta = 1.35
  # L0 = -6.69
  # L1 = -21.65
  # M0 = -4.62
  # M1 = -5.02
  # N0 = -8.56
  # N1 = -23.48
  # S_valence = 1 - exp((L1-L0)/alpha)
  # L = L0 + alpha * log(1.0 - S_valence * x^beta)
  # S_valence = 1 - exp((M1-M0)/alpha)
  # M = M0 + alpha * log(1.0 - S_valence * x^beta)
  # S_valence = 1 - exp((N1-N0)/alpha)
  # N = N0 + alpha * log(1.0 - S_valence * x^beta)
  # 쓰이는 부분이 없는 인자들인디?



  #elastic constants of Si [Mbar]
  #from Silicon-germaniums nanostructures, p.7
  #linear interpolation from Si and Ge
  C11_Si = 1.658
  C12_Si = 0.539
  C11_Ge = 1.285
  C12_Ge = 0.483
  C11 = C11_Si + (C11_Ge - C11_Si) * x
  C12 = C12_Si + (C12_Ge - C12_Si) * x
  #C11 = 1.675
  #C12 = 0.650

  #hydrostatic deformation potential for Si [eV]
  #arbitrarily given here 
  AV_Si = 2.46
  AV_Ge = 1.24
  AV = AV_Si + (AV_Ge - AV_Si) * x
  #AV = -100.1

  #Bir-Pikes deformation potential for Si [eV]
  #from [Yu & Cardona, 'Fundamentals of Semiconductors (Jpn. ver.)', p.135]
  B_Si = -2.2
  D_Si = -5.1
  B_Ge = -2.3
  D_Ge = -5.0
  B = B_Si + (B_Ge - B_Si) * x
  D = D_Si + (D_Ge - D_Si) * x
  #B = -2.2
  #D = -5.1 

  #spin orbit split-off energy [eV]
  #from [Yu & Cardona, 'Fundamentals of Semiconductors (Jpn. ver.)', p.81]
  DELTA_Si = 0.044
  DELTA_Ge = 0.295
  DELTA = DELTA_Si + (DELTA_Ge - DELTA_Si) * x
  #DELTA = 0.044

  #lattice constant of Si [A]
  A_Si = 5.43

  #lattice constant of Ge [A]
  A_Ge = 5.6575

  a = (L+2*M)/3+1
  b = (L-M)/3
  # c = math.sqrt((N*N-(L-M)**2)/3)
  #Lattinger parameters
  gamma1 = -a
  gamma2 = -b/2
  gamma3 = -N/6.0#math.sqrt(b**2/4+c**2/12)

  #unit of energy [eV]
  e_unit = HBAR**2*1e20/(2*EM0*EL)

  # Set Strain Matrix Element

  #lattice constant of Si substrate
  #a_sub = A_Si
  #a_sub = A_Si+0.200326*x*(1-x)+(A_Ge-A_Si)*x^2;

  #lattice constanf of SiGex layer
  a0 = A_Si+0.200326*x*(1-x)+(A_Ge-A_Si)*x**2

  #lattice constant of SiGex substrate
  #y = 0.0;
  a_sub = A_Si
  #a_sub = A_Si+0.200326*y*(1-y)+(A_Ge-A_Si)*y^2;           
  #a_sub = A_Si+0.200326*x*(1-x)+(A_Ge-A_Si)*x^2

  #lattice constant of strained Si inthe direction of perpendicular to the interface
  a_perp = a0*(1-2*C12*(a_sub-a0)/(C11*a0))

  #strain matrix element
  exx = (a_sub-a0)/a0
  eyy = exx
  ezz = -2*C12*exx/C11
  exy = 0
  eyz = 0
  ezx = 0




  #Set Hamiltonian for a strained bulk Si


  pk = gamma1*(kx**2+ky**2+kz**2)
  qk = gamma2*(kx**2+ky**2-2*kz**2)
  rk = -math.sqrt(3)*gamma2*(kx**2-ky**2)+I*2*math.sqrt(3)*gamma3*kx*ky
  sk = 2*math.sqrt(3)*gamma3*kz*kx-I*2*math.sqrt(3)*gamma3*ky*kz

  pe = -AV/e_unit*(exx+eyy+ezz)
  qe = -0.5*B/e_unit*(exx+eyy-2*ezz)
  re = math.sqrt(3)/2*B*(exx-eyy)-I*D*exy
  se = -D*(ezx-I*eyz)

  p = pk+pe
  q = qk+qe
  r = rk+re
  s = sk+se

  A[0][0] = p+q
  A[0][1] = -s
  A[0][2] = r
  A[0][3] = 0
  A[0][4] = -s/math.sqrt(2)
  A[0][5] = r*math.sqrt(2)

  A[1][1] = p-q
  A[1][2] = 0
  A[1][3] = r
  A[1][4] = -q*math.sqrt(2)#-q*math.sqrt(2) 논문과 다름
  A[1][5] = s*math.sqrt(1.5)

  A[2][2] = p-q
  A[2][3] = s
  A[2][4] = s.conjugate()*(math.sqrt(1.5))
  A[2][5] = q*math.sqrt(2)

  A[3][3] = p+q
  A[3][4] = -r.conjugate()*math.sqrt(2)
  A[3][5] = -s.conjugate()/math.sqrt(2)

  A[4][4] = p+DELTA/e_unit
  A[4][5] = 0

  A[5][5] = p+DELTA/e_unit

  for i in range (0,6):
    for j in range(i+1,6):
      A[j][i] = A[i][j].conjugate()
  # B = numpy.array(A,dtype = "complex_")
  return A