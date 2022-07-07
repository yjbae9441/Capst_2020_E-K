# 한양대학교 ERICA 나노광전자학과 2020-1학기 캡스톤
---------------------------------------
### SiGe의 조성에 따른 E-K diagram, Effective mass, Optical abosrption, Refractive index를 계산하는 모듈입니다.

## 파일 설명
----------------------------------------
### 본 코드를 이용하여 얻어낼 수 있는 결과는 다음과 같습니다.
+ SiGe의 조성비 따라 생기는 kx방향의 E-K diagram
    + ky,kz방향의 추가는 아직 구현하지 않았습니다!

+ SiGe E-K diagram을 이용한 HH,LH,SO, effective mass

+ effective mass에 따른 Optical_absorption 및 Refractive_index

-----------------------------------------
### 코드 사용 예시

+ run.py 에서 x 값으로 조성비를 입력하게 되면 입력한 조성비에 따른 SiGe의 유효질량, absoprtion, refractive index, 밴드구조의 그래프와 결과를 얻을 수 있습니다.

+ 나머지 모든 코드는 x값에 의해서만 바뀝니다. 조성비에 따라 바뀌는 굴절율과 흡수율은 Optical_absorption.py , Refractive_index.py 를 실행하시면 됩니다.

+ Mole_f_E_mass는 조성비에 따라 바뀌는 effective mass 를 보여주는 그래프입니다.

+ Optical_absorption는 조성비에 따라 바뀌는 optical absorption change 를 보여주는 그래프입니다.

+ Refractive_index는 조성비에 따라 바뀌는 refractive index change 를 보여주는 그래프입니다.

+ band_fork는 조성비에 따라 바뀌는 E-K diagram 을 보여주는 그래프입니다.