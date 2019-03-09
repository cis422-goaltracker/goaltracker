from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QSizePolicy
import sys
import time
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
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

class Canvas(FigureCanvas):
	def __init__(self, parent = None, width =5, height = 5, dpi =100):

		self.fig = Figure(figsize=(width, height), dpi=dpi)
		#self.fig = plt.figure()
		FigureCanvas.__init__(self, self.fig)
		FigureCanvas.setSizePolicy(self,
			QSizePolicy.Expanding,
			QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)
		self.setParent(parent)

	def plot_bar(self, datesList, valuesList):
		# Draw Bar Graph
		x = datesList
		y_heights = valuesList
		axes_bar = self.fig.add_subplot(111)
		axes_bar.set_title('Efforts')
		axes_bar.set_xlabel('Dates')
		if max(y_heights) < 1:
			if max(y_heights) < 1/60:
				y_heights = [y * 60 * 60 for y in y_heights]
				axes_bar.set_ylabel('Seconds')
			else:
				y_heights = [y * 60 for y in y_heights]
				axes_bar.set_ylabel('Minutes')
		else:
			axes_bar.set_ylabel('Hours')
		p1 = axes_bar.bar(x, y_heights,width = 0.7,color='g')
		def animate_bar(i):
			for rect, y in zip(p1, [(i+1)*y/60 for y in y_heights]):
				rect.set_height(y)
			return p1
		self.anim = animation.FuncAnimation(self.fig, animate_bar,repeat=False,frames=60,interval=10,blit=False)
		self.draw()

	def plot_ring(self, f_perc, uf_perc):
		#Draw Ring Graph
		axes_ring = self.fig.add_subplot(111)
		axes_ring.set_title('Goal Progress')
		labels = ["{0:.2f}% Finished".format(f_perc), "{0:.2f}% Unfinished".format(uf_perc)]
		colors = ['g', 'r']
		percentage = [f_perc, uf_perc]
		ring_chart = axes_ring.pie(percentage, wedgeprops=dict(width=0.5), startangle=90, labels = labels, colors = colors)
		def animate_ring(i): 
			ring_chart[0][1].set_theta1(90+i+1)
			return ring_chart[0][0], ring_chart[0][1]
		axes_ring.axis('off')
		if percentage[0] != 0:
			self.anim = animation.FuncAnimation(self.fig, animate_ring, repeat=False,frames=int(360*percentage[0]/100), interval=10, blit=False)
		self.draw()

	def stopAnimation(self):
		self.anim.event_source.stop()