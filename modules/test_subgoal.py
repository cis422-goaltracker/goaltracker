"""
    Authors: Isaac Lance, Weigang An
    Date: 03/02/19
    CIS422
    GoalTracker
"""
#Standard imports: pytest and the file to be tested
import pytest
import SubGoal
import datetime as DateTime
time = DateTime.datetime.now()
time2 = DateTime.date(2019, 1, 1)
finish = DateTime.date(1998, 6, 28)
subGoalInformation = {"name": "test"}
a = SubGoal.SubGoal(1, subGoalInformation, time)
b = SubGoal.SubGoal(2, subGoalInformation, time2)

def test_update():
    subGoalInformation = {"name": "test2"}
    subGoalInformation2 = {"name": 999}
    a.updateSubGoal(subGoalInformation)
    assert a.name == "test2"
    b.updateSubGoal(subGoalInformation2)
    assert b.name == 999
    # Now the subgoal b's name is int and it worked, that should be string. 
    return
        
def test_complete():
    assert not a.isComplete()
    a.completeSubGoal(finish)
    assert a.finishDate == finish
    assert a.isComplete()
    return
    
def test_getId():
    assert a.getId() == 1
    assert b.getId() == 2
    return
    
def test_getName():
    a.name = "test3"
    b.name = 33
    assert a.getName() == "test3"
    assert b.getName() == 33
    # b's name is int and it worked, it should be string.
    return

def test_getStartDate():
    assert a.getStartDate() == time
    assert b.getStartDate() == time2
    return
    
def test_getFinishDate():
    assert a.getFinishDate() == finish
    return
