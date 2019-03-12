"""
    Author: Isaac Lance, Weigang An
    Date: 03/11/19
    CIS422
    GoalTracker
"""
#Standard imports: pytest and the file to be tested
import pytest
from Goal import Goal, SubGoal
import datetime as DateTime
from GErrors import FlagError
#Setup values for tests.
astart = DateTime.datetime(1998, 6, 28)
adue = DateTime.datetime(2014, 6, 12)
bstart = DateTime.datetime(2000, 1, 1)
bdue = DateTime.datetime(2019, 9, 5)
afinish = DateTime.datetime(2050, 11, 11)
cstart = DateTime.datetime(2001, 6, 20)
cdue = DateTime.datetime(2020, 3, 12)
agoalInformation = {"name": "atest", "category" : "atest_category", "priority" : 1, "memo" : "testa", "dueDate" : adue}
bgoalInformation = {"name": "btest", "category" : "btest_category", "priority" : 2,  "memo" : "testb", "dueDate" : bdue}
cgoalInformation = {"name": "ctest", "category" : "ctest_category", "priority" : 2,  "memo" : "testc", "dueDate" : cdue}

#Subgoals first
time = DateTime.datetime.now()
subGoalInformation = {"name": "test"}
#Create two dummy subgoals
x = SubGoal(1)
y = SubGoal(2)
#Update subgoals, check that they were updated properly.
def test_SubGoal_update():
    x.update(subGoalInformation)
    y.update(subGoalInformation)
    assert x.name == subGoalInformation["name"]
#Check if we can complete subgoals
def test_Subgoal_complete():
    assert not(x.isCompleted)
    x.complete()
    assert x.isCompleted
#Check mainly if isComplete properly returns false for y
def test_SubGoal_isComplete():
    assert x.isComplete()
    assert not(y.isComplete())
#Check if the string representations are correct
def test_SubGoal_toString():
    assert "Name: test | Status: Complete" == x.toString()
    assert "Name: test | Status: Incomplete" == y.toString()

#Test Goals    
a = Goal(1)
b = Goal(2)
c = Goal(3)
#Update all the goals and assert information from the dictionaries
def test_update():
    a.update(agoalInformation)
    b.update(bgoalInformation)
    c.update(cgoalInformation)
    assert a.name == agoalInformation["name"]
    assert b.category == bgoalInformation["category"]
    assert c. priority == cgoalInformation["priority"]
    assert a.memo == agoalInformation["memo"]
    assert a.initialDueDate == agoalInformation["dueDate"]
    c.update(bgoalInformation)
    assert c.initialDueDate == cgoalInformation["dueDate"]
    assert c.dueDate == bgoalInformation["dueDate"]
#Test the comparison "<" for goals (enables sorting)
#The sorting value is initially "category"
def test_category_lt():
    assert a < c
    assert a < b
    assert not(c < b)
#Test sorting by priority instead
def test_priority_lt():
    a.setSortingMethod("priority")
    b.setSortingMethod("priority")
    assert a < b 
    assert not (b < c)
#Test the FlagError raised when the sorting flag is invalid
def test_priority2():
    with pytest.raises(FlagError):
        a.sortingMethod = "123"
        a < b 
    #should raise error message
#Test if we can check when a goal is recheduled
def test_hasBeenRescheduled():
    assert not(a.hasBeenRescheduled())
    assert c.hasBeenRescheduled()
    assert (b.hasBeenRescheduled() == False)
#Test some bool getters
def test_hasDueDate():
    assert b.hasDueDate()
    assert a.hasDueDate()
#"        "
def test_isOverDue():
    assert a.isOverDue()
    assert not(b.isOverDue())
#Test if the subgoal listi ncreases in size when we add a subgoal
def test_addSubGoal():
    a.addSubGoal(5)
    assert len(a.subGoalList) != 0
#Test updating subgoals
def test_updateSubGoal():
    a.updateSubGoal(5, subGoalInformation)
    assert a.subGoalList[0].name == "test"
#test completing subgoals
def test_completeSubGoal():
    a.completeSubGoal(5)
    assert a.subGoalList[0].isComplete
#Test deleting subgoals
def test_deleteSubGoal():
    a.deleteSubGoal(5)
    assert len(a.subGoalList) == 0
#test completing goals 
def test_completeGoal():
    a.complete(afinish)
    assert a.finishDate == afinish
#Test checking if a goal is complete
def test_isComplete():
    assert a.isComplete()
    assert not b.isComplete()
#Test effort tracking functionality.
def test_addEffortTrack():
    now = DateTime.datetime.now()
    later = now + DateTime.timedelta(hours = 9)
    delta = later - now
    assert len(a.effortTrackingData) == 0
    a.addEffortTrack(later, delta)
    assert len(a.effortTrackingData) == 1

    
