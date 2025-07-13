"""
1. 돔 전체 면적 구하는 함수 생성 
-> def sphere_area(diameter : ... , meterial : 디폴트 -> 유리,  thickness라는 : 디폴트 -> 1)
    유리: 2.4g /cm3
    알루미늄: 2.7g/cm3
    탄소강: 7.85g/cm3

2. 재질과 지름은 input()을 사용해서 사용자로 부터 입력을 받아야 한다
    meterial, thickness = map(input(float))


3. 지구 기준 중력 -> 화성의 중력으로 수정


4. 모든 계산 결과에서 소수점 이하의 결과가 나올 경우 소수점 이하 세 자리까지만 출력해서 결과가 지나치게 길어지는 것을 피한다.


5. 계산 결과가 나오면 전역변수에 계산한 값을 저장하고 다음과 같은 형태로 출력한다.
전역변수 이름:
재질: material
지름: diameter
두께: thickness
면적: area
무게: weight
출력 형식: 재질 =⇒ 유리, 지름 =⇒ 000, 두께 =⇒ 000, 면적 =⇒ 000, 무게 =⇒ 000 kg


6. 작업이 완료되면 design_dome.py 라는 이름으로 저장한다.
"""
# 0.전역변수 미리 선언하기
# math 를 사용한 이유 ->  math.pi 를 사용하기 위함.
import math

# 전역변수 초기화
material = ""
diameter = 10
thickness = 0
area = 0.0
weight = 0.0

# 재질별 밀도 (g/cm^3) -> (kg/m^3)로 변환
MATERIAL_DENSITY = {
    "유리": 2.4 * 1000,       # 2400 kg/m^3
    "알루미늄": 2.7 * 1000,   # 2700 kg/m^3
    "탄소강": 7.85 * 1000     # 7850 kg/m^3
}


# 1. 돔 전체 면적 구하기
# 필요 파라미터
    # 사용자로부터 받아오는 재질 meterial
    # 사용자로부터 받아오는 두께 thickness
    # 지름 diameter : 10 

"""
함수 지정 할 때 default 값을 미리 지정할 수 있는데, 
아래와 같이 def sphere_area( meterial , thickness, diameter=10 ):  로 하면 오류가 나타나지 않는다.
하지만  def sphere_area( meterial , diameter=10 , thickness): 
이렇게 작성하면 오류가 나타난다.

위와 같은 오류가 나는 이유는

[ GPT 답변 ]
파이썬 함수 정의 시, 기본값이 지정되지 않은 인자는 기본값이 있는 인자보다 앞에 위치해야 하기 때문입니다.

✅ 파이썬 함수 인자 규칙 요약:
파이썬에서 함수의 인자는 다음 순서를 따라야 합니다:

def 함수이름(위치 인자, 기본값 인자, *가변 인자, 키워드 전용 인자, **키워드 가변 인자)

1. 위치 인자 (기본값 없는 것) 
2. 기본값이 있는 인자
3. *args
4. 키워드 전용 인자 (*,)
5. **kwargs
"""
# 돔의 길이를 재어보니 10m인 반구체의 형태를 한 돔의 전체 면적 구하기
# 사용 할 수 있는 재료는 유리, 알루미늄, 탄소강이 있다
"""
[해당 sphere_area은 V1임. 1번 순서 먼저 진행하기 위해 제작된 함수. 이후 3번, 4번 문제를 해결한 sphere_area는 아래에 위치.]
 
def sphere_area(material_input="유리", thickness_input=0.01, diameter_input=10):
    global material, diameter, thickness, area, weight

    material = material_input
    diameter = diameter_input
    thickness = thickness_input

    radius = diameter / 2
    area = 3 * math.pi * (radius ** 2)  # 반구체 전체 면적 (곡면 + 바닥면)

    volume = area * thickness  # m^3
    density = MATERIAL_DENSITY[material]  # kg/m^3
    weight = volume * density
    

    return area, weight
"""
    
    
    
# 2. 재질과 지름은 input()을 사용해서 사용자로 부터 입력을 받아야 한다
def get_valid_thickness():
    """
    사용자에게 두께(thickness)를 입력받아 유효성을 검증한 후 반환하는 함수.

    예외 처리 내용:
    - 입력값이 숫자가 아닌 경우: ValueError 처리
    - 입력값이 음수이거나 0인 경우: 조건 검사 후 경고 메시지 출력

    Returns:
        float: 0보다 큰 유효한 실수 형태의 두께 값
    """
    while True:
        user_input = input("두께를 입력하세요 (양수만 가능): ").strip()
        try:
            thickness = float(user_input)  # 숫자로 변환 시도
            if thickness > 0:
                return thickness
            else:
                print("⚠️ 두께는 0보다 커야 합니다.")
        except ValueError:
            print("⚠️ 숫자로 입력해주세요.")  # 문자 등 변환 불가할 경우 처리


def get_valid_meterial(allowed_items):
    """
    사용자에게 재질(material)을 입력받아 허용된 목록 내의 값인지 확인하는 함수.

    예외 처리 내용:
    - 사용자가 입력한 값이 허용된 리스트에 없을 경우: 잘못된 입력으로 간주하여 재입력 요청

    Args:
        allowed_items (list): 허용 가능한 재질 목록 (예: ["유리", "알루미늄", "탄소강"])

    Returns:
        str: 허용된 재질 중 사용자가 입력한 값
    """
    while True:
        user_input = input(f"다음 값 중 하나를 입력하세요: {allowed_items} ").strip()
        if user_input in allowed_items:
            return user_input
        else:
            print("⚠️ 잘못된 입력입니다. 다시 입력해주세요.")

allowed_items = ["유리", "알루미늄", "탄소강"]
meterial = get_valid_meterial(allowed_items)
print(f"선택된 재질: {meterial}")

thickness = get_valid_thickness()
print(f"입력된 두께: {thickness}")




# 3. 지구 기준 중력 -> 화성의 중력으로 수정
# 화성 중력 (지구 중력의 약 0.38배)
# 4. 소수점 이하 세 자리까지만 출력
MARS_GRAVITY_RATIO = 0.38
def sphere_area(material_input="유리", thickness_input=0.01, diameter_input=10):
    global material, diameter, thickness, area, weight

    material = material_input
    diameter = diameter_input
    thickness = thickness_input

    radius = diameter / 2
    area = 3 * math.pi * (radius ** 2)  # 반구체 전체 면적 (곡면 + 바닥면)

    volume = area * thickness  # m^3
    density = MATERIAL_DENSITY[material]  # kg/m^3
    
    weight = volume * density * MARS_GRAVITY_RATIO  # kg (화성 기준)

    # 소수점 3자리까지 반올림
    area = round(area, 3)
    weight = round(weight, 3)

    return area, weight
    
    
# 함수 실행
area, weight = sphere_area(meterial, thickness, diameter)

# 결과 출력
print(f"재질 =⇒ {material}, 지름 =⇒ {diameter}, 두께 =⇒ {thickness}, 면적 =⇒ {area}, 무게 =⇒ {weight}kg")
