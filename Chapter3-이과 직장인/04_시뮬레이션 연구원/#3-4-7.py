def calculate_mode_amplitudes(kxx1_s, kyy1_s, kxx2_s, kyy2_s, damping_scale):
    """베어링 스케일 적용 후 모드 주파수와 응답 진폭 계산"""
    
    # 회전 속도 및 베어링 설정
    rotation_rpm = 7000
    kxx1, kyy1 = 5.50e8 * kxx1_s, 5.6114e8 * kyy1_s
    cxx1, cyy1 = kxx1 * damping_scale, kyy1 * damping_scale
    kxx2, kyy2 = 7.50e8 * kxx2_s, 7.09e8 * kyy2_s
    cxx2, cyy2 = kxx2 * damping_scale, kyy2 * damping_scale
    
    # 새로운 베어링과 로터 정의
    bearings = [rs.BearingElement6DoF(n, kxx, kyy, cxx, cyy) for n, kxx, kyy, cxx, cyy in 
                [(6, kxx1, kyy1, cxx1, cyy1), (28, kxx2, kyy2, cxx2, cyy2)]]
    rotor = rs.Rotor(shaft_elem, rotor_disks, bearings)
 
    # 불균형 및 오정렬 해석
    probe1 = Probe(1, 0)
    misalignment = rotor.run_misalignment(
        coupling="flex", dt=0.0001, tI=0, tF=5, kd=40e3, ks=38e3, eCOUPx=2e-4, eCOUPy=2e-4,
        misalignment_angle=5 * np.pi / 180, speed=Q_(rotation_rpm, "RPM"),
        unbalance_magnitude=np.array([5.013] * 7), unbalance_phase=np.array([-np.pi / 2] * 7), mis_type="parallel"
    )
 
    # 주파수 응답 데이터 추출
    x_data, y_data = misalignment.plot_dfft([probe1], range_freq=[0, 80], yaxis_type="log").data[0].x * 60, \
                     misalignment.plot_dfft([probe1], range_freq=[0, 80], yaxis_type="log").data[0].y
 
    # 모드 주파수와 응답 진폭 계산
    rotor_wns = rotor.run_modal(speed=(rotation_rpm * 2 * np.pi) / 60).wn / (2 * np.pi) * 60
    return [(wn, np.interp(wn, x_data, y_data)) for wn in rotor_wns[:3]]
