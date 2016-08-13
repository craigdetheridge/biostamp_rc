%%% Plot Electrocardiography Data

afeData=csvread('ecg.csv'); % read
afeData= afeData(2:end,:); % trim header

startTsMs = min(afeData(:,1));
tMs = afeData(:,1) - startTsMs;  % set start as 0ms
v = afeData(:,2); % unpack

plot(tMs,v,'b.');

legend('Potential (V)');
title('ECG Potential vs Time');
ylabel('ECG Potential (Volts)');
xlabel('Time since Recording Start (ms)');