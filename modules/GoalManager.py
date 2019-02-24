"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal
from Status import Status as Status

class GoalManager(object):
	"""CONSTRUCTOR FOR GOALMANAGER"""
	def __init__(self):
		pass

	"""METHODS FOR GOALMANAGER"""
	def addGoal(self, _goalList, _gid, _goalInformation):
		#use _goalInformation and _gid to create new Goal object
		#_goalInformation contains {name, category, priority, startdate}

		#append new Goal object to _goalList

		#return _goalList
		pass

	def editGoal(self, _goal, _goalInformation):
		#use _goalInformation to update _goal
		#_goalInformation contains {name, category, priority}

		#return _goal
		pass

	def deleteGoal(self, _goalList, _goal):
		#get id of _goal

		#find goal with matching id in _goalList

		#remove goal from _goalList

		#return _goalList and DG Status
		pass

	def completeGoal(self, _goal, _finishDate):
		_goal.completeGoal(_finishDate) #calls _goal's complete goal and passes _finish date
		return _goal #returns the updated goal

	"""GETTERS FOR GOALMANAGER"""


	"""SETTERS FOR GOALMANAGER"""
	