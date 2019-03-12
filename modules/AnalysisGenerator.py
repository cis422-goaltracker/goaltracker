"""
    Authors: Kellie Hawks, Isaac Lance, Jiazhen Cao
        Date: 03/09/2019
    CIS 422
    GoalTracker
"""
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import calendar
import datetime
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

class AnalysisGenerator(object):
    """CONSTRUCTOR FOR ANALYSISGENERATOR"""
    def __init__(self, _gid, _model):
        '''
        @param: _goalid (integer)
        @param: _model(Model)

        @return: None

        @purpose: Initializes the AnalysisGenerator.
        '''
        self.gid = _gid         #Initializes the goal id
        self.model = _model     #Initializes the model

    """METHODS FOR ANALYSISGENERATOR"""
    def getActiveTime(self):
        '''
        @param: None

        @return: number (day period)

        @purpose: Calculate the time you spend
        '''
        goal = self.model.getGoal(self.gid) #gets the goal form the model
        if goal.isComplete(): #if goal is complete
            return (goal.getStartDate() - goal.getFinishDate()).seconds / 86400 #find the difference between finish and start date
            
        else:
            return (goal.getStartDate() - datetime.datetime.now()).seconds / 86400 #find the difference between the current date and start date

    def trackProgress(self):
        '''
        @param: None

        @return: (float)  

        @purpose: track how many subgoals you already finished 
        '''
        goal = self.model.getGoal(self.gid) #gets the goal from the model
        subgoallist = goal.getSubGoalList() #grabs the dictionary of subgoals
        subcompletedcount = 0           #starts a counter for completed subgoals
        for subgoal in subgoallist: #for every value in dictionary
            if subgoal.isComplete():    #if that value is true i.e. goal is completed
                subcompletedcount += 1  #increase goal count
        if len(subgoallist) == 0:
            return 0
        return subcompletedcount / len(subgoallist) #return number completed over number of subgoals


    def getFasterSlower(self):
        '''
        @param: None

        @return: (boolean) when the goal has no due date / (int) the number days from anticipated finish date

        @purpose: get days you work faster or slower than anticipated
        '''
        goal = self.model.getGoal(self.gid) #gets the goal from the model
        if goal.hasDueDate() == False:  #if the goal does not have a due date
            return False;  #return False
        else:
            if goal.isComplete():   #if goal is complete
                return ((goal.getInitialDueDate() - goal.getFinishDate()).seconds / 86400) #calculates the number of days from anticipated finish date


    def getAverageTime(self):
        '''
        @param: None

        @return: (float)

        @purpose: get the average time for each goal
        '''
        goal = self.model.getGoal(self.gid) #get goal from model
        effortTrackingData = goal.getEffortTrackingData() #get effort tracking data for that goal

        ret = {} #create a dictionary to add these values to

        for pair in effortTrackingData: #for the pair in efforttracking data
            fintime = pair[0] #get finish time
            starttime= pair[1] #get end time

            complete = fintime - starttime #find total amoutn of time
            date = fintime.date() #get the date

            if not (date in ret): #if the date does not exist in the return dictionary
                ret[date] = complete #add it
            else:
                ret[date] += complete #sum the timedeltas

        for date in ret.keys():
            #for the time delta values in the new dictionary made
            values = ret[date]

            seconds = values.total_seconds() #solve for how many hours

            hours = seconds // 3600 #more computation

            ret[date] = int(hours) #assign hours to new dictionary

        timesum = sum(ret.values()) #sum all the values (now as hours)

        if len(ret) == 0: #if the length of the return dictionary is zero
            return 0 #return zero because can't div by zero
        else:
            return timesum / len(ret) #return the average per day


    def getBeforeDuedate(self):
        '''
        @param: None

        @return: (float)

        @purpose: Get the percentage of goals completed before the duedate
        '''
        reschedulecount = 0 #creates counter for number of goals rescheduled
        completedcount = 0  #creates counter for completed goals
        
        goalList = self.model.getGoalList() #get goallist from model

        for goal in goalList:   #looks through goals in model
            if goal.hasDueDate():
                if goal.hasBeenRescheduled() and goal.isComplete(): #increments if a completed goal has been rescheduled
                    reschedulecount += 1
                if goal.isComplete(): #increments completed goal count
                    completedcount += 1
        completed_before_due = completedcount - reschedulecount #finds number of goals not reschedules
        if completedcount == 0:
            return 0
        else:
            return ((completed_before_due/completedcount) * 100) #calculates and returns percentage of goals done befoe duedate


    def getAfterDuedate(self):
        '''
        @param: None

        @return: (float)

        @purpose:  Get the percentage of goals completed after the initial duedate
        '''
        reschedulecount = 0 #creates counter for number of goals rescheduled
        completedcount = 0  #creates counter for completed goals
        
        goalList = self.model.getGoalList() #get goallist from model

        for goal in goalList:   #loops through goals in model
            if goal.hasDueDate():
                if goal.hasBeenRescheduled() and goal.isComplete(): #increments if completed goal has been rescheduled
                    reschedulecount += 1
                if goal.isComplete(): #increments completed goal count
                    completedcount += 1

        if completedcount == 0:
            return 0
        else:
            return ((reschedulecount/completedcount) * 100) #calculates and returns percentage of goals completed after inital duedate
        
    def tranformDatesList(self, test = False):
        '''
        @param: Boolean

        @return: (List)

        @purpose: transform efforttracking data to a date string list
        '''
        goal = self.model.getGoal(self.gid) #get goal from model
        effortTrackingData = goal.getEffortTrackingData() #get effort tracking data for that goal

        ret = {} #create a dictionary to add these values to
        if test:
            ret = {
            "3/8/2019" : 4,
            "3/9/2019" : 3,
            "3/10/2019" : 5,
            "3/11/2019" : 2,
            }
            dates = list(ret.values()) #make a list of values
            return dates
        for pair in effortTrackingData: #for the pair in efforttracking data
            fintime = pair[0] #get finish time
            starttime= pair[1] #get end time

            complete = fintime - starttime #find total amoutn of time
            date = str(fintime.date()) #get the data

            if not (date in ret): #if the date does not exist in the return dictionary
                ret[date] = complete #add it
            else:
                ret[date] += complete #sum the timedeltas
        ret = self.sortDict(ret)
        dates = list(ret.keys()) #make a list of date strings

        return dates

    def tranformValuesList(self, test = False):
        '''
        @param: Boolean

        @return: (list)

        @purpose: transform efforttracking data to a value list
        '''
        goal = self.model.getGoal(self.gid) #get goal from model
        effortTrackingData = goal.getEffortTrackingData() #get effort tracking data for that goal

        ret = {} #create a dictionary to add these values to
        if test:
            ret = {
            "3/8/2019" : 4,
            "3/9/2019" : 3,
            "3/10/2019" : 5,
            "3/11/2019" : 2,
            }
            values = list(ret.values()) #make a list of values
            return values
        for pair in effortTrackingData: #for the pair in efforttracking data
            fintime = pair[0] #get finish time
            starttime= pair[1] #get end time

            complete = fintime - starttime #find total amoutn of time
            date = fintime.date() #get the data

            if not (date in ret): #if the date does not exist in the return dictionary
                ret[date] = complete #add it
            else:
                ret[date] += complete #sum the timedeltas

        for date in ret.keys():
            #for values in ret[date]: #for the time delta values in the new dictionary made
            values = ret[date]
            
            seconds = values.total_seconds() #solve for how many hours
            
            hours = seconds / 3600 #more computation
        
            ret[date] = hours #assign hours to new dictionary

        ret = self.sortDict(ret)
        values = list(ret.values()) #make a list of values

        return values

    def sortDict(self, adict):
        '''
        @param: adict(dictionary)

        @return: (dictionary)

        @purpose: sort dictionary
        '''
        temp = sorted(adict.items()) #sort items in ascending order
        ret = {}  #new dictionary
        for tup in temp: #for item in sorted dictionary
            ret[tup[0]] = tup[1] #assign value
        return ret   #return sorted dictionary


