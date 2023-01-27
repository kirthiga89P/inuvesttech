from selenium import webdriver
from selenium.webdriver.common.by import By
class mandatoryValidation:
    exp_cross_icon="data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23dc3545' viewBox='-2 -2 7 7'%3E%3Cpath stroke='%23dc3545' d='M0 0l3 3m0-3L0 3'/%3E%3Ccircle r='.5'/%3E%3Ccircle cx='3' r='.5'/%3E%3Ccircle cy='3' r='.5'/%3E%3Ccircle cx='3' cy='3' r='.5'/%3E%3C/svg%3E" 
    exp_bordervalue_mandatory="rgb(244, 67, 54)"
    def __init__(self,driver):
        self.driver=driver
    def get_bordervalue(self,element):
        actualbordervalue= self.driver.find_element(By.XPATH,element).value_of_css_property("border-color")  
        
        if actualbordervalue==self.exp_bordervalue_mandatory:
            return True
        else:
            return False    
    def get_background_image(self,element):
        cross_icon= self.driver.find_element(By.XPATH,element).value_of_css_property("background-image")
        
        if self.exp_cross_icon in cross_icon:
            return True
        else:
            return False
       




