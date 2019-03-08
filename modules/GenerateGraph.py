from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
import time
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FingureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
from matplotlib import animation
"""
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "Embed Matplotlib In PyQt5"
        top = 400
        left = 400
        width = 900
        height = 500
        #icon = "icon.png"

        self.setWindowTitle(title)
        self.setGeometry(top,left, width, height)
        #self.setWindowIcon(QIcon("icon.png"))
        self.MyUI()

    def MyUI(self):

		canvas = Canvas(self, width=8, height=4)
		canvas.move(0,0)

        button = QPushButton( "Button 1", self)
        button.move(100, 450)

        button = QPushButton("Button 2", self)
        button.move(250, 450)
"""

class Canvas(FingureCanvas):
	def __init__(self, parent = None, width =5, height = 5, dpi =100):

		self.fig = Figure(figsize=(width, height), dpi=dpi)
		#self.fig = plt.figure()
		FingureCanvas.__init__(self, self.fig)
		self.setParent(parent)

	def plot_bar(self):
		# Draw Bar Graph
		x = ['1/10/19', '1/11/19', '1/13/19', '1/14/19', '1/15/19', '1/16/19']
		y_heights = [10.0, 2.0, 7.0, 5.0, 2.0, 9.0]
		axes_bar = self.fig.add_subplot(111)
		p1 = axes_bar.bar(x, y_heights,width = 0.7,color='g')
		def animate_bar(i):
			for rect, y in zip(p1, [(i+1)*y/60 for y in y_heights]):
				rect.set_height(y)
			#print("Frame", i)
			return p1
		self.anim = animation.FuncAnimation(self.fig, animate_bar,repeat=False,frames=60,interval=10,blit=True)
		self.draw()

	def plot_ring(self):
		#Draw Ring Graph
		axes_ring = self.fig.add_subplot(111)
		labels = ["Finished", "Unfinished"]
		colors = ['g', 'r']
		percentage = [70, 30]
		ring_chart = axes_ring.pie(percentage, wedgeprops=dict(width=0.5), startangle=90, labels = labels, colors = colors)
		def animate_ring(i): 
			ring_chart[0][1].set_theta1(90+i+1)
			return ring_chart[0][0], ring_chart[0][1]
		axes_ring.axis('off')
		self.anim = animation.FuncAnimation(self.fig, animate_ring, repeat=False,frames=int(360*percentage[0]/100), interval=10, blit=True)
		self.draw()

	def stopAnimation(self):
		self.anim.event_source.stop()