"""
    Author: Isaac Lance
    Date: 2/28/19
    CIS422
    GoalTracker
"""
#Standard imports: pytest and the file to be tested
import pytest
from Goal import Goal
from SubGoal import SubGoal
import datetime as DateTime
from Model import Model
#3 Goals
astart = DateTime.date(1998, 6, 28)
adue = DateTime.date(2014, 6, 12)
bstart = DateTime.date(2000, 1, 1)
bdue = DateTime.date(2019, 9, 5)
cstart = DateTime.date(2000, 1, 6)
cdue = DateTime.date(2019, 9, 6)
afinish = DateTime.date(2050, 11, 11)
curr = DateTime.date(2018, 11, 11)
agoalInformation = {"name": "atest", "category" : "atest_category", "priority" : 1}
bgoalInformation = {"name": "btest", "category" : "btest_category", "priority" : 3}
cgoalInformation = {"name": "ctest", "category" : "aatest_category", "priority" : 2}
newa = Goal(1, bgoalInformation, astart, cdue)
a = Goal(1, agoalInformation, astart, adue)
a.completeGoal(afinish)
b = Goal(2, bgoalInformation, bstart, bdue)
c = Goal(3, cgoalInformation, bstart, bdue)
#Subgoal
time = DateTime.datetime.now()
subGoalInformation = {"name": "test"}
suba = SubGoal(1, subGoalInformation, time)
subgoals = [suba]
newa.setSubGoals(subgoals)
#Setup for model
glist = [a, b, c]
edict = {} 
#glist.extend(a,b,c)
m = Model(glist, 0 , 0, edict)

def test_getIncomplete():
    list = m.getIncompleteGoalList()
    assert len(list) == 2
    assert list[0] == b
    assert list[1] == c

def test_getOverDueGoalList():
    list = m.getOverDueGoalList(curr)
    assert len(list) == 1
    assert list[0] == a

def test_getGoal():
    d = m.getGoal(1)
    assert d == a

def test_setGoal():
    m.setGoal(newa)
    assert m.getGoal(1) == newa

def test_getSubGoalList():
    assert m.getSubGoalList(1)[0].name == suba.name

def test_setSubGoalList():
    m.setSubGoalList(2, subgoals)
    assert m.getSubGoalList(2)[0].name == suba.name
