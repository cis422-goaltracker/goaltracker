"""
    Test file
    Subgoal
    Isaac Lance 2/28/19
"""
#Standard imports: pytest and the file to be tested
import pytest
import SubGoal
import datetime as DateTime
time = DateTime.datetime.now()
finish = DateTime.date(1998, 6, 28)
subGoalInformation = {"name": "test"}
a = SubGoal.SubGoal(1, subGoalInformation, time)

def test_update():
    subGoalInformation = {"name": "test2"}
    a.updateSubGoal(subGoalInformation)
    assert a.name == "test2"
    return
        
def test_complete():
    assert not a.isComplete()
    a.completeSubGoal(finish)
    assert a.finishDate == finish
    assert a.isComplete()
    return
    
def test_getId():
    assert a.getId() == 1
    return
    
def test_getName():
    a.name = "test3"
    assert a.getName() == "test3"
    return

def test_getStartDate():
    assert a.getStartDate() == time
    return
    
def test_getFinishDate():
    assert a.getFinishDate() == finish
    return
