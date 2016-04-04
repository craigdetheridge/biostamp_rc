import numpy as np
import matplotlib.pyplot as plt

"""
  Plot Acceleration Data
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('accel.csv', delimiter=',', skip_header=1, names=['t','x','y','z'])
start_ts_ms = np.amin(data['t'])
t = np.subtract(data['t'],start_ts_ms)

fig = plt.figure()

ax1 = fig.add_subplot(111) # Format figure
ax1.set_title('Acceleration vs Time')    
ax1.set_xlabel('Time since Recording Start (ms)')
ax1.set_ylabel('Acceleration (g)')

ax1.plot(t,data['x'],color='r',linestyle='None',marker='.',alpha=0.7,label='X (g)')
ax1.plot(t,data['y'],color='g',linestyle='None',marker='.',alpha=0.7,label='Y (g)')
ax1.plot(t,data['z'],color='b',linestyle='None',marker='.',alpha=0.7,label='Z (g)')

leg = ax1.legend()
plt.show() # Draw