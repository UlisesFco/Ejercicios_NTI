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

pot = [-62 -66 -59  -70 -62];
per = (1/1000).*[4 14 62 91 18];

scatter(pot,per,'*k','linewidth',2)
title('PER vs Potencia (Escenario 3)')
xlabel 'Potencia dBm'
ylabel 'PER'