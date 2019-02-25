"""
	Names
	CIS 422
	GoalTracker
"""

from SubGoal import SubGoal as SubGoal

class Goal(object):
	"""CONSTRUCTORS FOR GOAL"""
	def __init__(self, _id, _goalInformation, _startDate, _anticipatedFinishDate):
		self.id = _id #integer
		self.name = _goalInformation["name"] #string
		self.category = _goalInformation["category"] #string
		self.priority = _goalInformation["priority"] #integer
		self.startDate = _startDate #DateTime
		self.anticipatedFinishDate = _anticipatedFinishDate #DateTime
		self.finishDate = None #DateTime/Null
		self.effortTracker = {} #dictionary of date-elapsedtime pairs
		self.subGoals = [] #list of SubGoals

	"""METHODS FOR GOAL"""
	'''Goal Operations'''
	def rescheduleGoal(self, _anticipatedFinishDate):
		self.anticipatedFinishDate = _anticipatedFinishDate #sets the anticipated finish date to the new anticipated finishd date

	def updateGoal(self, _goalInformation):
		self.name = _goalInformation["name"] #sets the name to the passed name
		self.category = _goalInformation["category"] #sets the category to the passed category
		self.priority = _goalInformation["priority"] #sets the priority to the passed priority

	def completeGoal(self, _finishDate):
		self.finishDate = _finishDate #sets the finish date to the passed finish date

	def isComplete(self):
		return self.finishDate != None #if finish date is not null, it is complete

	def isOverDue(self, _currentDate):
		return self.anticipatedFinishDate < _currentDate #if current date is greater than anticipated finish date, its overdue

	'''Effort Tracker Operations'''
	def addEffortTrack(self, _date, _elapsedtime):
		if _date in self.effortTracker: #checks if date already exists in effort tracker
			self.effortTracker[_date] = self.effortTracker[_date] + _elapsedtime #if it already exists, add elapsed times together
		else:
			self.effortTracker[_date] = _elapsedtime #else adds a key-value pair of <date, elapsetime> to effort tracker

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

	def getAnticipatedFinishDate(self):
		return self.anticipatedFinishDate #returns the Goal Anticipated Finish Date

	def getFinishDate(self):
		return self.finishDate #returns the Goal Finish Date

	def getEffortTracker(self):
		return self.effortTracker.copy() #returns a copy of the Effort Tracker of the Goal

	def getSubGoals(self):
		return self.subGoals.copy() #returns a copy of the Sub Goals of the Goal

	"""SETTERS FOR GOAL"""
	def setSubGoals(self, _subGoals):
		self.subGoals = _subGoals