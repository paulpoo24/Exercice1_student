import numpy as np
import subprocess
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pdb
import os

# Parameters
# TODO adapt to what you need (folder path executable input filename)
executable = './exo'  # Name of the executable (NB: .exe extension is required on Windows)
repertoire = r"/Users/arnaud/Desktop/EPFL/Physnum/Exercice1_student"
os.chdir(repertoire)

input_filename = 'configuration.in.example'  # Name of the input file


nsteps = np.array([40000]) # TODO change ok
nsimul = len(nsteps)  # Number of simulations to perform

tfin = 259200  # TODO: Verify that the value of tfin is EXACTLY the same as in the input file ok

dt = tfin / nsteps

paramstr = 'nsteps'  # Parameter name to scan
param = nsteps  # Parameter values to scan

# Simulations
outputs = []  # List to store output file names
convergence_list = []
for i in range(nsimul):
    output_file = f"{paramstr}={param[i]}.out"
    outputs.append(output_file)
    cmd = f"{repertoire}{executable} {input_filename} {paramstr}={param[i]:.15g} output={output_file}"
    cmd = f"{executable} {input_filename} {paramstr}={param[i]:.15g} output={output_file}"
    print(cmd)
    subprocess.run(cmd, shell=True)
    print('Done.')

error = np.zeros(nsimul)

fig, ax = plt.subplots(constrained_layout=True)
for i in range(nsimul):  # Iterate through the results of all simulations
    data = np.loadtxt(outputs[i])  # Load the output file of the i-th simulation
    t = data[:, 0]

    vx = data[-1, 1]  # final position, velocity, energy
    vy = data[-1, 2]
    xx = data[-1, 3]
    yy = data[-1, 4]
    En = data[-1, 5]
    convergence_list.append(yy)
    E = data[:, 5]
    # TODO compute the error for each simulation
    error[i] = np.max(E) - np.min(E)

    lw = 1.5
    fs = 16


# Chargement des données
x = data[:, 3]
y = data[:, 4]
E = data[:, 5]
d = np.sqrt(x**2 + y**2)

# Calcul de xl et dist_s_l
xl = 385000000 * 5.972e24 / (5.972e24 + 7.348e22)
dist_s_l = np.sqrt((xl - np.array(x))**2 + np.array(y)**2)

# Création de la figure et des axes
fig, ax = plt.subplots()

# Tracé de la trajectoire
ax.plot(x, y)

# Ajout du cercle de centre (xl, 0) et de rayon 1737100
rayon = 1737100
cercle = patches.Circle((xl, 0), rayon, color='k', fill=False, linestyle='-')
ax.add_patch(cercle)

# Détection du premier point d'intersection
first_intersection = None

for i in range(len(dist_s_l) - 1):
    # Vérifie si un point est exactement sur le cercle
    if dist_s_l[i] == rayon:
        first_intersection = (x[i], y[i])
        break
    # Vérifie si la trajectoire traverse le cercle entre deux points
    elif (dist_s_l[i] < rayon and dist_s_l[i+1] > rayon) or (dist_s_l[i] > rayon and dist_s_l[i+1] < rayon):
        # Interpolation linéaire pour estimer le point exact
        alpha = (rayon - dist_s_l[i]) / (dist_s_l[i+1] - dist_s_l[i])
        x_inter = x[i] + alpha * (x[i+1] - x[i])
        y_inter = y[i] + alpha * (y[i+1] - y[i])
        first_intersection = (x_inter, y_inter)
        break  # On arrête dès qu'on a trouvé le premier point

# Si un point d'intersection est trouvé, l'afficher
if first_intersection:
    xi, yi = first_intersection
    ax.scatter(xi, yi, color='red', zorder=3, marker=".", s=100)
    # Texte formaté avec boîte et couleurs
    textstr = f"X  {xi:,.0f}\nY  {yi:,.0f}"
    
    # Ajout d'une annotation avec une boîte de fond
    ax.annotate(textstr, (xi, yi),
                xytext=(xi + 2e6, yi - 1e6),  # Décalage du texte
                fontsize=12, color="red",
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))

# Configuration des axes et de la légende
ax.set_xlabel('x [m]', fontsize=fs)
ax.set_ylabel('y [m]', fontsize=fs)
ax.set_aspect('equal', adjustable='datalim')  # Pour que le cercle soit bien proportionné
ax.legend()

# Affichage
plt.show()


# uncomment the following if you want debug
#import pdb
#pbd.set_trace()
plt.figure()
plt.loglog(nsteps, error, 'g+-', linewidth=lw)
plt.xlabel('$N_s$', fontsize=fs)
plt.ylabel('$errE_{mec}$ [J]', fontsize=fs)
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.grid(True)
plt.ylim(1e0, 1e8)  # Définit les limites de l'axe des ordonnées de 10^0 à 10^8

"""
Si on n'a pas la solution analytique: on représente la quantite voulue
(ci-dessous v_y, modifier selon vos besoins)
en fonction de (Delta t)^norder, ou norder est un entier.
"""
norder = 1  # Modify if needed

plt.figure()
plt.plot(dt**norder, convergence_list, 'b+-', linewidth=lw)
plt.xlabel('\Delta t [s]', fontsize=fs)
plt.ylabel('v_y [m/s]', fontsize=fs)
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.grid(True)

plt.show()
