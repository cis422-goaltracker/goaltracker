"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal
from Status import Status as Status

class GoalManager(object):
	"""CONSTRUCTOR FOR GOALMANAGER"""
	def __init__(self, _currGID):
		self.currGID = _currGID #current goal id

	"""METHODS FOR GOALMANAGER"""
	def addGoal(self, _goalList, _goalInformation):
		#use _goalInformation and _currGID to create new Goal object

		#change _currGID to be a bigger ID (not previously seen)

		#append new Goal object to _goalList

		#return _goalList
		pass

	def editGoal(self, _goal, _goalInformation):
		#use _goalInformation to update _goal

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
	def getCurrGID():
		return self.currGID #returns the current Goal ID

	"""SETTERS FOR GOALMANAGER"""
	