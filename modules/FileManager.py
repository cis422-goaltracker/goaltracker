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

		#create list of Goal objects

		#get currGID and currSGID

		#get Effort Tracking Data

		#close file

		#return list of Goal objects, currGID, currSGID, EffortTrackingData, and IO STATUS
		pass

	'''Save Operations'''
	def save(self, _goalList, _currGID, _currSGID, effortTrackingData, _fileName=None): 
		_fileName = self.fileName if _fileName == None else _fileName #defaults to original file name unless a new one is specified
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
