%Problem 4
% T = 10^-8;
% u = ones(1,1001);
% n = 0:1000;
% t = n*T;
% h = 10^6*exp((-10^6)*t);
% 
% y = conv(u, h);
% 
% plot(y);
% title("Problem 4");
% xlabel("Value");
% ylabel("Time");
% xlim(1000);

% Problem 5
T = 10^-8;
u = ones(1,1001);
n = 0:1000;
t = n*T;
h = exp(-t).*sin(t).*cos(t);

y = conv(u, h);

plot(y);
title("Problem 5");
xlabel("Value");
ylabel("Time");
xlim(1000);