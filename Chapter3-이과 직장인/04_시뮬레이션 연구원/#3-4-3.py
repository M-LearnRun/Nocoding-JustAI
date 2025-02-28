import numpy as np
import ross as rs
 
# 강철 재료 정의 및 로터 파라미터 설정
steel2 = rs.Material(name="Steel", rho=7850, E=2.17e11, Poisson=0.3)
i_d, o_d, n = 0.05, 0.3, 33
L = np.array([0, 150, 300, 450, 600, 750, 900, 1050, 1200, 1350, 1500, 1650, 1800, 1950, 2100, 2250, 2400, 2550, 2700, 2850, 3000, 3150, 3300, 3450, 3600, 3750, 3900, 4050, 4200, 4350, 4500, 4650, 4800, 4950, 5100, 5200]) / 1000
L = [L[i] - L[i - 1] for i in range(1, len(L))]
 
# 샤프트 요소 생성
shaft_elem = [rs.ShaftElement6DoF(material=steel2, L=l, idl=i_d, odl=o_d, idr=i_d, odr=o_d, alpha=1, beta=1e-7, rotary_inertia=True, shear_effects=True) for l in L]
 
# 디스크 및 베어링 요소 생성
disks = [
    rs.DiskElement6DoF(n=n, m=m, Id=Id, Ip=Ip) for n, m, Id, Ip in 
    [(2, 100, 110.125, 50.5833), (3, 100, 110.125, 50.5833), (14, 20, 30.3375, 10.169), (31, 150, 100.35, 60.675)]
]
bearings = [
    rs.BearingElement6DoF(n=6, kxx=5.5e8, kyy=5.6114e8, cxx=5.5e3, cyy=5.6114e3),
    rs.BearingElement6DoF(n=28, kxx=7.5e8, kyy=7.09e8, cxx=7.5e3, cyy=7.09e3)
]
 
# 로터 생성 및 시각화
rotor = rs.Rotor(shaft_elem, disks, bearings)
rotor.plot_rotor(nodes=5) 
