"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal
from SubGoal import SubGoal as SubGoal
from Status import Status as Status
from Model import Model as Model
import shelve

class FileManager(object):
	"""CONSTRUCTOR FOR FILEMANAGER"""
	def __init__(self):
		pass
		
	"""METHODS FOR FILEMANAGER"""
	'''Load Operations'''
	def load(self, _fileName): #FUNCTION NEEDS TO BE BUILT
		self.fileName = _fileName
		#open file
		try:
			db = shelve.open(self.fileName)

			#create list of Goal objects / refer to hints in the save function on how to parse
			goalList = db['goalList']
			#get currGID and currSGID / refer to hints in the save function on how to parse
			currGID = db['currGID']
			currSGID = db['currSGID']
			#get Effort Tracking Data / refer to hints in the save function on how to parse
			effortTrackingData = db['effortTrackingData']
			#close file
			db.close()
			#create a Model object which contains
			#a list of Goal objects, currGID, currSGID, EffortTrackingData
			model = Model(goalList, currGID, currSGID, effortTrackingData)

			#return Model and IO Status

		except:
			model = Model([], 0, 0, {})

		#if IO STATUS (FileNotFound), do not crash, must create defaults of all data
		return model

	'''Save Operations'''
	def save(self, _model, _fileName=None): #FUNCTION NEEDS TO BE BUILT

		_fileName = self.fileName if _fileName == None else _fileName #defaults to original file name unless a new one is specified
		try:
			goalList = _model.getGoalList()
			currGID = _model.getCurrGID()
			currSGID = _model.getCurrSGID()
			effortTrackingData = _model.getEffortTrackingData()

			#the following 4 objects are contained within _model. read Model object to learn how a Model is built
			#look at Goal object to understand what a goal is composed of

			#please keep these two as abstract as possible when working with them as
			#we are not sure the data type of it yet.
			#_currGID is going to be a single element (string, number, not sure yet)
			#_currSGID is also going to be a single element (string, number, not sure yet)

			#_effortTrackingData is a dictionary with elements <key: GoalID, value: startTime (likely will be DateTime Object>
			#will need to convert from DateTime object to string when saving

			#open file
			db = shelve.open(_fileName)

			#parse goalList, create into JSON like data

			#write to file goal information, currGID and currSGID
			db['goalList'] = goalList
			db['currGID'] = currGID
			db['currSGID'] = currSGID
			db['effortTrackingData'] = effortTrackingData

			#close file
			db.close()
			return 0
		except:
			#return IO STATUS
			return 1

	"""GETTERS FOR FILEMANAGER"""
	def getFileName(self):
		return self.fileName #return the file name

	"""SETTERS FOR FILEMANAGER"""
