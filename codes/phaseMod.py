import numpy as np
from numpy import *
from scipy.integrate import quad as integrate
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from ampMod import AmplitudeModulation

class PhaseModulation(AmplitudeModulation):
	
	#Constant, Kp, Modulator Sensitivity
	kp= 1.2
	
	def createSignals(self):
		'''
		creates 'carrier', 'message' and 'modulated' signals
		
		c= Ac.sin(2.π.fc.t)
		m= Am.sin(2.π.fm.t)
		pm= Ac.sin(2.π.fc.t+ kp*m(t))
		
		'''
		#carrier signal
		c= lambda t: self.Ac*sin(2*pi*self.fc*t)
		
		#message signal
		m= lambda t: self.Am*sin(2*pi*self.fm*t)
		
		#modulated signal
		pm= lambda t: self.Ac*sin(2*pi*self.fc*t + self.kp*m(t))
		
		return c, m, pm

if __name__=='__main__':
	
	labels= {
	'title': '====Phase Modulation====',
	'xlabel': 'Time(Sec)',
	'ylabel': 'Amplitude',
	'subtitle1': 'Carrier Signal: Ac.sin(Wc*t)',
	'subtitle2': 'Message Signal: Am.sin(Wm*t)',
	'subtitle3': 'Frequency Modulated Signal:\nAc*sin(Wc*t+ kp*m(t))'
	}
	
	pm= PhaseModulation(Ac= 3, Am= 2, fc= 5, fm= 1)
	pm.plot(*pm.createSignals(), labels)