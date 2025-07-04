# 1. csv 내용 읽어와서 출력
# pandas 라는 라이브러리가 대중적으로 사용되어지고 있지만, 특정 라이브러리를 사용할 수 없다는 제약사항을 보았을 때, 내장 라이브러리인 csv 를 사용해서 하라고 듯


import csv



# 파일 열기 (읽기 모드)
# 파일을 오픈할 때 여러 옵션들이 존재.  하단은 open 이라는 함수의 내장 함수를 가져온 내용
"""
# Unbuffered binary mode: returns a FileIO
@overload
def open(
file: FileDescriptorOrPath,
mode: OpenBinaryMode,
buffering: Literal[0],
encoding: None = None,
errors: None = None,
newline: None = None,
closefd: bool = True,
opener: _Opener | None = None,
) -> FileIO: ...



여기서 mode 는 해당 파일을 읽어와 어떠한 행동을 할 지를 결정해주는 모드이다. 
OpenBinaryMode 를 한번 더 들어가보면 
OpenTextMode = Literal['r+', '+r', 'rt+', 'r+t', '+rt', 'tr+', 't+r',
'+tr', 'w+', '+w', 'wt+', 'w+t', '+wt', 'tw+', 't+w', '+tw', 'a+', '+a', 'at+', 
'a+t', '+at', 'ta+', 't+a', '+ta', 'x+', '+x', 'xt+', 'x+t', '+xt', 'tx+', 
't+x', '+tx', 'w', 'wt', 'tw', 'a', 'at', 'ta', 'x', 'xt', 'tx', 'r', 'rt',
'tr', 'U', 'rU', 'Ur', 'rtU', 'rUt', 'Urt', 'trU', 'tUr', 'Utr']
와 같이 나타난다. 해당 영어들은 읽고, 쓰고, 삭제 등을 할 수 있는 기능들이다.

gpt 답변

주요 파일 모드:
'r' (읽기 모드):
파일을 읽기 위해 엽니다. 파일이 존재하지 않으면 오류가 발생합니다.
'w' (쓰기 모드):
파일을 쓰기 위해 엽니다. 파일이 존재하면 내용을 덮어쓰고, 존재하지 않으면 새로 생성합니다.
'a' (추가 모드):
파일의 끝에 내용을 추가하기 위해 엽니다. 파일이 존재하지 않으면 새로 생성합니다.
'b' (바이너리 모드):
바이너리 데이터를 읽거나 쓰기 위해 사용합니다. 텍스트 파일과 구분하여 사용합니다.
'+' (읽기/쓰기 모드):
파일을 읽고 쓸 수 있도록 열립니다. 예를 들어, `'r+'`는 읽기 및 쓰기, `'w+'`는 쓰기 및 읽기, `'a+'`는 추가 및 읽기 기능을 제공합니다. 
"""




# 파일 읽어 출력 + 읽어서 python의 list로 객체변환
mars_list = list()
with open('Mars_Base_Inventory_List.csv', 'r', newline='', encoding='utf-8') as csvfile:
    # csv.reader 객체 생성
    reader = csv.reader(csvfile)

    # 헤더 읽기 (선택 사항)
    header = next(reader, None)
    print("헤더:", header)

    # 각 행 읽기
    for row in reader:
        # 각 행 별 데이터는 Substance,Weight (g/cm³),Specific Gravity,Strength,Flammability 로 구성되어있다
        # 각각에 대한 수치 및 데이터는 모두 문자열로 저장되어지는데, 이러면 나중 과제에서 숫자에 대한 정렬방식에서 문제가 생길 수 있기 때문에 각각에 대한 문자인지, 숫자인지를 지정해주고 시작
        # 타입 변환 후 리스트로 저장
        sub, weight, gravity, strength, flam = row
        print(row)
        ## 작업중 나타난 오류
        ### -> weight,gravity 에 'Various' 라는 수치가 아닌 문자가 나타난 부분이 있다. 
        # 해결방법 > try-except 구문을 사용해서 "Various" 또는 숫자로 변환할 수 없는 값을 수정
        # 'Various'나 숫자 아님을 처리
        weight = float(weight) if weight.lower() != 'various' else None
        gravity = float(gravity) if gravity.lower() != 'various' else None
        flam = float(flam)
        
        mars_list.append([
                str(sub),
                weight,
                gravity,
                str(strength),
                flam
            ])


