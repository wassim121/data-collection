from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium.webdriver.support.wait import WebDriverWait


class Commentaire:
    def __init__(self, date, nom_utilisateur, titre,texte, score):
        self.date = date
        self.titre = titre
        self.nom_utilisateur = nom_utilisateur
        self.texte = texte
        self.score = score

    def afficher_commentaire(self):
        print(f"Date: {self.date}, Nom d'utilisateur: {self.nom_utilisateur},titre: {self.titre}, Texte: {self.texte}, Score: {self.score}")


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
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://fr.indeed.com/?from=gnav-acme--acme-webapp")
time.sleep(2)

avis=find_element_xpath(driver, by=By.XPATH, value="/html/body/div[1]/header/nav/div/div/div[1]/div/div[2]/a")
avis.click()
time.sleep(2)
recherche=find_element_xpath(driver, by=By.XPATH, value="/html/body/div[2]/div/main/div/div[1]/form/div/div[1]/div/div/div/span/input")
recherche.send_keys("Symolia")#juste en peut modifier le nom de sociter puis le xpath
recherche.send_keys(Keys.RETURN)
time.sleep(2)
entreprise=find_element_xpath(driver, by=By.XPATH, value="/html/body/div[2]/div/main/div/div[2]/section/div[2]/div[1]/div/div[2]/div[1]/a")#juste en peut modifier le xpath
entreprise.click()
time.sleep(2)
avis_entreprise=find_element_xpath(driver, by=By.XPATH, value="/html/body/div[2]/div/div[1]/header/div[2]/div[3]/div/div/div/div[2]/nav/div/ul/li[3]/a")
avis_entreprise.click()
time.sleep(2)


titres = find_elements(driver, by=By.CLASS_NAME, value="css-1edqxdo.e1tiznh50")
score = find_elements(driver, by=By.CLASS_NAME, value="css-1qo6hjc.e37uo190")
date = find_elements(driver, by=By.CLASS_NAME, value="css-8a5o2x.e1wnkr790")
comment = find_elements(driver, by=By.CLASS_NAME, value="css-hxk5yu.eu4oa1w0")
employer = find_elements(driver, by=By.CLASS_NAME, value="css-8a5o2x.e1wnkr790")

print(len(titres))
print(len(score))
print(len(date))
print(len(comment))
print(len(employer))

all_comments = []

for i in range(0, len(titres)):
    date_1 = date[i].text.split('-')[-1].strip()

    commentaire = Commentaire(date_1, employer[i].text, titres[i].text, comment[i].text, score[i].text)
    all_comments.append(commentaire)

for c in all_comments:
    c.afficher_commentaire()



