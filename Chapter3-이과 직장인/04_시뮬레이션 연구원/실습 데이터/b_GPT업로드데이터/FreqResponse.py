"""질량 및 위상 불평형을 삽입하고 국부 응답을 정의합니다."""

rotation_rpm = 7000

# 불균형 질량 배열 (각기 다른 값으로 설정)
massunbt  = np.array([5.013] * 7)
# 불균형 위상 배열 (각기 다른 위상 값으로 설정)
phaseunbt = np.array([-np.pi / 2] * 7)

# 탐침 설정 (노드 번호, 방향)
probe1 = Probe(1, 0)  # 1번 노드에 0° 방향으로 탐침 설정

"""오정렬 해석 수행"""
# 플렉시블 커플링과 함께 오정렬 해석 실행
misalignment = rotor.run_misalignment(
    coupling            = "flex",          # 커플링 종류 (플렉시블)
    dt                  = 0.0001,          # 시간 간격 (단위: 초)
    tI                  = 0,               # 시뮬레이션 시작 시간 (단위: 초)
    tF                  = 5,               # 시뮬레이션 종료 시간 (단위: 초)
    kd                  = 40 * 10 ** 3,    # 커플링 동강성 (단위: N/m)
    ks                  = 38 * 10 ** 3,    # 커플링 축강성 (단위: N/m)
    eCOUPx              = 2 * 10 ** -4,    # x축에서 커플링 불균형 (단위: m)
    eCOUPy              = 2 * 10 ** -4,    # y축에서 커플링 불균형 (단위: m)
    misalignment_angle  = 5 * np.pi / 180, # 오정렬 각도 (단위: rad)
    TD                  = 0,               # 토크 불균형
    TL                  = 0,               # 부하 토크
    n1                  = 0,               # 시작 노드
    speed               = Q_(rotation_rpm, "RPM"),  # 회전 속도 (단위: RPM)
    unbalance_magnitude = massunbt,         # 불평형 질량
    unbalance_phase     = phaseunbt,        # 불평형 위상
    mis_type            = "parallel",       # 오정렬 종류 (병렬, 각도 또는 결합)
    print_progress      = True,             # 시뮬레이션 진행 상황 출력 여부
)

"""시간 응답 플롯"""
# 시간 응답 결과 계산 및 플롯
results = misalignment.run_time_response()  # 시간 응답 시뮬레이션 실행
results.plot_1d([probe1]).show()  # 탐침 1에 대한 시간 응답 플롯 표시

"""주파수 응답 플롯 (로그 축 사용)"""
# 주파수 응답 플롯 계산 및 표시
misalignment.plot_dfft([probe1], range_freq=[0, 80], yaxis_type="log")  # 탐침 1에 대한 주파수 응답 플롯 표시 (로그 축 사용)

# Plotly 데이터에서 x, y 데이터를 추출
fig = misalignment.plot_dfft([probe1], range_freq=[0, 80], yaxis_type="log")  # 탐침 1에 대한 주파수 응답 플롯 표시 (로그 축 사용)
x_data = fig.data[0].x  # x 데이터 (Hz 값)
y_data = fig.data[0].y  # y 데이터 (응답 진폭 값)

# Hz를 RPM으로 변환: 1 Hz = 60 RPM
x_data_rpm = x_data * 60  # 주파수를 RPM으로 변환

"""고유 진동수 해석 (모드 해석)"""
speed_rad_s = (rotation_rpm * 2 * np.pi) / 60  # rad/s로 변환
modal = rotor.run_modal(speed=speed_rad_s)  # 6000 RPM에 해당하는 속도에서 모드 해석 수행
rotor_wns = modal.wn / 2 / np.pi * 60  # 자연 주파수 (고유 진동수) 값 출력

"""Matplotlib을 사용해 다시 플롯"""
plt.figure(figsize=(8, 6))
plt.plot(x_data_rpm, y_data, label="Response Amplitude")
plt.xscale("linear")
plt.yscale("log")
plt.xlabel("Frequency (RPM)")
plt.ylabel("Amplitude")
plt.title("Frequency Response (Log-Log Scale)")
plt.legend()
plt.grid(True)
plt.show()