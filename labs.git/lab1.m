%Problem 1
% x = 0:0.05:10;
% t = heaviside(x-5);
% plot(x, t);
% stem(x, t);
% title("Heaviside Graph");
% xlabel("Time");
% ylabel("Amplitude");
% ylim([-1 2]);

%Problem 2
Yes

%Problem 3
% A = 1;
% a = 0.8;
% T = 0.1;
% k = 0:100;
% n = k*T;
% x = A*a.^n;
% stem(k, x);

%Problem 4
% A = 1;
% a = 1.6;
% T = 0.1;
% k = 0:100;
% n = k*T;
% x = A*a.^n;
% stem(n, x);

%Problem 5
% A = 1;
% a = 1;
% T = 0.1;
% k = 0:25;
% n = k*T;
% x = A*a.^n;
% stem(n, x);
% ylim([-1 2]);

%Problem 6
% A = 1;
% a = 1;
% T = 1;
% k = 0:25;
% n = k*T;
% x = cos(pi*n/4);
% plot(n, x);
% ylim([-2 2]);

%Problem 7
% A = 1;
% a = 1;
% T = 1;
% k = 0:25;
% n = k*T;
% x = cos(pi*n/4);
% hold on;
% plot(k, x);
% ylim([-2 2]);
% x2 = cos(pi*(n+8)/4);
% plot(k, x2);
% hold off;

%Problem 8
A = 1;
a = 1;
T = 1;
k = 0:25;
n = k*T;
x = cos((3*pi*n)/8);
hold on;
plot(k, x);
ylim([-2 2]);
x2 = cos((3*pi*(n+16))/8);
plot(k, x2);
hold off;

%Problem 9
%The frequency of graph 8 is higher

%Problem 10
% It takes longer for graph 8 to appear periodic 
% because the peaks of the waveforms don't start
% repeating until t = 22
