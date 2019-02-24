"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal
from SubGoal import SubGoal as SubGoal
from Status import Status as Status

class FileManager(object):
	"""CONSTRUCTOR FOR FILEMANAGER"""
	def __init__(self, _fileName):
		self.fileName = _fileName
		
	"""METHODS FOR FILEMANAGER"""
	'''Load Operations'''
	def load(self, _fileName=None):
		_fileName = self.fileName if _fileName == None else _fileName
		#open file

		#read file

		#parse file

		#create list of Goal objects / refer to hints in the save function on how to parse

		#get currGID and currSGID / refer to hints in the save function on how to parse

		#get Effort Tracking Data / refer to hints in the save function on how to parse

		#close file

		#return list of Goal objects, currGID, currSGID, EffortTrackingData, and IO STATUS
		#if IO STATUS (FileNotFound), do not crash, must create defaults of all data
		pass

	'''Save Operations'''
	def save(self, _goalList, _currGID, _currSGID, effortTrackingData, _fileName=None): 
		_fileName = self.fileName if _fileName == None else _fileName #defaults to original file name unless a new one is specified
		
		#look at Goal object to understand what a goal is composed of

		#please keep these two as abstract as possible when working with them as
		#we are not sure the data type of it yet.
		#_currGID is going to be a single element (string, number, not sure yet)
		#_currSGID is also going to be a single element (string, number, not sure yet)

		#_effortTrackingData is a dictionary with elements <key: GoalID, value: startTime (likely will be DateTime Object>
		#will need to convert from DateTime object to string when saving

		#open file

		#parse goalList, create into JSON like data

		#write to file goal information, currGID and currSGID

		#close file

		#return IO STATUS
		pass

	"""GETTERS FOR FILEMANAGER"""
	def getFileName(self):
		return self.fileName #return the file name

	"""SETTERS FOR FILEMANAGER"""
