"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal
from Model import Model as Model

class ActiveTimer(object):
	"""CONSTRUCTOR FOR ACTIVETIMER"""
	def __init__(self):
		pass

	"""METHODS FOR ACTIVETIMER"""
	def calculateActiveTime(self, _gid, _model, _currentDate):
		goal = _model.getGoal(_gid) #gets the goal form the model
		if goal.isComplete(): #if goal is complete
			return goal.getFinishDate() - goal.getStartDate() #find the difference between finish and start date
		else:
			return _currentDate - goal.getStartDate() #find the difference between the current date and start date

	"""GETTERS FOR ACTIVETIMER"""


	"""SETTERS FOR ACTIVETIMER"""
	