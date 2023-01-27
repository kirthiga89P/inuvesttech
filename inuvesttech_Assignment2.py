

######Assignment_2 - Moving to 6month tab
####Screenshot of result will get captured in "Screenshot\Assignment2" folder -"Assignment2.png"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
servobj=Service(r"C:\Users\kirthiga\OneDrive\Desktop\webdriver\chromedriver_win32(1)\chromedriver.exe") #Update current webdriver location
driver=webdriver.Chrome(service=servobj)
driver.get("https://inuvest.tech/")
driver.maximize_window()
driver.execute_script("document.body.style.zoom='75%'") ###Zoom in so that all the details of the price will display as per screenshot
###scroll down to the bottom section
driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.XPATH,"/html/body/app-root/nb-layout/nb-layout-column/div/div/app-home/div/div[2]/div[14]/div/p")) 
element =driver.find_element(By.XPATH,"/html/body/app-root/nb-layout/nb-layout-column/div/div/app-home/div/div[3]/button[3]")
####Click the 6month tab
driver.execute_script("arguments[0].click();", element);
time.sleep(5) # To see the result 
###Capture the screenshot
driver.save_screenshot(".\\Screenshot\\Assignment2\\" +"Assignment2.png")
driver.close()


    
