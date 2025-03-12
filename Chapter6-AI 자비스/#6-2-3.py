import numpy as np
  
  # 범위 설정
  n_values = range(3, 101)
  a_b_c_range = range(1, 101)
  
  # 결과 저장 변수
  results = []
  
  # 수치적 검증
  for n in n_values:
      for a in a_b_c_range:
          for b in a_b_c_range:
              for c in a_b_c_range:
                  if a**n + b**n == c**n:
                      results.append((a, b, c, n))
  
  results
