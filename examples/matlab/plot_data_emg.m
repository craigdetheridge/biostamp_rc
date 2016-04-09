%%% Plot Electromyography Data

afeData=csvread('emg.csv'); % read
afeData= afeData(2:end,:); % trim header

startTsMs = min(afeData(:,1));
tMs = afeData(:,1) - startTsMs;  % set start as 0ms
v = afeData(:,2); % unpack

plot(tMs,v,'b.');

legend('Potential (V)');
title('EMG Potential vs Time');
ylabel('EMG Potential (Volts)');
xlabel('Time since Recording Start (ms)');