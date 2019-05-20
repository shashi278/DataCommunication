import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from ampMod import AmplitudeModulation
class FrequencyModulation(AmplitudeModulation):
	
	#Constant, Kf, Modulator Sensitivity
	kf= 0.5
	
	def createSignals(self):
		'''
		creates 'carrier', 'message' and 'modulated' signals
		
		c= Ac.sin(2.π.fc.t)
		m= Am.sin(2.π.fm.t)
		am= (Ac+Am.sin(2.π.fm.t)).sin(2.π.fc.t)
		
		'''