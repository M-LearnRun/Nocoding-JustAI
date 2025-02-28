import numpy as np
from scipy.optimize import minimize
 
# 목표 mode_amplitudes
target_modes = [(2006.69, 0.002479289), (2878.38, 0.000740412), (3626.57, 0.00005978)]
optim_max_iter = 200
iterations = []
 
# [목적 함수]: 모드 주파수 및 진폭 차이 계산
def objective_function(scale_factors):
    kxx1_s, kyy1_s, kxx2_s, kyy2_s, damping_scale = scale_factors
    mode_amplitudes = calculate_mode_amplitudes(kxx1_s, kyy1_s, kxx2_s, kyy2_s, damping_scale)
    total_error = sum(((mode_amplitudes[i][0] - target_modes[i][0]) / target_modes[i][0]) ** 2 +
                      3 * ((mode_amplitudes[i][1] - target_modes[i][1]) / target_modes[i][1]) ** 2 for i in range(3))
    return total_error
 
# [콜백 함수]: 최적화 진행 상황 확인
def callback_function(scale_factors):
    iterations.append(scale_factors)
    print(f"Iteration: {len(iterations)}, Scales: {scale_factors}")
 
# 초기 추정값 및 범위 설정
initial_guess = [1.0, 1.0, 1.0, 1.0, 1e-5]
bounds = [(0.5, 3.0), (0.5, 3.0), (0.5, 3.0), (0.5, 3.0), (1e-5, 1e-4)]
 
# [최적화 실행]
result = minimize(objective_function, initial_guess, method='Nelder-Mead', callback=callback_function,
                  options={'maxiter': optim_max_iter}, bounds=bounds)
 
# [최적화 결과 출력]
optimal_scales = result.x
print(f"Optimal scales: {optimal_scales}")
 
# [최종 mode_amplitudes 확인]
optimal_mode_amplitudes = calculate_mode_amplitudes(*optimal_scales)
for i, (mode, amplitude) in enumerate(optimal_mode_amplitudes):
    print(f"Mode {i+1}: {mode:.2f} RPM, Amplitude: {amplitude:.6f}")
