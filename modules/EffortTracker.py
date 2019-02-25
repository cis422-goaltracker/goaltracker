"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal
from Model import Model as Model

class EffortTracker(object):
	"""CONSTRUCTOR FOR EFFORTTRACKER"""
	def __init__(self):
		pass

	"""METHODS FOR EFFORTTRACKER"""
	def startEffortTracker(self, _gid, _model, _startTime): #FUNCTION NEEDS TO BE BUILT
		trackingDict = _model.getTrackingData() #gets the tracking data from the model
		#create key-value pair <_gid, _startTime>

		#add pair to the tracking dictionary

		_model.setTrackingData(trackingDict) #sets the updated tracking data in the model
		return _model #returns the model

	def isEffortTracking(self, _gid, _model): #FUNCTION NEEDS TO BE BUILT
		trackingDict = _model.getTrackingData() #gets the tracking data from the model
		#check if _goal is in the tracking dictionary by checking id, true if it is, false if it isn't

	def stopEffortTracker(self, _gid, _model, _finishTime): #FUNCTION NEEDS TO BE BUILT
		trackingDict = _model.getTrackingData() #gets the tracking data from the model
		goal = _model.getGoal(_gid) #gets the goal from the model using goal id
		

		date = None #find date of _finishTime (DateTime object)
		elapsedTime = None  #find elapsed time between finish and start time
		
		#pops the pair with the _goal as the key out of tracking dictionary

		#finds the elapsed time between _finishTime and _startTime

		#creates new entry in _goal's effort tracker with <date, elapsed time>
		#if date already exists, add new elapsed time to old time

		goal.addEffortTrack(date, elapsedTime) #adds an effort track to the goal
		_model.setGoal(goal) #sets the updated goal in the model
		return _model #returns model

	"""GETTERS FOR EFFORTTRACKER"""

	"""SETTERS FOR EFFORTTRACKER"""
