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

import time
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.lemondeinformatique.fr")
time.sleep(2)
cockies = find_element_xpath(driver, by=By.XPATH,value="/html/body/div[1]/div/div/div/div/div/div[3]/button[2]")
cockies.click()
input=find_element_xpath(driver, by=By.XPATH, value="/html/body/header/div[1]/div[3]/form/div/input")
input.send_keys("dev")
input.send_keys(Keys.RETURN)
time.sleep(2)
wait = WebDriverWait(driver, 10)
for i in range(2, 10):
    try:
        print("//////////////////////////////////////////////////")
        element_xpath = f"//article[{i}]/div/div[1]"
        liens = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        liens.click()
        time.sleep(2)
        titre_xpath = "//article/div/div/div[1]/div[2]/p[1]"
        text_xpath = "//article/div/div/div[1]/div[2]/div[1]"
        titre = wait.until(EC.visibility_of_element_located((By.XPATH, titre_xpath)))
        text = wait.until(EC.visibility_of_element_located((By.XPATH, text_xpath)))
        print(titre.text)
        print(text.text)
        driver.back()
    except Exception as e:
        print(f"Erreur: {e}")
        driver.back()