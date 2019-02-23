"""
	Names
	CIS 422
	GoalTracker
"""

class SubGoal(object):
	"""CONSTRUCTORS FOR SUBGOAL"""
	def __init__(self, _id, _name, _startDate):
		self.id = _id #sets the id to the passed it
		self.name = _name #sets the name to the passed name
		self.startDate = _startDate #sets the start date to the passed start date
		self.finishDate = None #defaults the finish date to null

	"""METHODS FOR SUBGOAL"""
	'''SubGoal Operations'''
	def updateSubGoal(self, _name):
		self.name = _name #sets the name to the passed name

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
	