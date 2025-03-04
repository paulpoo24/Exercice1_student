fname1= 'nsteps=4000alpha=05.out' % put your own file name
fname2= 'nsteps=4000alpha=1.out' % put your own file name
fname3= 'nsteps=4000alpha=0.out' % put your own file name

% (un)comment the lines coresponding to the (desired)undesired analysed cases

data=load(fname1);
t1 = data(:,3);
y1 = data(:,4);
data=load(fname2);
t2 = data(:,3);
y2 = data(:,4);
data=load(fname3);
t3 = data(:,3);
y3 = data(:,4);
%data=load(fname4);
%t4 = data(:,1);
%y4 = data(:,2);

lw=1.5; fs=16;
%figure(1) % goes to figure(1) or opens new figure(1) if it does not exist
figure % opens a new figure 
plot(t1,y1,'-ok', 'linewidth',lw);
% with '-or' you get a line with small circles in red colour
% type 'help plot' from the Matlab command line to see all possible options 
hold on; % subsequent calls to plot will add to the existing figure
plot(t2, y2, '-+r', 'linewidth',lw);
plot(t3, y3, '-db', 'linewidth',lw);
%plot(t4, y4, '-sm', 'linewidth',lw);

set(gca,'fontsize',fs) % useful to have large enough fonts when printing
  %  axis([0 200 0 120])   % select (zoom) axis([xmin xmax ymin ymax]);
title('Ex.1 Voiture folle - Euler');
%axis square;
grid('on'); % type grid off to remove the dotted grid lines
xlabel('temps t [s]');
ylabel('vitesse v [m/s]')

% export the eps file
print -f1 -r600 -depsc output_file_name.eps % (un)comment if needed
% the -f1 option means "figure 1"
% the -r600 option means 600 dpi resolution

% or the jpg
%print -f1 -r100 -djpeg output_file_name.jpg % (un)comment if needed

% or the png
%print -f1  -dpng output_file_name.png % (un)comment if needed
