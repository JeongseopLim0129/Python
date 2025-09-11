from selenium import webdriver
from selenium.webdriver.common.by import By

# 지시사항 1번을 작성하세요.
with webdriver.Firefox() as driver:
# 지시사항 2번을 작성하세요.
    driver.get('http://localhost:8080')
# 지시사항 3번을 작성하세요.
    a = driver.find_element(By.TAG_NAME,'title')
    print(a.text)
# 지시사항 4번을 작성하세요.
    b_list = driver.find_elements(By.TAG_NAME,'img')
    for i in b_list:
        print(i.get_attribute('src'))
# 지시사항 5번을 작성하세요.
c = driver.find_element(By.TAG_NAME,'div')
for div in c:
    p_list = div.find_element(By.TAG_NAME, 'p')
    for p in p_list:
        print(c.text)