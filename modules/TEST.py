"""
	Names
	CIS 422
	GoalTracker
"""

from Goal import Goal as Goal
from SubGoal import SubGoal as SubGoal
from Status import Status as Status

def main():
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


if __name__ == '__main__':
	main()