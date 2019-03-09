"""
	Authors: Noah Palmer, Holly Hardin
	Date: 03/09/2019
	CIS 422
	GoalTracker
"""
#System Imports
from datetime import datetime, timedelta
import copy

#Module Imports
from Goal import Goal, SubGoal

class Model(object):
	"""CONSTRUCTOR FOR MODEL"""
	def __init__(self, _goalList, _currGID, _currSGID, _effortTracker):
		'''
		@param: _goalList (list)
		@param: _currGID (integer)
		@param: _currSGID (integer)
		@param: _effortTracker (dictionary)

		@return: None

		@purpose: Initialize the model by setting the list of goals, the current goal ID,
                          the current subgoal ID, and the effort tracker.
		'''
		self.goalList = _goalList #list of goal objects
		self.currGID = _currGID #integer
		self.currSGID = _currSGID #integer
		self.effortTracker = _effortTracker #dictionary goalid-starttime pairs

	"""METHODS FOR MODEL"""
	'''********************GOALLIST OPERATIONS********************'''
	def getCompletedGoalList(self):
		'''
		@param: None

		@return: (list) - goals that are completed.

		@purpose: This function filters the goalList leaving only Goals that have been completed.
		It then returns the filtered list.
		'''
		return [goal for goal in self.goalList if goal.isComplete()] #retruns a list of completed goals

	def getCurrentGoalList(self):
		'''
		@param: None

		@return: (list) - goals that are current (not completed - may be overdue).

		@purpose: This function filters the goalList leaving only Goals that have not been completed.
		It then returns the filtered list.
		'''
		return [goal for goal in self.goalList if not goal.isComplete()] #returns a list of not completed goals

	def getOverDueGoalList(self):
		'''
		@param: None

		@return: (List) - goals that are overdue.

		@purpose: This function filters the goalList leaving only Goals that are over due.
		It then returns the filtered list.
		'''
		return [goal for goal in self.goalList if goal.isOverDue() and not goal.isComplete()] #returns of a list of over due and not completed goals

	def getGoalList(self):
		'''
		@param: None

		@return (List) - goals

		@purpose: This function makes a copy of the goalList. It then returns the copied list.
		'''
		return copy.deepcopy(self.goalList) #returns a copy of the Goal List

	'''********************GOAL OPERATIONS********************'''
	def addGoal(self):
		'''
		@param: None

		@return: None

		@purpose: Creates a Goal object and then appends it to the goalList
		'''
		newGID = self.getNewGID() #gets a new id
		self.goalList.append(Goal(newGID)) #appends a new goal with the new id to the goallist
		return newGID #returns the new gid

	def editGoal(self, _gid, _goalInformation):
		'''
		@param: _gid (integer)
		@param: _goalInformation (dictionary) - a dictionary containing a "name" (string), 
		a "category" (string), a "priority" (integer), a "memo" (string), and a "dueDate" (DateTime)

		@return: None

		@purpose: updates the goal of the given goal id with the goal information passed
		'''
		self.goalList[self.getIndex(_gid)].update(_goalInformation) #updates goal with the goal information

	def completeGoal(self, _gid, _finishDate = datetime.now()):
		'''
		@param: _gid (integer)
		@param: _finishDate (datetime) - defaults to current time

		@return: None

		@purpose: sets the goal of the given id to completed status
		'''
		self.goalList[self.getIndex(_gid)].complete(_finishDate) #sets goal to complete

	def deleteGoal(self, _gid):
		'''
		@param: _gid (integer)

		@return: None

		@purpose: Deletes a goal of the given goal id from the goal list.
		'''
		self.goalList.pop(self.getIndex(_gid)) #delete goal from goal list

	def getGoal(self, _gid):
		'''
		@param: _gid (integer)

		@return: (Goal)

		@purpose: Gets a goal of given goal id from the goal list.
		'''
		return self.goalList[self.getIndex(_gid)] #returns goal from goal list

	'''********************SUBGOALLIST OPERATIONS********************'''
	def getSubGoalList(self, _gid):
		'''
		@param: _gid (integer)

		@return: None

		@purpose: Gets the subgoal list of the given goal id. 
		'''
		return self.goalList[self.getIndex(_gid)].getSubGoalList() #returns subgoal list

	'''********************SUBGOAL OPERATIONS********************'''
	def addSubGoal(self, _gid):
		'''
		@param: _gid (integer)

		@return: None

		@purpose: Adds a new subgoal to the subgoallist of the given goal id.
		'''
		newSGID = self.getNewSGID() #gets a new subgoal id
		self.goalList[self.getIndex(_gid)].addSubGoal(newSGID) #creates new subgoal and adds to subgoal list
		return newSGID #returns new subgoal id

	def editSubGoal(self, _gid, _sgid, _subGoalInformation):
		'''
		@param: _gid (integer)
		@param: _sgid (integer)
		@param: _subGoalInformation (dictionary)

		@return: None

		@purpose: Edit a subgoalgoal from the subgoallist.
		'''
		self.goalList[self.getIndex(_gid)].updateSubGoal(_sgid, _subGoalInformation) #updates subgoal with subgoal information

	def completeSubGoal(self, _gid, _sgid):
		'''
		@param: _gid (integer)
		@param: _sgid (integer)

		@return: None

		@purpose: Complete a subgoal from the list.
		'''
		self.goalList[self.getIndex(_gid)].completeSubGoal(_sgid) #completes subgoal

	def deleteSubGoal(self, _gid, _sgid):
		'''
		@param: _gid (integer)
		@param: _sgid (integer)

		@return: None

		@purpose: Deletes a subgoal from the list.
		'''
		self.goalList[self.getIndex(_gid)].deleteSubGoal(_sgid) #deletes subgoal

	def getSubGoal(self, _gid, _sgid):
		'''
		@param: _gid (integer)
		@param: _sgid (integer)

		@return: None

		@purpose: Gets a subgoal from the list.
		'''
		return self.goalList[self.getIndex(_gid)].getSubGoal(_sgid) #retrieves subgoal

	'''********************EFFORT TRACKER OPERATIONS********************'''
	def startEffortTracker(self, _gid):
		'''
		@param: _gid (integer)

		@return: None

		@purpose: Starts a timer to keep track of how much time - or effort - a user puts in to accomplishing a goal.
		'''
		self.effortTracker[_gid] = datetime.now() #starts the effort tracker

	def isEffortTracking(self, _gid):
		'''
		@param: _gid (integer)

		@return: (boolean)

		@purpose: Returns the goal's ID whose timer is going.
		'''
		return _gid in self.effortTracker #checks if a specific goal is still tracking

	def stopEffortTracker(self, _gid):
		'''
		@param: _gid (integer)

		@return: None

		@purpose: Stops the timer that is keeping track of how much time
                          - or effort - a user puts in to accomplishing a goal.
		'''
		self.goalList[self.getIndex(_gid)].addEffortTrack(datetime.now(), self.effortTracker.pop(_gid)) #stops the goal tracker

	def manuallyInputEffort(self, _gid, _startTime, _finishTime):
		'''
		@param: _gid (integer)
		@param: _startTime (datetime)
		@param: _finishTime (datetime)

		@return: None

		@purpose: This method takes the _gid to find the goal in the goal list, then it adds an
		effort track to the goal with _startTime and _finishTime
		'''
		self.goalList[self.getIndex(_gid)].addEffortTrack(_finishTime, _startTime) #allows a user to manually input data

	def getEffortTracker(self):
		'''
		@param: None

		@return: (dictionary) - list of times the user has put into accomplishing a goal.

		@purpose: This method returns a copy of the effort tracking data
		'''
		return copy.deepcopy(self.effortTracker) #returns the a copy of the effort tracking data

	'''********************GID AND SGID OPERATIONS********************'''
	def getNewGID(self):
		'''
		@param: None

		@return: (integer) - goal ID

		@purpose: This method generates a new goal id and then returns it
		'''
		self.currGID = self.currGID + 1 #increments current goal id
		return self.currGID #returns current goal id

	def getNewSGID(self):
		'''
		@param: None

		@return: (integer) - subgoal ID

		@purpose: This method generates a new subgoal id and then returns it
		'''
		self.currSGID = self.currSGID + 1 # increments current subgoal id
		return self.currSGID #returns current subgoal id

	def getCurrGID(self):
		'''
		@param: None 

		@return: (integer) - current goal ID

		@purpose: Gets the current goal's ID.
		'''
		return self.currGID #returns current goal id

	def getCurrSGID(self):
		'''
		@param: None

		@return: (integer) - current subgoal ID

		@purpose: Gets the current subgoal's ID.
		'''
		return self.currSGID #returns current subgoal id

	'''********************SORT OPERATIONS********************'''
	def categorySort(self):
		'''
		@param: None

		@return: None

		@purpose: This method sets the goal list to be sorted by the category attribute
		'''
		for index, goal in enumerate(self.goalList): #cycles through goal list
			self.goalList[index].setSortingMethod("category") #sets the sorting method of all goals to category
		self.goalList = sorted(self.getGoalList()) #sets goallist to the sorted version of goallist

	def prioritySort(self):
		'''
		@param: None

		@return: None

		@purpose: This method sets the goal list to be sorted by the priority attribute
		'''
		for index, goal in enumerate(self.goalList): #cycles through goal list
			self.goalList[index].setSortingMethod("priority") #sets the sorting method of all goals to priority
		self.goalList = sorted(self.getGoalList()) #sets goallist to the sorted version of goallist

	'''********************MISCELLANEOUS OPERATIONS********************'''
	def getIndex(self, _gid):
		'''
		@param: _gid (integer)

		@return: (integer) - an index of the goal in the list.

		@purpose: Gets the index of the goal's index in the list.
		'''
		for index, goal in enumerate(self.goalList): #cycles trough goallist
			if goal.getId() == _gid: #if goal id matches passed goalid
				return index #return the index
		return -1 #return erroring -1
		
