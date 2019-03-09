"""
	Author: Isaac Lance
	Date: 03/09/2019
 	CIS422
	GoalTracker
"""

class BaseError(Exception):
    pass
    
class FlagError(BaseError):
    def __init__(self, flag, p_values, value):
        self.flag = flag
        self.p_values = p_values
        self.value = value
    def __repr__(self):
        val_string = []
        for val in self.p_values:
            val_string += (" " + str(val) + ",")
        
        return("Flag " + str(self.flag)" " + "has expected values:" + val_string + ". But had the value: " + str(self.value))

class GoalNotFoundError(BaseError):
    def __init__(self, Id: int, subgoal = False):
        self.ID = Id
        self.subgoal = subgoal
    def __repr__(self):
        string = "Goal not found with id " + str(self.ID)
        if self.subgoal:
            string = "Sub" + str
        return(string)
        
class DueDateExistenceError(BaseError):
    def __init__(self, Id: int):
        self.ID = Id
    def __repr__(self):
        return("Goal with ID: " + str(self.ID) +" has no DueDate but DueDate was accessed")
