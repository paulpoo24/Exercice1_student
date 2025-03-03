import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Charger les fichiers de sortie
def load_data(filename):
    data = np.loadtxt(filename)
    return data[:, 3], data[:, 4]  # x, y

# Fichiers pour différentes valeurs de n_steps
files_4000 = ["nsteps=4000alpha=1.out", "nsteps=4000alpha=0.out", "nsteps=4000alpha=05.out"]
files_40000 = ["nsteps=40000alpha=1.out", "nsteps=40000alpha=0.out", "nsteps=40000alpha=05.out"]

labels = ["Euler Explicite", "Euler Implicite", "Euler Semi-implicite"]
colors = ['b', 'r', 'g']

# Position du centre du cercle
xl = 385000000 * 5.972e24 / (5.972e24 + 7.348e22)  # Centre du cercle
rayon = 1737100  # Rayon du cercle

# Tracer les résultats pour n_steps = 4000
fig, ax = plt.subplots(figsize=(12, 8))

for file, label, color in zip(files_4000, labels, colors):
    x, y = load_data(file)
    ax.plot(x, y, label=label, color=color)

# Ajouter le cercle qui doit être bien circulaire
cercle = plt.Circle((xl, 0), rayon, color='black', fill=False, linestyle='solid', linewidth=2)
ax.add_patch(cercle)

ax.set_xlim(1e8, 15e8)  # Échelle correcte en x
ax.set_ylim(-2e8, 2e8)  # Échelle plus raisonnable en y
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_title("Comparaison des schémas d'Euler (n=4000)")
ax.legend()
ax.grid()
ax.set_aspect('equal')  # Garde un rapport 1:1 entre x et y
plt.show()

# Tracer les résultats pour n_steps = 40000
fig, ax = plt.subplots(figsize=(12, 8))

for file, label, color in zip(files_40000, labels, colors):
    x, y = load_data(file)
    ax.plot(x, y, label=label, color=color)

# Ajouter le cercle
cercle = plt.Circle((xl, 0), rayon, color='black', fill=False, linestyle='solid', linewidth=2)
ax.add_patch(cercle)

ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.legend()
ax.grid()
ax.set_aspect('equal')  # Assure que le cercle apparaît bien circulaire
plt.show()