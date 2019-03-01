"""
	Names Kellie Hawks 
	CIS 422
	GoalTracker
"""
import sys
from Model import CalendarModel
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import calendar
import datetime
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

#For Kellie to work on
#need to pip install pyqtgraph
class AnalysisGenerator(object):
	"""CONSTRUCTOR FOR ANALYSISGENERATOR"""
	def __init__(self):
		pass

	def calculateActiveTime(self, _gid, _model, _currentDate):
		goal = _model.getGoal(_gid) #gets the goal form the model
		if goal.isComplete(): #if goal is complete
			return goal.getFinishDate() - goal.getStartDate() #find the difference between finish and start date
		else:
			return _currentDate - goal.getStartDate() #find the difference between the current date and start date

	def trackProgress(self, _gid, _model):
		pass

	def trackEffort(self, _gid, _model):
		pass


	def calculateFasterSlower(self, _gid, _model):
		goal = _model.getGoal(_gid)	#gets the goal from the model
		if goal.isComplete(): 	#if goal is complete
			return goal.getInitialAnticipatedFinishDate() - goal.getFinishDate() #calculates the number of days from anticipated finish date

	def calculateAveragetime(self, _gid, _model):
		ret = {} #creates a dictionary to return
		for dt in dict.keys(): #loops through keys in dictionarya
			if not (dt.date() in ret): #if date is not in return dictioary
					ret[dt.date()] = dict[dt] #add timedelta if does not exist
			else:
				returnet[dt.date()] += dict[dt] #adds timedelta if date already exists
		timesum = sum(d.values()) #sum all the values
		return timesum/ len(ret) #return the average per day


	def calculateBeforeDuedate(self, _model):
		reschedulecount = 0	#creates counter for number of goals rescheduled
		completedcount = 0 	#creates counter for completed goals
		for i in _model:	#looks through goals in model
			if _model.getGoal(i).hasBeenRescheduled() and _model.getGoal(i).isComplete(): #increments if a completed goal has been rescheduled
				reschedulecount += 1
			if _model.getGoal(i).isComplete(): #increments completed goal count
				completedcount += 1
		completed_before_due = completedcount - reschedulecount #finds number of goals not reschedules
		return completed_before_due/completedcount #calculates and returns percentage of goals done befoe duedate


	def calculateAfterDuedate(self, _model):
		reschedulecount = 0 #creates counter for number of goals rescheduled
		completedcount = 0 	#creates counter for completed goals
		for i in _model:	#loops through goals in model
			if _model.getGoal(i).hasBeenRescheduled() and _model.getGoal(i).isComplete(): #increments if completed goal has been rescheduled
				reschedulecount += 1
			if _model.getGoal(i).isComplete(): #increments completed goal count
				completedcount += 1
		return reschedulecount/completedcount #calculates and returns percentage of goals completed after inital duedate
		
	def tranformDatesList(self, _model):
		ret = {} #creates a dictionary to return
		for dt in dict.keys(): #loops through keys in dictionarya
			if not (dt.date() in ret): #if date is not in return dictioary
					ret[dt.date()] = dict[dt] #add timedelta if does not exist
			else:
				returnet[dt.date()] += dict[dt] #add timedelta if date already exists
		
		for key in dict.keys(): #for every key in the dictionary
			datetime.strftime(key,'%b %d, %Y') #turn it into a string
		
		dates = list(ret.keys()) #make a list of date strings

		return dates

	def tranformValuesList(self, _model):
		ret = {} #creates a dictionary to return
		for dt in dict.keys(): #loops through keys in dictionarya
			if not (dt.date() in ret): #if date is not in return dictioary
					ret[dt.date()] = dict[dt] #add timedelta if does not exist
			else:
				returnet[dt.date()] += dict[dt] #add timedelta if date already exists
		
		values = list(ret.values()) #make a list of values

		return values


	# time_took = calculateActiveTime()
	# end_time_comp = calculateFasterSlower()
	# time_per_day_summed = calculateAverageTime()
	# before_due_num = calculateBeforeDuedate()
	# after_due_num = calculateAfterDuedate()
		
	"""METHODS FOR ANALYSISGENERATOR"""


	"""GETTERS FOR ANALYSISGENERATOR"""


	"""SETTERS FOR ANALYSISGENERATOR"""


class CustomWidget(pg.GraphicsWindow):
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')
    ptr1 = 0
    def __init__(self, parent=None, **kargs):
        pg.GraphicsWindow.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle('PyQt Graph : Time spent per day for Task')    #adds title for window
        p1 = self.addPlot(labels =  {'left':'Time Spent', 'bottom':'Day'}) #adds labels to left and bottom side
        
        self.data1 = np.random.normal(size=10)		   # what does this line do?
        print(data1)
        
        self.curve1 = p1.plot(self.data1, pen=(3,3))   #this is how the data is plotted, with 3,3 for pen size

        timer = pg.QtCore.QTimer(self)			#create timer
        timer.timeout.connect(self.update)		#connect time to update
        timer.start(60) 						#Updates itself every 60 seconds (1 minute)

    def update(self):
        self.data1[:-1] = self.data1[1:]  		# shift data in the array one sample left
                            # (see also: np.roll)
        self.data1[-1] = np.random.normal()
        self.ptr1 += 1
        self.curve1.setData(self.data1)
        self.curve1.setPos(self.ptr1, 0)

if __name__ == '__main__':
    w = CustomWidget()
    w.show()
    QtGui.QApplication.instance().exec_()
