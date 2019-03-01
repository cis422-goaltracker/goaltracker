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
agoalInformation = {"name": "test", "category" : "atest_category", "priority" : 1}
bgoalInformation = {"name": "test", "category" : "btest_category", "priority" : 2}

a = Goal.Goal(1, agoalInformation, astart, adue)
b = Goal.Goal(2, bgoalInformation, bstart, bdue)

def test_category_sort():
    assert a < b
def test_priority_sort():
    Goal.sorting = "priority"
    assert a < b