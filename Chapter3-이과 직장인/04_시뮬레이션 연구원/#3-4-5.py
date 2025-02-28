from ross import Probe, Q_
import matplotlib.pyplot as plt
 
# [질량 및 위상 불평형 삽입]
rotation_rpm = 7000
massunbt = np.array([5.013] * 7)        # 불균형 질량 배열
phaseunbt = np.array([-np.pi / 2] * 7)  # 불균형 위상 배열
probe1 = Probe(1, 0)                    # 1번 노드에 0° 방향 탐침 설정
 
# [오정렬 해석 수행]
misalignment = rotor.run_misalignment(
    coupling="flex", dt=0.0001, tI=0, tF=5, kd=40e3, ks=38e3, eCOUPx=2e-4,
    eCOUPy=2e-4, misalignment_angle=5 * np.pi / 180, TD=0, TL=0, n1=0,
    speed=Q_(rotation_rpm, "RPM"), unbalance_magnitude=massunbt,
    unbalance_phase=phaseunbt, mis_type="parallel", print_progress=True
)
# [시간 및 주파수 응답 플롯]
results = misalignment.run_time_response()
results.plot_1d([probe1]).show()  # 시간 응답
misalignment.plot_dfft([probe1], range_freq=[0, 80], yaxis_type="log

speed_rad_s = (rotation_rpm * 2 * np.pi) / 60
modal = rotor.run_modal(speed=speed_rad_s)
rotor_wns = modal.wn / 2 / np.pi * 60  # 고유 진동수 계산

# [주파수 응답 데이터 추출 및 플롯]
fig = misalignment.plot_dfft([probe1], range_freq=[0, 80], yaxis_type="log")
x_data, y_data = fig.data[0].x * 60, fig.data[0].y  # Hz -> RPM 변환
plt.figure(figsize=(8, 6))
