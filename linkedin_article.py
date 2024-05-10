from bs4 import BeautifulSoup
import requests

url = 'https://www.linkedin.com/pulse/topics/ad-tech-s41292/'#on va presiser la liste des topics par theme




class Article:
    def __init__(self, titre, texte, nom_site):
        self.titre = titre
        self.texte = texte
        self.nom_site = nom_site

    def afficher_article(self):
        print(f"Titre: {self.titre}\nTexte: {self.texte}\nNom du site: {self.nom_site}")





page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

article_titre = soup.find_all("h2",class_="mb-1 overflow-hidden break-words font-sans text-lg font-[500] babybear:text-md")
article_body = soup.find_all("p",class_="content-description mt-0.5 break-words font-sans text-sm font-normal babybear:text-xs")
article_lien = soup.find_all("a",class_="content-hub-entities !no-underline")
print(len(article_titre))
print(len(article_body))
print(len(article_lien))

liste_article=[]
n=0
i=0
for element in article_lien:

    print(i)
    titre_content = article_titre[i].get_text(strip=True)
    i=i+1


    hrefi = element.get('href')

    page = requests.get(hrefi)
    soup = BeautifulSoup(page.content, 'html.parser')
    body=soup.find_all("div",class_="article-main__content")
    for e in body:
        tbody1 = e.get_text(strip=True)

    body2 = soup.find_all("div", class_="contribution__text-wrapper relative")
    for e in body2:
        tbody2 = e.get_text(strip=True)

    texttt = tbody1 + tbody2
    article = Article(titre_content, texttt, "linkedin")
    liste_article.append(article)

for article in liste_article:
    article.afficher_article()
