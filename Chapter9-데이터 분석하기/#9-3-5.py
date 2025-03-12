# 필요한 라이브러리 불러오기
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
# 데이터 로드
file_path_engine_data = '/mnt/data/히트맵, 페어 플롯 - 엔진 시험 평가 데이터.csv'
engine_data = pd.read_csv(file_path_engine_data)
 
# 페어 플롯 생성
sns.pairplot(
    engine_data, 
    plot_kws={
        'color': 'darkblue',  # 점의 색상을 진한 남색으로 설정
        'marker': 'o',        # 점의 모양을 원형(o)으로 설정
        's': 20               # 점의 크기를 20으로 설정
    }
)
 
# 플롯 제목 추가
plt.suptitle("Pair Plot of Automotive Engineering Design Variables (Dark Blue Circles)", y=1.02)
 
# 플롯 표시
plt.show()
