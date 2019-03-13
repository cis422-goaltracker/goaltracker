"""
    Author: Isaac Lance, Weigang An
    Date: 03/11/19
    CIS422
    GoalTracker
"""
#Standard imports: pytest and the file to be tested
import pytest
from Goal import Goal, SubGoal
from datetime import datetime  as dt, timedelta
from GErrors import FlagError
from Model import Model
from AnalysisGenerator import AnalysisGenerator
#Setup values for tests.
m = Model([], 0, 0, {}) #create an empty Model object where everything is set to 0 or empty
#Setup goals
adue = dt(2014, 6, 12)
bdue = dt(2019, 9, 5)
cdue = dt(2020, 3, 12)

agoalInformation = {"name": "atest", "category" : "atest_category", "priority" : 1, "memo" : "testa", "dueDate" : adue}
bgoalInformation = {"name": "btest", "category" : "btest_category", "priority" : 2,  "memo" : "testb", "dueDate" : bdue}
cgoalInformation = {"name": "ctest", "category" : "ctest_category", "priority" : 3,  "memo" : "testc", "dueDate" : cdue}

nows = [dt.now() - timedelta(days = 2, hours = 12),
        dt.now() - timedelta(days = 2, hours = 5),
        dt.now() - timedelta(hours = 2)]
laters = [nows[0] + timedelta(hours=5), nows[1] + timedelta(hours = 7), nows[2] + timedelta(hours = 1)]
goalsinfo = [agoalInformation, bgoalInformation, cgoalInformation]
for i in range(3):
    gid = m.addGoal()
    m.editGoal(gid, goalsinfo[gid-1])
for i in range(3):
    m.manuallyInputEffort(gid, nows[i], laters[i])

m.goalList[2].startDate = nows[0]
ag = AnalysisGenerator(gid, m)

print(ag.getActiveTime())
    
 