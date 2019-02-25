"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal
from SubGoal import SubGoal as SubGoal
from Status import Status as Status

'''PREGENERATION METHODS'''
def buildGoalsArray(numberOfGoals):
	pass

def buildSubGoalsArray(numberOfSubGoals):
	pass

'''TESTING OBJECTS'''
def testGoal():
	#TEST 1
	try:
		#build test here
		goalInformation = {
			"name": "Water the Plants",
			"category": "Gardening",
			"priority": 1
		}
		goal1 = Goal(1, goalInformation, "01012019")
		print(goal1.getId())
		print(goal1.getName())
		print(goal1.getCategory())
		print(goal1.getPriority())
		print(goal1.getStartDate())

		if(goal1.isComplete()):
			print(goa11.getFinishDate())
		else:
			print("Incomplete")

		goal1.completeGoal("0202019")

		if(goal1.isComplete()):
			print(goal1.getFinishDate())
		else:
			print("Incomplete")

		print("***************GOAL TEST 1: SUCCESS***************\n")
	except:
		print("***************GOAL TEST 1: FAIL***************\n")

	#TEST 2
	try:
		#build test here
		
		print("***************GOAL TEST 2: SUCCESS***************\n")
	except:
		print("***************GOAL TEST 2: FAIL***************\n")

	#TEST 3
	try:
		#build test here
		
		print("***************GOAL TEST 3: SUCCESS***************\n")
	except:
		print("***************GOAL TEST 3: FAIL***************\n")

def testSubGoal():
	#TEST 1
	try:
		#build test here
		
		print("***************SUBGOAL TEST 1: SUCCESS***************\n")
	except:
		print("***************SUBGOAL TEST 1: FAIL***************\n")

	#TEST 2
	try:
		#build test here
		
		print("***************SUBGOAL TEST 2: SUCCESS***************\n")
	except:
		print("***************SUBGOAL TEST 2: FAIL***************\n")

	#TEST 3
	try:
		#build test here
		
		print("***************SUBGOAL TEST 3: SUCCESS***************\n")
	except:
		print("***************SUBGOAL TEST 3: FAIL***************\n")

def testStatus():
	#TEST 1
	try:
		#build test here
		
		print("***************STATUS TEST 1: SUCCESS***************\n")
	except:
		print("***************STATUS TEST 1: FAIL***************\n")

	#TEST 2
	try:
		#build test here
		
		print("***************STATUS TEST 2: SUCCESS***************\n")
	except:
		print("***************STATUS TEST 2: FAIL***************\n")

	#TEST 3
	try:
		#build test here
		
		print("***************STATUS TEST 3: SUCCESS***************\n")
	except:
		print("***************STATUS TEST 3: FAIL***************\n")

def testModel():
	#TEST 1
	try:
		#build test here
		
		print("***************MODEL TEST 1: SUCCESS***************\n")
	except:
		print("***************MODEL TEST 1: FAIL***************\n")

	#TEST 2
	try:
		#build test here
		
		print("***************MODEL TEST 2: SUCCESS***************\n")
	except:
		print("***************MODEL TEST 2: FAIL***************\n")

	#TEST 3
	try:
		#build test here
		
		print("***************MODEL TEST 3: SUCCESS***************\n")
	except:
		print("***************MODEL TEST 3: FAIL***************\n")

'''TESTING MODULES'''
def testFileManager():
	#TEST 1
	try:
		#build test here
		
		print("***************FILEMANAGER TEST 1: SUCCESS***************\n")
	except:
		print("***************FILEMANAGER TEST 1: FAIL***************\n")

	#TEST 2
	try:
		#build test here
		
		print("***************FILEMANAGER TEST 2: SUCCESS***************\n")
	except:
		print("***************FILEMANAGER TEST 2: FAIL***************\n")

	#TEST 3
	try:
		#build test here
		
		print("***************FILEMANAGER TEST 3: SUCCESS***************\n")
	except:
		print("***************FILEMANAGER TEST 3: FAIL***************\n")

def testGoalManager():
	#TEST 1
	try:
		#build test here
		
		print("***************GOALMANAGER TEST 1: SUCCESS***************\n")
	except:
		print("***************GOALMANAGER TEST 1: FAIL***************\n")

	#TEST 2
	try:
		#build test here
		
		print("***************GOALMANAGER TEST 2: SUCCESS***************\n")
	except:
		print("***************GOALMANAGER TEST 2: FAIL***************\n")

	#TEST 3
	try:
		#build test here
		
		print("***************GOALMANAGER TEST 3: SUCCESS***************\n")
	except:
		print("***************GOALMANAGER TEST 3: FAIL***************\n")

