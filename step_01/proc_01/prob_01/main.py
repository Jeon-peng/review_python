"""
수행과제
로그 분석을 위해 Python으로 소프트웨어를 개발해야 한다. 이를 위해서 먼저 Python을 설치해야 한다.
빠른 개발을 위해 Python 개발 도구들을 알아보고 비교해서 하나의 도구를 선정해서 설치한다.
설치가 잘 되었는지 확인 하기 위해서 ‘Hello Mars’를 출력해 본다.
본격적으로 로그를 분석하기 위해서 mission_computer_main.log 파일을 열고 전체 내용을 화면에 출력해 본다. 이때 코드는 main.py 파일로 저장한다.
(로그 데이터는 별도 제공)
파일을 처리 할 때에 발생할 수 있는 예외를 처리한다.
mission_computer_main.log의 내용을 통해서 사고의 원인을 분석하고 정리해서 보고서(log_analysis.md)를 Markdown 형태로 를 작성해 놓는다.
"""

# - 설치가 잘 되었는지 확인 하기 위해서 ‘Hello Mars’를 출력해 본다.
print('Hello mars')




# - 파일을 처리 할 때에 발생할 수 있는 예외를 처리한다.
# 오류가 나타날 수 있는 경우는 무엇일까?
# 인코딩이 제대로 인식가능한지?
# 해당 파일이 지정한경로 ( 같은 위치에 )애 있는지?
# 공백 파일일경우, 파일 내 자료가 있을 경우?
#file_path가 폴더인데 실수로 열려고 하면 발생  IsADirectoryError
# 사용자의 개입으로 중단되었을 때  KeyboardInterrupt
print('Hello mars')

file_path = "mission_computer_main.log"
log_arr = []
try:
    with open(file_path, "r", encoding="utf-8") as f:
        is_empty = True
        for line in f:
            print(line.strip())
            log_arr.append(line)
            is_empty = False
        if is_empty:
            print("[⚠️ 경고] 파일은 존재하지만 내용이 없습니다.")
except FileNotFoundError:
    print(f"[❌ 오류] 파일을 찾을 수 없습니다: {file_path}")
except UnicodeDecodeError:
    print(f"[❌ 오류] 인코딩 문제로 파일을 읽을 수 없습니다: {file_path}")
except PermissionError:
    print(f"[❌ 오류] 파일에 접근할 권한이 없습니다: {file_path}")
except IsADirectoryError:
    print(f"[❌ 오류] 지정한 경로가 디렉토리입니다 (파일이 아님): {file_path}")
except KeyboardInterrupt:
    print("\n[🛑 중단] 사용자가 실행을 취소했습니다.")
except Exception as e:
    print(f"[❌ 예외 발생] 알 수 없는 오류: {e}")



"""
보너스 과제
출력 결과를 시간의 역순으로 정렬해서 출력한다.
출력 결과 중 문제가 되는 부분만 따로 파일로 저장한다.
"""
# 로그의 출력물을 배열로 저장되어 있으니 내장함수 reversed로 역순정렬한다
# 출력 결과 중 문제가 되는 부분??
# 특정 단어가 들어간 로그만 추출 
## 특정 단어 : unstable, explosion
exception_word = ['unstable', 'explosion']
err_arr = []
for line in reversed(log_arr):
    if any(word in line.lower() for word in exception_word):
        err_arr.append(line)
    print(line.strip())


# 에러 로그 출력
print("---------")
print("err_word:")
for err in err_arr:
    print(err.strip())

# 에러 로그 파일로 저장
with open("err.log", "w", encoding="utf-8") as f:
    for err in err_arr:
        f.write(err)