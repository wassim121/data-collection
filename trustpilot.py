from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import re
from selenium.webdriver.support.wait import WebDriverWait
from langdetect import detect
from translate import Translator


class Commentaire:
    def __init__(self, date, nom_utilisateur, titre,texte, score):
        self.date = date
        self.titre = titre
        self.nom_utilisateur = nom_utilisateur
        self.texte = texte
        self.score = score

    def afficher_commentaire(self):
        print(f"Date: {self.date}, Nom d'utilisateur: {self.nom_utilisateur},titre: {self.titre}, Texte: {self.texte}, Score: {self.score}")




def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return None

def translate(text, target_language='en'):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation



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
driver.minimize_window()
driver.get("https://fr.trustpilot.com")#on peut changer selon le num de page
time.sleep(5)
cockies=find_element_xpath(driver, by=By.XPATH, value="/html/body/div[2]/div[2]/div/div[2]/button")
cockies.click()
recherche=find_element_xpath(driver, by=By.XPATH, value="/html/body/div[1]/div/div/main/div[2]/div/div[2]/div/div/div/form/div/input")
recherche.send_keys("service informatique")
time.sleep(2)
btn_recherche=find_element_xpath(driver, by=By.XPATH, value="/html/body/div[1]/div/div/main/div[2]/div/div[2]/div/div/div/form/div/button[1]")
btn_recherche.click()
time.sleep(2)

liens=find_elements_name(driver, by=By.NAME, value="business-unit-card")
x=len(liens)



all_comment=[]

for i  in range(0,x):
    time.sleep(2)
    lien= find_elements_name(driver, by=By.NAME, value="business-unit-card")[i]
    nom_societe=find_elements(driver, by=By.CLASS_NAME, value="styles_businessUnitMain__PuwB7")[1]
    try:
        p_element = nom_societe.find_element(By.TAG_NAME, 'p')
        if p_element:
            print("nom entreprise  :"+p_element.text)#nn entreprise
    except NoSuchElementException:
        print(" element found inside the div.")


    lien.click()
    time.sleep(10)
    avis=find_elements(driver, by=By.CLASS_NAME, value="styles_reviewContent__0Q2Tg")
    print(len(avis))
    if len(avis)>0:
        print("**************************************************************************************************************")
        for i in range(0,len(avis)):

            avis = find_elements(driver, by=By.CLASS_NAME, value="styles_reviewContent__0Q2Tg")[i]
            print()

            try:
                titre_xpath = "/html/body/div[1]/div/div/main/div/div[4]/section/div[{}]/article/div/section/div[2]/a/h2".format(
                    4 + i)
                titre = find_element_xpath(driver, by=By.XPATH, value=titre_xpath)
                titre_comment=titre.text
            except Exception as e:
                titre_comment="vide"
                print("Error fetching title ")

            try:
                text_xpath = "/html/body/div[1]/div/div/main/div/div[4]/section/div[{}]/article/div/section/div[2]/p[1]".format(
                    4 + i)
                text = find_element_xpath(driver, by=By.XPATH, value=text_xpath)
                text_comment= translate(text.text)

            except Exception as e:
                text_comment="vide"
                print(f"Error fetching text ")

            try:
                date_xpath = "/html/body/div[1]/div/div/main/div/div[4]/section/div[{}]/article/div/section/div[2]/p[2]".format(
                    4 + i)
                date = find_element_xpath(driver, by=By.XPATH, value=date_xpath)
                date_pattern = re.compile(r'\b\d{2} [a-zA-Z]+ \d{4}\b')

                # Find the date in the text using the pattern
                match = re.search(date_pattern, date.text)

                if match:
                    extracted_date = match.group()
                else:
                    extracted_date="vide"

            except Exception as e:
                extracted_date = "vide"

            commentaire = Commentaire(extracted_date, "user", titre_comment, text_comment, avis.text)
            commentaire.afficher_commentaire()
            all_comment.append(commentaire)

            print("////////////////////////")
            print("////////////////////////")





    time.sleep(2)
    driver.back()



time.sleep(40)

