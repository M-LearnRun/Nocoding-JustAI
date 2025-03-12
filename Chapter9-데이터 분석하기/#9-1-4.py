# 모듈 설치
!pip install /mnt/data/koreanize_matplotlib-0.1.1-py3-none-any.whl
 
import matplotlib.pyplot as plt
import pandas as pd
 
# 데이터 로드
data = pd.DataFrame({
    '연령대': ['20-29', '30-39', '40-49', '50-59', '60-69'],
    '소득(달러)': [3, 4.5, 5, 5.2, 4],
    '인구수(명)': [500, 600, 550, 580, 400]
})
 
# 시각화 업데이트 (Y축 범위 조정 및 겹치지 않도록 수정)
fig, ax1 = plt.subplots(figsize=(12, 8))
 
# 좌측 Y축: 소득 (막대그래프, 하늘색 기본, 30~39세는 다른 색상)
colors = ['#87CEEB' if age != '30-39' else '#4682B4' for age in data['연령대']]
bars = ax1.bar(data['연령대'], data['소득(달러)'], color=colors, label='소득(만 달러)')
ax1.set_xlabel('연령대', fontsize=20, fontweight='bold', color='black')
ax1.set_ylabel('소득 (만 달러)', fontsize=20, fontweight='bold', color='skyblue')
ax1.tick_params(axis='y', labelsize=20, colors='skyblue')
ax1.tick_params(axis='x', labelsize=20, colors='black')
ax1.set_ylim(0, 8)  # 소득 Y축 범위 조정
 
# 데이터 라벨 표시 (소득)
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height + 0.2, f'{height:.1f}',
             ha='center', va='bottom', fontsize=16, fontweight='bold', color='skyblue')
 
# 우측 Y축: 인구수 (선그래프, 빨간색, 막대그래프 위로 이동)
ax2 = ax1.twinx()
ax2.plot(data['연령대'], data['인구수(명)'] + 10, marker='o', color='red', label='인구수 (천 명 단위)', linewidth=2)
ax2.set_ylabel('인구수 (천 명 단위)', fontsize=20, fontweight='bold', color='red')
ax2.tick_params(axis='y', labelsize=20, colors='red')
ax2.set_ylim(0, data['인구수(명)'].max() + 20)  # 인구수 Y축 범위 조정
 
# 데이터 라벨 표시 (인구수)
for i, val in enumerate(data['인구수(명)'] + 10):
    ax2.text(i, val + 2, f'{val:.0f}', ha='center', va='bottom', fontsize=16, fontweight='bold', color='red')
 
# 제목 및 범례 설정
plt.title('나이에 따른 소득과 인구수', fontsize=24, fontweight='bold', color='black')
fig.legend(loc='upper right', fontsize=18)
 
# X, Y축 그리드 제거
ax1.grid(False)
ax2.grid(False)
 
# 그래프 표시
plt.tight_layout()
plt.show()
