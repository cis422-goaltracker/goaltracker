"""
    Test file
    Goal
    Isaac Lance 2/28/19
"""
#Standard imports: pytest and the file to be tested
import pytest
import Goal
import SubGoal
import datetime as DateTime
astart = DateTime.date(1998, 6, 28)
adue = DateTime.date(2014, 6, 12)
bstart = DateTime.date(2000, 1, 1)
bdue = DateTime.date(2019, 9, 5)
afinish = DateTime.date(2050, 11, 11)
agoalInformation = {"name": "atest", "category" : "atest_category", "priority" : 1}
bgoalInformation = {"name": "btest", "category" : "btest_category", "priority" : 2}

a = Goal.Goal(1, agoalInformation, astart, adue)
b = Goal.Goal(2, bgoalInformation, bstart, bdue)

def test_category_lt():
    assert a < b
def test_priority_lt():
    Goal.sorting = "priority"
    assert a < b
def test_reschedule():
    a.reschedule(bdue)
    assert a.dueDate == b.dueDate
def test_hasBeenRescheduled():
    assert a.hasBeenRescheduled()
def test_updateGoal():
    a.updateGoal(bgoalInformation)
    assert a.name == b.name
def test_completeGoal():
    a.completeGoal(afinish)
    assert a.finishDate == afinish
def test_isComplete():
    assert a.isComplete()
    assert not b.isComplete()
#TODO: Test isOverDue? I think it shouldn;t be a function
def test_addEffortTrack():
    now = DateTime.datetime.now()
    later = now + timedelta(hours = 9)
    delta = later - now
    a.addEffortTrack(later, delta)
    assert 1 == 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    