print(mars_list)


# 시간 역순 출력
"""
현재 mars_list의 형식은
[['Urea', '1.32', '1.32', 'Weak', '0.6'], ['Phenolic Resin', 'Various', 'Various', 'Various', '0']]
와 같이 나타난다. 내장함수인 sorted에 lambda 식을 붙여 정렬을 할 수 있따.
lambda의 x 를 기준으로 reverse(역순으로 할거면 true, 아니면 false) 의 조건을 걸어한다.
x[0]은 현재 리스트의 x 는 ['Urea', '1.32', '1.32', 'Weak', '0.6'] 를 이야기 하기떄문에 몇번째 인덱스에 있는 변수를 기준으로 할지를 골라야 하는 것
x[0]은 첫번쨰 'urea'가 있는 위치를 기준으로 하겠다는 뜻.
현재는 인화성이 높은 순이라 햇으니, 인화성은 Flammability 이니 맨 마지막 인덱스다. (맨마지막 인덱스 : 4 )
"""
high_flammability_mars_list = sorted(mars_list, key=lambda x: x[4], reverse=True)


print('------high_flammability_mars_list -----')
for row in high_flammability_mars_list:
    print(row)




# - 인화성 지수가 0.7 이상되는 목록을 뽑아서 별도로 출력한다.
# 인화성지수 Flammability 의 필터링을 위해 파이썬의 리스트 컴프리헨션으로 조건을 붙여 진행

"""
mars_list라는 기존 리스트에서
각 item을 하나씩 꺼내면서,
item[4] (즉, 인화성 지수)가 0.7 이상인 경우만
새로운 리스트에 담는다 → 그게 high_flammability_list
"""
high_flammability_list = [item for item in high_flammability_mars_list if item[4] >= 0.7]

print('------high_flammability_mars (upper 0.7) -----')
for row in high_flammability_list:
    print(row)



# CSV로 저장
output_file = "Mars_Base_Inventory_danger.csv"
with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    # 헤더
    writer.writerow(["Substance", "Weight", "Specific Gravity", "Strength", "Flammability"])
    # 내용
    writer.writerows(high_flammability_list)
    
    




# ## 제약사항
# - Python에서 기본 제공되는 명령어만 사용해야 하며 별도의 라이브러리나 패키지를 사용해서는 안된다.
# - 파일을 다루는 부분들은 모두 예외처리가 되어 있어야 한다.
# ## 보너스 과제
# - 인화성 순서로 정렬된 배열의 내용을 이진 파일형태로 저장한다. 
# - 파일이름은 Mars_Base_Inventory_List.bin
# 저장된 Mars_Base_Inventory_List.bin 의 내용을 다시 읽어 들여서 화면에 내용을 출력한다.
# - 텍스트 파일과 이진 파일 형태의 차이점을 설명하고 장단점을 함께 설명할 수 있게 준비한다.



import pickle

# high_flammability_mars_list 는 인화성 순으로 정렬된 리스트라고 가정
# "wb": 쓰기 + 바이너리 모드 (write binary)
# pickle.dump(): 객체를 파일에 직렬화하여 저장

print('*'*100)
with open("Mars_Base_Inventory_List.bin", "wb") as bin_file:
    pickle.dump(high_flammability_mars_list, bin_file)

    
    
with open("Mars_Base_Inventory_List.bin", "rb") as bin_file:
    loaded_data = pickle.load(bin_file)

# 출력
for row in loaded_data:
    print(row)
print('*'*100)