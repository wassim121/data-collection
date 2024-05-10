from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait







class Article:
    def __init__(self, titre, texte, nom_site):
        self.titre = titre
        self.texte = texte
        self.nom_site = nom_site

    def afficher_article(self):
        print(f"Titre: {self.titre}\nTexte: {self.texte}\nNom du site: {self.nom_site}")






def find_elements(driver, by=By.CLASS_NAME, value=None):
    return driver.find_elements(by, value)
def find_element(driver, by=By.CLASS_NAME, value=None):
    return driver.find_element(by, value)

def find_elements_id(driver, by=By.ID, value=None):
    return driver.find_elements(by, value)
def find_element_id(driver, by=By.ID, value=None):
    return driver.find_element(by, value)

def find_elements_name(driver, by=By.NAME, value=None):
    return driver.find_elements(by, value)
def find_element_name(driver, by=By.NAME, value=None):
    return driver.find_element(by, value)


def find_elements_xpath(driver, by=By.XPATH, value=None):
    return driver.find_elements(by, value)
def find_element_xpath(driver, by=By.XPATH, value=None):
    return driver.find_element(by, value)



def find_elements_LINK_TEXT(driver, by=By.LINK_TEXT, value=None):
    return driver.find_elements(by, value)
def find_element_LINK_TEXT(driver, by=By.LINK_TEXT, value=None):
    return driver.find_element(by, value)


def find_elements_LINK_TEXT_para(driver, by=By.PARTIAL_LINK_TEXT, value=None):
    return driver.find_elements(by, value)
def find_element_LINK_TEXT_para(driver, by=By.PARTIAL_LINK_TEXT, value=None):
    return driver.find_element(by, value)



print("work correctlly")


# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
driver.get("https://www.welcometothejungle.com/fr/articles")
driver.maximize_window()
driver.minimize_window()

time.sleep(2)

cockies=find_element_xpath(driver, by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/button[3]")
cockies.click()
time.sleep(2)
recherche=find_element_xpath(driver, by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[4]/div/form/input")
recherche.send_keys("web")
recherche.send_keys(Keys.RETURN)
time.sleep(3)
all_article=[]
for i in range(1,30):
    lien = find_element_xpath(driver, by=By.XPATH,value=f"/html/body/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div/ol/div[{i}]/li/article/div[2]/header/a")
    lien.click()
    time.sleep(1)
    titre=find_element_xpath(driver, by=By.XPATH,value="/html/body/div[1]/div[1]/div/div/div/div/main/div[1]/div/div[1]/header/h1")
    text=find_element_xpath(driver, by=By.XPATH,value="/html/body/div[1]/div[1]/div/div/div/div/main/div[1]/div/div[1]/div[4]/div")
    article=Article(titre.text,text.text,"welcom to the jungle")
    all_article.append(article)
    driver.back()
    time.sleep(2)

for a in all_article:
    a.afficher_article()










time.sleep(30)
