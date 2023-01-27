from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    link_login="//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[1]"
    textbox_email="//*[@id='first']/div[1]/div/input"
    textbox_password="//*[@id='first']/div[2]/div/input"
    link_forgot_pwd="//*[@id='first']/div[2]/div/p/span"
    link_signup="//*[@id='first']/div[3]/p[2]/span"
    label_acc="//*[@id='first']/div[3]/p[2]"
    btn_login="//*[@id='first']/div[3]/button"
    btn_signin="//*[@id='first']/div[3]/p[1]/a"
    
    btn_error="/html/body/div[3]/div/div[3]/button[1]"
    
    def __init__(self,driver):
        self.driver=driver
    def set_email(self,email):        
        self.driver.find_element(By.XPATH,self.textbox_email).send_keys(email)
    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password).send_keys(password)
    def get_acc(self):
        return self.driver.find_element(By.XPATH,self.label_acc).text
    #def get_error_msg(self):
       # msg=self.driver.find_element(By.XPATH,self.errormsg).text
        #return self.msg
    def click_login_page(self):
        self.driver.find_element(By.XPATH,self.link_login).click()
    def click_login(self):
        self.driver.find_element(By.XPATH,self.btn_login).click()
    def click_signin(self):
        self.driver.find_element(By.XPATH,self.btn_signin).click()
    def click_forgot_pwd(self):
        self.driver.find_element(By.XPATH,self.link_forgot_pwd).click()
    def click_signup(self):
        self.driver.find_element(By.XPATH,self.link_signup).click()
    def click_errorbtn(self):
        element=WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self.btn_error)) 
                )        
        element.click()
    