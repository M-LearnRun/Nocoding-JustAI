# [EDA 시각화 코드]
def grouped_by_name_univariate_eda_limited(data):
    # 그룹핑 규칙 설정
    groups = {key: [col for col in data.columns if key in col] for key in ['ROOF_RAIL', 'ROOF_XMBR', 'BPOST', 'R_SUPT', 'FR_SMBR', 'SEAT_SMBR', 'SSILL', 'RR_SMBR', 'CTR_SMBR', 'STEP1_FREQ']}
    
    # 각 그룹에 대해 최대 6개의 subplot 생성
    for group_name, group_columns in groups.items():
        if group_columns:
            plt.figure(figsize=(20, 12))
            for j, column in enumerate(group_columns[:6]):
                plt.subplot(2, 3, j + 1)
                plt.hist(data[column].dropna(), bins=30, edgecolor='k', alpha=0.7)
                plt.title(f'{column} 분포')
            plt.suptitle(f'{group_name} 그룹')
            plt.tight_layout(rect=[0, 0, 1, 0.96])
            plt.show()
