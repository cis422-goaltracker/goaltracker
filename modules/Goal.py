"""
    Authors: Noah Palmer, Isaac Lance
    Date: 03/10/2019
    CIS 422
    GoalTracker
"""
#System Imports
from datetime import datetime, timedelta
import copy
from GErrors import FlagError

class Goal(object):
    """CONSTRUCTORS FOR GOAL"""
    def __init__(self, _id):
        '''
        @param: _id (integer)

        @return: None

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
        @param: other (Goal)

        @return: (boolean)

        @purpose: Override less than, aka "<", so self<right_goal
        '''
        if self.sortingMethod == "category": #if the sorting method is category
            return (self.category.lower() < other.category.lower()) #sort by category
        if self.sortingMethod == "priority": #if the sorting method is priority
            return (self.priority < other.priority) #sort by priority
        raise FlagError("sorting_method", "category, priority", self.sortingMethod)

    """METHODS FOR GOAL"""
    '''Goal Operations'''
    def hasDueDate(self):
        '''
        @param: None

        @return: (boolean)

        @purpose: returns if the goal has a duedate
        '''
        return self.dueDate != None #if due date doesn't equal none, then returns true, otherwise false

    def hasBeenRescheduled(self):
        '''
        @param: None

        @return: (boolean)

        @purpose: returns if the goal has been rescheduled
        '''
        if self.hasDueDate(): #if has a duedate
            return self.dueDate != self.initialDueDate #if due date and initial due date are same, return false, otherwise true
        else:
            return None #otherwise returns none

    def update(self, _goalInformation):
        '''
        @param: _goalInformation (Dictionary)

        @return: None

        @purpose: updates the goal to contain the new goal information
        '''
        self.name = _goalInformation["name"] #sets the name to the passed name
        self.category = _goalInformation["category"] #sets the category to the passed category
        self.priority = _goalInformation["priority"] #sets the priority to the passed priority
        self.memo = _goalInformation["memo"] #sets the memo to the passed memo
        if not self.hasDueDate() and self.initialDueDate == None: #if has a duedate and intial due date doesn't equal none
            self.initialDueDate = _goalInformation["dueDate"] #sets initial due date to the duedate (can only be set once per goal)
        self.dueDate = _goalInformation["dueDate"] #sets the duedate to the passed due date

    def complete(self, _finishDate):
        '''
        @param: _finishDate (DateTime)

        @return: None

        @purpose: completes the goal and completes the subgoals contained within the goal
        '''
        self.finishDate = _finishDate #sets the finish date to the passed finish date
        for index, subgoal in enumerate(self.subGoalList): #cycles through the subgoal list
            self.subGoalList[index].complete() #completes each subgoal

    def isComplete(self):
        '''
        @param: None

        @return: (boolean)

        @purpose: returns if the goal has been completed
        '''
        return self.finishDate != None #if finish date is not null, it is complete

    def isOverDue(self):
        '''
        @param: None

        @return: (boolean)

        @purpose: returns if the goal is overdue
        '''
        if self.hasDueDate(): #if goal has a due date
            return self.dueDate < datetime.now() #if current date is greater than due date, its overdue
        else:
            return False  #otherwise returns false

    '''Subgoal Operations'''
    def addSubGoal(self, _sgid):
        '''
        @param: _sgid (integer)

        @return: None

        @purpose: adds a new subgoal to the subgoal list
        '''
        self.subGoalList.append(SubGoal(_sgid)) #appends a new subgoal to the subgoal list

    def updateSubGoal(self, _sgid, _subGoalInformation):
        '''
        @param: _sgid (integer)
        @param: _subGoalInformation (Dictionary)

        @return: None

        @purpose: updates a subgoal with the subgoal information
        '''
        self.subGoalList[self.getIndex(_sgid)].update(_subGoalInformation) #updates subgoal with subgoal information

    def completeSubGoal(self, _sgid):
        '''
        @param: _sgid (integer)

        @return: None

        @purpose: #completes a subgoal
        '''
        self.subGoalList[self.getIndex(_sgid)].complete() #completes subgoal

    def deleteSubGoal(self, _sgid):
        '''
        @param: _sgid (integer)

        @return: None

        @purpose: deletes a subgoal
        '''
        self.subGoalList.pop(self.getIndex(_sgid)) #deletes subgoal

    def getSubGoal(self, _sgid):
        '''
        @param: _sgid (integer)

        @return: (SubGoal)

        @purpose: #gets a subgoal
        '''
        return self.subGoalList[self.getIndex(_sgid)] #returns a subgoal

    def getIndex(self, _sgid):
        '''
        @param: _sgid (integer)

        @return: (integer)

        @purpose: #gets the index of a subgoal id
        '''
        for index, subgoal in enumerate(self.subGoalList): #cycles through subgoal list
            if subgoal.getId() == _sgid: #if subgoal id matches the passed subgoal id
                return index #return the index
        return -1 #return error code -1

    '''Effort Tracker Operations'''
    def addEffortTrack(self, _finishTime, _startTime):
        '''
        @param: _finishTime (DateTime)
        @param: _startTime (DateTime)

        @return: None

        @purpose: appends a tuple to the effort tracking data of a start time and finish time
        '''
        self.effortTrackingData.append((_finishTime, _startTime)) #adds a tuple (finish time, start time) to the effort tracker

    '''To String Operations'''
    def toString(self):
        '''
        @param: None

        @return: (string)

        @purpose: builds the string for a goal
        '''
        priority = None #priority defaults to none
        if self.priority == 3: #if priority is 3
            priority = "Low" #sets phrase to low
        elif self.priority == 2: #if priority is 2
            priority = "Medium" #sets phrase to medium
        elif self.priority == 1: #if priority is 1
            priority = "High" #sets phrase to high
        else:
            priority = "Error" #else, sets to error

        status = None #status defaults to none
        if self.isComplete(): #if goal is complete
            status = "Complete" #status is complete
        else:
            status = "Incomplete" #else, status is incomplete

        if self.hasDueDate(): #if goal has a duedate
            return "Name: " + self.name + " | Due Date: " + self.dueDate.strftime("%d %b %Y %H:%M") + " | Category: " + self.category + " | Priority: " + priority + " | Status: " + status #prints with duedate
        else:
            return "Name: " + self.name + "| Category: " + self.category + " | Priority: " + priority + " | Status: " + status #prints without due date

    """GETTERS FOR GOAL"""
    def getId(self):
        '''
        @param: None

        @return: (integer)

        @purpose: returns goal id
        '''
        return self.id #returns the Goal ID

    def getName(self):
        '''
        @param: None

        @return: (string)

        @purpose: returns goal name
        '''
        return self.name #returns the Goal Name

    def getCategory(self):
        '''
        @param: None

        @return: (string)

        @purpose: returns goal category
        '''
        return self.category #returns the Goal Category

    def getPriority(self):
        '''
        @param: None

        @return: (integer)

        @purpose: returns goal priority
        '''
        return self.priority #returns the Goal Priority

    def getMemo(self):
        '''
        @param: None

        @return: (string)

        @purpose: returns goal memo
        '''
        return self.memo #returns the Goal Memo

    def getStartDate(self):
        '''
        @param: None

        @return: (DateTime)

        @purpose: returns goal start date
        '''
        return self.startDate #returns the Goal Start Date

    def getDueDate(self):
        '''
        @param: None

        @return: (DateTime)

        @purpose: returns goal due date
        '''
        return self.dueDate #returns the Goal Due Date

    def getInitialDueDate(self):
        '''
        @param: None

        @return: (DateTime)

        @purpose: returns goal initial due date
        '''
        return self.initialDueDate #returns the Goal Initial Due Date

    def getFinishDate(self):
        '''
        @param: None

        @return: (DateTime)

        @purpose: returns goal finish date
        '''
        return self.finishDate #returns the Goal Finish Date

    def getEffortTrackingData(self):
        '''
        @param: None

        @return: (List)

        @purpose: returns goal tracking data
        '''
        return copy.deepcopy(self.effortTrackingData) #returns a copy of the Effort Tracker of the Goal

    def getSubGoalList(self):
        '''
        @param: None

        @return: (List)

        @purpose: returns subgoal list
        '''
        return copy.deepcopy(self.subGoalList) #returns a copy of the Sub Goals of the Goal

    def getSortingMethod(self):
        '''
        @param: None

        @return: (string)

        @purpose: returns the goal sorting method
        '''
        return self.sortingMethod #returns goal sorting method

    """SETTERS FOR GOAL"""
    def setSortingMethod(self, _sortingMethod):
        '''
        @param:_sortingMethod (string)

        @return: None

        @purpose: sets the sorting method of the goal
        '''
        self.sortingMethod = _sortingMethod #sets the sorting method of the goal

