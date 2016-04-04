%%% Plot Acceleration Data

accelData=csvread('accel.csv'); % read
accelData= accelData(2:end,:); % trim header

startTsMs = min(accelData(:,1));
tMs = accelData(:,1) - startTsMs;  % set start as 0ms
xG = accelData(:,2); % unpack
yG = accelData(:,3);
zG = accelData(:,4);

hold on;
plot(tMs,xG,'r.');
plot(tMs,yG,'b.');
plot(tMs,zG,'g.');

legend('X (g)','Y (g)','Z (g)');
title('Acceleration vs Time');
ylabel('Acceleration (g)');
xlabel('Time since Recording Start (ms)');