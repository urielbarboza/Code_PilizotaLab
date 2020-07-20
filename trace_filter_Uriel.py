import numpydoc as np
from matplotlib import pyplot as plt
import os
from scipy import signal

def trace_filter(data,window,w):
	sp=data[:,1]
	time=data[:,0]
	sp=abs(sp)
	index=[]

	for i in range(len(sp)):
		if sp[i]>49 and sp[i]<51 or sp[i]<10:
			index.append(i)	
	time=np.delete(time,index)
	sp=np.delete(sp,index)
        
	speed=sp

	for i in range(len(speed)):
		if i>window or len(speed)-i>window:
			thresh=np.mean(speed[i-window:i+window])
		elif i<window:
			thresh=np.mean(speed[0:i+window])
		elif len(speed)-i<window:
			thresh=np.mean(speed[i-window:len(speed)])
			
		if speed[i]<thresh:
			speed[i]=thresh
	speed=signal.medfilt(speed,w)

	return(time,speed)

def median(data,w):
	sp=data[:,1]
	time=data[:,0]
	sp=abs(sp)
	index=[]

	for i in range(len(sp)):
		if sp[i]>49 and sp[i]<51 or sp[i]<10:
			index.append(i)	
	time=np.delete(time,index)
	sp=np.delete(sp,index)

	speed=sp

	speed=signal.medfilt(speed,w)

	return(time,speed)

def trace_filter2(data,window):
	sp=data[:,1]
	time=data[:,0]
	sp=abs(sp)
	index=[]

	for i in range(len(sp)):
		if sp[i]>49 and sp[i]<51 or sp[i]<10:
			index.append(i)	
	time=np.delete(time,index)
	sp=np.delete(sp,index)

	speed=sp

	for i in range(len(speed)):
		if i>window or len(speed)-i>window:
			thresh=np.mean(speed[i-window:i+window])
		elif i<window:
			thresh=np.mean(speed[0:i+window])
		elif len(speed)-i<window:
			thresh=np.mean(speed[i-window:len(speed)])
			
		if speed[i]<thresh:
			speed[i]=thresh

	return(time,speed)

def twosigma(data,window,w):
	sp=data[:,1]
	time=data[:,0]
	sp=abs(sp)
	index=[]

	for i in range(len(sp)):
		if sp[i]==50:
			index.append(i)	
	time=np.delete(time,index)
	sp=np.delete(sp,index)

	speed=sp

	for i in range(len(speed)):
		if i>window or len(speed)-i>window:
			mean=np.mean(speed[i-window:i+window])
		elif i<window:
			mean=np.mean(speed[0:i+window])
		elif len(speed)-i<window:
			mean=np.mean(speed[i-window:len(speed)])
			
		if abs((speed[i]-mean)/mean)>0.1:
			speed[i]=mean
	speed=signal.medfilt(speed,w)
	return(time,speed)

def delta_filter(data,thresh):
	raws=abs(data[:,1])
	rawt=data[:,0]

	fils=np.array(raws)
	filt=np.array(rawt)

	thresh=10

#index=[]

	for i in range(len(fils)-1):
		if abs(fils[i]-fils[i+1])>thresh:
			if fils[i]>fils[i+1]:
				fils[i+1]=fils[i]
			else:
				fils[i]=fils[i+1]

	return(filt, fils)

def normalise(speed):
	init_speed=speed[0:3000]
	sp=[]
	for i in range(0,59):
		s=np.max(init_speed[i*50:i*50+49])
		sp.append(s)

	norm=np.mean(sp)
	nspeed=speed*100.0/norm

	return(norm,nspeed)

def exponent(x,alfa):
	y=np.exp(-alfa*x)*100
	#y=2*(1/(2-10^10*alfa*x))
	return y
	

def medianfilter(data,w):
	sp=data[:,1]
	time=data[:,0]

	speed=sp

	speed=signal.medfilt(speed,w)

	return(time,speed)
    
    
def medianfilter2(data,w):
	sp=data[:,1]
	time=data[:,0]
	index=[]

	for i in range(len(sp)):
		if sp[i]>-55 and sp[i]<51:
			index.append(i)	
	time=np.delete(time,index)
	sp=np.delete(sp,index)

	speed=sp
	#speed=signal.medfilt(speed,w)


	return(time,speed)