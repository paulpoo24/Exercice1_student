% Ce script Matlab automatise la production de resultats
% lorsqu'on doit faire une serie de simulations en
% variant un des parametres d'entree.
% 
% Il utilise les arguments du programme (voir ConfigFile.h)
% pour remplacer la valeur d'un parametre du fichier d'input
% par la valeur scannee.
%

%% Parametres %%
%%%%%%%%%%%%%%%%

repertoire = '/Users/arnaud/Desktop/EPFL/Physnum/Exercice1_student'; % Chemin d'acces au code compile (NB: enlever le ./ sous Windows)
executable = 'exo'; % Nom de l'executable (NB: ajouter .exe sous Windows)
input = 'configuration.in.example'; % Nom du fichier d'entree de base MODIFIER SELON VOS BESOINS

nsimul = 3; % Nombre de simulations a faire

nsteps = round(logspace(2,4,nsimul)); % Nombre d'iterations entier de 10^2 a 10^4  MODIFIER SELON VOS BESOINS

paramstr = 'nsteps'; % Nom du parametre a scanner  MODIFIER SELON VOS BESOINS
param = nsteps; % Valeurs du parametre a scanner  MODIFIER SELON VOS BESOINS

%% Simulations %% 
%%%%%%%%%%%%%%%%%
% Lance une serie de simulations (= executions du code C++)
% Normalement, on ne devrait pas avoir besoin de modifier cette partie

output = cell(1, nsimul); % Tableau de cellules contenant les noms des fichiers de sortie
for i = 1:nsimul
    output{i} = [paramstr, '=', num2str(param(i)), '.out'];
    % Execution du programme en lui envoyant la valeur a scanner en argument
    cmd = sprintf('%s%s %s %s=%.15g output=%s', repertoire, executable, input, paramstr, param(i), output{i});
    disp(cmd)
    system(cmd);
end

%% Analyse %%
%%%%%%%%%%%%%
% Ici, on aimerait faire une etude de convergence: erreur fonction de dt, sur diagramme log-log.
% A MODIFIER ET COMPLETER SELON VOS BESOINS

error = zeros(1,nsimul);
for i = 1:nsimul % Parcours des resultats de toutes les simulations
    data = load(output{i}); % Chargement du fichier de sortie de la i-ieme simulation
    dt(i) = data(2,1)-data(1,1); % Delta t = t_2-t_1
    xend = data(end,2); % Extraire le x final
    zend = data(end,3); % Extraire le z final
    x_th = 0.0; % TODO: Entrer la vraie solution analytique a tfin
    z_th = 0.0; % TODO: Entrer la vraie solution analytique a tfin
    error(i) = sqrt((xend-x_th)^2+(zend-z_th)^2); % erreur sur la position finale
end

figure
loglog(dt, error, 'k+')
xlabel('\Delta t')
ylabel('Maximum de l''erreur sur la position')
grid on



