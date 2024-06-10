from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from time import sleep





# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Filters:


   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       # Explicit wait
       self.wait = WebDriverWait(self.driver, 10)


   def boot(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.wait = WebDriverWait(self.driver, 10)
       
   def Expandall(self):
       self.wait.until(ec.presence_of_element_located((By.XPATH, "//span[text()='Expand all']"))).click
       self.wait = WebDriverWait(self.driver, 10)
       
   def Name(self,Name):
       #self.wait.until(ec.presence_of_element_located((By.XPATH, "//input[@id='text-input__3']"))).send_keys("Tharani")
       fullXPath = "//div[text()='Name']"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Name)
       self.wait = WebDriverWait(self.driver, 10)
       
       
   def Birthdate(self,Birthdate):
       fullXPath = "//div[text()='Birth date']"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Birthdate)
       self.wait = WebDriverWait(self.driver, 10)
       
   def Birthday(self,Birthday):
       fullXPath = "//div[text()='Birthday']"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Birthday)
       self.wait = WebDriverWait(self.driver, 10)
       
   def Awardsrecognition(self,Awardsrecognition):
       fullXPath = "//div[text()='Awards & recognition']"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Awardsrecognition)
       self.wait = WebDriverWait(self.driver, 10)
       
   def Pagetopics(self,Pagetopics):
       fullXPath = "//div[text()='Page topics']"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Pagetopics)
       self.wait = WebDriverWait(self.driver, 10)
       
   def Deathdate(self,Deathdate):
       fullXPath = "//div[text()='Death date']"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Deathdate)
       self.wait = WebDriverWait(self.driver, 10)
       
       
   def Genderidentity(self,Genderidentity):
       fullXPath = "//div[text()='Gender identity']"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Genderidentity)
       self.wait = WebDriverWait(self.driver, 10)
       
       
   def Credits(self,Credits):
       fullXPath = "//div[text()='Credits']"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Credits)
       self.wait = WebDriverWait(self.driver, 10)
       
       
   def Adultnames(self,Adultnames):
       fullXPath = "//div[text()='Adult names']"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Adultnames)
       self.wait = WebDriverWait(self.driver, 10)
       
       
   def Searchfilters(self,Searchfilters):
       fullXPath = "//div[text()='Search filters']"
       element = self.driver.find_element(by=By.XPATH, value=fullXPath)
       element.send_keys(Searchfilters)
       self.wait = WebDriverWait(self.driver, 10)
       
    
obj = Filters("https://www.imdb.com/search/name//")
obj.boot()
#obj.Expandall()
obj.Name("Tharani")
obj.Birthdate("05-05-1990")
obj.Birthday("10-10")
obj.Awardsrecognition("Best Acterss-Nominated")
obj.Pagetopics("Biography")
obj.Deathdate("10-10-2090")
obj.Genderidentity("Male")
obj.Credits("100")
obj.Adultnames("Include")
obj.Searchfilters()
