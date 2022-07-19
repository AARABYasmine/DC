from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import json
import time

PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://realpython.github.io/fake-jobs/")
Data_liste=[]
elem=driver.find_elements(By.ID, "ResultsContainer")
for elems in elem:
    i = 1
    while i<=5:
    #try:
    #  job_title1 = WebDriverWait(driver, 5).until(
    #        EC.presence_of_element_located((By.XPATH, '//h2'))
    #   )
      #driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="ResultsContainer"]/div[i]/div/div/div[1]/div[2]/h2')).text
      job_title1=elems.find_element(By.XPATH, '//*[@id="ResultsContainer"]/div["+i+"]/div/div/div[1]/div[2]/h2').text
      name1=elems.find_element(By.XPATH, '//*[@id="ResultsContainer"]/div["i+1"]/div/div/div[1]/div[2]/h3').text
      city1=elems.find_element(By.XPATH, '//*[@id="ResultsContainer"]/div["i+1"]/div/div/div[2]/p[1]').text
      Date1=elems.find_element(By.XPATH, '//*[@id="ResultsContainer"]/div["i+1"]/div/div/div[2]/p[2]').text
      #driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="ResultsContainer"]/div[2]'))
      #text_apply1=elem.find_element(By.LINK_TEXT, "Apply").click()
      i=i+1
      dictionary ={
           'job_title':job_title1,
            'name' :name1,
            'city' :city1,
           'Date' :Date1
           #'text_apply': text_apply1
      }
      Data_liste.append(dictionary)
      with open("DC.json", "w") as outfile:
       json.dump(Data_liste, outfile)
#      Data_liste.append(job_title1)

#    finally:
    driver.quit()
#print(job_title1)