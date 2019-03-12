"""
    Authors: Jiazhen Cao
    Date: 03/09/2019
    CIS422
    GoalTracker
"""

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QSizePolicy
from matplotlib.figure import Figure
from matplotlib import animation
import matplotlib.pyplot as plt
import sys

class Canvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        '''
        @param: parent - set to None by default, parents of the Canvas
                width - canvas width, if not specified, default set to 5
                height - canvas height, if not specified, default set to 5
                dpi - matplotlib size, default set to 100

        @return: None

        @purpose: Initializes the canvas.
        '''
        self.fig = Figure(figsize=(width, height), dpi=dpi) # initialize a figure by using param
        FigureCanvas.__init__(self, self.fig) # FigureCanvas init function
        FigureCanvas.setSizePolicy(self, # Set size policy so FigureCanvas expand to fit the widget
            QSizePolicy.Expanding,
            QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self) # update the Geometry
        self.fig.set_facecolor('None') # set the figure background to None, i.e. transparent
        self.setStyleSheet("background-color:transparent;") # set canvas backgound to transparent
        self.setParent(parent) # set the parent for the Canvas

    def plot_bar(self, datesList, valuesList):
        '''
        @param: datesList - a list of string that represents days that has effort tracker data
                valuesList - a list of float that represents the effort of each day in the datesList

        @return: None

        @purpose: Analyze the data and draw the Bar Chart by using effort data with animation
        '''
        x = datesList # assign dataList to x
        y_heights = valuesList # assign valuesList to y_heights
        axes_bar = self.fig.add_subplot(111) # add a subplot at position 1,1,1 of the figure
        axes_bar.set_title('Efforts', fontsize = 20) # set the plot title
        axes_bar.set_xlabel('Dates', fontsize = 16) # set the x axis label
        axes_bar.set_facecolor('None') # set the background of the plot to transparent
        if len(y_heights) != 0 and max(y_heights) < 1: # if valuesList is not empty and the max effort data is less than 1 hour
            if max(y_heights) < 1/60: # if the max effort data is less than 1 minute
                if max(y_heights) < 1/(60 * 60): # if the max effort data is less than 1 second
                    y_heights = [y * 60 * 60 * 1000 for y in y_heights] # convert effort data into milliseconds
                    axes_bar.set_ylabel('Milliseconds', fontsize = 16) # set the y axis label
                else: # if the max effort data is greater than 1 second but less than a minute
                    y_heights = [y * 60 * 60 for y in y_heights] # convert effort data into seconds
                    axes_bar.set_ylabel('Seconds', fontsize = 16) # set the y axis label
            else: # if the max effort data is less than an hour but greater than a minute
                y_heights = [y * 60 for y in y_heights] # convert effort data into minute
                axes_bar.set_ylabel('Minutes', fontsize = 16) # set the y axis label
        else: # if the effort data exist and greater than an hour
            axes_bar.set_ylabel('Hours', fontsize = 16) # set the y axis label
        p1 = axes_bar.bar(x, y_heights, width = 0.7,color='g') # draw the bar chart with color green 
        if len(y_heights) == 0: # if y_heights is empty, don't do animation, otherwise, error
            p1 = axes_bar.text(0, 0, "You have not used Effort Tracker yet.", horizontalalignment='center', \
                verticalalignment='center', fontsize = 16)
            # plot a text information
        
        def animate_bar(i):
            '''
            @param: i - index

            @return: a bar container

            @purpose: update the height of the bar every iteration for animation
            '''
            for rect, y in zip(p1, [(i+1)*y/60 for y in y_heights]): # get each bar and the y height
                rect.set_height(y) # update each bar's height 
            return p1 #return the bar container

        if len(y_heights) != 0: # if y_heights is empty, don't do animation
            self.anim = animation.FuncAnimation(self.fig, animate_bar,repeat=False,frames=60,interval=10,blit=True)
        # Matplotlib built in animation function which take the animate_bar as the iterating function.
        self.draw() # display the figure

    def plot_ring(self, f_perc, uf_perc):
        '''
        @param: f_perc - the percentage of the number of finished subgoals with respect to the number of subgoals.
                uf_perc - the percentage of the number of unfinished subgoals with respect to the number of subgoals.

        @return: None

        @purpose: Draw the ring chart by using the percentage data with animation
        '''
        axes_ring = self.fig.add_subplot(111) # add a subplot at position 1,1,1 of the figure
        axes_ring.set_title('Subgoal Progress', fontsize = 20) # set the title of the plot
        axes_ring.set_facecolor('None') # set the background color to None, i.e. transparent
        labels = ["{0:.2f}% Finished".format(f_perc), "{0:.2f}% Unfinished".format(uf_perc)] # format the labels for data
        colors = ['g', 'r'] # set the brush color for plotting
        percentage = [f_perc, uf_perc] # create a list of percentage
        ring_chart = axes_ring.pie(percentage, wedgeprops=dict(width=0.5), startangle=90, \
            labels = labels, colors = colors)
        # draw a pie chart that used wedgeprops to display as a ring chart
        ring_chart[1][0].set_fontsize(16) # set label size
        ring_chart[1][1].set_fontsize(16) # set label size

        def animate_ring(i):
            '''
            @param: i - index

            @return: a pie container

            @purpose: update the first theta of the green colored 'finished' portion
            ''' 
            ring_chart[0][1].set_theta1(90+i+1) # update the theta1 of the wedge which represents finished portion
            return ring_chart[0][0], ring_chart[0][1] # return the two wedges in a sequence
        
        axes_ring.axis('off') # turn off the axis
        if percentage[0] != 0: # if percentage of finished portion is 0, don't do animation, otherwise, error
            self.anim = animation.FuncAnimation(self.fig, animate_ring, repeat=False, \
                frames=int(360*percentage[0]/100), interval=10, blit=True)
            # Matplotlib built in animation function which take the animate_bar as the iterating function.
        self.draw() # display the figure

    def stopAnimation(self):
        '''
        @param: None

        @return: None

        @purpose: Stop the plotting animation
        '''
        self.anim.event_source.stop() # force the animation to stop