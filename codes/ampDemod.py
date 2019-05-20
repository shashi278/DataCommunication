import numpy as np
from numpy import *
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

	
from ampMod import AmplitudeModulation

class CoherentDetectionDemod(AmplitudeModulation):
	
	#Few Filter requirements
	order= 9 #order
	fs= 50.0 #sample rate
	cutoff= 1 #can be changed as per requirement
	
	def lowpass(self, cutoff, fs, order=5):
		nyq = 0.5 * fs
		normal_cutoff = cutoff / nyq
		b, a = butter(order, normal_cutoff, btype='low', analog=False)
		return b, a
	
	def lowpass_filter(self, data, cutoff, fs, order=5):
		b, a = self.lowpass(cutoff, fs, order=order)
		y = lfilter(b, a, data)
		return y
	
	def createSignals(self, am):
		'''
		parameters:
		==============
		
		am: amplitude modulated signal
		
		Procedure:
		==============
		Multiply modulated signal with local
		oscillator and pass the resultant through
		Low Pass Filter
		
		Circuit Diagram:
		==============
		
		am ------>(x)------>[LPF]------>msg signal(m)
						 ^
						 |
						 |
						 |
		  [Local Oscillator](lo)
		
		'''
		'''
		In Ideal cases, local oscillator os is same as
		the carrier signal except the amplitude parts
		'''
		
		#local oscillator
		lo= lambda t: sin(2*pi*self.fc*t)
		
		Vx= lambda t: am(t)*lo(t)
		
		#retrieved message signal
		msg  = lambda t: self.lowpass_filter(Vx(t), self.cutoff, self.fs, self.order)
		
		return am, Vx, msg

if __name__=='__main__':
	
	labels= {
	'title': '====Coherent Demodulation====',
	'xlabel': 'Time(Sec)',
	'ylabel': 'Amplitude',
	'subtitle1': 'Modulated Signal: [Ac+m(t)]sin(Wc.t)' ,
	'subtitle2': 'Vx= Modulated*Local oscillator',
	'subtitle3': 'Message Signal'
	}
	
	cdd= CoherentDetectionDemod(Ac= 3, Am= 2, fc= 5, fm= 1)
	#message signal
	m= lambda t: cdd.Am*sin(2*pi*cdd.fm*t)
	
	#modulated signal
	am= lambda t: (cdd.Ac+m(t))*sin(2*pi*cdd.fc*t)
	
	cdd.plot(*cdd.createSignals(am), labels)