# [KOSPI 및 KOSDAQ 전체 데이터를 CSV 파일로 저장]
# KOSPI 및 KOSDAQ 데이터를 UTF-8(BOM) 인코딩으로 저장
kospi_data_full.to_csv('/mnt/data/kospi_data_full.csv', encoding='utf-8-sig')
kosdaq_data_full.to_csv('/mnt/data/kosdaq_data_full.csv', encoding='utf-8-sig')
