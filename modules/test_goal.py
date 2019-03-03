"""
    Test file
    Goal
    Isaac Lance 2/28/19
    Weigang An 3/2/19
"""
#Standard imports: pytest and the file to be tested
import pytest
from Goal import Goal
#from SubGoal import SubGoal
import datetime as DateTime
astart = DateTime.date(1998, 6, 28)
adue = DateTime.date(2014, 6, 12)
bstart = DateTime.date(2000, 1, 1)
bdue = DateTime.date(2019, 9, 5)
afinish = DateTime.date(2050, 11, 11)
cstart = DateTime.date(2001, 6, 20)
cdue = DateTime.date(2020, 3, 12)
agoalInformation = {"name": "atest", "category" : "atest_category", "priority" : 1}
bgoalInformation = {"name": "btest", "category" : "btest_category", "priority" : 2}
cgoalInformation = {"name": "ctest", "category" : "ctest_category", "priority" : 2}

a = Goal(1, agoalInformation, astart, adue)
b = Goal(2, bgoalInformation, bstart, bdue)
c = Goal(3, cgoalInformation, cstart, cdue)
#Subgoal
time = DateTime.datetime.now()
subGoalInformation = {"name": "test"}
suba = SubGoal(1, subGoalInformation, time)
subgoals = [suba]

def test_category_lt():
    assert a < b < c
def test_priority_lt():
    Goal.sorting = "priority"
    print (Goal.sorting)
    assert a < b 
    assert not (b < c)

def test_priority2():
    Goal.sorting = "123"
    print(a < b)
    assert a < b < c 
    #should raise error message

def test_reschedule():
    a.reschedule(bdue)
    assert a.dueDate == b.dueDate
    b.reschedule(cdue)
    assert b.dueDate == c.dueDate

def test_hasBeenRescheduled():
    assert a.hasBeenRescheduled()
    assert b.hasBeenRescheduled()

def test_updateGoal():
    a.updateGoal(cgoalInformation)
    assert a.name == c.name

def test_completeGoal():
    a.completeGoal(afinish)
    assert a.finishDate == afinish

def test_isComplete():
    assert a.isComplete()
    assert not b.isComplete()

#TODO: Test isOverDue? I think it shouldn;t be a function
def test_addEffortTrack():
    now = DateTime.datetime.now()
    later = now + DateTime.timedelta(hours = 9)
    delta = later - now
    assert len(a.effortTracker) == 0
    a.addEffortTrack(later, delta)
    assert len(a.effortTracker) == 1

def test_setSubGoals():
    a.setSubGoals(subgoals)
    assert a.subGoals[0] == suba
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    