"""
	Names
	CIS 422
	GoalTracker
"""

import datetime as DateTime

class SubGoal(object):
	"""CONSTRUCTORS FOR SUBGOAL"""
	def __init__(self, _id, _subGoalInformation, _startDate):
		self.id = _id #integer
		self.name = _subGoalInformation["name"] #string
		self.startDate = _startDate #DateTime
		self.finishDate = None #DateTime/Null

	"""METHODS FOR SUBGOAL"""
	'''SubGoal Operations'''
	def updateSubGoal(self, _subGoalInformation):
		self.name = _subGoalInformation["name"] #sets the name to the name in _subGoalInformation

	def completeSubGoal(self, _finishDate):
		self.finishDate = _finishDate #sets the finished date to the passed finished date

	def isComplete(self):
		return self.finishDate != None #if finish date is not null, it is complete

	"""GETTERS FOR SUBGOAL"""
	def getId(self):
		return self.id #returns the SubGoal ID

	def getName(self):
		return self.name #returns the SublGoal Name

	def getStartDate(self):
		return self.startDate #returns the SubGoal Start Date

	def getFinishDate(self):
		return self.finishDate #returns the SubGoal Finish Date

	"""SETTERS FOR SUBGOAL"""
	