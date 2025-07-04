from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# ChromeDriver 설정
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # 전체 창
service = Service("/path/to/chromedriver")  # Mac 기준 chromedriver 경로 설정

# 드라이버 실행
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://kirin-highschool.tistory.com/")

# 데이터프레임 초기화
df = pd.DataFrame(columns=["timestamp", "text"])

# 웹 요소 XPATH
button_xpath = '/html/body/div[2]/header/div/div/div/a/button/img'
text_xpath = '/html/body/div[2]/header/div/a/div'

# 반복 횟수 설정
repeat = 10

for i in range(repeat):
    try:
        # 버튼 클릭
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        button.click()

        # 텍스트 나타날 때까지 대기 후 추출
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, text_xpath)))
        text_element = driver.find_element(By.XPATH, text_xpath)
        text = text_element.text.strip()

        # 데이터프레임에 추가
        df.loc[len(df)] = [time.strftime("%Y-%m-%d %H:%M:%S"), text]
        print(df.tail(1))  # 실시간 출력

        time.sleep(1)  # 너무 빠른 클릭 방지
    except Exception as e:
        print("오류 발생:", e)
        break

driver.quit()

# 최종 결과 출력
print("\n📦 최종 수집된 텍스트 목록:")
print(df)