def testSubGoalManager():
	#TEST 1
	try:
		#build test here
		
		print("***************SUBGOALMANAGER TEST 1: SUCCESS***************\n")
	except:
		print("***************SUBGOALMANAGER TEST 1: FAIL***************\n")

	#TEST 2
	try:
		#build test here
		
		print("***************SUBGOALMANAGER TEST 2: SUCCESS***************\n")
	except:
		print("***************SUBGOALMANAGER TEST 2: FAIL***************\n")

	#TEST 3
	try:
		#build test here
		
		print("***************SUBGOALMANAGER TEST 3: SUCCESS***************\n")
	except:
		print("***************SUBGOALMANAGER TEST 3: FAIL***************\n")

def testEffortTracker():
	#TEST 1
	try:
		#build test here
		
		print("***************EFFORTTRACKER TEST 1: SUCCESS***************\n")
	except:
		print("***************EFFORTTRACKER TEST 1: FAIL***************\n")

	#TEST 2
	try:
		#build test here
		
		print("***************EFFORTTRACKER TEST 2: SUCCESS***************\n")
	except:
		print("***************EFFORTTRACKER TEST 2: FAIL***************\n")

	#TEST 3
	try:
		#build test here
		
		print("***************EFFORTTRACKER TEST 3: SUCCESS***************\n")
	except:
		print("***************EFFORTTRACKER TEST 3: FAIL***************\n")

def testActiveTimer():
	#TEST 1
	try:
		#build test here
		
		print("***************ACTIVETIMER TEST 1: SUCCESS***************\n")
	except:
		print("***************ACTIVETIMER TEST 1: FAIL***************\n")

	#TEST 2
	try:
		#build test here
		
		print("***************ACTIVETIMER TEST 2: SUCCESS***************\n")
	except:
		print("***************GOAL TEST 2: FAIL***************\n")

	#TEST 3
	try:
		#build test here
		
		print("***************ACTIVETIMER TEST 3: SUCCESS***************\n")
	except:
		print("***************ACTIVETIMER TEST 3: FAIL***************\n")

def testSortManager():
	#TEST 1
	try:
		#build test here
		
		print("***************SORTMANAGER TEST 1: SUCCESS***************\n")
	except:
		print("***************SORTMANAGER TEST 1: FAIL***************\n")

	#TEST 2
	try:
		#build test here
		
		print("***************SORTMANAGER TEST 2: SUCCESS***************\n")
	except:
		print("***************GOAL TEST 2: FAIL***************\n")

	#TEST 3
	try:
		#build test here
		
		print("***************SORTMANAGER TEST 3: SUCCESS***************\n")
	except:
		print("***************SORTMANAGER TEST 3: FAIL***************\n")

def testProgressTracker():
	#TEST 1
	try:
		#build test here
		
		print("***************PROGRESSTRACKER TEST 1: SUCCESS***************\n")
	except:
		print("***************PROGRESSTRACKER TEST 1: FAIL***************\n")

	#TEST 2
	try:
		#build test here
		
		print("***************PROGRESSTRACKER TEST 2: SUCCESS***************\n")
	except:
		print("***************PROGRESSTRACKER TEST 2: FAIL***************\n")

	#TEST 3
	try:
		#build test here
		
		print("***************PROGRESSTRACKER TEST 3: SUCCESS***************\n")
	except:
		print("***************PROGRESSTRACKER TEST 3: FAIL***************\n")

def testAnalysisViewer():
	#TEST 1
	try:
		#build test here
		
		print("***************ANALYSISVIEWER TEST 1: SUCCESS***************\n")
	except:
		print("***************ANALYSISVIEWER TEST 1: FAIL***************\n")

	#TEST 2
	try:
		#build test here
		
		print("***************ANALYSISVIEWER TEST 2: SUCCESS***************\n")
	except:
		print("***************ANALYSISVIEWER TEST 2: FAIL***************\n")

	#TEST 3
	try:
		#build test here
		
		print("***************ANALYSISVIEWER TEST 3: SUCCESS***************\n")
	except:
		print("***************ANALYSISVIEWER TEST 3: FAIL***************\n")

def main():
	testGoal()
	#testSubGoal()
	#testStatus()
	#testModel()

	#testFileManager()
	#testGoalManager()
	#testSubGoalManager()
	#testEffortTracker()
	#testActiveTimer()
	#testSortManager()
	#testProgressTracker()
	#testAnalysisViewer()

if __name__ == '__main__':
	main()