

## 바이너리 파일이란?

- 0과 1로 이루어진 이진 데이터 형식으로 저장된 파일
- 사람이 읽을 수 없는 형태 (텍스트 편집기로 열면 깨짐)
- 파이썬 객체 전체 구조를 유지한 채 저장 가능 (ex. 리스트, 딕셔너리, 클래스 인스턴스 등)

---

##  바이너리 파일의 장점과 단점

| 항목 | 장점 | 단점 |
|------|------|------|
|  성능 | 읽기/쓰기 속도가 빠름 (특히 대용량 데이터 처리 시) | 사람이 직접 읽거나 편집할 수 없음 |
| 구조 유지 | 객체의 구조/형태(리스트, 딕셔너리, 클래스 등)를 그대로 보존 가능 | 포맷에 대한 사전 지식 필요 (`pickle`, `struct` 등) |
| 저장 효율 | 저장 용량이 텍스트보다 작음 (공백, 포맷, 구분자 없음) | 다른 언어나 환경과의 호환성 낮음 |
| 보안 | 사람이 쉽게 볼 수 없기 때문에 보안성 우수 | 디버깅 어려움 (직접 파일 열어볼 수 없음) |

---

## 🛠️ 바이너리 파일이 필요한 상황

1. 대용량 데이터를 자주 저장/불러오는 경우 (ex. 머신러닝 모델 저장/로드)
2. 데이터 구조(객체)를 그대로 보존해야 할 때 (ex. 복잡한 딕셔너리, 리스트)
3. 데이터 노출을 막아야 할 때 (ex. 사용자 설정, 인증 정보 등)
4. 속도가 중요한 시스템 (ex. 게임 저장, 센서 데이터 로깅 등)

---

## 파이썬에서의 사용 이점

| 기술 요소 | 설명 |
|-----------|------|
| `pickle` | Python 객체를 직렬화하여 `.bin` 저장 후 복원 가능 |
| `struct` | C 스타일의 바이너리 구조를 다룰 수 있음 |
| `joblib` | 넘파이 배열, 머신러닝 모델 저장에 특화된 직렬화 도구 |

### 예시 1: `pickle`로 저장

```python
import pickle

data = [{'name': 'oxygen', 'flammability': 0.9}, {'name': 'hydrogen', 'flammability': 1.0}]
with open('data.bin', 'wb') as f:
    pickle.dump(data, f)
```

###  예시 2: `pickle`로 복원

```python
with open('data.bin', 'rb') as f:
    restored_data = pickle.load(f)
print(restored_data)
```

---

## `.csv` vs `.bin` 비교

| 항목 | CSV 파일 | BIN 파일 |
|------|----------|----------|
| 사용 예 | 엑셀/텍스트로 열기 | 파이썬 리스트/딕셔너리 저장 |
| 도구 | 엑셀, pandas, csv | pickle, joblib |
| 가독성 | 있음 (사람이 읽음) | 없음 (기계 전용) |
| 타입 정보 | 손실 (모두 문자열) | 유지 (객체 그대로) |
| 보안성 | 낮음 | 높음 |

---

## 요약

- `.bin`은 파이썬 객체 저장에 매우 적합
- `pickle`을 사용하여 빠르고 구조 보존이 용이함
- 대규모 데이터, 모델 저장, 고속 입출력에 매우 유리
