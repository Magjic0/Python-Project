from bs4 import BeautifulSoup

def extraire_indice(code_secret, fichier_html):
    with open(fichier_html, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    balise = soup.find("div", {"class": "indice-secrete", "data-code": code_secret})
    return balise.text.strip() if balise else "Aucun indice trouvé pour ce code."

if __name__ == "__main__":
    code = "SECRET51"
    chemin_html = "./scripts/scraping/indice_zone51.html"
    resultat = extraire_indice(code, chemin_html)
    print("Indice caché :", resultat)