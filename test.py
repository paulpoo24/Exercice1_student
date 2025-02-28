import numpy as np
import matplotlib.pyplot as plt

# Charger les fichiers de sortie
def load_data(filename):
    data = np.loadtxt(filename)
    return data[:, 3], data[:, 4]  # t, v, h

# Fichiers de sortie correspondant aux trois schémas et aux deux valeurs de n_steps
files_4000 = ["nsteps=4000alpha=1.out", "nsteps=4000alpha=0.out", "nsteps=4000alpha=05.out"]
files_40000 = ["nsteps=40000alpha=1.out", "nsteps=40000alpha=0.out", "nsteps=40000alpha=05.out"]

labels = ["Euler Explicite", "Euler Implicite", "Euler Semi-implicite"]
colors = ['b', 'r', 'g']

# Tracer les résultats pour n_steps = 4000
plt.figure(figsize=(10, 5))
for file, label, color in zip(files_4000, labels, colors):
    t, v = load_data(file)
    plt.plot(t, v, label=label, color=color)

plt.xlabel(" x [m]")
plt.ylabel("y [m]")
plt.title("Comparaison des schémas d'Euler (n=4000)")
plt.legend()
plt.grid()
plt.show()

# Tracer les résultats pour n_steps = 40000
plt.figure(figsize=(10, 5))
for file, label, color in zip(files_40000, labels, colors):
    t, v = load_data(file)
    plt.plot(t, v, label=label, color=color)

plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Comparaison des schémas d'Euler (n=40000)")
plt.legend()
plt.grid()
plt.show()