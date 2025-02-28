import numpy as np
import matplotlib.pyplot as plt
import ross as rs
from ross.units import Q_
 
# [스케일링 비율 정의 및 데이터 저장]
stiffness_scale = [0.5, 0.7, 1.0, 1.2, 1.5]
damping_scale = 1e-5
x_data_list, y_data_list = [], []
 
# [각 스케일 값에 대해 결과 계산 및 데이터 추출]
for scale in stiffness_scale:
    kxx1, kyy1 = 5.50e8 * scale, 5.6114e8 * scale
    cxx1, cyy1 = kxx1 * damping_scale, kyy1 * damping_scale
    kxx2, kyy2 = 7.50e8 * scale, 7.09e8 * scale
    cxx2, cyy2 = kxx2 * damping_scale, kyy2 * damping_scale
 
    # 새로운 베어링 정의
    bearing0 = rs.BearingElement6DoF(n=6, kxx=kxx1, kyy=kyy1, cxx=cxx1, cyy=cyy1)
    bearing1 = rs.BearingElement6DoF(n=28, kxx=kxx2, kyy=kyy2, cxx=cxx2, cyy=cyy2)
 
    # 로터 정의 및 불균형 질량 설정
    rotor = rs.Rotor(shaft_elem, rotor_disks, [bearing0, bearing1])
    massunbt, phaseunbt = np.array([5.013] * 7), np.array([-np.pi / 2] * 7)
    probe1 = rs.Probe(1, 0)
 
    # [오정렬 해석 수행]
    misalignment = rotor.run_misalignment(
        coupling="flex", dt=0.0001, tI=0, tF=3, kd=40e3, ks=38e3, eCOUPx=2e-4,
        eCOUPy=2e-4, misalignment_angle=5 * np.pi / 180, speed=Q_(rotation_rpm, "RPM"),
        unbalance_magnitude=massunbt, unbalance_phase=phaseunbt, mis_type="parallel"
    )
 
    # [주파수 응답 플롯]
    fig = misalignment.plot_dfft([probe1], range_freq=[0, 80], yaxis_type="log")
    x_data_list.append(fig.data[0].x * 60)  # Hz를 RPM으로 변환
    y_data_list.append(fig.data[0].y)
 
# [결과 플롯]
plt.figure(figsize=(10, 6))
for i, (x_data_rpm, y_data) in enumerate(zip(x_data_list, y_data_list)):
    plt.plot(x_data_rpm, y_data, label=f'Scale {stiffness_scale[i]}')
