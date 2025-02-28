import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
 
# 1. 데이터 파일 경로 설정
file_path = '/mnt/data/1_대한출판문화협회_분야별 발행부수_10년_.csv'
 
# 2. CSV 파일로부터 데이터 불러오기
data = pd.read_csv(file_path)
 
# 3. 데이터 전처리: 숫자 데이터에서 콤마 제거 및 정수형 변환
data.iloc[:, 1:] = data.iloc[:, 1:].replace(',', '', regex=True).astype(int)
 
# 4. 합계 데이터 계산
data['합계'] = data.iloc[:, 1:].sum(axis=1)
 
# 5. 합계 선그래프 축약
plt.plot(data.columns[1:-1], data.iloc[:, 1:-1].sum(), marker='o', label='합계')
plt.legend(); plt.show()
 
# 6. 개별 분야의 선그래프 축약 (합계 제외)
for i, row in data.iterrows():
    if row['구분'] != '합계':
        plt.plot(data.columns[1:-1], row[1:-1], marker='o', label=row['구분'])
plt.legend(); plt.show()
 
# 7. 누적 막대그래프 축약
colors = list(mcolors.TABLEAU_COLORS)[:len(data['구분'])-1]  # 합계 제외
data[data['구분'] != '합계'].set_index('구분').T.plot(kind='bar', stacked=True, color=colors)
