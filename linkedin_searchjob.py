import requests
from bs4 import BeautifulSoup
import math




class Job:
    # Constructeur de la classe
    def __init__(self, date, nom_societe, titre_offre, type_contrat, localisation, maniere_travail, description):
        self.date = date
        self.nom_societe = nom_societe
        self.titre_offre = titre_offre
        self.type_contrat = type_contrat
        self.localisation = localisation
        self.maniere_travail = maniere_travail
        self.description = description

    # Méthode pour afficher les informations de l'offre d'emploi
    def display_info(self):
        print(f"Date: {self.date}, Société: {self.nom_societe}, Titre: {self.titre_offre}, "
              f"Contrat: {self.type_contrat}, Localisation: {self.localisation}, "
              f"Travail: {self.maniere_travail}, Description: {self.description}")






#it work*********************************
l = []
o = {}
liste_jobs = []

# Replace 'YOUR_LOCATION' with the desired location
location = 'Paris,fr,FR,France,Toulouse'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
target_url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python%20%28Programming%20Language%29&location={location}&geoId=100293800&currentJobId=3415227738&start={{}}'

# Iterate over pages
for i in range(0, math.ceil(125 / 25)):
    res = requests.get(target_url.format(i))
    soup = BeautifulSoup(res.text, 'html.parser')
    alljobs_on_this_page = soup.find_all("li")

    print(len(alljobs_on_this_page))

    # Iterate over jobs on the page
    for x in range(0, len(alljobs_on_this_page)):
        jobid = alljobs_on_this_page[x].find("div", {"class": "base-card"}).get('data-entity-urn').split(":")[3]
        l.append(jobid)

# Iterate over job details
all_titres=[]
target_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
for j in range(0, len(l)):
    resp = requests.get(target_url.format(l[j]))
    soup = BeautifulSoup(resp.text, 'html.parser')

    try:
        company = soup.find("div", {"class": "top-card-layout__card"}).find("a").find("img").get('alt')
    except:
        company = None

    try:
         job_title = soup.find("div", {"class": "top-card-layout__entity-info"}).find("a").text.strip()
         all_titres.append(job_title)
    except:
         job_title  = None

    try:
         level  = soup.find("ul", {"class": "description__job-criteria-list"}).find("li").text.replace(
            "Seniority level", "").strip()
    except:
         level  = None
    from datetime import datetime


    aujourdhui = datetime.now()

    job1 = Job(aujourdhui, company, job_title, "contra_vide", "Paris", "présentiel_vide",level)


    liste_jobs.append(job1)
    o = {}
for job in liste_jobs:
    job.display_info()

print(all_titres)


data = ["cloud","database", "sql", "data engineer", "data analyst"]
dev = ["web", "frontend", "backend", "full stack", "developer", "React", "Java", "Python", "JavaScript","software", "backend", "developer", "engineer", "developer"]
ia = ["ia","ai", "artificial intelligence", "machine learning", "deep learning", "data scientist"]
securite = ["security", "secure", "cybersecurity", "infosec", "penetration testing", "firewall", "encryption", "security analyst", "vulnerability", "security engineer"]


# Initialiser les listes de classification
offres_data = []
offres_dev = []
offres_ia = []
offres_securite = []

# Classifier les titres des offres
for titre in all_titres:
    titre_lower = titre.lower()

    if any(mot in titre_lower for mot in data):
        offres_data.append(titre)
    elif any(mot in titre_lower for mot in ia):
        offres_ia.append(titre)
    elif any(mot in titre_lower for mot in securite):
        offres_securite.append(titre)
    elif any(mot in titre_lower for mot in dev):
        offres_dev.append(titre)



# Afficher les résultats
print("totatle offre",str(len(all_titres)))
print("Offres dans la catégorie Data :", str(len(offres_data)))
print("Offres dans la catégorie Développement :", str(len(offres_dev)))
print("Offres dans la catégorie IA :", str(len(offres_ia)))
print("Offres dans la catégorie Sécurité :", str(len(offres_securite)))




# le nom de societer doit etre en miniscule et en chercher comment s apper dans le url de welcom to the jungle