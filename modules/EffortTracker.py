"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal

class EffortTracker(object):
	"""CONSTRUCTOR FOR EFFORTTRACKER"""
	def __init__(self):
		self.trackingData = {} #dictionary to track effort on different goals

	"""METHODS FOR EFFORTTRACKER"""
	def startEffortTracker(self, _goal, _startTime):
		#create key-value pair <_goal, _startTime>

		#add pair to the tracking data
		pass

	def isEffortTracking(self, _goal):
		#check if _goal is in the map by checking id, true if it is, false if it isn't
		pass

	def stopEffortTracker(self, _goal, _finishTime):
		#pops the pair with the _goal as the key out of trackingData

		#finds the elapsed time between _finishTime and _startTime

		#creates new entry in _goal's effort tracker with <date, elapsed time>
		#if date already exists, add new elapsed time to old time

		#return _goal
		pass

	"""GETTERS FOR EFFORTTRACKER"""
	def getTrackingData(self):
		return self.trackingData.copy() #returns a copy of the tracking data

	"""SETTERS FOR EFFORTTRACKER"""
