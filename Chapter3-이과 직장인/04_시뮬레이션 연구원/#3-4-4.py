import numpy as np
from ross import Probe, Q_
 
# RPM 값을 Hz로 변환
rpm_values = [1000, 6000, 10000]
frequency_range = np.array([rpm / 60 for rpm in rpm_values])
 
# 불평형 질량 설정 (항공기 제트 터빈 크기 기준)
n1, m1, p1 = 12, 5.0, 0  # 첫 번째 불균형: 노드 12, 질량 5kg, 위상 0 rad
n2, m2, p2 = 24, 4.0, 0  # 두 번째 불균형: 노드 24, 질량 4kg, 위상 0 rad
 
# 불평형 응답 계산
results_unbalance = rotor.run_unbalance_response([n1, n2], [m1, m2], [p1, p2], frequency_range)
 
# 탐침 설정 및 응답 시각화
probe1 = Probe(1, Q_(45, "deg"))  # 1번 노드에 45도 탐침
results_unbalance.plot_deflected_shape(speed=frequency_range[1])  # 주파수 범위에서 6000 RPM에 대한 응답 시각화
