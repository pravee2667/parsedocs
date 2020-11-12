# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from bin import loader
import logging

def skills_linkdn(url):
    options = Options()
    conf=loader.load_conf()
    options.add_argument("--headless")
    driver=webdriver.Chrome(conf['webdriver_dir'],chrome_options=options)
    
    driver.get(url)
    #linkedin.com/in/avisek-sukul
    #'https://www.linkedin.com/in/praveensk-kumarsk227'
    
    sleep(6)
    xpat=driver.find_element_by_link_text("Sign in")
    
    xpat.click()
    
    sleep(6)
    
    uname=driver.find_element_by_name("session_key")
    uname.send_keys(conf['uname'])
    sleep(1)
    pwd=driver.find_element_by_name("session_password")
    pwd.send_keys(conf['pwd'])
    sleep(1)
    print("yes")
    try:
        sign_in=driver.find_element_by_xpath('//input[@id="login-submit"]')
        sign_in.click()
    except Exception as ex:
        logging.warn("Submit button does not exist")
        sign_in=driver.find_element_by_xpath('//button[contains(text(),"Sign in")]')
        sign_in.click()
    sleep(6)
    driver.maximize_window()
    sleep(2)
    driver.execute_script("window.scrollTo(0, 1780);")
    sleep(2)
    try:
        showmore=driver.find_element_by_xpath('//section[contains(@class,"pv-profile-section pv-skill-categories-section")]/div[2]/button')
        showmore.click()
    except Exception as ex:
        showmore=driver.find_element_by_xpath('//button[@class="pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--fluid "]')
        showmore.click()
    
    sleep(2)
    
    tabl=driver.find_element_by_xpath('//div[@id="skill-categories-expanded"]/div[2]/ol')
    
    rows=tabl.find_elements_by_xpath('.//li')
    skills=[]
    for row in rows:
        try:
            txtt=row.find_element_by_xpath('div/div/p/span')
            skills.append(txtt.text)
        except Exception as ex:
            txtt=row.find_element_by_xpath('div/div/p/a/span')
            skills.append(txtt.text)
            
    print(skills)
    driver.close()
    return skills
    
    

#options = Options()
#options.add_argument("--headless")
#driver=webdriver.Chrome('C://Users//P0142221//Downloads//chromedriver_win32//chromedriver.exe')
#
#driver.get('https://www.linkedin.com/in/praveensk-kumarsk227')
##linkedin.com/in/avisek-sukul
##'https://www.linkedin.com/in/praveensk-kumarsk227'
#
#sleep(10)
#xpat=driver.find_element_by_link_text("Sign in")
#
#xpat.click()
#
#sleep(10)
#
#uname=driver.find_element_by_name("session_key")
#uname.send_keys('praveen159sk@gmail.com')
#sleep(1)
#pwd=driver.find_element_by_name("session_password")
#pwd.send_keys('Websites@27')
#sleep(1)
#print("yes")
#try:
#    sign_in=driver.find_element_by_xpath('//input[@id="login-submit"]')
#    sign_in.click()
#except Exception as ex:
#    print(ex)
#    
#    
#sleep(8)
#driver.maximize_window()
#sleep(2)
#driver.execute_script("window.scrollTo(0, 1780);")
##showmore=driver.find_element_by_xpath('//div[@class="profile-detail"]')
##sso=showmore.find_element_by_xpath('.//div[7]/div')
##sso1=sso.find_element_by_xpath('//section/div[2]/button')
##sso2=sso1.find_element_by_xpath('.//button')
##sso1.click()
##//div[@class="profile-detail"]/div[7]/div/section/div[2]/button
#sleep(2)
##showmore=driver.find_element_by_xpath('//section[@class="pv-profile-section pv-skill-categories-section artdeco-container-card artdeco-card ember-view"]/div[2]/button')
#
#showmore=driver.find_element_by_xpath('//section[contains(@class,"pv-profile-section pv-skill-categories-section")]/div[2]/button')
#showmore.click()
#
#sleep(2)
#
#tabl=driver.find_element_by_xpath('//div[@id="skill-categories-expanded"]/div[2]/ol')
#
#rows=tabl.find_elements_by_xpath('.//li')
#
#for row in rows:
#    try:
#        txtt=row.find_element_by_xpath('div/div/p/span')
#    except Exception as ex:
#        txtt=row.find_element_by_xpath('div/div/p/a/span')
#        
#    print(txtt.text)
#driver.close()
#    

#uname=driver.find_element_by_name("session_key")
#uname.send_keys('praveen159sk@gmail.com')
#sleep(1)
#pwd=driver.find_element_by_name("session_password")
#pwd.send_keys('Websites@27')
#
#sign_in=driver.find_element_by_class_name("sign-in-form__submit-button")
#sign_in.click()
#sleep(10)
#
#search=driver.find_element_by_class_name("search-global-typeahead__input always-show-placeholder")
#
#search.send_keys('Sunjit rana')
#
#driver.get('linkedin.com/in/avisek-sukul')

