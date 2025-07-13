"""
1. numpy import 하기 
-> pip install numpy 해서 해당 라이브러리 설치하고 사용할 python 파일에 import 하면 끝

2.mars_base_main_parts-001.csv, mars_base_main_parts-002.csv, mars_base_main_parts-003.csv 파일들을 모두 numpy를 사용해서 읽어들여서 각각 arr1, arr2, arr3 과 같이 ndarray 타입으로 가져온다.
-> 2-1. csv를 numpy를 사용해서 읽어들이는 방법 ?
    -> np.loadtxt('data.csv', delimiter=',') ,  np.genfromtxt('data_with_missing.csv', delimiter=',', filling_values=np.nan)
    -> 두가지 방법이 있는데 해당 방법 차이는 README.md에 추가 작성해놓음 
        -> README.md # 1.NumPy 파일 불러오기 함수 비교: loadtxt() vs genfromtxt()

-> 2-2. 각각 arr1, arr2, arr3 과 같이 ndarray 타입으로 가져온다.
    -> ndarray란 무엇일까?
        -> README.md # 2.Ndarray란?


3.3개의 배열을 하나로 합치고(merge) 이름을 parts 라는 ndarray 를 생성한다.
    -> 합치는 방법이 merge뿐인걸까? 다른 방법들로는 
        -> README.md # 3.NumPy 배열 합치기 총정리

4. parts를 이용해서 각 항목의 평균값을 구한다.
    -> numpy에는 str로 저장되어 있기 때문에 따로 수치형 데이터 strengths 를 추출해서 .mean() 으로 평균값을 구한다.
    
    
5. 평균값이 50 보다 작은 값을 뽑아내서 parts_to_work_on.csv 라는 파일로 별도로 저장한다.
    -> 4번으로 구한 평균값을 기준으로 필터링하여 mean 이하인 데이터만 따로 추출 및 csv로 저장 ( csv는 prob_03 에서 진행한 코드 그대로 사용)
"""

# 1. numpy import하기
import numpy as np


# 2-1. csv를 numpy를 사용해서 읽어들이기
# 결측치가 있는지 없는지 모르기떄문에 혹시 있을 수 있는 결측치 처리를 위해 getfromtxt()를 사용

# -> 예외처리 추가 예정
data1 = np.genfromtxt('mars_base_main_parts-001.csv', delimiter=',', encoding='utf-8-sig', dtype=str, filling_values=np.nan)
data2 = np.genfromtxt('mars_base_main_parts-002.csv', delimiter=',', encoding='utf-8-sig', dtype=str, filling_values=np.nan)
data3 = np.genfromtxt('mars_base_main_parts-003.csv', delimiter=',', encoding='utf-8-sig', dtype=str, filling_values=np.nan)
# print(data1)

# 2-2. 각각 arr1, arr2, arr3 과 같이 ndarray 타입으로 가져온다.
# 각각의 데이터는 str, int 로 구성되어 있는 상태
arr1 = np.array(data1)
arr2 = np.array(data2)
arr3 = np.array(data3)

# print(arr1)
# print(arr2)
# print(arr3)

# 3개의 배열을 하나로 합치고(merge) 이름을 parts 라는 ndarray 를 생성한다.
# arr2, arr3 에서 [1:]을 사용하는 이유는 헤더를 제외하고 합ㅊㅕ야 하기 때문
parts = np.vstack([arr1, arr2[1:], arr3[1:]])

# print(parts)
# [['parts' 'strength']
#  ['Concrete' '36']
#  ['Steel' '45']
#  ['Brick' '71']
#  ['Wood' '11']
#  ...


# print(np.shape(parts))
# (303, 2)

# strength 열만 정수로 추출
strengths = parts[1:, 1].astype(int)

# parts를 이용해서 각 항목의 평균값을 구한다.
print(f'strengths.mean : {strengths.mean()}')

# 평균값이 50 보다 작은 값을 뽑아내서 parts_to_work_on.csv 라는 파일로 별도로 저장한다.
# 평균보다 작은 행만 필터링 + 헤더 붙이기
filtered_parts = np.vstack([
    parts[0],
    parts[1:][strengths < strengths.mean()]
])
# print(filtered_parts)

# CSV로 저장
import csv
output_file = "parts_to_work_on.csv"
with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    # 내용
    writer.writerows(filtered_parts)
    
    
