import numpy as np
import matplotlib.pyplot as plt

"""
  Plot Electrocardiography Data
"""
data = np.genfromtxt('ecg.csv', delimiter=',', skip_header=1, names=['t','v'])
start_ts_ms = np.amin(data['t'])
t = np.subtract(data['t'],start_ts_ms)

fig = plt.figure()

ax1 = fig.add_subplot(111) # Format figure
ax1.set_title('ECG Potential vs Time')    
ax1.set_xlabel('Time since Recording Start (ms)')
ax1.set_ylabel('ECG Potential (Volts)')

ax1.plot(t,data['v'],color='r',linestyle='None',marker='.',alpha=0.7,label='ECG Potential (V)')

leg = ax1.legend()
plt.show() # Draw
