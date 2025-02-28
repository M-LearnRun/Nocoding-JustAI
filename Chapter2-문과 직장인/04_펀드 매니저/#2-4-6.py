def create_pivot_table(df):
    # 'Year'와 'Month' 열 생성 (인덱스에서 연도와 월 추출)
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    # 'Monthly Return' 값을 기준으로 연도별 월별 피벗 테이블 생성
    return df.pivot_table(values='Monthly Return', index='Year', columns='Month')
# KOSPI 및 KOSDAQ의 피벗 테이블 생성
kospi_pivot = create_pivot_table(kospi_monthly_returns)
kosdaq_pivot = create_pivot_table(kosdaq_monthly_returns)
 
tools.display_dataframe_to_user(name="KOSPI Monthly Returns Pivot", dataframe=kospi_pivot)
tools.display_dataframe_to_user(name="KOSDAQ Monthly Returns Pivot", dataframe=kosdaq_pivot)
