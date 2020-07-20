import numpy as np
from matplotlib import pyplot as plt
import os
from scipy.optimize import curve_fit
from scipy import signal 




#conds=['0.1Hz','0.2Hz','0.3Hz','1Hz','2Hz','2.8Hz','10ms','50ms','100ms','200ms']	


path='C:\\Users\\s1879315\\1.Uriel_Data\\firsttest 16may\\Speed vs Time 0\\Speed vs time cell_1.txt'

data=np.loadtxt(path)


time,speed=median(data,201)
norm,nspeed=normalise(speed)

print len(time), len(speed), len(nspeed)

		#nspeed=nspeed[0:75000]
		#time=time[0:75000]

popt,pcov=curve_fit(exponent,time[0:-1],nspeed[0:-1],maxfev=20000)
x=np.linspace(0,900,90000)
fit=exponent(x,*popt)
alfa=popt[0]	

	
plt.plot(time/60,nspeed,linestyle='none',marker='o', markersize=1,zorder=1,color='purple')
plt.plot(x/60,fit,lw=3, color='red',zorder=2)
plt.plot(x/60,fit,lw=2,label='a=%f'%alfa, color='navy',zorder=3)
plt.axis(xmin=0, xmax=15,ymin=0,ymax=120)
plt.legend()
plt.axis(ymin=0, ymax=120)
plt.title('July29_1.6V_395nm(UV)_1',size=12.5)
plt.ylabel('Normalised motor speed, %',size=12.5)
plt.xlabel('Time,min',size=12.5)
plt.savefig('C:\\Users\\s1879315\\1.Uriel_Data\\1.Raw Data Microscope\\Deltafilter.png')
plt.show()		