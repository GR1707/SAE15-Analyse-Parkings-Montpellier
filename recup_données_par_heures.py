import requests, json, time

TAB=[]
def demande_data():

    response = requests.get("https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000") # 
    data = response.json() # Convert the response to JSON data
    response = requests.get("https://portail-api-data.montpellier3m.fr/bikestation?limit=1000")
    dataVelo = response.json()
    return data, dataVelo

#Pour les parkings voitures
def place_parking(data):

    with open('donnee.json', 'w') as file:  

        tab = []
        for i in range(len(data)):
            Nb_place = data[i]['availableSpotNumber']['value']
            Name = data[i]['name']['value'] 
            Nb_place_total = data[i]['totalSpotNumber']['value']
            pourcentage = Nb_place * 100 / Nb_place_total 
            pourcentage = round(pourcentage, 2)
            tab.append(pourcentage)
        TAB.append(tab)
        json.dump(TAB, file, indent=4)

#Pour les parkingsvélos
def place_parking2(dataVelo):

    with open('donnee.json', 'w') as file:  
        tab = []
        for i in range(len(dataVelo)):
            Nb_place = dataVelo[i]['freeSlotNumber']['value'] 
            Name = dataVelo[i]['address']['value']['streetAddress'] 
            Nb_place_total = dataVelo[i]['totalSlotNumber']['value']
            pourcentage = Nb_place * 100 / Nb_place_total 
            pourcentage = round(pourcentage, 2)
            tab.append(pourcentage)
        TAB.append(tab)
        json.dump(TAB, file, indent=4)

def boucle():


    global temps # Importe la variable temps de maniere global pour l'utiliser dans la fonction
    marche = True
    n = 0
    while marche : 
        data, dataVelo  = demande_data()
        place_parking(data)
        place_parking2(dataVelo)
        n += 1
        print(f"Données mises à jour {n} fois")
        time.sleep(temps) # attendre X secondes avant de refaire une demande
        
temps = int(input("Donnez l'intervalle de temps entre chaque mise à jour en secondes : "))   
print(" Cntrl + C pour arrêter le programme. \n")

boucle()
