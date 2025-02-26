function plotOutput(files,colors)
% plotOutput(files,colors) PLOTS FIGURES OF exo 1
%
% files est un tableau de cellule avec {}: files={'output1.dat'}
%
% colors est un tableau de couleur: colors=['b','r']
%
% EXEMPLES : >>plotOutput({'output.dat'},['b']);
%            >>plotOutput({'output_1.dat','output_2.dat'},['b','c']);

if(exist('files')~=1)
  files={'output.dat'};
end
N=size(files,2);
if(exist('colors')~=1 || size(colors,2)<N)
  colors=[];
  for icolor=1:N
    colors=[colors 'b'];
  end
end

fontSize=16;
lineWidth=2;

target=100.0;

figure
set(gca,'FontSize',fontSize);
xlabel('t[s]');
ylabel('v[m/s]');
hold on
for iFile=1:N
  data=load(files{iFile});
  color=colors(iFile);
  t = data(:,1);
  index=findPosition(target,t);
  v = data(:,2);
  fprintf('file=%s target=%f index=%d time=%f velocity=%f\n',files{iFile},target,index,t(index),v(index));
  plot(t,v,'Color',color,'LineWidth',lineWidth);
end

figure
set(gca,'FontSize',fontSize);
xlabel('t[s]');
ylabel('h[m]');
hold on
for iFile=1:N
  data=load(files{iFile});
  color=colors(iFile);
  t = data(:,1);
  h = data(:,3);
  plot(t,h,'Color',color,'LineWidth',lineWidth);
end

figure
set(gca,'FontSize',fontSize);
xlabel('h[m]');
ylabel('v[m/s]');
hold on
for iFile=1:N
  data=load(files{iFile});
  color=colors(iFile);
  v = data(:,2);
  h = data(:,3);
  plot(h,v,'Color',color,'LineWidth',lineWidth);
end

function index=findPosition(target,table)
  index=1;
  spread=abs(table(index)-target);
  for jindex=index:size(table,1)
    tmp=abs(target-table(jindex));
    if(tmp<spread)
      spread=tmp;
      index=jindex;
    end
  end
