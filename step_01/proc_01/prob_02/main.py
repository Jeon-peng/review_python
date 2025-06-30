"""
수행과제
mission_computer_main.log 파일을 읽어들여서 출력한다. 콤마를 기준으로 날짜 및 시간과 로그 내용을 분류해서 Python의 리스트(List) 객체로 전환한다.
(여기서 말하는 리스트는 배열이 아니라 파이썬에서 제공하는 리스트 타입의 객체를 의미한다.)
전환된 리스트 객체를 화면에 출력한다.
리스트 객체를 시간의 역순으로 정렬(sort)한다.
리스트 객체를 사전(Dict) 객체로 전환한다.
사전 객체로 전환된 내용을 mission_computer_main.json 파일로 저장하는데 파일 포멧은 JSON(JavaScript Ontation)으로 저장한다.
"""


import json

# 파일 경로
file_path = "mission_computer_main.log"
output_json = "mission_computer_main.json"


log_list = list()


# 리스트에  콤마를 기준으로 날짜 및 시간과 로그 내용을 분류해서 넣어야한다.
# 리스트 안에 리스트를 넣을 수 있기 때문에
# list.append([날짜, 시간, 로그]) 이런식으로 분류해서 넣는 작업 진행

try:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # 빈 줄 건너뜀
            parts = line.split(",", maxsplit=2)
            if len(parts) == 3:
                timestamp, event, message = parts
                log_list.append([timestamp, event, message])
            else:
                print(f"[⚠️ 경고] 형식이 잘못된 줄: {line}")
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



# 리스트 출력
# for item in log_list:
#     print(item)

# 시간 역순 출력
log_list.sort(key=lambda x: x[0], reverse=True)



# 리스트 → 딕셔너리로 전환
print('역순 프로세스 start...')
log_dict_list = [
    {"timestamp": ts, "event": ev, "message": msg}
    for ts, ev, msg in log_list
]
print('역순 프로세스 success')

# JSON 파일로 저장
try:
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(log_dict_list, f, indent=4, ensure_ascii=False)
    print(f"JSON 파일로 저장 완료: {output_json}")
except Exception as e:
    print(f"저장 오류 {e}")
    
    

# 추가 보너스
# 사전 객체로 전환된 내용에서 특정 문자열 (예를 들어 Oxygen)을 입력하면 해당 내용을 출력하는 코드를 추가한다.
# 사전 객체로 변환하면서 'Oxygen' 포함 여부도 필터링
OXYGEN_KEYWORD = "Oxygen"

oxygen_dict_list = [
    {"timestamp": ts, "event": ev, "message": msg}
    for ts, ev, msg in log_list
    # .lower 을 쓰는 이유는 Oxygen의 대문자 소문자로인한 차이로 인식되지 않는것까지도 포함하기위함
    if OXYGEN_KEYWORD.lower() in msg.lower()
]

for item in log_list:
    print(oxygen_dict_list)