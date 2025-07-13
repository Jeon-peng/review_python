
수행과제
1. numpy를 사용하기 위해서 import를 한다.
2. mars_base_main_parts-001.csv,
mars_base_main_parts-002.csv,
mars_base_main_parts-003.csv 파일들을
모두 numpy를 사용해서 읽어들여서 각각 arr1, arr2, arr3 과 같이 ndarray 타입으로 가져온다.
3. 3개의 배열을 하나로 합치고(merge) 이름을 parts 라는 ndarray 를 생성한다.
4. parts를 이용해서 각 항목의 평균값을 구한다.
5. 평균값이 50 보다 작은 값을 뽑아내서 parts_to_work_on.csv 라는 파일로 별도로 저장한다.
6. 작성된 코드는 design_dome.py 라는 이름으로 저장한다.




---
numpy를 먼저 알아보자
---
### numpy란 무엇인가?
NumPy는 Python에서 과학 연산을 위한 가장 기본적인 패키지 중 하나입니다. NumPy는 "Numeric Python"의 약자이며 대규모 다차원 배열과 행렬 연산에 필요한 다양한 함수와 메소드를 제공합니다. NumPy는 데이터 분석, 데이터 처리, 선형 대수, 머신 러닝 등 다양한 분야에서 널리 사용되고 있습니다.
[https://velog.io/@euisuk-chung/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8B%9C%EA%B0%81%ED%99%94-%EB%A7%88%EC%8A%A4%ED%84%B0%ED%95%98%EA%B8%B0-Numpy]

numpy의 기본 구조는 배열이라고 한다.


---
### python list vs Numpy array
Python list vs NumPy array 메모리 구조:

리스트:
[1] -> [2] -> [3] -> [4] (각각 객체 포인터가 따로 존재)

NumPy array:
[1][2][3][4] (연속된 메모리 블록)


---
| 비교항목    | Python list | NumPy ndarray         |
| ------- | ----------- | --------------------- |
| 자료형     | 혼합 가능       | 동일 자료형만 허용            |
| 메모리 구조  | 비연속, 포인터 기반 | 연속 메모리 블록             |
| 연산 속도   | 느림          | 매우 빠름 (C 기반)          |
| 다차원 지원  | 제한적         | 강력한 지원 (n차원까지)        |
| 주 사용 분야 | 범용 프로그래밍    | 수치 계산, 통계, ML, 데이터 가공 |




# 1. NumPy 파일 불러오기 함수 비교: `loadtxt()` vs `genfromtxt()`

## ✅ 1. `np.loadtxt()` – 간단하고 빠른 로딩

### 📌 특징
- 빠르고 메모리 효율적임
- 파일 전체가 **결측값 없이**, **동일한 타입**이어야 함
- 결측값, 문자열, 주석 등은 잘 처리 못함

### ✅ 사용 예시

```python
import numpy as np
data = np.loadtxt('data.csv', delimiter=',')
```

**예시 CSV (`data.csv`)**
```
1.0, 2.0, 3.0
4.0, 5.0, 6.0
7.0, 8.0, 9.0
```

### ⚠️ 주의사항
결측값이 있는 경우 오류 발생

```
1.0, 2.0, 3.0
4.0, , 6.0
7.0, 8.0, 9.0
```

→ `ValueError: could not convert string to float: ''`

---

## ✅ 2. `np.genfromtxt()` – 결측값 및 유연한 구조 처리

### 📌 특징
- 결측값 처리 가능 (`missing_values`, `filling_values`)
- 다양한 데이터 타입, 주석, 문자열 포함된 데이터 지원
- `dtype` 자동 유추 또는 수동 지정 가능

### ✅ 사용 예시

```python
data = np.genfromtxt('data_with_missing.csv', delimiter=',', filling_values=np.nan)
```

**예시 CSV (`data_with_missing.csv`)**
```
1.0, 2.0, 3.0
4.0, , 6.0
7.0, 8.0, 9.0
```

→ 비어 있는 값이 `np.nan`으로 채워짐

---

## 🆚 함수 비교 요약

| 항목              | `np.loadtxt()`                         | `np.genfromtxt()`                          |
|------------------|----------------------------------------|--------------------------------------------|
| 결측값 처리       | ❌ 불가능                                | ✅ `filling_values`, `missing_values` 지원   |
| 속도              | ✅ 빠름                                 | ❌ 느림 (기능이 많아서)                    |
| 파일 유연성       | ❌ 동일한 타입만 처리 가능               | ✅ 다양한 타입 처리 가능                    |
| 주석/헤더 처리    | 제한적 (`comments='#'`)                 | ✅ `names=True`, `skip_header` 등 다양       |
| 문자열 포함        | ❌ 거의 불가                              | ✅ `dtype=str`, `usecols` 등으로 가능       |
| 구조 복잡한 파일  | ❌ 비추천                                | ✅ 추천                                     |

---

## ✅ 사용 상황 추천

| 상황 | 추천 함수 | 설명 |
|------|-----------|------|
| 단순 숫자 CSV     | `np.loadtxt()` | 간단하고 빠름 |
| 결측값 포함 CSV   | `np.genfromtxt()` | `filling_values` 사용 |
| 헤더 있는 CSV     | `np.genfromtxt(..., names=True)` | 구조화 배열로 로딩 가능 |
| 문자열 포함       | `np.genfromtxt(..., dtype=None)` | 자동 추론 가능 |
| 복잡한 파일 or 실무 | `pandas.read_csv()` | 최고 유연성, 전처리까지 지원 |

---

## ✅ 실무 흐름 예시

```python
# 결측값 없고 간단한 CSV
data = np.loadtxt('clean_data.csv', delimiter=',')

# 결측값 있음
data = np.genfromtxt('missing_data.csv', delimiter=',', filling_values=np.nan)

# 실전 데이터
import pandas as pd
df = pd.read_csv('real_world.csv')
```


# 2.Ndarray란?
## 2-1. ndarray란?
 
ndarray (N-dimensional array)는 Numpy 라이브러리의 핵심 데이터 구조입니다.

다차원 배열로, 같은 타입의 데이터를 효율적으로 저장하고 연산할 수 있게 설계됐어요.

파이썬 내장 리스트와 달리, 메모리 상에 연속된 공간에 데이터를 저장해 빠른 연산과 적은 메모리 사용이 가능합니다.


## 2-2. Numpy ndarray VS    Python List
| 구분     | 파이썬 리스트                  | Numpy ndarray              |
| ------ | ------------------------ | -------------------------- |
| 데이터 타입 | 다양한 타입 혼합 가능             | 동일한 데이터 타입만 저장 가능          |
| 메모리 구조 | 포인터 배열 (각 요소가 별도 메모리 위치) | 연속적인 메모리 블록                |
| 연산 속도  | 느림 (for문 기반 반복 처리 필요)    | 매우 빠름 (C로 구현된 벡터 연산 지원)    |
| 기능     | 기본적인 컨테이너 역할             | 과학/수학 연산, 브로드캐스팅 등 강력한 기능  |
| 차원     | 1차원부터 다차원 리스트 중첩 가능      | 다차원 배열 지원 (1D, 2D, 3D, nD) |
| 메모리 사용 | 상대적으로 비효율적               | 메모리 효율적                    |




# 3.NumPy 배열 합치기 총정리

## ✅ 예제 배열
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])
```
---

## ✅ 배열 합치는 주요 방법들

| 함수 이름 | 방향 | 목적 | 예시 | 특이점 |
|-----------|------|------|------|--------|
| `np.concatenate()` | 축 기반 | 일반적인 배열 연결 | `np.concatenate([a, b, c])` | 1차원 이상 모두 사용 가능 |
| `np.stack()` | 축 추가 후 병합 | 새로운 차원 생성 | `np.stack([a, b, c])` | 차원이 증가함 |
| `np.hstack()` | 수평 합치기 | 가로방향으로 붙이기 | `np.hstack([a, b, c])` | 1D → 1D 유지 |
| `np.vstack()` | 수직 합치기 | 세로방향으로 붙이기 | `np.vstack([a, b, c])` | 1D → 2D로 변환 |
| `np.column_stack()` | 열 기준 결합 | 열 기준으로 붙이기 | `np.column_stack([a, b, c])` | 1D → 2D (열 기준) |
| `np.row_stack()` | 행 기준 결합 | 행 기준으로 붙이기 | `np.row_stack([a, b, c])` | `vstack`과 거의 동일 |
| `np.append()` | 간단한 연결 | 기존 배열 끝에 추가 | `np.append(a, b)` | 내부적으로 `ravel()` 사용 |
| `np.block()` | 블록 형태 결합 | 2D 행렬 블록 구성 | `np.block([[a], [b], [c]])` | 형태가 다양해야 유리 |

---

## 1. `np.concatenate()`
- 📌 사용: `np.concatenate((a, b, c), axis=0)`
- ✅ 장점: 단순하고 빠름. 다차원 배열도 처리 가능
- ⚠️ 단점: 축 맞춰야 함. 차원이 다르면 오류 발생
- 👍 사용 추천 상황: 같은 차원의 배열들을 한 축으로 단순 이어붙일 때

---

## 2. `np.stack()`
- 📌 사용: `np.stack((a, b, c), axis=0)`
- ✅ 장점: **새로운 차원 생성** → shape 추적 용이
- ⚠️ 단점: 차원이 증가함 (1D → 2D, 2D → 3D)
- 👍 사용 추천 상황: 시간 축 등 추가 차원 필요할 때

```python
>>> np.stack([a, b, c]).shape
(3, 3)
```

---

## 3. `np.hstack()` / `np.vstack()`
- 📌 `np.hstack((a, b, c))` : 가로 방향  
- 📌 `np.vstack((a, b, c))` : 세로 방향
- ✅ 장점: 축 지정 없이 직관적인 방향 사용
- ⚠️ 단점: 1D 배열이 자동으로 2D로 바뀜 → 예기치 않은 shape
- 👍 사용 추천 상황: 빠르게 row/column 기준으로 정리할 때

```python
>>> np.vstack([a, b, c]).shape
(3, 3)
>>> np.hstack([a, b, c]).shape
(9,)    # 수평으로 이어붙여 1차원
```

---

## 4. `np.column_stack()` / `np.row_stack()`
- 📌 `column_stack((a, b, c))` → 열 단위로 쌓음  
- 📌 `row_stack((a, b, c))` → 행 단위로 쌓음
- ✅ 장점: 1D를 자동으로 2D 처리 (reshape 불필요)
- ⚠️ 단점: 내부적으로 변환이 일어나므로 의도하지 않은 결과 주의
- 👍 사용 추천 상황: 각 배열이 열, 행의 역할을 할 때 유용

```python
>>> np.column_stack([a, b, c])
array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])
```

---

## 5. `np.append()`
- 📌 사용: `np.append(a, b)`
- ✅ 장점: 간단한 연결에 유용
- ⚠️ 단점: 내부적으로 `ravel()` → 다차원 flatten됨
- 👍 사용 추천 상황: flatten 후 단순 이어붙일 때 (주의해서 사용)

```python
np.append([[1, 2], [3, 4]], [[5, 6]], axis=0)  # 축 지정 시 가능
```

---

## 6. `np.block()`
- 📌 사용: `np.block([[a], [b], [c]])`
- ✅ 장점: 블록 형태로 배열 배치 가능 (직관적인 매트릭스 합성)
- ⚠️ 단점: 리스트 중첩이 많아 가독성 떨어질 수 있음
- 👍 사용 추천 상황: 행렬 연산 또는 배열 배치를 시각적으로 구성하고 싶을 때

```python
np.block([[a], [b], [c]])
```

---

## ✅ 결론: 상황별 선택 기준 요약

| 목적/상황 | 추천 방식 |
|-----------|------------|
| 단순 1D 배열 연결 | `concatenate` 또는 `append` |
| 다차원 배열 연결 | `concatenate(axis=0 or 1)` |
| 새로운 차원 필요 | `stack` |
| 수직 또는 수평 연결 | `vstack`, `hstack` |
| 열/행 기준 정렬 | `column_stack`, `row_stack` |
| 매트릭스 배치 시각화 | `block` |