class SubGoal(object):
    """CONSTRUCTORS FOR SUBGOAL"""
    def __init__(self, _id):
        '''
        @param: _id (integer)

        @return: None

        @purpose: initializes a subgoal
        '''
        self.id = _id #sets the subgoal id
        self.name = "" #defaults the name to blank
        self.isCompleted = False #defaults completed status false

    """METHODS FOR SUBGOAL"""
    def update(self, _subGoalInformation):
        '''
        @param: _subGoalInformation (Dictionary) containing a "name" (string)

        @return: None

        @purpose: updates the subgoal with the passed information
        '''
        self.name = _subGoalInformation["name"]

    def complete(self):
        '''
        @param: None

        @return: None

        @purpose: sets the completed status to true
        '''
        self.isCompleted = True #sets the completed status to true

    def isComplete(self):
        '''
        @param: None

        @return: (boolean)

        @purpose: #returns true if subgoal is complete
        '''
        return self.isCompleted #returns true if subgoal is complete

    def toString(self):
        '''
        @param: None

        @return: (string)

        @purpose: creates a string of goal information
        '''
        if self.isCompleted: #if subgoal is complete
            return "Name: " + self.name + " | Status: Complete" #creates a string with status complete
        else:
            return "Name: " + self.name + " | Status: Incomplete" #otherwise, creates a string with status incomplete

    """GETTERS FOR SUBGOAL"""
    def getId(self):
        '''
        @param: None

        @return: (integer)

        @purpose: returns subgoal id
        '''
        return self.id #returns subgoal id

    def getName(self):
        '''
        @param: None

        @return: (string)

        @purpose: returns subgoal name
        '''
        return self.name #returns subgoal name
