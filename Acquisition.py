import requests
import time
import math

# ===== URL des API =====
URL_PARKINGS = "https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000"
URL_VELOS = "https://portail-api-data.montpellier3m.fr/bikestation?limit=1000"

# ===== Fonctions statistiques =====
def moyenne(liste):
    if len(liste) == 0:
        return 0
    return sum(liste) / len(liste)

def ecart_type(liste):
    if len(liste) == 0:
        return 0
    m = moyenne(liste)
    variance = sum((x - m) ** 2 for x in liste) / len(liste)
    return math.sqrt(variance)

# ===== Paramètres utilisateur =====
Te = int(input("Période d'échantillonnage Te (en secondes) : "))
duree = int(input("Durée de l'acquisition (en secondes) : "))
nom_fichier = input("Nom du fichier de sauvegarde : ")

nb_mesures = duree // Te

# ===== Listes pour analyses statistiques =====
taux_voitures = []
taux_velos = []

# ===== Acquisition =====
with open(nom_fichier, "w", encoding="utf-8") as fichier:
    fichier.write("timestamp;type;nom;disponible;total;taux_occupation\n")

    for i in range(nb_mesures):
        timestamp = int(time.time())

        # =====================================
        # PARKINGS VOITURES
        # =====================================
        response = requests.get(URL_PARKINGS)
        parkings = response.json()

        for parking in parkings:
            if parking["status"]["value"] == "Open":
                nom = parking["name"]["value"]
                libres = parking["availableSpotNumber"]["value"]
                total = parking["totalSpotNumber"]["value"]

                if total > 0:
                    taux_occupation = (total - libres) / total
                else:
                    taux_occupation = 0

                taux_voitures.append(taux_occupation)

                fichier.write(
                    f"{timestamp};PARKING;{nom};{libres};{total};{taux_occupation:.3f}\n"
                )

        # =====================================
        # STATIONS VELOS
        # =====================================
        response = requests.get(URL_VELOS)
        stations = response.json()

        for station in stations:
            if station["status"]["value"] == "working":
                nom = station["address"]["value"]["streetAddress"]
                velos = station["availableBikeNumber"]["value"]
                total = station["totalSlotNumber"]["value"]

                if total > 0:
                    taux_occupation = velos / total
                else:
                    taux_occupation = 0

                taux_velos.append(taux_occupation)

                fichier.write(
                    f"{timestamp};VELO;{nom};{velos};{total};{taux_occupation:.3f}\n"
                )

        fichier.flush()
        print(f"Mesure {i + 1}/{nb_mesures} enregistrée")
        time.sleep(Te)

print("Fin de l'acquisition.")

# ===== Calculs statistiques =====
moy_voitures = moyenne(taux_voitures)
std_voitures = ecart_type(taux_voitures)

moy_velos = moyenne(taux_velos)
std_velos = ecart_type(taux_velos)

# ===== Fichier de synthèse =====
nom_synthese = "synthese_" + nom_fichier

with open(nom_synthese, "w", encoding="utf-8") as f:
    f.write("=== SYNTHESE DES DONNEES SAE15 ===\n\n")

    f.write("PARKINGS VOITURES\n")
    f.write(f"Nombre de mesures : {len(taux_voitures)}\n")
    f.write(f"Moyenne taux occupation : {moy_voitures:.3f}\n")
    f.write(f"Ecart-type : {std_voitures:.3f}\n")
    f.write(f"Minimum : {min(taux_voitures):.3f}\n")
    f.write(f"Maximum : {max(taux_voitures):.3f}\n\n")

    f.write("STATIONS VELOS\n")
    f.write(f"Nombre de mesures : {len(taux_velos)}\n")
    f.write(f"Moyenne taux occupation : {moy_velos:.3f}\n")
    f.write(f"Ecart-type : {std_velos:.3f}\n")
    f.write(f"Minimum : {min(taux_velos):.3f}\n")
    f.write(f"Maximum : {max(taux_velos):.3f}\n")

print(f"Fichier de synthèse généré : {nom_synthese}")
