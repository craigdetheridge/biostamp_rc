%%% Plot Gyroscope Data

gyroData=csvread('gyro.csv'); % read
gyroData= gyroData(2:end,:); % trim header

startTsMs = min(gyroData(:,1));
tMs = gyroData(:,1) - startTsMs;  % set start as 0ms
xDps = gyroData(:,2); % unpack
yDps = gyroData(:,3);
zDps = gyroData(:,4);

hold on;
plot(tMs,xDps,'r.');
plot(tMs,yDps,'b.');
plot(tMs,zDps,'g.');

legend('X (°/s)','Y (°/s)','Z (°/s)');
title('Rotation vs Time');
ylabel('Axis Rotation (°/s)');
xlabel('Time since Recording Start (ms)');