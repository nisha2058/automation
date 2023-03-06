import schedule
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import pyautogui as pg


def job():

    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': os.getcwd(), 'plugins.always_open_pdf_externally': True}
    chrome_options.add_experimental_option('prefs', prefs)
    #chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options=chrome_options)


    driver.get("https://thehimalayantimes.com/")
    driver.maximize_window()
    time.sleep(5)
    folder= driver.find_element(By.XPATH,"//div[@class='extraLink HideMobile']//a[text()='E-Paper']").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(50)
    time.sleep(5)
    Continue=driver.find_element(By.XPATH,"//p[text()='Continue']").click()
    time.sleep(5)
    download=driver.find_element(By.XPATH,"//div[@id='ext-container-195']/..").click()
    #pg.leftClick(1138,172,1,1)
    driver.implicitly_wait(50)
    selectAll=driver.find_element(By.XPATH,"//div[text()='Select All']").click()
    driver.implicitly_wait(50)
    downloadd=driver.find_element(By.XPATH,"//div[text()='Download']").click()
    driver.implicitly_wait(50)
    ok=driver.find_element(By.XPATH,"//div[@style='text-align:center;']//input").click()
    driver.implicitly_wait(50)
    driver.switch_to.window(driver.window_handles[2])
    pdf=driver.find_element(By.TAG_NAME,'a').click()
    driver.switch_to.window(driver.window_handles[3])
    time.sleep(10)
    driver.quit()

    
    time.sleep(5)

    driver1 = webdriver.Chrome(chrome_options=chrome_options)        
    driver1.get("https://epaper.gorkhapatraonline.com/")
    driver1.maximize_window()
    time.sleep(5)
    folder= driver1.find_element(By.XPATH,"//a//img[@alt='rising-nepal']").click()
    #driver.switch_to.window(driver.window_handles[1])
    driver1.implicitly_wait(30)
    a=driver1.find_element(By.XPATH,"//div[@class='paperdesign'][1]").click()
    #driver.switch_to.window(driver.window_handles[2])
    driver1.switch_to.window(driver1.window_handles[1])
    driver1.implicitly_wait(30)   
    d=driver1.find_element(By.XPATH,"//button[@id='download' and @title='Download']").click()
    driver1.implicitly_wait(50)
    time.sleep(15)
    driver1.quit()




schedule.every().day.at("21:49").do(job)

while True:
 schedule.run_pending()
 time.sleep(1)



