#Signup functionality test case Scenario - Used Pytest framework
#Run in command Prompt: pytest -v --html=Report\Signup_report.html testcase\testSignUP.py --browser chrome
#Screenshot of failed Test Cases Captured in inuvesttech\Screenshot\SignUp\Fail_Test_Case\
#Screenshot of Passed Test Cases Captured in inuvesttech\Screenshot\SignUp\Pass_Test_Case\
#Report of all Signup case get generated in Report\Signup_report.html
#Log will get captured in Logs Folder
import pytest
from selenium import webdriver
from pageobject.SignUp import SignUp
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.custom_logger import Loggen
from utilities.mandatory_validation import mandatoryValidation
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,time
class Test_SIGNUP_001:
    baseURL=ReadConfig.getApplicationURL()    
    logger=Loggen.loggen()   
    
    #Test Case Id:TC_SIGNUP_001 - Signup with Valid Input Details including mobile number
    def test_signUp_ValidInput(self,setup): 
        try:
            first_name="testintern"
            last_name="p"
            mobile="1233434339"
            email="test39@inuvest.tech"  ####Please give new mail id before running
            password="testintern" #### Please give password
            self.logger.info("******************Test_001_SIGNUP******************************************")
            self.logger.info("*****************Verifying Signup Page with Mobile Number*********************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)
            sp.click_signup_page()
            self.driver.maximize_window()
            #time.sleep(5)
            sp.set_first_name(first_name)
            sp.set_last_name(last_name)
            sp.set_mobile(mobile)
            sp.set_email(email)
            sp.set_password(password)
            sp.click_signup_resend()           
            if self.driver.current_url == "https://inuvest.tech/auth/signup":
                element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='swal2-title']")) 
                )
                confirm_msg=element.text
                #print(confirm_msg)
                if confirm_msg=="Confirmation email has been sent to your email address. Please confirm to continue.":
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_signup_with_mobilenumber_scenario.png")
                    sp.click_ok_msg()
                    self.logger.info("*****************Proper message displayed and email sent as per requirement*************************************")
                    self.logger.info("*****************SignUp Test with Mobile Number is Passed*************************************")
                    self.driver.close()
                    assert True                 
                else:
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_with_mobilenumber_scenario.png")
                    sp.click_ok_msg()
                    self.logger.error("*****************SignUp Test with Mobile Number is Failed*************************************")
                    self.logger.error("*****************Message not displayed per requirement*************************************")
                    self.driver.close()
                    assert  False
            else:
                self.logger.error("*****************SignUp Test with Mobile Number is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_with_mobilenumber_scenario.png")
                self.driver.close()
                assert  False            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False   

    #Test Case Id:TC_SIGNUP_002- Signup with valid Input Details not including mobile number

    def test_signUp_ValidInput_without_mobileno(self,setup): 
        try:
            first_name="test2"
            last_name="p"            
            email="test42@inuvest.tech" ####Please give new mail id before running
            password="testing345" ####Please give password before running
            self.logger.info("******************Test_001_SIGNUP******************************************")
            self.logger.info("*****************Verifying Signup Page without Mobile number*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)
            sp.click_signup_page()
            self.driver.maximize_window()
            #time.sleep(5)
            sp.set_first_name(first_name)
            sp.set_last_name(last_name)            
            sp.set_email(email)
            sp.set_password(password)
            sp.click_signup_resend()          
                 
            if self.driver.current_url == "https://inuvest.tech/auth/signup" :
                element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='swal2-title']")) 
                )
                confirm_msg=element.text
                if confirm_msg=="Confirmation email has been sent to your email address. Please confirm to continue.":  
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_signup_without_mobilenumber_scenario.png")
                    sp.click_ok_msg()
                    self.logger.info("*****************Proper message displayed and email sent as per requirement*************************************")
                    self.logger.info("*****************SignUp Test with out Mobile Number is Passed*************************************")
                    self.driver.close()
                    assert True                   

                else:
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_without_mobilenumber_scenario.png")
                    sp.click_ok_msg()
                    self.logger.error("*****************SignUp Test with out Mobile Number is Failed*************************************")
                    self.logger.error("*****************Message not displayed per requirement*************************************")
                    self.driver.close()
                    assert  False
            else:
                    self.logger.error("*****************SignUp Test with out Mobile Number is Failed*************************************")                    
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_without_mobilenumber_scenario.png")
                    self.driver.close()
                    assert  False            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False 

     #Test Case Id:TC_SIGNUP_003 - Signup with already existing email id
    def test_signUp_existingmail(self,setup): 
        try:
            first_name="test3"
            last_name="p"        
            mobile="9232323232"
            email="testprofile@inuvest.tech"
            password="testing123"
            self.logger.info("******************Test_001_SIGNUP******************************************")
            self.logger.info("*****************Verifying Signup Page with existing mail id*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)
            sp.click_signup_page()
            self.driver.maximize_window()
            #time.sleep(5)
            sp.set_first_name(first_name)
            sp.set_last_name(last_name)
            sp.set_mobile(mobile)
            sp.set_email(email)
            sp.set_password(password)
            sp.click_signup_resend()
           
                 
            if self.driver.current_url == "https://inuvest.tech/auth/signup":
                element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='swal2-title']")) 
                )
                error_msg=element.text
                if error_msg=="This user already exists": 
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_signup_existing_email_scenario.png")
                    sp.click_ok_msg() 
                    self.logger.info("*****************Signup Page with existing mail id scenario is Passed*************************************")
                    self.logger.info("*****************Signup Page Failed and Proper message displayed*************************************")
                    self.driver.close()
                    assert True
                else:
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_existing_email_scenario.png")
                    sp.click_ok_msg()
                    self.logger.error("*****************Signup Page with existing mail id scenario is Failed*************************************")
                    self.logger.error("*****************Signup Failed and message not displayed as per requiement*************************************")
                    self.driver.close()
                    assert  False

            else:
                self.logger.error("*****************Signup Page with existing mail id scenario is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_existing_email_scenario.png")
                self.driver.close()
                assert  False
            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False
            
    #Test Case Id:TC_SIGNUP_004 - Resend confirmation message after signup with mobilenumber
    def test_Resend_confirm_ValidInput(self,setup): 
        try:
            first_name="test4"
            last_name="s"
            mobile="1233434339"
            email="testinternship54@inuvest.tech"####Please give new mail id before running
            password="testing123"
            self.logger.info("******************Test_001_SIGNUP******************************************")
            self.logger.info("*****************Verifying Resend Confirmation with Mobile Number*********************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)
            sp.click_signup_page()
            self.driver.maximize_window()
            #time.sleep(5)
            sp.set_first_name(first_name)
            sp.set_last_name(last_name)
            sp.set_mobile(mobile)
            sp.set_email(email)
            sp.set_password(password)
            sp.click_signup_resend()  
            sp.click_ok_msg()                 
            
            if self.driver.current_url == "https://inuvest.tech/auth/signup" and sp.check_resend_confirm_visible()=="RESEND CONFIRMATION":
                #print("test")
                sp.click_signup_resend() 
                element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='swal2-title']")) 
                )
                confirm_msg=element.text             
                if confirm_msg=="Confirmation email has been sent to your email address. Please confirm to continue.": 
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_resend_with_mobilenumber_scenario.png")
                    sp.click_ok_msg()
                    self.logger.info("*****************Proper message displayed and email sent as per requirement*************************************")
                    self.logger.info("*****************Resend Test with Mobile Number is Passed*************************************")
                    self.driver.close()
                    assert True                   

                else:
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_resend_with_mobilenumber_scenario.png")
                    sp.click_ok_msg()
                    self.logger.error("*****************Resend Test with Mobile Number is Failed*************************************")
                    self.logger.error("*****************Message not displayed per requirement*************************************")
                    self.driver.close()
                    assert  False
            else:
                    self.logger.error("*****************Resend Test with Mobile Number is Failed*************************************")                    
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_resend_with_mobilenumber_scenario.png")
                    self.driver.close()
                    assert  False
            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False   

    #Test Case Id:TC_SIGNUP_005 - Resend confirmation message after signup without mobile number
    def test_resend_ValidInput_without_mobileno(self,setup): 
        try:
            first_name="test5"
            last_name="s"            
            email="testinternship44@inuvest.tech"####Please give new mail id before running
            password="testing456"
            self.logger.info("******************Test_001_SIGNUP******************************************")
            self.logger.info("*****************Verifying Resend Confirmation without Mobile Number*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)
            sp.click_signup_page()
            self.driver.maximize_window()
            #time.sleep(5)
            sp.set_first_name(first_name)
            sp.set_last_name(last_name)            
            sp.set_email(email)
            sp.set_password(password)
            sp.click_signup_resend()            
            sp.click_ok_msg()   
            if self.driver.current_url == "https://inuvest.tech/auth/signup" and sp.check_resend_confirm_visible()=="RESEND CONFIRMATION":
                sp.click_signup_resend()
                element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='swal2-title']")) 
                )
                confirm_msg=element.text
                if confirm_msg=="Confirmation email has been sent to your email address. Please confirm to continue.":  
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_resend_without_mobilenumber_scenario.png")
                    sp.click_ok_msg()
                    self.logger.info("*****************Proper message displayed and email sent as per requirement*************************************")
                    self.logger.info("*****************Resend Test with out Mobile Number is Passed*************************************")
                    self.driver.close()
                    assert True                   

                else:
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_resend_without_mobilenumber_scenario.png")
                    sp.click_ok_msg()
                    self.logger.error("*****************Resend Test with out Mobile Number is Failed*************************************")
                    self.logger.error("*****************Message not displayed per requirement*************************************")
                    self.driver.close()
                    assert  False
            else:
                    self.logger.error("*****************Resend Test with out Mobile Number is Failed*************************************")                    
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_resend_without_mobilenumber_scenario.png")
                    self.driver.close()
                    assert  False
            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False 

    #Test Case Id:TC_SIGNUP_006 - Validating Invalid Email Format
    def test_signup_invalidEmail_format(self,setup): 
        try:
            firstname="test"
            lastname="p"
            mobile="1233434339"
            email="test"          
            password="tessample"           
            self.logger.info("******************Test_001_Signup******************************************")
            self.logger.info("*****************Verifying Invalid Email format*************************************")
            self.driver=setup
            mand_validate= mandatoryValidation(self.driver)
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)            
            sp.click_signup_page()
            self.driver.maximize_window()
            sp.set_first_name(firstname)
            sp.set_last_name(lastname)
            sp.set_mobile(mobile)
            sp.set_email(email)
            sp.set_password(password)
            sp.click_signup_resend()         
            time.sleep(2)           
            
            if self.driver.current_url=="https://inuvest.tech/auth/signup":                
                if mand_validate.get_bordervalue(sp.textbox_email)==True and mand_validate.get_background_image(sp.textbox_email)==True:
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_signup_Email_invalid_format.png")
                    self.logger.info("****************Invalid Email format test is Passed*************************************")
                    self.logger.info("****************Email Textbox was higlighted in red and cross icon is displayed*************")
                    self.driver.close()
                    assert True
                else:
                    self.logger.error("*****************Invalid Email format test is Failed*************************************")
                    self.logger.error("****************Email Textbox may not higlighted in red or cross icon not displayed*************************************")
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_Email_invalid_format.png")
                    self.driver.close()
                    assert  False
            else:
                self.logger.error("*****************Invalid Email format test is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_Email_invalid_format.png")
                self.driver.close()
                assert  False
            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False  

    #Test Case Id:TC_SIGNUP_007 - Signup without FirstName
    def test_signup_NoFirstName(self,setup): 
        try:
            lastname="p"
            mobile="1233434339"
            email="testsample@intern.com"
            password="tessample"            
            self.logger.info("******************Test_001_SignUP******************************************")
            self.logger.info("*****************Verifying First Name mandatory test*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)  
            mand_validate= mandatoryValidation(self.driver)
            sp.click_signup_page()
            self.driver.maximize_window()            
            sp.set_last_name(lastname)
            sp.set_mobile(mobile)
            sp.set_email(email)
            sp.set_password(password)
            sp.click_signup_resend()         
            time.sleep(2)
            if self.driver.current_url == "https://inuvest.tech/auth/signup":
                #print(lp.get_bordervalue_txtemail())
                if mand_validate.get_bordervalue(sp.textbox_first_name)==True and mand_validate.get_background_image(sp.textbox_first_name)==True:
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_signup_firstname_mandatory.png")
                    self.logger.info("****************First Name mandatory test is Passed*************************************")
                    self.logger.info("****************First Name Textbox was higlighted in red and cross icon is displayed*************")
                    self.driver.close()
                    assert True
                else:
                    self.logger.error("*****************First Name mandatory test is Failed*************************************")
                    self.logger.error("****************First Name Textbox may not higlighted in red or cross icon not displayed*************************************")
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_firstname_mandatory.png")
                    self.driver.close()
                    assert  False
            else:
                self.logger.error("*****************First Name mandatory test is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_firstname_mandatory.png")
                self.driver.close()
                assert  False
            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False  

     #Test Case Id:TC_SIGNUP_008 - Signup without LastName
    def test_signup_NoLastName(self,setup): 
        try:            
            firstname="test"
            mobile="1233434339"
            email="testsample@intern.com"
            password="tessample"
            self.logger.info("******************Test_001_Signup******************************************")
            self.logger.info("*****************Verifying Last Name Mandatory*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)  
            mand_validate= mandatoryValidation(self.driver)
            sp.click_signup_page()
            self.driver.maximize_window()
            sp.set_first_name(firstname)            
            sp.set_mobile(mobile)
            sp.set_email(email)
            sp.set_password(password)
            sp.click_signup_resend()         
            time.sleep(2)
            if self.driver.current_url == "https://inuvest.tech/auth/signup":
                #print(lp.get_bordervalue_txtemail())
                if mand_validate.get_bordervalue(sp.textbox_last_name)==True and mand_validate.get_background_image(sp.textbox_last_name)==True:
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_signup_lastname_mandatory.png")
                    self.logger.info("****************Last Name mandatory test is Passed*************************************")
                    self.logger.info("****************Last Name Textbox was higlighted in red and cross icon is displayed*************")
                    self.driver.close()
                    assert True
                else:
                    self.logger.error("*****************Last Name mandatory test is Failed*************************************")
                    self.logger.error("****************Last Name Textbox may not higlighted in red or cross icon not displayed*************************************")
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_lastname_mandatory.png")
                    self.driver.close()
                    assert  False
            else:
                self.logger.error("*****************Last Name mandatory test is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_lastname_mandatory.png")
                self.driver.close()
                assert  False
            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False  

     #Test Case Id:TC_SIGNUP_009 - Signup without Email
    def test_signup_NoEmail(self,setup): 
        try:            
            firstname="test"
            lastname="p"
            mobile="1233434339"
            password="tessample"
            self.logger.info("******************Test_001_SignUp******************************************")
            self.logger.info("*****************Verifying Email Mandatory*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)  
            mand_validate= mandatoryValidation(self.driver)
            sp.click_signup_page()
            self.driver.maximize_window()
            sp.set_first_name(firstname)
            sp.set_last_name(lastname)
            sp.set_mobile(mobile)            
            sp.set_password(password)
            sp.click_signup_resend()        
            time.sleep(2)
            if self.driver.current_url == "https://inuvest.tech/auth/signup":
                #print(lp.get_bordervalue_txtemail())
                if mand_validate.get_bordervalue(sp.textbox_email)==True and mand_validate.get_background_image(sp.textbox_email)==True:
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_signup_Email_mandatory.png")
                    self.logger.info("****************Email mandatory test is Passed*************************************")
                    self.logger.info("****************Email Textbox was higlighted in red and cross icon is displayed*************")
                    self.driver.close()
                    assert True
                else:
                    self.logger.error("*****************Email mandatory test is Failed*************************************")
                    self.logger.error("****************Email Textbox may not higlighted in red or cross icon not displayed*************************************")
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_Email_mandatory.png")
                    self.driver.close()
                    assert  False
            else:
                self.logger.error("*****************Email mandatory test is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_Email_mandatory.png")
                self.driver.close()
                assert  False
            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False 
            
   #Test Case Id:TC_SIGNUP_010- Signup without Password
    def test_signup_NoPassword(self,setup): 
        try:
            firstname="test"
            lastname="p"
            mobile="1233434339"
            email="testsample@intern.com"            
            self.logger.info("******************Test_001_Signup******************************************")
            self.logger.info("*****************Verifying Password Mandatory*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)
            mand_validate= mandatoryValidation(self.driver)
            sp.click_signup_page()          
            self.driver.maximize_window()
            sp.set_first_name(firstname)
            sp.set_last_name(lastname)
            sp.set_mobile(mobile)
            sp.set_email(email)            
            sp.click_signup_resend()      
            time.sleep(2)
            if self.driver.current_url == "https://inuvest.tech/auth/signup":
                if mand_validate.get_bordervalue(sp.textbox_password)==True and mand_validate.get_background_image(sp.textbox_password)==True :
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_signup_Password_mandatory.png")
                    self.logger.info("****************Password mandatory test is Passed*************************************")
                    self.logger.info("****************Password Textbox was higlighted in red and cross icon is  displayed*************************************")
                    self.driver.close()
                    assert True
                else:
                    self.logger.error("*****************Password mandatory test is Failed*************************************")
                    self.logger.error("****************Password Textbox may not higlighted in red or cross icon not displayed*************************************")
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_Password_mandatory.png")
                    self.driver.close()
                    assert  False
            else:
                self.logger.error("*****************Password mandatory test is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_Password_mandatory.png")
                self.driver.close()
                assert  False
            
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False 
   
    #Test Case Id:TC_SIGNUP_011 - Validating terms and conditions link
    def test_signUp_terms_cond(self,setup): 
        try:
            self.logger.info("******************Test_001_SIGNUP******************************************")
            self.logger.info("*****************Verifying Terms and Conditions link*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)
            sp.click_signup_page()
            self.driver.maximize_window()            
            sp.click_terms_cond()    
            ids= self.driver.window_handles
            child_window_id=None
            if len(ids)==2:            
                child_window_id=ids[1]           
            if  child_window_id  is not None:
                self.driver.switch_to.window(child_window_id)
                if self.driver.current_url == "https://inuvest.tech/terms-and-conditions":
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_signup_terms_cond_scenario.png")
                    self.logger.info("***************** Terms and Conditions link work as per expectd*************************************")
                    self.driver.quit()
                    assert True
                else:
                    self.logger.info("*****************Terms and Conditions link is Failed*************************************")
                    self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_terms_cond_scenario.png")
                    self.driver.quit()
                    assert  False

            else:
                self.logger.error("*****************Terms and Conditions link is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_terms_cond_scenario.png")
                self.driver.quit()
                assert  False
            
        except Exception as ex:
            self.driver.quit()
            print(ex)
            assert  False

    #Test Case Id:TC_SIGNUP_012 - Check the login link is working
    def test_signUp_login_link(self,setup): 
        try:
            self.logger.info("******************Test_001_SIGNUP******************************************")
            self.logger.info("*****************Verifying login link*************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)
            sp.click_signup_page()
            self.driver.maximize_window()           
            sp.click_login()  
            if self.driver.current_url == "https://inuvest.tech/auth":
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_signup_login_link.png")
                self.logger.info("***************** Login link work as per expectd*************************************")
                self.driver.close()
                assert True
            else:                
                self.logger.info("*****************Login link is Failed*************************************")
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_login_link.png")
                self.driver.close()
                assert  False           
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False

    #Test Case Id:TC_SIGNUP_013 - Verifying By signing up, you agree to our label is present
    def test_signup_label(self,setup):
        try:
            self.logger.info("******************Test_001_SIGNUP******************************************")
            self.logger.info("*****************Verifying By signing up, you agree to our label present *************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)
            sp.click_signup_page()              
            
            if "By signing up, you agree to our" in sp.get_signup():
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_signup_label_link.png")
                self.logger.info("***************** By signing up, you agree to our label present as per expected*************************************")
                self.driver.close()
                assert True
            else:                
                self.logger.error("*****************By signing up, you agree to our label not present as per expected*************************************")
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_label_link.png")
                self.driver.close()
                assert  False           
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False

    #Test Case Id:TC_SIGNUP_014 - Verifying Already have a account? label is present
    def test_acc_label(self,setup):
        try:
            self.logger.info("******************Test_001_SIGNUP******************************************")
            self.logger.info("*****************Verifying Already have a account? label present *************************************")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30) 
            sp=SignUp(self.driver)
            sp.click_signup_page()                    
            
            if "Already have a account?" in sp.get_acc_signup():
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Pass_Test_Case\\" +"test_signup_alreadyacc_label_link.png")
                self.logger.info("***************** Already have a account? label present as per expected*************************************")
                self.driver.close()
                assert True
            else:                
                self.logger.error("*****************Already have a account? not present as per expected*************************************")
                self.driver.save_screenshot(".\\Screenshot\\SignUp\\Fail_Test_Case\\" +"test_signup_alreadyacc_label_link.png")
                self.driver.close()
                assert  False           
        except Exception as ex:
            self.driver.close()
            print(ex)
            assert  False