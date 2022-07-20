from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import json
import time
from scrapy import Selector

PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://realpython.github.io/fake-jobs/")
response=Selector(text=driver.page_source)
elem=response.xpath('//*[@id="ResultsContainer"]')
Data_liste=[]
for i in range(1,3):
    #try:
    #  job_title1 = WebDriverWait(driver, 5).until(
    #        EC.presence_of_element_located((By.XPATH, '//h2'))
    #   )
      #driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="ResultsContainer"]/div[i]/div/div/div[1]/div[2]/h2')).text
      job_title1=response.xpath('//div['+str(i)+']//h2/text()').get()
      name1=response.xpath ('//div['+str(i)+']//h3/text()').get()
      city1=response.xpath ('//div['+str(i)+']/div/div/div[2]/p[1]/text()').get().strip()
      Date1=response.xpath ('//div['+str(i)+']/div/div/div[2]/p[2]/time/text()').get()
      driver.find_element("xpath",'//div['+str(i)+']//a[2]').click()
      #description1 = WebDriverWait(driver, 5).until(
      #      EC.presence_of_element_located((By.XPATH, '//p[1]/text()'))
      # )
      #driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="ResultsContainer"]/div[2]'))
      #text_apply1=elem.find_element(By.LINK_TEXT, "Apply").click()
      dictionary ={
           'job_title':job_title1,
            'name' :name1,
            'city' :city1,
           'Date' :Date1,
       #    'description': description1
      }
      Data_liste.append(dictionary)
      time.sleep(3)
with open("DC.json", "w") as outfile:
    json.dump(Data_liste, outfile)
#      Data_liste.append(job_title1)

#    finally:
    #driver.quit()
#print(job_title1)