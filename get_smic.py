import requests
from bs4 import BeautifulSoup

# URL de la page web
url = "https://www.service-public.fr/particuliers/vosdroits/F2300"

# Envoie une requête GET pour récupérer le contenu HTML de la page
try:
    # Envoie une requête GET pour récupérer le contenu HTML de la page
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("ERROR: Failed to get URL:", e)
    smic="ERROR, choose manually"
    # Gérer l'erreur ici, par exemple en affichant un message à l'utilisateur
    # ou en utilisant une valeur par défaut pour le SMIC
else:
    html_content = response.content

    # Crée un objet BeautifulSoup à partir du contenu HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Recherche le tableau contenant les montants du Smic
    table = soup.find_all('span', class_='sp-prix')

    try:
        smic_tmp=table[1].get_text().strip().replace(" ","").replace("€","").replace(",",".")   
    except IndexError:
        print("ERROR: Failed to get SMIC")
        smic="ERROR, choose manually"
    else: 

        smic = float(smic_tmp)

        if smic < 10 or smic > 20:
            smic="ERROR, choose manually"
