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
	def startEffortTracker(self, _gid, _model, _startTime):
		trackingDict = _model.getTrackingData() #gets the tracking data from the model
		trackingDict[_gid] = _startTime #create key-value pair <_gid, _startTime> and add to tracking dictionary
		_model.setTrackingData(trackingDict) #sets the updated tracking data in the model
		return _model #returns the model

	def isEffortTracking(self, _gid, _model):
		trackingDict = _model.getTrackingData() #gets the tracking data from the model
		return _gid in trackingDict #check if _gid is in the tracking dictionary by checking id, true if it is, false if it isn't

	def stopEffortTracker(self, _gid, _model, _finishTime):
		trackingDict = _model.getTrackingData() #gets the tracking data from the model
		goal = _model.getGoal(_gid) #gets the goal from the model using goal id
		startTime = trackingDict.pop(_gid) #remove <_gid, starttime> pair from tracking dictionary, and stores startTime
		elapsedTime = _finishTime - startTime #calculates elapsed time as difference between finish and start time
		goal.addEffortTrack(_finishTime, elapsedTime) #adds an effort track to the goal
		_model.setGoal(goal) #sets the updated goal in the model
		return _model #returns model

	"""GETTERS FOR EFFORTTRACKER"""

	"""SETTERS FOR EFFORTTRACKER"""
