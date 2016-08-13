import numpy as np
import matplotlib.pyplot as plt

"""
  Plot Acceleration Data
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('gyro.csv', delimiter=',', skip_header=1, names=['t','x','y','z'])
start_ts_ms = np.amin(data['t'])
t = np.subtract(data['t'],start_ts_ms)

fig = plt.figure()

ax1 = fig.add_subplot(111) # Format figure
ax1.set_title('Rotation vs Time')    
ax1.set_xlabel('Time since Recording Start (ms)')
ax1.set_ylabel('Axis Rotation ($^\circ$/s)')

ax1.plot(t,data['x'],color='r',linestyle='None',marker='.',alpha=0.7,label='X ($^\circ$/s)')
ax1.plot(t,data['y'],color='g',linestyle='None',marker='.',alpha=0.7,label='Y ($^\circ$/s)')
ax1.plot(t,data['z'],color='b',linestyle='None',marker='.',alpha=0.7,label='Z ($^\circ$/s)')

leg = ax1.legend()
plt.show() # Draw