import matplotlib.pyplot as plt
import numpy as np

# =========================
# Données
# =========================

voitures = [
46.94,44.45,43.40,43.18,43.35,41.88,42.17,45.10,50.89,57.62,60.81,62.00,
62.79,64.27,65.42,66.41,66.65,66.74,66.71,66.58,66.31,65.70,63.25,56.46,
48.99,44.85,44.59,44.93,44.56,43.37,44.44,45.81,50.19,56.66,58.91,59.05,
60.10,61.87,64.00,64.90,65.30,65.41,65.41,65.57,65.48,64.72,61.68,54.25,
44.92,41.19,39.58,39.24,39.32,38.48,39.91,43.18,49.51,56.19,59.41,59.76,
60.56,62.78,64.39,65.79,66.35,66.33,66.47,66.69,66.63,66.34,63.91,57.23,
50.65,47.49,46.77,46.48,46.35,45.58,46.47,49.47,53.87,59.75,61.00,60.29,
60.27,61.48,63.99,65.64,66.72,66.77,66.95,67.16,67.22,67.11,66.71,64.81,
61.86,58.58,56.49,54.99,53.87,52.45,51.72,51.82,52.11,53.23,54.91,54.88,
57.10,59.10,62.15,64.16,65.91,66.14,66.49,66.69,66.63,66.38,65.75,64.46,
63.70,63.66,63.12,63.38,64.58,65.11,64.86,64.19,63.70,64.56,64.65,65.59,
66.01,67.05,67.69,68.00,68.09,68.04,68.10,68.12,67.59,66.91,64.30,56.73,
49.44
]

velos = [
61.66,61.32,61.25,61.69,62.01,62.25,61.55,60.24,60.57,60.33,59.59,59.29,
59.47,59.50,59.26,59.54,59.25,59.26,59.10,59.43,58.99,59.10,59.65,60.00,
60.57,60.43,60.46,60.99,61.04,60.35,61.67,59.99,61.21,61.11,60.47,60.47,
60.51,60.18,59.94,59.81,59.67,59.35,59.72,59.94,59.72,60.16,60.89,61.22,
61.87,60.49,61.56,61.52,61.62,62.22,63.35,62.75,62.32,61.36,61.85,60.58,
60.36,59.75,59.38,59.93,59.24,58.27,59.32,59.69,59.37,59.36,59.36,60.32,
60.74,60.95,61.14,61.20,61.42,61.20,60.19,59.57,58.97,58.53,58.72,58.68,
58.14,58.25,58.10,58.10,58.65,58.28,58.12,57.88,58.10,57.73,57.87,57.94,
58.39,58.83,59.10,58.36,59.24,60.57,60.55,60.19,59.52,59.00,60.26,59.70,
58.88,59.34,58.95,59.04,59.96,60.36,58.14,58.17,57.52,57.77,57.71,57.62,
57.76,60.37,60.86,60.61,62.02,62.32,62.74,63.11,61.69,61.31,60.46,59.30,
58.66,59.03,58.92,59.58,59.14,59.69,59.34,59.34,59.34,59.34,59.56,62.04,
61.25
]

# =========================
# Statistiques
# =========================

voitures_np = np.array(voitures)
velos_np = np.array(velos)

print("=== Voitures ===")
print(f"Moyenne : {np.mean(voitures_np):.2f} %")
print(f"Écart-type : {np.std(voitures_np):.2f}")
print(f"Min : {np.min(voitures_np):.2f} %")
print(f"Max : {np.max(voitures_np):.2f} %")

print("\n=== Vélos ===")
print(f"Moyenne : {np.mean(velos_np):.2f} %")
print(f"Écart-type : {np.std(velos_np):.2f}")
print(f"Min : {np.min(velos_np):.2f} %")
print(f"Max : {np.max(velos_np):.2f} %")

# Corrélation voiture / vélo
corr = np.corrcoef(voitures_np[:len(velos_np)], velos_np)[0, 1]
print(f"\nCorrélation voitures / vélos : {corr:.2f}")

# =========================
# Graphique avec jours
# =========================

heures_par_jour = 24
nb_jours = len(voitures) // heures_par_jour

positions_jours = [i * heures_par_jour for i in range(nb_jours)]
labels_jours = [f"Jour {i+1}" for i in range(nb_jours)]

plt.figure(figsize=(15, 6))

plt.plot(voitures, linestyle='--', marker='o', label="Voitures")
plt.plot(velos, linestyle='-', marker='x', label="Vélos")

# Moyennes
plt.axhline(np.mean(voitures_np), linestyle=':', linewidth=2, label="Moyenne voitures")
plt.axhline(np.mean(velos_np), linestyle='--', linewidth=2, label="Moyenne vélos")

# Séparateurs de jours
for pos in positions_jours:
    plt.axvline(pos, linestyle=':', alpha=0.2)

plt.xticks(positions_jours, labels_jours, rotation=45)
plt.title("Occupation des parkings voiture et vélo par jour")
plt.xlabel("Jour")
plt.ylabel("Taux d'occupation (%)")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

