from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class SignUp:
    link_signup="//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[2]"
    textbox_first_name="//*[@id='first']/div[1]/div/input"
    textbox_last_name="//*[@id='first']/div[2]/div/input"
    textbox_mobile="//*[@id='first']/div[3]/div/input"
    textbox_email="//*[@id='first']/div[4]/div/input"
    textbox_password="//*[@id='first']/div[5]/div/input"
    link_terms_cond="//*[@id='first']/div[6]/a"
    link_login="//*[@id='first']/div[7]/p/span"
    label_signup="//*[@id='first']/div[6]"
    label_acc="//*[@id='first']/div[7]/p"
    btn_signup_resend="//*[@id='first']/div[7]/button"
    btn_ok="/html/body/div[2]/div/div[3]/button[1]"
    
    def __init__(self,driver):
        self.driver=driver
    def set_first_name(self,firstname):        
        self.driver.find_element(By.XPATH,self.textbox_first_name).send_keys(firstname)
    def set_last_name(self,lastname):
        self.driver.find_element(By.XPATH,self.textbox_last_name).send_keys(lastname)
    def set_mobile(self,mobile):
        self.driver.find_element(By.XPATH,self.textbox_mobile).send_keys(mobile)
    def set_email(self,email):
        self.driver.find_element(By.XPATH,self.textbox_email).send_keys(email)
    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password).send_keys(password)
    def get_acc_signup(self):
        return self.driver.find_element(By.XPATH,self.label_acc).text
    def get_signup(self):
        return self.driver.find_element(By.XPATH,self.label_signup).text
    def click_signup_page(self):
        self.driver.find_element(By.XPATH,self.link_signup).click()
    def click_login(self):
        self.driver.find_element(By.XPATH,self.link_login).click()
    def click_signup_resend(self):
        self.driver.find_element(By.XPATH,self.btn_signup_resend).click()    
    def click_terms_cond(self):
        self.driver.find_element(By.XPATH,self.link_terms_cond).click()
    def click_ok_msg(self):
        element=WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self.btn_ok)) 
                )
        element.click()        
    def check_resend_confirm_visible(self):
        labelbtn=self.driver.find_element(By.XPATH,self.btn_signup_resend).text
        #print(str(labelbtn))
        return str(labelbtn)



