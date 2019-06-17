t = 0:0.01:11;
T = 2.1;
k = 1;
pole = 1-T*k;
y = (1-T*k).^t;

plot(t, exp(-k*t))

figure
subplot(3, 2, 1)
plot(t, exp(-k*t))
hold on
plot(t, y)
hold off
title("F.D. T=2.1 Pole="+ pole)

T = 1.5;
pole = 1-T*k;
y = (1-T*k).^t;
subplot(3, 2, 3)
plot(t, exp(-k*t))
hold on
plot(t, y)
hold off
title("F.D. T=" + T + " Pole=" + pole);

T = 0.8;
pole = 1-T*k;
y = (1-T*k).^t;
subplot(3, 2, 5)
plot(t, exp(-k*t))
hold on
plot(t, y)
hold off
title("F.D. T=" + T + " Pole=" + pole);

T = 2.1;
pole = 1/(1+T*k);
y = (1+k*T).^-t;
subplot(3, 2, 2)
plot(t, exp(-k*t))
hold on
plot(t, y)
hold off
title("B.D. T=" + T + " Pole=" + pole);

T = 1.5;
pole = 1/(1+T*k);
y = (1+k*T).^-t;
subplot(3, 2, 4)
plot(t, exp(-k*t))
hold on
plot(t, y)
hold off
title("B.D. T=" + T + " Pole=" + pole);

T = 0.8;
pole = 1/(1+T*k);
y = (1+k*T).^-t;
subplot(3, 2, 6)
plot(t, exp(-k*t))
hold on
plot(t, y)
hold off
title("B.D. T=" + T + " Pole=" + pole);