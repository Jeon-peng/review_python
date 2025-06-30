# - 설치가 잘 되었는지 확인 하기 위해서 ‘Hello Mars’를 출력해 본다.
print('Hello mars')




# - 파일을 처리 할 때에 발생할 수 있는 예외를 처리한다.
# 오류가 나타날 수 있는 경우는 무엇일까?
# 인코딩이 제대로 인식가능한지?
# 해당 파일이 지정한경로 ( 같은 위치에 )애 있는지?
# 공백 파일일경우, 파일 내 자료가 있을 경우?
print('Hello mars')

file_path = "mission_computer_main.log"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        is_empty = True
        for line in f:
            print(line.strip())
            is_empty = False
        if is_empty:
            print("[⚠️ 경고] 파일은 존재하지만 내용이 없습니다.")
except FileNotFoundError:
    print(f"[❌ 오류] 파일을 찾을 수 없습니다: {file_path}")
except UnicodeDecodeError:
    print(f"[❌ 오류] 인코딩 문제로 파일을 읽을 수 없습니다: {file_path}")
except PermissionError:
    print(f"[❌ 오류] 파일에 접근할 권한이 없습니다: {file_path}")
except Exception as e:
    print(f"[❌ 예외 발생] 알 수 없는 오류: {e}")
