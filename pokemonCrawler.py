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
print(macro.crawlByXpath('//*[@id="mw-content-text"]/div/div[1]/div[1]/div[1]/div[1]/strong'))              
