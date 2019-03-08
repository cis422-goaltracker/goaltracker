"""
	Names
	CIS 422
	GoalTracker
"""
#System Imports
from datetime import datetime, timedelta
import copy

class Goal(object):
	"""CONSTRUCTORS FOR GOAL"""
	def __init__(self, _id):
		'''
        @param:

        @return:

        @purpose:
        '''
		#constant features
		self.id = _id #integer
		self.startDate = datetime.now() #DateTime

		#user updateable features
		self.name = "" #string
		self.category = "" #string
		self.priority = 1 #integer
		self.memo = "" #string
		self.dueDate = None #DateTime

		#programmatically updateable features
		self.initialDueDate = None #DateTime
		self.finishDate = None #DateTime/Null
		self.effortTrackingData = [] #list of tuples (finish time, start time)
		self.subGoalList = [] #list of SubGoals
		self.sortingMethod = "category" #string
	
	"""Special Methods"""
	def __lt__(self, other):
		'''
        @param:

        @return:

        @purpose: Override less than, aka "<", so self<right_goal
        '''
		if self.sortingMethod == "category":
			return (self.category.lower() < other.category.lower())
		if self.sortingMethod == "priority":
			return (self.priority < other.priority)
		return("ERROR: This should never happen (Sort error)")

	"""METHODS FOR GOAL"""
	'''Goal Operations'''
	def hasDueDate(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.dueDate != None

	def hasBeenRescheduled(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		if self.hasDueDate():
			return self.dueDate != self.initialDueDate #if due date and initial due date are same, return false, otherwise true
		else:
			return None

	def update(self, _goalInformation):
		'''
        @param:

        @return:

        @purpose:
        '''
		self.name = _goalInformation["name"] #sets the name to the passed name
		self.category = _goalInformation["category"] #sets the category to the passed category
		self.priority = _goalInformation["priority"] #sets the priority to the passed priority
		self.memo = _goalInformation["memo"]
		if not self.hasDueDate() and self.initialDueDate == None:
			self.initialDueDate = _goalInformation["dueDate"]
		self.dueDate = _goalInformation["dueDate"]

	def complete(self, _finishDate):
		'''
        @param:

        @return:

        @purpose:
        '''
		self.finishDate = _finishDate #sets the finish date to the passed finish date

	def isComplete(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.finishDate != None #if finish date is not null, it is complete

	def isOverDue(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		if self.hasDueDate():
			return self.dueDate < datetime.now() #if current date is greater than due date, its overdue
		else:
			return False

	'''Subgoal Operations'''
	def addSubGoal(self, _sgid):
		'''
        @param:

        @return:

        @purpose:
        '''
		self.subGoalList.append(SubGoal(_sgid))

	def updateSubGoal(self, _sgid, _subGoalInformation):
		'''
        @param:

        @return:

        @purpose:
        '''
		self.subGoalList[self.getIndex(_sgid)].update(_subGoalInformation)

	def completeSubGoal(self, _sgid):
		'''
        @param:

        @return:

        @purpose:
        '''
		self.subGoalList[self.getIndex(_sgid)].complete()

	def deleteSubGoal(self, _sgid):
		'''
        @param:

        @return:

        @purpose:
        '''
		self.subGoalList.pop(self.getIndex(_sgid))

	def getSubGoal(self, _sgid):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.subGoalList[self.getIndex(_sgid)]

	def getIndex(self, _sgid):
		'''
        @param:

        @return:

        @purpose:
        '''
		for index, subgoal in enumerate(self.subGoalList):
			if subgoal.getId() == _sgid:
				return index
		return -1

	'''Effort Tracker Operations'''
	def addEffortTrack(self, _finishTime, _startTime):
		'''
        @param:

        @return:

        @purpose:
        '''
		self.effortTrackingData.append((_finishTime, _startTime)) #adds a tuple (finish time, start time) to the effort tracker

	'''To String Operations'''
	def toString(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		priority = None
		if self.priority == 3:
			priority = "Low"
		elif self.priority == 2:
			priority = "Medium"
		elif self.priority == 1:
			priority = "High"
		else:
			priority = "Error"

		status = None
		if self.isComplete():
			status = "Complete"
		else:
			status = "Incomplete"

		if self.hasDueDate():
			return "Name: " + self.name + " | Due Date: " + self.dueDate.strftime("%d %b %Y %H:%M") + " | Category: " + self.category + " | Priority: " + priority + " | Status: " + status
		else:
			return "Name: " + self.name + "| Category: " + self.category + " | Priority: " + priority + " | Status: " + status

	"""GETTERS FOR GOAL"""
	def getId(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.id #returns the Goal ID

	def getName(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.name #returns the Goal Name

	def getCategory(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.category #returns the Goal Category

	def getPriority(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.priority #returns the Goal Priority

	def getMemo(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.memo #returns the Goal Memo

	def getStartDate(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.startDate #returns the Goal Start Date

	def getDueDate(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.dueDate #returns the Goal Due Date

	def getInitialDueDate(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.initialDueDate #returns the Goal Initial Due Date

	def getFinishDate(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.finishDate #returns the Goal Finish Date

	def getEffortTrackingData(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return copy.deepcopy(self.effortTrackingData) #returns a copy of the Effort Tracker of the Goal

	def getSubGoalList(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return copy.deepcopy(self.subGoalList) #returns a copy of the Sub Goals of the Goal

	def getSortingMethod(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.sortingMethod

	"""SETTERS FOR GOAL"""
	def setSortingMethod(self, _sortingMethod):
		'''
        @param:

        @return:

        @purpose:
        '''
		self.sortingMethod = _sortingMethod

class SubGoal(object):
	"""CONSTRUCTORS FOR SUBGOAL"""
	def __init__(self, _id):
		'''
        @param:

        @return:

        @purpose:
        '''
		self.id = _id
		self.name = ""
		self.isCompleted = False

	"""METHODS FOR SUBGOAL"""
	def update(self, _subGoalInformation):
		'''
        @param:

        @return:

        @purpose:
        '''
		self.name = _subGoalInformation["name"]

	def complete(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		self.isCompleted = True

	def isComplete(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.isCompleted

	def toString(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		if self.isCompleted:
			return "Name: " + self.name + " | Status: Complete"
		else:
			return "Name: " + self.name + " | Status: Incomplete"

	"""GETTERS FOR SUBGOAL"""
	def getId(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.id

	def getName(self):
		'''
        @param:

        @return:

        @purpose:
        '''
		return self.name