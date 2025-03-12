# 필요한 라이브러리 불러오기
import squarify
import pandas as pd
import matplotlib.pyplot as plt
 
# 데이터 로드
file_path_treemap_data = '/mnt/data/트리맵 - 미국 시가총액 상위 100위 섹터.csv'
treemap_data = pd.read_csv(file_path_treemap_data)
 
# 데이터 준비: 섹터별 시가총액 합계 계산
sector_aggregated = treemap_data.groupby('Sector', as_index=False).agg({'marketcap': 'sum'})
 
# 트리맵 생성
plt.figure(figsize=(12, 8))  # 플롯 크기 설정
squarify.plot(
    sizes=sector_aggregated['marketcap'],  # 각 섹터의 크기(시가총액 합계)
    label=sector_aggregated['Sector'],  # 섹터 이름 라벨
    alpha=0.8,  # 투명도 설정
    color=plt.cm.tab20.colors  # 색상 팔레트 설정
)
plt.title("Treemap of US Stock Market Top 100 Companies by Sector", fontsize=16)  # 제목 설정
plt.axis('off')  # 축 비활성화
plt.show()  # 플롯 표시
