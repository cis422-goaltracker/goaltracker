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
		
	"""METHODS FOR ANALYSISGENERATOR"""


	"""GETTERS FOR ANALYSISGENERATOR"""


	"""SETTERS FOR ANALYSISGENERATOR"""
		



ui = ['Analysis.ui', 'UncompletedAnalysis.ui', 'viewgoal.ui']

class Analysis_Event(QDialog):
	def __init__(self, model):
	super(Analysis_Event, self).__init__()
	loadUi(ui.[3], self)
	#command to click

class AnalysisViewer(object):
	"""CONSTRUCTORS FOR ANALYSISVIEWER"""
	def __init__(self, model):
	super(AnalysisViewer, self).__init__()
	loadUi(ui.[1],self)	

	self.m = model

	#Skeleton_code

	#time_took = start_time - stop_time
	#time_took needs to be rounded to days (ex. 3.4 days)
	#Push string "This Goal took you" + time_took + "days to complete" to label_daystook

	#end_time_comp = anticipated_end_time - actual_end_time
	#end_time_comp needs to be rounded to days (ex. 3.4 days)
	#Push string "That is" + end_time_comp + "days faster/slower than anticipated" to label_fasterslower
	
	#time_per_day_summed = (from dictionary of time and dates from effort time, need time per day summed) / time_took
	#time_per_day_summed needs to be in hours (ex. 9.3 hours)
	#Push string "You spend on average" + time_per_day_summed + "hours a day working on your goal" to label_numhours

	#before_due_num = number_of_goals_completed_before_due / num_completed_goals
	#after_due_num = number_of_goals_completed_after_due / num_completed_goals
	#before_due_num and after_due_num need to be less than or equal to one
	#greater_val = max(before_due_num, after_due_num)
	#if greater_val == before_due_num:
	#	Push string "You completed %" + greater_val + of your goals faster than aniticpated!" to label_lowerlinetext_1
	#	Push string "Great job, keep up the good work!" to label_lowerlinetext_2
	#	Push string "" to label_lowerlinetext_3

	#if greater_val != before_due_num:
	#	Push string "You completed %" + greater_val + of your goals slower than aniticpated." to label_lowerlinetext_1
	#	Push string "You seem to have trouble sticking to your goals. Consider giving" to label_lowerlinetext_2
	#	Push string "yourself more time next time!" to label_lowerlinetext_3


	"""METHODS FOR ANALYSISVIEWER"""

	"""GETTERS FOR ANALYSISVIEWER"""

	"""SETTERS FOR ANALYSISVIEWER"""

class AnalysisViewerUnfinished(object):
	"""CONSTRUCTORS FOR ANALYSISVIEWER"""
	def __init__(self, model):

	self.m = model

	#before_due_num = number_of_goals_completed_before_due / num_completed_goals
	#after_due_num = number_of_goals_completed_after_due / num_completed_goals
	#before_due_num and after_due_num need to be less than or equal to one
	#greater_val = max(before_due_num, after_due_num)
	#if greater_val == before_due_num:
	#	Push string "You completed %" + greater_val + of your goals faster than aniticpated!" to label_lowerlinetext_1
	#	Push string "Great job, keep up the good work!" to label_lowerlinetext_2
	#	Push string "" to label_lowerlinetext_3

	#if greater_val != before_due_num:
	#	Push string "You completed %" + greater_val + of your goals slower than aniticpated." to label_lowerlinetext_1
	#	Push string "You seem to have trouble sticking to your goals. Consider giving" to label_lowerlinetext_2
	#	Push string "yourself more time next time!" to label_lowerlinetext_3

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
