from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Macro:
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome("/Users/ihanjin/Downloads/chromedriver", options=chrome_options)

    def waitMsg(self, work):
        print("기다리는 중 : "+ work)
        
    def completeMsg(self, work):
        print("완료함 : " + work)

    def loadUrl(self, url, siteName):
        Macro.driver.get(url)
        Macro.completeMsg(self, "사이트 로드")

    def crawlByXpath(self, xpath):
        return Macro.driver.find_element_by_xpath(xpath).text

    # 엔터가 클릭보다 빠르다, 클릭으로 안되고 엔터만 되는 버튼도 있음
    def enterButtonNow(self, xpath, buttonName):
        button = Macro.driver.find_elements_by_xpath(xpath)
        if len(button) != 0:
            button[0].send_keys(Keys.ENTER)
            completeMsg(buttonName+" 클릭")

    def clickButtonNow(self, xpath, buttonName):
        button = Macro.driver.find_elements_by_xpath(xpath)
        if len(button) != 0:
            button[0].click
            completeMsg(buttonName+" 클릭")

    def waitNewPage(self):
        print("새로운 페이지 기다리는중...")
        Macro.driver.implicitly_wait(10)
        Macro.completeMsg(self, "새 페이지 로드")
        
    
        
    # 클릭 안되는 버튼은 iframe이 둘러싸고 있는지 확인하고,
    # 만약 그렇다면 iframe을 전환해줘야 한다.    
    def switchIframe(self, xpath):
        driver.switch_to.frame(driver.find_element_by_xpath(xpath))
        print("프레임 변경 완료")
        
    
macro = Macro()
macro.waitNewPage()
macro.loadUrl('https://pokemon.fandom.com/ko/wiki/%EC%9D%B4%EC%83%81%ED%95%B4%EC%94%A8_(%ED%8F%AC%EC%BC%93%EB%AA%AC)', '이상해씨')

#포켓몬 이름
print(macro.crawlByXpath('//*[@id="mw-content-text"]/div/div[1]/div[1]/div[1]/div[1]/strong'))              

#속성1
print(macro.crawlByXpath('/html/body/div[4]/div[3]/div[5]/main/div[3]/div[1]/div/div[1]/table/tbody/tr[2]/td[1]/div/span/a[1]/span'))
#속성2
print(macro.crawlByXpath('/html/body/div[4]/div[3]/div[5]/main/div[3]/div[1]/div/div[1]/table/tbody/tr[2]/td[1]/div/span/a[2]/span'))

#분류
print(macro.crawlByXpath('/html/body/div[4]/div[3]/div[5]/main/div[3]/div[1]/div/div[1]/table/tbody/tr[2]/td[2]'))


#도감번호 TODO: 도감 제목과 번호 분리
#관동
print(macro.crawlByXpath('/html/body/div[4]/div[3]/div[5]/main/div[3]/div[1]/div/div[1]/table/tbody/tr[7]/td/table/tbody/tr[2]/td[1]'))
#성도
print(macro.crawlByXpath('/html/body/div[4]/div[3]/div[5]/main/div[3]/div[1]/div/div[1]/table/tbody/tr[7]/td/table/tbody/tr[2]/td[2]'))
#호연
print(macro.crawlByXpath('/html/body/div[4]/div[3]/div[5]/main/div[3]/div[1]/div/div[1]/table/tbody/tr[7]/td/table/tbody/tr[2]/td[3]'))
#칼로스
print(macro.crawlByXpath('/html/body/div[4]/div[3]/div[5]/main/div[3]/div[1]/div/div[1]/table/tbody/tr[7]/td/table/tbody/tr[3]/td[1]'))
#가라르 TODO: 코스트/센트럴/마운틴 도감 분류
print(macro.crawlByXpath('/html/body/div[4]/div[3]/div[5]/main/div[3]/div[1]/div/div[1]/table/tbody/tr[7]/td/table/tbody/tr[3]/td[2]'))

#도감 색 TODO: 색상코드 가져오기
print(macro.crawlByXpath('/html/body/div[4]/div[3]/div[5]/main/div[3]/div[1]/div/div[1]/table/tbody/tr[11]/td[1]'))

#기초 친밀도
print(macro.crawlByXpath('/html/body/div[4]/div[3]/div[5]/main/div[3]/div[1]/div/div[1]/table/tbody/tr[11]/td[2]'))

#키

#몸무게

#포획률

#성비

#알그룹

#부화걸음수

