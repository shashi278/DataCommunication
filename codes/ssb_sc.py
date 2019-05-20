import numpy as np
from numpy import *
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from ampMod import AmplitudeModulation

class SSBSC(AmplitudeModulation):
	
	def createSignals(self):
		'''
		Note:
		==========
		creates 'carrier', 'message', 'lower band
		modulated' and 'upper band modulated'
		signals
		
		#upper side band modulated signal
		usb= m(t).cos(2.π.fc.t) - m'(t).sin(2.π.fc.t)
		
		#upper side band modulated signal
		lsb= m(t).cos(2.π.fc.t) + m'(t).sin(2.π.fc.t)
		
		m'(t) ---> Hilbert Transform of m(t)
		i.e. m'(t)= m(t)/π.t 
		'''
		#carrier signal
		c= lambda t: self.Ac*sin(2*pi*self.fc*t)
		
		#message signal
		m= lambda t: self.Am*sin(2*pi*self.fm*t)
		
		#hilbert transform, m'(t)
		mh= lambda t: m(t)/(pi*t)
		
		#upper side band
		usb= lambda t: m(t)*cos(2*pi*self.fc*t) - mh(t)*sin(2*pi*self.fc*t)
		
		#lower side band
		lsb= lambda t: m(t)*cos(2*pi*self.fc*t) + mh(t)*sin(2*pi*self.fc*t)
		
		return c, m, usb, lsb

if __name__=='__main__':
	
	labels= {
	'title': '====SSB-SC Modulation====',
	'xlabel': 'Time(Sec)',
	'ylabel': 'Amplitude',
	'subtitle1': 'Carrier Signal: Ac.sin(Wc*t)',
	'subtitle2': 'Message Signal: Am.sin(Wm*t)',
	'subtitle3': 'SSB-SC Modulated Signal(USB)\nm(t)*cos(Wc*t) - m\'(t)*sin(Wc*t)',
	'subtitle4': 'SSB-SC Modulated Signal(LSB)\nm(t)*cos(Wc*t) + m\'(t)*sin(Wc*t)'
	}
	
	ssb= SSBSC(Ac= 3, Am= 2, fc= 5, fm= 1)
	ssb.plot(*ssb.createSignals()[0:3], labels, ssb.createSignals()[3])