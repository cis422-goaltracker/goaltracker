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
<<<<<<< HEAD
    """CONSTRUCTOR FOR ANALYSISGENERATOR"""
    def __init__(self, _gid, _model):
        self.gid = _gid
        self.model = _model

    def getActiveTime(self):
        goal = self.model.getGoal(self.gid) #gets the goal form the model
        if goal.isComplete(): #if goal is complete
            return str((goal.getFinishDate() - goal.getStartDate()).seconds // 86400) #find the difference between finish and start date
            
        else:
            return str((datetime.datetime.now() - goal.getStartDate()).seconds // 86400) #find the difference between the current date and start date

    def trackProgress(self):
        
        goal = self.model.getGoal(self.gid) #gets the goal from the model
        subgoallist = goal.getSubGoalList() #grabs the dictionary of subgoals
        subcompletedcount = 0           #starts a counter for completed subgoals
        for subgoal in subgoallist: #for every value in dictionary
            if subgoal.isComplete():    #if that value is true i.e. goal is completed
                subcompletedcount += 1  #increase goal count
        if len(subgoallist) == 0:
            return 0
        return subcompletedcount/ len(subgoallist) #return number completed over number of subgoals


    def getFasterSlower(self):
        
        goal = self.model.getGoal(self.gid) #gets the goal from the model
        if goal.hasDueDate() == False:  #if the goal does not have a due date #???? Does this function exist ????
            return -10000;  #return -10000 (a number that is almost possible to achieve in normal day to day use)
        else:
            if goal.isComplete():   #if goal is complete
                return ((goal.getInitialDueDate() - goal.getFinishDate()).seconds // 86400) #calculates the number of days from anticipated finish date


    def getAverageTime(self):
        
        goal = self.model.getGoal(self.gid) #get goal from model
        effortTrackingData = goal.getEffortTrackingData() #get effort tracking data for that goal

        ret = {} #create a dictionary to add these values to

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
            #for the time delta values in the new dictionary made
            values = ret[date]

            seconds = values.total_seconds() #solve for how many hours

            hours = seconds // 86400 #more computation

            ret[date] = int(hours) #assign hours to new dictionary

        timesum = sum(ret.values()) #sum all the values (now as hours)

        if len(ret) == 0: #if the length of the return dictionary is zero
            return str(0) #return zero because can't div by zero
        else:
            return str(timesum/ len(ret)) #return the average per day


    def getBeforeDuedate(self):
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
            
            hours = seconds / 86400 #more computation
        
            ret[date] = hours #assign hours to new dictionary

        ret = self.sortDict(ret)
        values = list(ret.values()) #make a list of values

        return values

    def sortDict(self, adict):
        temp = sorted(adict.items())
        ret = {}
        for tup in temp:
            ret[tup[0]] = tup[1]
        return ret