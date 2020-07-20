# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:28:49 2019
Notes from Jerko:
mask2_forbias
returns a numpy array of true/false values, where anything >-15 Hz is False.
This is done because the FFT code sometimes (or always) doesn't make a bin centred around 0, instead you might have a bin around -2 and a bin around 2, meeting at 0.
So when calculating bias, just saing when speed <0 will also count some of the zero values.
I am not sure why I made the threshold -15, probably to avoid some super short aborted switches as I didn't know how they add to tumble events.

bias
takes a given array of speeds, applies the mask to find out how many points are below 15 Hz, and returns the that number divided by the original array length

moving window
You specify a window in points and run it over the input array, calculating bias after every step. For example, for 1 minute window, it would be 6000 points if you used deltaT = 0.01 in the FFT program like I did.
Notice that nothing is calculated for the initial window/2 and final window/2 length of the array, due to the nature of the moving window. Keep in mind where your time axis starts and finishes while plotting.
Keep in mind that I always used a even number of points in my window, if you use an odd number, then due to nature of integer division, then the moving window will be 1 point short at the end of the loop and return an error. I think.




@author: s1879315
"""

def mask2_forbias(array):
    """ A mask that sets everything below -15 Hz to False"""
    speed=np.copy(array)
    mask=speed<-15 # select for ccw
    return mask

def CWbias(array):
    """ Just CW Bias from array"""
    speed=np.copy(array)
    length=len(speed)
    speed=speed[mask2_forbias(speed)]
    return float(len(speed))/length

def bias_movingwin(array, window):
    speed=np.copy(array)
    output=[]
    for i in range(window/2,len(speed)-window/2):
        speed_part=speed[i-window/2:i+window/2]
        output.append(CWbias(speed_part))
    return output

