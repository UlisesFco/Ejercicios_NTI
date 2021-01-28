%escenario 1
clear all
clc
% pot = [-70 -79 -65 -76 -82 -69 -80];
% per = (1/1000).*[11 86 52 327 666 26 355];
% 
% scatter(pot,per,'*k','linewidth',2)
% title('PER vs Potencia (Escenario 1)')
% xlabel 'Potencia dBm'
% ylabel 'PER'

% pot = [-54 -74 -80 -82 -88];
% per = (1/1000).*[11 60 77 81 127];
% 
% scatter(pot,per,'*k','linewidth',2)
% title('PER vs Potencia (Escenario 2)')
% xlabel 'Potencia dBm'
% ylabel 'PER'

pot = [-40 -43 -49 -70 -64 -78 -77 -79 -84 -76 -80 -85 -90 ];
per = (1/1000).*[0 0 60 70 50 60 90 80 90 70 80 90 100];
dist = [0 10 20 30 40 50 60 70 80 90 100 110 120];

k = 20;
gamma = 3.2;

perdidas = k + 10*gamma*log10(dist);
prx = -perdidas;

scatter(dist,pot,'*k','linewidth',2)
hold on
plot(dist,prx)
title('PER vs Potencia')
xlabel 'Distancia m'
ylabel 'Potencia dbm'