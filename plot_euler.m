% Affichage pour n_steps = 4000
figure;
plotOutput({'nsteps=4000alpha=05.out', 'nsteps=4000alpha=0.out', 'nsteps=4000alpha=1.out'}, ['b', 'r', 'g']);
title('Comparaison des 3 schémas - n = 4000');

% Affichage pour n_steps = 40000
figure;
plotOutput({'nsteps=40000alpha=05.out', 'nsteps=40000alpha=0.out', 'nsteps=40000alpha=1.out'}, ['b', 'r', 'g']);
title('Comparaison des 3 schémas - n = 40000');