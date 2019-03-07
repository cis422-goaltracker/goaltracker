"""
	Names Kellie Hawks 
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

#For Kellie to work on
#need to pip install pyqtgraph

class AnalysisGenerator(object):
	"""CONSTRUCTOR FOR ANALYSISGENERATOR"""
	def __init__(self):
		pass

	def getActiveTime(self, _gid, _model):
		goal = _model.getGoal(_gid) #gets the goal form the model
		if goal.isComplete(): #if goal is complete

			return str((goal.getFinishDate() - goal.getStartDate()).seconds // 86400) #find the difference between finish and start date
			
		else:
			return str((datetime.datetime.now() - goal.getStartDate()).seconds // 86400) #find the difference between the current date and start date

	def trackProgress(self, _gid, _model):
		goal = _model.getGoal(_gid) #gets the goal from the model
		subgoallist = goal.getSubGoalList(_gid)	#grabs the dictionary of subgoals
		subcompletedcount = 0			#starts a counter for completed subgoals
		for subgoal in subgoallist:	#for every value in dictionary
			if subgoal.isComplete():	#if that value is true i.e. goal is completed
				subcompletedcount += 1	#increase goal count
		return subcompletedcount/ len(subgoallist) #return number completed over number of subgoals


	def getFasterSlower(self, _gid, _model):
		goal = _model.getGoal(_gid)	#gets the goal from the model
		if goal.hasDueDate() == False:	#if the goal does not have a due date #???? Does this function exist ????
			return -10000;	#return -10000 (a number that is almost possible to achieve in normal day to day use)
		else:
			if goal.isComplete(): 	#if goal is complete
				return str((goal.getInitialDueDate() - goal.getFinishDate()).seconds // 86400) #calculates the number of days from anticipated finish date


	def getAverageTime(self, _gid, _model):
		goal = _model.getGoal(_gid)
		effortTrackingData = goal.getEffortTrackingData()

		ret = {}

		for pair in effortTrackingData:
			fintime = pair[0]
			starttime= pair[1]

			complete = fintime - starttime
			date = fintime.date()

			if not (date in ret):
				ret[date] = complete
			else:
				ret[date] += complete

		for values in ret.keys(): #for the time delta values in the new dictionary made

			seconds = values.total_seconds() #solve for how many hours
			hours = seconds // 86400 #more computation

		timesum = sum(ret.values()) #sum all the values (now as hours)

		if len(ret) == 0:
			return str(0)
		else:
			return str(timesum/ len(ret)) #return the average per day


	def getBeforeDuedate(self, _model):
		reschedulecount = 0	#creates counter for number of goals rescheduled
		completedcount = 0 	#creates counter for completed goals
		
		goalList = _model.getGoalList()

		for goal in goalList:	#looks through goals in model
			if goal.hasDueDate():
				if goal.hasBeenRescheduled() and goal.isComplete(): #increments if a completed goal has been rescheduled
					reschedulecount += 1
				if goal.isComplete(): #increments completed goal count
					completedcount += 1
		completed_before_due = completedcount - reschedulecount #finds number of goals not reschedules
		return str(completed_before_due/completedcount) #calculates and returns percentage of goals done befoe duedate


	def getAfterDuedate(self, _model):
		#should this be changed? it originally relied on having a due date fro every goal. now the stats 
		#aren't as accurate. should i just be looking at the goals that DID have a due date attached to them?

		reschedulecount = 0 #creates counter for number of goals rescheduled
		completedcount = 0 	#creates counter for completed goals
		
		goalList = _model.getGoalList()

		for goal in goalList:	#loops through goals in model
			if goal.hasDueDate():
				if goal.hasBeenRescheduled() and goal.isComplete(): #increments if completed goal has been rescheduled
					reschedulecount += 1
				if goal.isComplete(): #increments completed goal count
					completedcount += 1

		return str(reschedulecount/completedcount) #calculates and returns percentage of goals completed after inital duedate
		
	#jiazhen looking into this
	def tranformDatesList(self, _model):
		ret = {} #creates a dictionary to return
		for dt in dict.keys(): #loops through keys in dictionarya
			if not (dt.date() in ret): #if date is not in return dictioary
					ret[dt.date()] = dict[dt] #add timedelta if does not exist
			else:
				ret[dt.date()] += dict[dt] #add timedelta if date already exists
		
		for key in ret.keys(): #for every key in the dictionary
			datetime.strftime(key,'%b %d, %Y') #turn it into a string
		
		dates = list(ret.keys()) #make a list of date strings

		return dates

	def tranformValuesList(self, _model):
		ret = {} #creates a dictionary to return
		for dt in dict.keys(): #loops through keys in dictionarya
			if not (dt.date() in ret): #if date is not in return dictioary
					ret[dt.date()] = dict[dt] #add timedelta if does not exist
			else:
				returnet[dt.date()] += dict[dt] #add timedelta if date already exists
		
		for values in ret.keys(): #for the time delta values in the new dictionary made
			seconds = values.total_seconds() #solve for how many hours
			hours = seconds // 3600 #more computation
			
			ret[values] = hours #assign hours to new dictionary ???? What is the right way to assign this ???? 

		values = list(ret.values()) #make a list of values

		return values

	
	"""METHODS FOR ANALYSISGENERATOR"""


	"""GETTERS FOR ANALYSISGENERATOR"""


	"""SETTERS FOR ANALYSISGENERATOR"""
