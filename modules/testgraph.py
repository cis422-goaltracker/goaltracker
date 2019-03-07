from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FingureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
from matplotlib import animation

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
        self.setWindowIcon(QIcon("icon.png"))
        self.MyUI()

    def MyUI(self):

        canvas = Canvas(self, width=8, height=4)
        canvas.move(0,0)

        button = QPushButton( "Button 1", self)
        button.move(100, 450)

        button = QPushButton("Button 2", self)
        button.move(250, 450)


class Canvas(FingureCanvas):
	def __init__(self, parent = None, width =5, height = 5, dpi =100):

		self.fig = Figure(figsize=(width, height), dpi=dpi)
		#self.fig = plt.figure()
		self.axes_bar = self.fig.add_subplot(121)
		self.axes_ring = self.fig.add_subplot(122)
		FingureCanvas.__init__(self, self.fig)
		self.setParent(parent)
		self.plot()

	def plot(self):
		# Draw Bar Graph
		x = ['1/10/19', '1/11/19', '1/13/19', '1/14/19', '1/15/19', '1/16/19']
		y_heights = [10.0, 2.0, 7.0, 5.0, 2.0, 9.0]
		p1 = self.axes_bar.bar(x, y_heights,width = 0.7,color='g')
		#ax = self.figure.add_subplot(111)
		def animate_bar(i):
			for rect, y in zip(p1, [i*y/60 for y in y_heights]):
				rect.set_height(y)
		anim_bar = animation.FuncAnimation(self.fig,animate_bar,repeat=False,frames=60,interval=10,blit=False)
		
		#Draw Ring Graph
		self.axes_ring.set_xlim([0, 10])
		self.axes_ring.set_ylim([0, 10])

		#patches = [mpatches.Wedge((5,5), 4, 0, 0, width = 1.2, color = 'g', label='Finished'),\
		#		   mpatches.Wedge((5,5), 4, 180, 180, width = 1.2, color = 'r', label='Unfinished')]
		patch_one = mpatches.Wedge((5,5), 4, 90, 90, width = 1.2, color = 'g', label='Finished')
		self.axes_ring.add_patch(patch_one)
		#self.axes_ring.add_patch(patch_two)
		#p = PatchCollection(patches)
		#self.axes_ring.add_collection(p)
		self.axes_ring.legend()
		#patches_children = p.get_children()
		def animate_ring(i):
			patch_one.set_theta2(90+i+1)
			return patch_one,

		self.axes_ring.axis('off')
		anim_ring = animation.FuncAnimation(self.fig, animate_ring, repeat=False,frames=270, interval=10, blit=True)

		self.draw()

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()

'''
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
plt.grid(True)

patch_one = mpatches.Wedge((5,5), 4, 90, 90, width = 1.2, color = 'g', label='Finished')

ax.add_patch(patch_one)
ax.legend()
def animate(i):
    patch_one.set_theta2(90+i+1)
    #patch_one._recompute_path()
    return patch_one,

ax.axis('off')
anim = animation.FuncAnimation(fig, animate, repeat=False,frames=180, interval=10, blit=True)

plt.show()
'''