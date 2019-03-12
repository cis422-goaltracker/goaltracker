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

x = SubGoal(1)
y = SubGoal(2)
def test_SubGoal_update():
    x.update(subGoalInformation)
    y.update(subGoalInformation)
    assert x.name == subGoalInformation["name"]
    
def test_Subgoal_complete():
    assert not(x.isCompleted)
    x.complete()
    assert x.isCompleted
    
def test_SubGoal_isComplete():
    assert x.isComplete()
    assert not(y.isComplete())
    
def test_SubGoal_toString():
    assert "Name: test | Status: Complete" == x.toString()
    assert "Name: test | Status: Incomplete" == y.toString()

#Goals    
a = Goal(1)
b = Goal(2)
c = Goal(3)
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

def test_category_lt():
    assert a < c
    assert a < b
    assert not(c < b)
    
def test_priority_lt():
    a.setSortingMethod("priority")
    b.setSortingMethod("priority")
    assert a < b 
    assert not (b < c)
        

def test_priority2():
    with pytest.raises(FlagError):
        a.sortingMethod = "123"
        a < b 
    #should raise error message

def test_hasBeenRescheduled():
    assert not(a.hasBeenRescheduled())
    assert c.hasBeenRescheduled()
    assert (b.hasBeenRescheduled() == False)

def test_hasDueDate():
    assert b.hasDueDate()
    assert a.hasDueDate()

def test_isOverDue():
    assert a.isOverDue()
    assert not(b.isOverDue())

def test_addSubGoal():
    a.addSubGoal(5)
    assert len(a.subGoalList) != 0

def test_updateSubGoal():
    a.updateSubGoal(5, subGoalInformation)
    assert a.subGoalList[0].name == "test"

def test_completeSubGoal():
    a.completeSubGoal(5)
    assert a.subGoalList[0].isComplete

def test_deleteSubGoal():
    a.deleteSubGoal(5)
    assert len(a.subGoalList) == 0
    
def test_completeGoal():
    a.complete(afinish)
    assert a.finishDate == afinish

def test_isComplete():
    assert a.isComplete()
    assert not b.isComplete()
    
def test_addEffortTrack():
    now = DateTime.datetime.now()
    later = now + DateTime.timedelta(hours = 9)
    delta = later - now
    assert len(a.effortTrackingData) == 0
    a.addEffortTrack(later, delta)
    assert len(a.effortTrackingData) == 1

    
