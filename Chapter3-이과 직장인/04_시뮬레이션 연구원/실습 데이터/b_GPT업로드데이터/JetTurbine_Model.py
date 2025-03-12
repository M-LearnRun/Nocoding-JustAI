import numpy as np

import ross as rs
from ross.faults import *
from ross.units import Q_
from ross.probe import Probe
import matplotlib.pyplot as plt

# uncomment the lines below if you are having problems with plots not showing
# import plotly.io as pio
# pio.renderers.default = "notebook"

#주어진 요소 수로 예제 로터 생성
steel2 = rs.Material(name="Steel", rho=7850, E=2.17e11, Poisson=0.3)  
# 강철 재료 정의 (밀도: 7850 kg/m³, 탄성 계수: 2.17e11 N/m², 포아송 비: 0.3)

# 항공기 제트 터빈의 실제 크기로 로터 생성
i_d  = 0.05      # 샤프트 내부 직경 (단위: m, 예: 0.05 m)
o_d  = 0.3       # 샤프트 외부 직경 (단위: m, 예: 0.3 m)
n    = 33        # 노드 수

# fmt: off
L = np.array(
        [0   ,  150,  300, 450, 600, 750, 900, 1050, 1200, 1350,
         1500, 1650, 1800, 1950, 2100, 2250, 2400, 2550, 2700, 2850,
         3000, 3150, 3300, 3450, 3600, 3750, 3900, 4050, 4200, 4350,
         4500, 4650, 4800, 4950, 5100, 5200] 
         ) / 1000  # 길이 값 (단위: m, 예: 최대 약 5.2 m)
# fmt: on

# 샤프트 각 요소의 길이 계산
L = [L[i] - L[i - 1] for i in range(1, len(L))]

# 6 자유도를 가진 샤프트 요소 생성 (항공기 제트 터빈 크기로)
shaft_elem = [
    rs.ShaftElement6DoF(
        material       = steel2,   # 재료: steel2
        L              = l,        # 샤프트 요소 길이
        idl            = i_d,      # 왼쪽 내부 직경
        odl            = o_d,      # 왼쪽 외부 직경
        idr            = i_d,      # 오른쪽 내부 직경
        odr            = o_d,      # 오른쪽 외부 직경
        alpha          = 1,        # 재료 감쇠 계수
        beta           = 1e-7,     # 재료 감쇠 계수
        rotary_inertia = True,     # 회전 관성 포함
        shear_effects  = True,     # 전단 효과 포함
    )
    for l in L
]

# 디스크 요소 관성 모멘트 정의 (질량과 크기에 맞춰 수정)
Id_frt = 110.125  # 프론트 디스크 축 방향 관성 모멘트 (단위: kg·m²)
Ip_frt = 50.5833 # 프론트 디스크 극관성 모멘트 (단위: kg·m²)

Id_mid = 30.3375  # 센터 디스크 축 방향 관성 모멘트 (단위: kg·m²)
Ip_mid = 10.169   # 센터 디스크 극관성 모멘트 (단위: kg·m²)

Id_rr  = 100.35   # 리어 디스크 축 방향 관성 모멘트 (단위: kg·m²)
Ip_rr  = 60.675  # 리어 디스크 극관성 모멘트 (단위: kg·m²)

# 두 개의 디스크 요소 생성 (항공기 제트 터빈 크기에 맞게 수정)
disk_frt1 = rs.DiskElement6DoF(n=2, m=100, Id=Id_frt, Ip=Ip_frt)  # 프론트-첫 번째 디스크 요소 (질량 150kg)
disk_frt2 = rs.DiskElement6DoF(n=3, m=100, Id=Id_frt, Ip=Ip_frt)  # 프론트-두 번째 디스크 요소 (질량 150kg)
disk_mid1 = rs.DiskElement6DoF(n=14, m=20, Id=Id_mid, Ip=Ip_mid) # 센터-첫 번째 디스크 요소 (질량 50kg)
disk_mid2 = rs.DiskElement6DoF(n=15, m=20, Id=Id_mid, Ip=Ip_mid) # 센터-두 번째 디스크 요소 (질량 50kg)
disk_mid3 = rs.DiskElement6DoF(n=16, m=20, Id=Id_mid, Ip=Ip_mid) # 센터-세 번째 디스크 요소 (질량 50kg)
disk_mid4 = rs.DiskElement6DoF(n=17, m=20, Id=Id_mid, Ip=Ip_mid) # 센터-네 번째 디스크 요소 (질량 50kg)
disk_rr1  = rs.DiskElement6DoF(n=31, m=150, Id=Id_rr, Ip=Ip_rr)   # 리어-첫 번째 디스크 요소 (질량 200kg)
rotor_disks = [disk_frt1, disk_frt2, disk_mid1, disk_mid2, disk_mid3, disk_mid4, disk_rr1]

# 베어링 스프링 상수 및 감쇠 계수 정의 (항공기 제트 터빈의 큰 베어링에 맞게 수정)
kxx1 = 5.50e8      # 첫 번째 베어링 x 방향 스프링 상수 (단위: N/m)
kyy1 = 5.6114e8    # 첫 번째 베어링 y 방향 스프링 상수 (단위: N/m)
kzz  = 0           # z 방향 스프링 상수 (0으로 설정)
cxx1 = kxx1*1e-5   # 첫 번째 베어링 x 방향 감쇠 계수 (단위: N*s/m)
cyy1 = kyy1*1e-5   # 첫 번째 베어링 y 방향 감쇠 계수 (단위: N*s/m)
czz  = 0           # z 방향 감쇠 계수 (0으로 설정)

kxx2 = 7.50e8      # 두 번째 베어링 x 방향 스프링 상수 (단위: N/m)
kyy2 = 7.09e8      # 두 번째 베어링 y 방향 스프링 상수 (단위: N/m)
cxx2 = kxx2*1e-5   # 두 번째 베어링 x 방향 감쇠 계수 (단위: N*s/m)
cyy2 = kyy2*1e-5   # 두 번째 베어링 y 방향 감쇠 계수 (단위: N*s/m)

# 두 개의 베어링 요소 생성 (위치 6, 28, 항공기 제트 터빈 크기로 수정)
bearing0 = rs.BearingElement6DoF(
    n=6, kxx=kxx1, kyy=kyy1, cxx=cxx1, cyy=cyy1, kzz=kzz, czz=czz
)  # 첫 번째 베어링 요소

bearing1 = rs.BearingElement6DoF(
    n=28, kxx=kxx2, kyy=kyy2, cxx=cxx2, cyy=cyy2, kzz=kzz, czz=czz
)  # 두 번째 베어링 요소

# 로터 생성 (샤프트 요소, 디스크 요소, 베어링 요소 포함)
rotor = rs.Rotor(shaft_elem, rotor_disks, [bearing0, bearing1])

# 로터의 5번 노드에서의 로터 플롯 출력
rotor.plot_rotor(nodes=5)