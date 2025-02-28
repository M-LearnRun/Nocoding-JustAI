def apply_custom_investment_strategy(df, start_month, end_month):
    df = df.copy()
    # 투자 전략 설정: 시작월부터 종료월까지 투자하고 그 외에는 투자하지 않음
    if start_month <= end_month:
        # 한 해 안에서 투자하는 경우 (예: 1월~6월)
        df['Investment'] = ((df.index.month >= start_month) & (df.index.month <= end_month)).astype(int)
    else:
        # 두 해에 걸쳐 투자하는 경우 (예: 11월~4월)
        df['Investment'] = ((df.index.month >= start_month) | (df.index.month <= end_month)).astype(int)
    df['Strategy Return'] = df['Monthly Return'] * df['Investment']
    df['Cumulative Return'] = (1 + df['Strategy Return']).cumprod()
    return df
