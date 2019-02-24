"""
	Names
	CIS 422
	GoalTracker
"""

from SubGoal import SubGoal as SubGoal
from Status import Status as Status

class SubGoalManager(object):
	"""CONSTRUCTOR FOR SUBGOALMANAGER"""
	def __init__(self):
		pass

	"""METHODS FOR SUBGOALMANAGER"""
	def addSubGoal(self, _subGoalList, _sgid, _subGoalInformation):
		#use _subGoalInformation and _sgid to create new SubGoal object
		#subGoalInformation includes {name, startdate}

		#append new SubGoal object to _subGoalList

		#return _subGoalList
		pass

	def editSubGoal(self, _subGoal, _subGoalInformation):
		#use _subGoalInformation to update _subGoal

		#return _subGoal
		pass

	def deleteSubGoal(self, _subGoalList, _subGoal):
		#get id of _subGoal

		#find subGoal with matching id in _subGoalList

		#remove subGoal from _subGoalList

		#return _subGoalList and DSG Status
		pass

	def completeSubGoal(self, _subGoal, _finishDate):
		_subGoal.completeSubGoal(_finishDate) #calls _subgoal's complete subgoal and passes _finish date
		return _subGoal #returns the updated subgoal

	"""GETTERS FOR SUBGOALMANAGER"""

	"""SETTERS FOR SUBGOALMANAGER"""
		