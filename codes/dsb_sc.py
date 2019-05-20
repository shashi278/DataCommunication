import numpy as np
from numpy import *
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from ampMod import AmplitudeModulation

class DSBSC(AmplitudeModulation):
	
	def createSignals(self):
		'''
		creates 'carrier', 'message' and 'modulated' signals
		
		## only difference from Normal Amplitude modulation is, the modulated signal won't have Ac term present in it
		
		c= Ac.sin(2.π.fc.t)
		m= Am.sin(2.π.fm.t)
		am= (Am.sin(2.π.fm.t)).sin(2.π.fc.t)
		
		'''
		#carrier signal
		c= lambda t: self.Ac*sin(2*pi*self.fc*t)
		
		#message signal
		m= lambda t: self.Am*sin(2*pi*self.fm*t)
		
		#modulated signal
		am= lambda t: (0+m(t))*sin(2*pi*self.fc*t)
		
		return c, m, am

if __name__=='__main__':
	
	labels= {
	'title': '====DSB-SC Modulation====',
	'xlabel': 'Time(Sec)',
	'ylabel': 'Amplitude',
	'subtitle1': 'Carrier Signal: Ac.sin(Wc*t)',
	'subtitle2': 'Message Signal: Am.sin(Wm*t)',
	'subtitle3': 'DSB-SC Modulated Signal: m(t)*sin(Wc*t)'
	}
	
	dsb= DSBSC(Ac= 3, Am= 2, fc= 5, fm= 1)
	dsb.plot(*dsb.createSignals(), labels)