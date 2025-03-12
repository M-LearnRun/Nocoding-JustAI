# 데이터 로드
file_path = '/mnt/data/방사형 차트-FIFA 스타일의 축구선수 능력치 데이터.csv'
radar_data = pd.read_csv(file_path)
 
# DEF 값을 41로 수정
radar_data.loc[radar_data['Stat'] == 'DEF', 'Value'] = 41
 
# 데이터 준비
categories = radar_data['Stat']
values = radar_data['Value']
values = np.append(values, values[0])  # 시작점과 끝점 연결
 
# 각 축에 대한 각도 계산
num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # 시작점과 끝점 연결
 
# 방사형 차트 생성
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
 
# 각 축 설정
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=8)
ax.set_ylim(0, 100)
 
# 데이터 그리기
ax.plot(angles, values, linewidth=2, linestyle='solid', color='teal')
ax.fill(angles, values, color='teal', alpha=0.25)
 
# 제목 추가
plt.title('CAPTAIN', size=20, color='teal', y=1.1)
 
# 그래프 표시
plt.tight_layout()
plt.show()
