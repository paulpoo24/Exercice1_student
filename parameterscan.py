import numpy as np
import subprocess
import matplotlib.pyplot as plt
import pdb
import os

# Parameters
# TODO adapt to what you need (folder path executable input filename)
executable = './exo'  # Name of the executable (NB: .exe extension is required on Windows)
repertoire = r"/Users/arnaud/Desktop/EPFL/Physnum/Exercice1_student"
os.chdir(repertoire)

input_filename = 'configuration.in.example'  # Name of the input file


nsteps = np.array([2000,4000,8000,12000,16000,20000,30000,40000,50000,100000]) # TODO change ok
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
    # TODO compute the error for each simulation
    error[i] =  0 

    lw = 1.5
    fs = 16
    
    x = data[:, 3]
    y = data[:, 4]
    E = data[:, 5]
    d = np.sqrt(x**2 + y**2)
    

    ax.plot(t, E)
    ax.set_xlabel('t [s]', fontsize=fs)
    ax.set_ylabel('Emec [J]', fontsize=fs)



# uncomment the following if you want debug
#import pdb
#pbd.set_trace()
plt.figure()
plt.plot(1/(np.array(nsteps)), convergence_list, 'r+-', linewidth=lw)
plt.xlabel('$1/N_s$', fontsize=fs)
plt.ticklabel_format(style='sci', axis='x', scilimits=(-4,-4))
plt.ylabel('$y_{end}$ [m]', fontsize=fs)
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.grid(True)

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
