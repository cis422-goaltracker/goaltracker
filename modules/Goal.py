"""
	Names
	CIS 422
	GoalTracker
"""

from SubGoal import SubGoal as SubGoal

class Goal(object):
	"""CONSTRUCTORS FOR GOAL"""
	def __init__(self, _id, _name, _category, _priority, _startDate):
		self.id = _id #sets the id to the passed id
		self.name = _name #sets the name to the passed name
		self.category = _category #sets the category to the passed category
		self.priority = _priority #sets the priority to the passed priority
		self.startDate = startDate #sets the start date to the passed start date
		self.finishDate = None #defaults finish date to null
		self.effortTracker = {} #defaults effort tracker to empty dictionary
		self.subGoals = [] #defaults subl goals to empty list

	"""METHODS FOR GOAL"""
	'''Goal Operations'''
	def updateGoal(self, _name, _category, _priority):
		self.name = _name #sets the name to the passed name
		self.category = _category #sets the category to the passed category
		self.priority = _priority #sets the priority to the passed priority

	def completeGoal(self, _finishDate):
		self.finishDate = _finishDate #sets the finish date to the passed finish date

	def isComplete(self):
		return self.finishDate != None #if finish date is not null, it is complete

	'''SubGoal Operations'''
	def appendSubGoal(self, _subgoal):
		self.subGoals.append(_subgoal) #appends the passed subgoal to the subgoal list

	'''Effort Tracker Operations'''
	def addEffortTrack(self, _date, _elapsedtime):
		self.effortTracker[_date] = _elapsedtime #adds a key-value pair of <date, elapsetime> to effort tracker

	"""GETTERS FOR GOAL"""
	def getId(self):
		return self.id #returns the Goal ID

	def getName(self):
		return self.name #returns the Goal Name

	def getCategory(self):
		return self.category #returns the Goal Category

	def getPriority(self):
		return self.priority #returns the Goal Priority

	def getStartDate(self):
		return self.startDate #returns the Goal Start Date

	def getFinishDate(self):
		return self.finishDate #returns the Goal Finish Date

	def getEffortTracker(self):
		return self.effortTracker.copy() #returns a copy of the Effort Tracker of the Goal

	def getSubGoals(self):
		return self.subGoals.copy() #returns a copy of the Sub Goals of the Goal

	"""SETTERS FOR GOAL"""
