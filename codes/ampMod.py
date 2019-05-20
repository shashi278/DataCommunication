import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class AmplitudeModulation():
	def __init__(self, Ac, Am, fc, fm):
		'''
		parameters:
		=================
		Ac: Amplitude of carrier signal
		Am: Amplitude of message signal
		fc: frequency of carrier signal
		fm: freaquency of message signal
		
		'''
		self.Ac= Ac
		self.Am= Am
		self.fc= fc
		self.fm= fm
		self.t= np.arange(0, 2*pi, 0.01)
	
	def createSignals(self):
		'''
		creates 'carrier', 'message' and 'modulated' signals
		
		c= Ac.sin(2.π.fc.t)
		m= Am.sin(2.π.fm.t)
		am= (Ac+Am.sin(2.π.fm.t)).sin(2.π.fc.t)
		
		'''
		#carrier signal
		c= lambda t: self.Ac*sin(2*pi*self.fc*t)
		
		#message signal
		m= lambda t: self.Am*sin(2*pi*self.fm*t)
		
		#modulated signal
		am= lambda t: (self.Ac+m(t))*sin(2*pi*self.fc*t)
		
		return c, m, am
	
	
	def plot(self, c, m, am, labels, *args):
		'''
		parameters
		===================
		c: carrier signal
		m: message signal
		am: modulated signal
		labels: dictionary of labels for the graph
		'''
		
		if len(args)==1:
			fig, (ax1, ax2, ax3, ax4)= plt.subplots(4,1)
			ax= (ax1, ax2, ax3, ax4)
		else:
			fig, (ax1, ax2, ax3)= plt.subplots(3,1)
			ax= (ax1, ax2, ax3)
		
		fig.suptitle(labels['title'])
		
		for each in ax:
			each.set_ylabel(labels['ylabel'])
			each.set_xlabel(labels['xlabel'])
			each.axhline()
		
		ax1.set_title(labels['subtitle1'])
		ax2.set_title(labels['subtitle2'])
		ax3.set_title(labels['subtitle3'])
		
		line1, =ax1.plot(self.t, c(self.t))
		line2, =ax2.plot(self.t, m(self.t))
		line3, =ax3.plot(self.t, am(self.t), color='r')
		
		anim1= FuncAnimation(fig, self.animate, fargs= (c, line1), init_func= None, interval=2, blit=True, save_count=50 )
		anim2= FuncAnimation(fig, self.animate, fargs= (m, line2), init_func= None, interval=2, blit=True, save_count=50 )
		anim3= FuncAnimation(fig, self.animate, fargs= (am, line3), init_func= None, interval=2, blit=True, save_count=50 )
		
		if len(args)==1:
			ax4.set_title(labels['subtitle4'])
			line4, =ax4.plot(self.t, args[0](self.t), color='r')
			#anim3=''
			anim4= FuncAnimation(fig, self.animate, fargs= (am, line4), init_func= None, interval=2, blit=True, save_count=50 )
		
		plt.tight_layout()
		plt.show()
	
	def animate(self, i, *fargs):
		func= fargs[0]
		line= fargs[1]
		line.set_ydata(func(self.t+i/40))
		return line,

if __name__=='__main__':
	
	labels= {
	'title': '====Amplitude Modulation====',
	'xlabel': 'Time(Sec)',
	'ylabel': 'Amplitude',
	'subtitle1': 'Carrier Signal: Ac.sin(Wc*t)',
	'subtitle2': 'Message Signal: Am.sin(Wm*t)',
	'subtitle3': 'Amplitude Modulated Signal: [Ac+m(t)]sin(Wc.t)',
	'subtitle4': 'optional'
	}
	
	am= AmplitudeModulation(Ac= 3, Am= 2, fc= 5, fm= 1)
	am.plot(*am.createSignals(), labels)