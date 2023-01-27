#Login test case Scenario - Used Pytest framework
#Run in command Prompt: pytest -v --html=Report\Login_report.html testcase\testLogin.py --browser chrome
#Screenshot of failed Test Cases Captured inuvesttech\Screenshot\Login\Fail_Test_Case\
#Screenshot of Passed Test Cases Captured inuvesttech \Screenshot\Login\Pass_Test_Case\
#Report of all Login case get generated in inuvesttech\Report\ 
#Log will get captured in Logs Folder
import pytest
from selenium import webdriver
from pageobject.Login import Login
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.custom_logger import Loggen
from utilities.mandatory_validation import mandatoryValidation
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,time
class Test_LOGIN_001:
    baseURL=ReadConfig.getApplicationURL()    
    logger=Loggen.loggen()     
    
    #Test Case Id:TC_LOGIN_001 - Login with valid details
    def test_login_ValidInput(self,setup): 
        try:
            email="testprofile@inuvest.tech"
            password="Internshala@123"
            self.logger.info("******************Test_001_Login******************************************")
            self.logger.info("*****************Verifying Login Page with valid details*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            lp=Login(self.driver)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp.click_login_page() 
            self.driver.maximize_window()
            lp.set_email(email)
            lp.set_password(password)
            lp.click_login()      
        #time.sleep(5)
        #To make  wait till the page is completely loaded
            element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='navbarSupportedContent-3']/ul[2]/li/a")) #This is a dummy element
            )
        
            if self.driver.current_url == "https://inuvest.tech/dashboard/liveStrategies":
                self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\" +"test_login_valid_scenario.png")
                self.logger.info("*****************LoginTest with valid Details is Passed*************************************")
                self.driver.close()
                assert True
            else:
                self.logger.error("*****************LoginTest with valid Details is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_valid_scenario.png")
                self.driver.close()
                assert  False
            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False        
            
    #Test Case Id:TC_LOGIN_002  - Login with invalid Password
    def test_login_ValidEmail_InvalidPasswd(self,setup):  
        try:        
            email="testprofile@inuvest.tech"
            password="intern"
            self.logger.info("******************Test_001_Login******************************************")
            self.logger.info("*****************Verifying Login Page with invalid Password************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp=Login(self.driver)
            lp.click_login_page()
            self.driver.maximize_window()
            #time.sleep(5)
            lp.set_email(email)
            lp.set_password(password)             
            lp.click_login()             
                         
            if self.driver.current_url == "https://inuvest.tech/auth":
                element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='swal2-title']")) 
                )
                error_msg=element.text
                if error_msg=="Wrong username or password": 
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\" +"test_login_invalid_password_scenario.png")
                    lp.click_errorbtn()
                    self.logger.info("*****************LoginTest with Invalid Password Details is Passed*************************************")
                    self.logger.info("*****************Login Failed and Proper message displayed*************************************")
                    self.driver.close()
                    assert True
                else:
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_invalid_password_scenario.png")
                    lp.click_errorbtn()
                    self.logger.error("*****************LoginTest with Invalid Password Detail is Failed*************************************")
                    self.logger.error("*****************Login Failed and message not displayed as per requirement*************************************")
                    self.driver.close()
                    assert  False
            else:
                self.logger.error("*****************LoginTest with Invalid Password Detail is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_invalid_password_scenario.png")
                self.driver.close()
                assert  False            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False

    #Test Case Id:TC_LOGIN_003- Login with Invalid Email      
    def test_login_InValidEmail_validPasswd(self,setup):
        try:
            email="testprfile@inuvest.tech"
            password="Internshala@123"
            self.logger.info("******************Test_001_Login******************************************")
            self.logger.info("*****************Verifying Login Page with Invalid Email*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp=Login(self.driver)
            lp.click_login_page()
            self.driver.maximize_window()
            #time.sleep(5)
            lp.set_email(email)
            lp.set_password(password)            
            lp.click_login()      
             
            if self.driver.current_url == "https://inuvest.tech/auth":
                #print("true")
            #self.driver.switch_to.window(self.driver.current_window_handle)
                element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='swal2-title']")) 
                )
                error_msg=element.text
                if error_msg=="Wrong username or password": 
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\" +"test_login_invalid_email_scenario.png")
                    lp.click_errorbtn()
                    self.logger.info("*****************LoginTest with Invalid Email Details is Passed*************************************")
                    self.logger.info("*****************Login Failed and Proper message displayed*************************************")
                    self.driver.close()
                    assert True
                else:
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_invalid_email_scenario.png")
                    lp.click_errorbtn()
                    self.logger.error("*****************LoginTest with Invalid Email Details is Failed*************************************")
                    self.logger.error("*****************Login Failed and message not displayed as per requirement*************************************")
                    self.driver.close()
                    assert  False

            else:
                self.logger.error("*****************LoginTest with Invalid Email Details is Failed*************************************")
                #self.logger.info("*****************Error in Log*************************************")                       
                self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_invalid_email_scenario.png")
                self.driver.close()
                assert  False            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False

    #Test Case Id:TC_LOGIN_004 - Login with Invalid Details    
    def test_login_InValidEmail_InvalidPasswd(self,setup):
        try:
            email="testprfile@inuvest.tech"
            password="Internshala@1"
            self.logger.info("******************Test_001_Login******************************************")
            self.logger.info("*****************Verifying Login Page with Invalid Details*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp=Login(self.driver)
            lp.click_login_page()
            self.driver.maximize_window()
            #time.sleep(5)
            lp.set_email(email)
            lp.set_password(password)             
            lp.click_login()  
             
            if self.driver.current_url == "https://inuvest.tech/auth":
                #print("true")
            #self.driver.switch_to.window(self.driver.current_window_handle)
                element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='swal2-title']")) 
                )
                error_msg=element.text
                if error_msg=="Wrong username or password": 
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\" +"test_login_invalid_email_pwd_scenario.png")
                    lp.click_errorbtn()
                    self.logger.info("*****************LoginTest with Invalid login Details is Passed*************************************")
                    self.logger.info("*****************Login Failed and Proper message displayed*************************************")
                    self.driver.close()
                    assert True
                else:
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_invalid_email_pwd_scenario.png")
                    lp.click_errorbtn()
                    self.logger.error("*****************LoginTest with Invalid login Details is Failed*************************************")
                    self.logger.error("*****************Login Failed and message not displayed as per requirement*************************************")
                    self.driver.close()
                    assert  False

            else:
                self.logger.error("*****************LoginTest with Invalid login Details is Failed*************************************")
                #self.logger.info("*****************Error in Log*************************************")                       
                self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_invalid_email_pwd_scenario.png")
                self.driver.close()
                assert  False            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False

    #Test Case Id:TC_LOGIN_005  - New Login without confirming mail    
    def test_login_without_confirmmail(self,setup): 
        try:
            email="test19@inuvest.tech"
            password="testintern"
            self.logger.info("******************Test_001_Login******************************************")
            self.logger.info("*****************Verifying Login Page without confirm email*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp=Login(self.driver)
            lp.click_login_page()
            self.driver.maximize_window()
            #time.sleep(5)
            lp.set_email(email)
            lp.set_password(password)             
            lp.click_login()   
            
            if self.driver.current_url == "https://inuvest.tech/auth":
                element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='swal2-title']")) 
                )
                error_msg=element.text
                if error_msg=="Please confirm your email using the link sent to your email address.": 
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\" +"test_login_without_confirm_email_scenario.png")
                    lp.click_errorbtn()
                    self.logger.info("*****************Login Page without confirm email is Passed*************************************")
                    self.logger.info("*****************Login failed and Proper message displayed as per requirement*************************************")
                    self.driver.close()
                    assert True
                else:
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_without_confirm_email_scenario.png")
                    lp.click_errorbtn()
                    self.logger.error("*****************Login Page without confirm email is Failed*************************************")
                    self.logger.error("*****************Message not displayed per requirement*************************************")
                    self.driver.close()
                    assert False
            else:
                self.logger.error("*****************Login Page without confirm email is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_without_confirm_email_scenario.png")
                self.driver.close()
                assert  False
            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False 
            
    #Test Case Id:TC_LOGIN_006 - Validating forgot password link with valid Emailid    
    def test_login_forgotPasswd(self,setup):
        try:
            email="testprofile@inuvest.tech"
            self.logger.info("******************Test_001_Login******************************************")
            self.logger.info("*****************Verifying Forgot password with Valid Emailid*********************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp=Login(self.driver)
            lp.click_login_page()
            self.driver.maximize_window()
            #time.sleep(5)
            lp.set_email(email)
            lp.click_forgot_pwd()             
            
            if self.driver.current_url == "https://inuvest.tech/auth":
                #print("true")
            #self.driver.switch_to.window(self.driver.current_window_handle)
                element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='swal2-title']")) 
                )
                error_msg=element.text
                if error_msg=="An email has been sent to your registered email to change the password": 
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\" +"test_login_forgotpasswrd_validemail.png")
                    lp.click_errorbtn()
                    self.logger.info("*****************Forget Password with valid Email working as per expected*************************************")
                    self.logger.info("*****************Proper message displayed and email sent as per requirement*************************************")
                    self.driver.close()
                    assert True
                else:
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_forgotpasswrd_validemail.png")
                    lp.click_errorbtn()
                    self.logger.error("*****************Forget Password with valid email not working as per expected*************************************")
                    self.logger.error("*****************Message not displayed per requirement*************************************")
                    self.driver.close()
                    assert  False

            else:
                self.logger.error("*****************Forget Password not working as per expected*************************************")
                #self.logger.info("*****************Error in Log*************************************")                       
                self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_forgotpasswrd_validemail.png")
                self.driver.close()
                assert  False            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False

    #Test Case Id:TC_LOGIN_007- Validating Forgot Password with invalid Email  
    def test_login_forgotPasswd_Invalidemail(self,setup):
        try:
            email="testprofile@inuvet.tech"
            self.logger.info("******************Test_001_Login******************************************")
            self.logger.info("*****************Verifying Forgot Password with Invalid Email*******************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp=Login(self.driver)
            lp.click_login_page()
            self.driver.maximize_window()
            #time.sleep(5)
            lp.set_email(email)
            lp.click_forgot_pwd()      
            
            if self.driver.current_url == "https://inuvest.tech/auth":
                
                element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='swal2-title']")) 
                )
                error_msg=element.text               
                if error_msg=="This email does not exist": 
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\"+"test_login_forgotpasswrd_Invalidemail.png")
                    lp.click_errorbtn()
                    self.logger.info("*****************Forget Password with Invalid Email working as per expected*************************************")
                    self.logger.info("*****************Proper message displayed as per requirement*************************************")
                    self.driver.close()
                    assert True
                else:
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\"+"test_login_forgotpasswrd_Invalidemail.png")
                    lp.click_errorbtn()
                    self.logger.error("*****************Forget Password with Invalid Email not working as per expected*************************************")
                    self.logger.error("*****************Message not displayed per requirement*************************************")
                    self.driver.close()
                    assert  False

            else:
                self.logger.error("*****************Forget Password not working as per expected*************************************")
                self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_forgotpasswrd_Invalidemail.png")
                self.driver.close()
                assert  False            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False

    #Test Case Id:TC_LOGIN_008 - Validating Forgot Password without Entering Email       
    def test_login_forgotpwd_NoEmail(self,setup):
        try:
            self.logger.info("******************Test_001_Login******************************************")
            self.logger.info("*****************Verifying Forgot Password without Entering Email**********")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp=Login(self.driver)
            lp.click_login_page()
            self.driver.maximize_window() 
            #time.sleep(5)
            lp.click_forgot_pwd() 
                       
            if self.driver.current_url == "https://inuvest.tech/auth":
                #print("true")
            #self.driver.switch_to.window(self.driver.current_window_handle)
                element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='swal2-title']")) 
                )
                error_msg=element.text
                
                if error_msg=="Please enter email.": 
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\" +"test_login_forgotpasswrd_Noemail.png")
                    lp.click_errorbtn()
                    self.logger.info("*****************Forget Password with No Email working as per expected*************************************")
                    self.logger.info("*****************Proper message displayed  as per requirement*************************************")
                    self.driver.close()
                    assert True
                else:
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_forgotpasswrd_Noemail.png")
                    lp.click_errorbtn()
                    self.logger.error("*****************Forget Password with No Email not working as per expected*************************************")
                    self.logger.error("*****************Message not displayed per requirement*************************************")
                    self.driver.close()
                    assert  False

            else:
                self.logger.error("*****************Forget Password with No Email not working as per expected*************************************")
                #self.logger.info("*****************Error in Log*************************************")                       
                self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_forgotpasswrd_Noemail.png")
                self.driver.close()
                assert  False            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False

    #Test Case Id:TC_LOGIN_009 - Login without Email
    def test_login_NoEmail(self,setup): 
        try:
            
            password="testIntern"
            self.logger.info("******************Test_001_Login******************************************")
            self.logger.info("*****************Verifying Login without Email*****************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp=Login(self.driver)  
            mand_validate= mandatoryValidation(self.driver)
            lp.click_login_page()
            self.driver.maximize_window()
            lp.set_password(password)
            lp.click_login()          
            time.sleep(2)
            if self.driver.current_url == "https://inuvest.tech/auth":
                #print(lp.get_bordervalue_txtemail())
                if mand_validate.get_bordervalue(lp.textbox_email)==True and mand_validate.get_background_image(lp.textbox_email)==True:
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\" +"test_login_Email_mandatory.png")
                    self.logger.info("****************Email mandatory test is Passed*************************************")
                    self.logger.info("****************Email Textbox was higlighted in red and cross icon is displayed*************")
                    self.driver.close()
                    assert True
                else:

                    self.logger.error("*****************Email mandatory test is Failed*************************************")
                    self.logger.error("****************Email Textbox may not higlighted in red or cross icon not displayed*************************************")
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_Email_mandatory.png")
                    self.driver.close()
                    assert  False
            else:
                self.logger.error("*****************Email mandatory test is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_Email_mandatory.png")
                self.driver.close()
                assert  False
            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False
            
    #Test Case Id:TC_LOGIN_010 - Login with Invalid Email Format
    def test_login_invalidEmail_format(self,setup): 
        try:
            email="test"
            password="tessample"
            self.logger.info("******************Test_001_Login******************************************")
            self.logger.info("*****************Verifying Login with Invalid Email Format****************")
            self.driver=setup
            mand_validate= mandatoryValidation(self.driver)
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp=Login(self.driver)            
            lp.click_login_page()
            self.driver.maximize_window()
            lp.set_email(email)
            lp.set_password(password)
            lp.click_login()          
            time.sleep(2)
            if self.driver.current_url == "https://inuvest.tech/auth":
                #print(lp.get_bordervalue_txtemail())
                if mand_validate.get_bordervalue(lp.textbox_email)==True and mand_validate.get_background_image(lp.textbox_email)==True:
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\" +"test_login_Email_invalid_format.png")
                    self.logger.info("****************Invalid Email format test is Passed*************************************")
                    self.logger.info("****************Email Textbox was higlighted in red and cross icon is displayed*************")
                    self.driver.close()
                    assert True
                else:
                    self.logger.error("*****************Invalid Email format test is Failed*************************************")
                    self.logger.error("****************Email Textbox may not higlighted in red or cross icon not displayed*************************************")
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_Email_invalid_format.png")
                    self.driver.close()
                    assert  False
            else:
                self.logger.error("*****************Invalid Email format test is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_Email_invalid_format.png")
                self.driver.close()
                assert  False
            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False 
            
     #Test Case Id:TC_LOGIN_011 - Login without Password
    def test_login_NoPassword(self,setup): 
        try:
            email="testprofile@inuvest.tech"            
            self.logger.info("******************Test_001_Login******************************************")
            self.logger.info("*****************Verifying Login without Password*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp=Login(self.driver)
            mand_validate= mandatoryValidation(self.driver)
            lp.click_login_page()            
            self.driver.maximize_window()
            lp.set_email(email)
            lp.click_login()        
            time.sleep(2)
            if self.driver.current_url == "https://inuvest.tech/auth":
                if mand_validate.get_bordervalue(lp.textbox_password)==True and mand_validate.get_background_image(lp.textbox_password)==True :
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\" +"test_login_Password_mandatory.png")
                    self.logger.info("****************Password mandatory test is Passed*************************************")
                    self.logger.info("****************Password Textbox was higlighted in red and cross icon is  displayed*************************************")
                    self.driver.close()
                    assert True
                else:
                    self.logger.error("*****************Password mandatory test is Failed*************************************")
                    self.logger.error("****************Password Textbox may not higlighted in red or cross icon not displayed*************************************")
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_Password_mandatory.png")
                    self.driver.close()
                    assert  False
            else:
                self.logger.error("*****************Password mandatory test is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_Password_mandatory.png")
                self.driver.close()
                assert  False
            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False 

    #Test Case Id:TC_LOGIN_012 - Verifying Signup link
    def test_login_signup_link(self,setup): 
        try:
            self.logger.info("******************Test_001_LOGIN******************************************")
            self.logger.info("*****************Verifying signup link*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp=Login(self.driver)
            lp.click_login_page()
            self.driver.maximize_window()          
            lp.click_signup()
             #To make  wait till the page is completely loaded
            element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='first']/div[7]/button")) # To check any web element displayed in the page
            )
            if self.driver.current_url == "https://inuvest.tech/auth/signup":
                self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\" +"test_login_signup_link.png")
                self.logger.info("***************** Signup link work as per expectd*************************************")
                self.driver.quit()
                assert True
            else:                
                self.logger.error("*****************Signup link is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_signup_link.png")
                self.driver.quit()
                assert  False           
        except Exception as ex:
            self.driver.quit()
            print(ex)
            assert  False
    
  #Test Case Id:TC_LOGIN_013 - Check that the google account page opened once sigin link button clicked
  ###Checked just the google account page displayed but didnt check the entire signin process using gmail account
    def test_login_SignIn_Gmailaccount(self,setup): 
        try:
            self.logger.info("******************Test_001_Login******************************************")
            self.logger.info("*****************Verifying Signin Gmail account In Login Page*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            lp=Login(self.driver)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp.click_login_page()  
            self.driver.maximize_window()
            lp.click_signin()  
            time.sleep(5)
            ids= self.driver.window_handles            
            child_window_id=None
            if len(ids)==2:            
                child_window_id=ids[1]              
            if  child_window_id  is not None:
                self.driver.switch_to.window(child_window_id)            
                googleaccountopentext=self.driver.find_element(By.XPATH,"//*[@id='headingSubtext']/span/button").text
                if googleaccountopentext=="inuvest.tech":
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\" +"test_login_sigin_email.png")
                    self.logger.info("****************Signin Gmail account Page opened successfully*************************************")
                    self.driver.quit()
                    assert True
                else:
                    self.logger.error("*****************Signin Gmail account Page opened test is Failed*************************************")
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_sigin_email.png")
                    self.driver.quit()
                    assert  False 
            else:
                    self.logger.error("******************Signin Gmail account Page opened test is Failed*************************************")
                    self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_sigin_email.png")
                    self.driver.quit()
                    assert  False 
                  
        except Exception as ex:
            self.driver.quit()
            print(ex)
            assert  False 

    #Test Case Id:TC_LOGIN_014 - Verifying Dont have a account? label
    def test_login_Chk_lbl_Donthaveaaccount(self,setup): 
        try:
            self.logger.info("******************Test_001_Login******************************************")
            self.logger.info("*****************Verifying Dont have a account? label in Login Page*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            lp=Login(self.driver)
            lp.click_login_page()
            self.driver.maximize_window()                                          
            if "Dont have a account?" in lp.get_acc() :
                self.driver.save_screenshot(".\\Screenshot\\Login\\Pass_Test_Case\\" +"test_login_dontacc_label.png")
                self.logger.info("****************Dont have a account? label in Login Page test is Passed*************************************")
                self.driver.close()
                assert True
            else:
                self.logger.error("*****************Dont have a account? label in Login Page test is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\Login\\Fail_Test_Case\\" +"test_login_dontacc_label.png")
                self.driver.close()
                assert  False            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False   