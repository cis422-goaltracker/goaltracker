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
	goal1 = Goal(1, "Water the Plants", "Gardening", 1, "01012019")
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


def testSubGoal():
	pass

def testStatus():
	pass

'''TESTING MODULES'''
def testFileManager():
	pass

def testGoalManager():
	pass

def testSubGoalManager():
	pass

def testEffortTracker():
	pass

def testActiveTimer():
	pass

def testSortManager():
	pass

def testProgressTracker():
	pass

def testAnalysisViewer():
	pass

def testAnalysisViewer():
	pass

def main():


if __name__ == '__main__':
	main()