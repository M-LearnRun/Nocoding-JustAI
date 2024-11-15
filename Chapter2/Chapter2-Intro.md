# Chapter 2: Intro

이 폴더에는 Chapter 2에서 사용하는 데이터와 코드를 포함한 파일들이 포함되어 있습니다. 각 파일의 목적과 내용을 아래에 설명합니다.

---

## 포함된 파일

### 1. **dataset.csv**
- **설명**: 이 데이터셋은 AI 모델 학습에 사용되는 샘플 데이터를 포함하고 있습니다.
- **구성**:
  - `id`: 고유 식별자
  - `age`: 사용자의 나이
  - `purchase_amount`: 구매 금액
  - `category`: 상품 카테고리
- **용도**:
  - 데이터 전처리 및 기본 통계 분석 실습.

---

### 2. **data_preprocessing.py**
- **설명**: 데이터 전처리를 자동으로 수행하는 Python 코드입니다.
- **주요 기능**:
  - 결측치 제거
  - 이상치 탐지 및 처리
  - 데이터 정규화
- **사용법**:
  ```bash
  python data_preprocessing.py dataset.csv
