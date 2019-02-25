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
	def calculateActiveTime(self, _gid, _model, _currentDate): #FUNCTION NEEDS TO BE BUILT
		goal = _model.getGoal(_gid) #gets the goal form the model

		elapsedTime = None
		#if complete, goal finishdate - startdate

		#if not complete, currentdate - startdate

		return elapsedTime #returns the elapsed time

	"""GETTERS FOR ACTIVETIMER"""


	"""SETTERS FOR ACTIVETIMER"""
	