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
from GErrors import FlagError, GoalNotFoundError, DueDateExistenceError
from Model import Model

m = Model([], 0, 0, {}) #create an empty Model object where everything is set to 0 or empty
#Setup goals
adue = DateTime.datetime(2014, 6, 12)
bdue = DateTime.datetime(2019, 9, 5)
cdue = DateTime.datetime(2020, 3, 12)

agoalInformation = {"name": "atest", "category" : "atest_category", "priority" : 1, "memo" : "testa", "dueDate" : adue}
bgoalInformation = {"name": "btest", "category" : "btest_category", "priority" : 2,  "memo" : "testb", "dueDate" : bdue}
cgoalInformation = {"name": "ctest", "category" : "ctest_category", "priority" : 3,  "memo" : "testc", "dueDate" : cdue}

goalsinfo = [agoalInformation, bgoalInformation, cgoalInformation]

def test_goal_management():
    for i in range(3):
        gid = m.addGoal()
        assert len(m.goalList) == i+1
        goal = m.getGoal(gid)
        m.editGoal(gid, goalsinfo[gid-1])
        assert goal.priority == goalsinfo[gid-1]["priority"]
    
    m.completeGoal(gid)
    assert len(m.getCompletedGoalList()) == 1
    assert m.getCompletedGoalList()[0].id == gid
    assert len(m.getGoalList()) == 3
    m.deleteGoal(gid)
    assert len(m.getCompletedGoalList()) == 0
    assert len(m.getGoalList()) == 2