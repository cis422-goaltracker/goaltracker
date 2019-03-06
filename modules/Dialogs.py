"""
    Names: Holly Hardin (HH)
    CIS 422
    GoalTracker
        Reference [0]: https://stackoverflow.com/questions/21213853/pyside-how-to-delete-widgets-from-gridlayout

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
from enum import Enum
import pyqtgraph as pg

from Goal import Goal, SubGoal
from Model import Model
from FileManager import FileManager
from AnalysisGenerator import AnalysisGenerator

# Global variable for storing UI files (HH)
UI_PATHS = {"MainWindow": "../UI/MainWindow.ui", "AddEditViewGoal": "../UI/AddEditViewGoal.ui", "AddEditViewSubgoal": "../UI/AddEditViewSubgoal.ui", "Analysis": "../UI/Analysis.ui", "UncompletedAnalysis": "../UI/UncompletedAnalysis.ui"}

class Method(Enum):
    ADD = 1
    EDITVIEW = 2


class AddEditViewGoal(QDialog):
    def __init__(self, _model, _goalid = None): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        super(AddEditViewGoal, self).__init__()
        
        loadUi(UI_PATHS["AddEditViewGoal"], self) # Load the AddEditViewGoal UI

        #Class Variables
        self.model = _model
        self.goalid = _goalid
        self.selectedListItemId = None


        #Signals
        self.push_effort.clicked.connect(self.toggleEffortTracker)
        self.checkBox_due_date.clicked.connect(self.toggleDueDate)
        self.push_add_subgoal.clicked.connect(self.loadAddSubGoal)
        self.push_complete_subgoal.clicked.connect(self.loadCompleteSubGoal)
        self.push_edit_view_subgoal.clicked.connect(self.loadEditViewSubGoal)
        self.push_delete_subgoal.clicked.connect(self.loadDeleteSubGoal)
        self.push_save.clicked.connect(self.loadSaveGoal)
        self.push_cancel.clicked.connect(self.loadCancelGoal)
        self.listWidget.itemSelectionChanged.connect(self.setChosenItem)

        self.refreshListView()

        if self.goalid == None:
            self.method = Method.ADD
            self.setWindowTitle('Add Goal')
            self.goalid = self.model.addGoal()
            self.dateTimeEdit_due_date.setDate(QDate.currentDate())

        else:
            self.method = Method.EDITVIEW
            self.setWindowTitle('Edit/View Goal')
            goal = self.model.getGoal(self.goalid)
            self.lineEdit_goal_name.setText(goal.getName())
            if goal.isComplete():
                self.label_status.setText("Status: Complete")
            else:
                self.label_status.setText("Status: Incomplete")
            self.dateTimeEdit_due_date.setDate(goal.getDueDate())

            if goal.getPriority() == 3:
                self.radio_priority_low.isChecked()
            elif goal.getPriority() == 2:
                self.radio_priority_medium.isChecked()
            else:
                self.radio_priority_high.isChecked()

            self.lineEdit_category.setText(goal.getCategory())
            self.textEdit.setText(goal.getMemo())

    '''********************PYQTSLOT OPERATIONS********************'''
    @pyqtSlot()
    def toggleEffortTracker(self): #FUNCTION NEEDS TO BE BUILT
        pass

    @pyqtSlot()
    def toggleDueDate(self): #FUNCTION NEEDS TO BE BUILT
        pass

    @pyqtSlot()
    def loadAddSubGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        window = AddEditViewSubGoal(self, self.model, self.goalid) #open add AddEditViewGoal window, pass it model
        if window.exec():
            self.refreshListView()

    @pyqtSlot()
    def loadCompleteSubGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        if self.subGoalIsSelected():
            subgoalid = self.selectedListItemId
            self.model.completeSubGoal(self.goalid, subgoalid)
            self.refreshListView()
        else:
            print("No Subgoals")

    @pyqtSlot()
    def loadEditViewSubGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        if self.subGoalIsSelected():
            subgoalid = self.selectedListItemId
            window = AddEditViewSubGoal(self, self.model, self.goalid, subgoalid) #open AddEditViewSubGoal window, passes it model and subgoal id
            if window.exec():
                self.refreshListView()
        else:
            print("No Subgoals")

    @pyqtSlot()
    def loadDeleteSubGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        if self.subGoalIsSelected():
            subgoalid = self.selectedListItemId
            self.model.deleteSubGoal(self.goalid, subgoalid)
            self.refreshListView()
        else:
            print("No Subgoals")

    @pyqtSlot()
    def loadSaveGoal(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''

        goalName = self.lineEdit_goal_name.text()
        dueDate = self.dateTimeEdit_due_date.date()
        category = self.lineEdit_category.text()
        if self.radio_priority_low.isChecked():
            priority = 3
        elif self.radio_priority_medium.isChecked():
            priority = 2
        else:
            priority = 1
        memo = self.textEdit.toPlainText()

        self.model.editGoal(self.goalid, {"name": goalName, "category": category, "priority": priority, "memo": memo, "dueDate": dueDate})


        self.accept() #exit dialog

    @pyqtSlot()
    def loadCancelGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        if self.method == Method.ADD:
            self.model.deleteGoal(self.goalid) #delete goal from model
        self.close() #exit dialog

    '''********************CLASS METHODS OPERATIONS********************'''
    def subGoalIsSelected(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        return self.selectedListItemId != None

    def setChosenItem(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        selectedlist = [item.data(Qt.UserRole) for item in self.listWidget.selectedItems()]
        if not selectedlist:
            self.selectedListItemId = None
        else:
            self.selectedListItemId = selectedlist[0]

    def addToListView(self, _subGoalList):
        '''
        @param:

        @return:

        @purpose:
        '''
        #cycle through list, to string every goal and place into listview
        self.listWidget.clear()
        for subGoal in _subGoalList:
            item = QListWidgetItem()
            item.setText(subGoal.toString())
            item.setData(Qt.UserRole, subGoal.getId())
            self.listWidget.addItem(item)

    def refreshListView(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        if len(self.model.getGoalList()) != 0:
            subGoalList = self.model.getSubGoalList(self.goalid)
            self.addToListView(subGoalList)


class AddEditViewSubGoal(QDialog):
    def __init__(self, _parent, _model, _goalid, _subgoalid = None): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        super(AddEditViewSubGoal, self).__init__()
        
        loadUi(UI_PATHS["AddEditViewSubgoal"], self) # Load the AddEditViewSubGoal UI

        #Class Variables
        self.parent = _parent
        self.model = _model
        self.goalid = _goalid
        self.subgoalid = _subgoalid

        #Signals
        self.push_save.clicked.connect(self.loadSaveSubGoal)
        self.push_cancel.clicked.connect(self.loadCancelSubGoal)

        if self.subgoalid == None:
            self.method = Method.ADD
            self.setWindowTitle('Add Subgoal')
            self.subgoalid = self.model.addSubGoal(self.goalid)
        else:
            self.method = Method.EDITVIEW
            self.setWindowTitle('Edit/View Subgoal')
            subgoal = self.model.getSubGoal(self.goalid, self.subgoalid)
            self.lineEdit.setText(subgoal.getName())
            if subgoal.isComplete():
                self.label_status.setText("Status: Complete")
            else:
                self.label_status.setText("Status: Incomplete")

    @pyqtSlot()
    def loadSaveSubGoal(self): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        #update subGoal information model
        self.model.editSubGoal(self.goalid, self.subgoalid, {"name": str(self.lineEdit.text())})
        self.accept() #exit dialog

    @pyqtSlot()
    def loadCancelSubGoal(self):
        '''
        @param:

        @return:

        @purpose:
        '''
        if self.method == Method.ADD:
            self.model.deleteSubGoal(self.goalid, self.subgoalid)
        self.close() #exit dialog


class Analysis(QDialog):
    def __init__(self, _model, _goalid): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        #how do I access these functions? ask noah. is everything connected right

        super(Analysis, self).__init__()
        
        loadUi(UI_PATHS["Analysis"], self) # Load the AddEditViewSubGoal UI

        self.model = _model
        self.goalid = _goalid

        # string1 = "This Goal took you" + time_took(self.goalid) + "days to complete"
        # #if goal does not have duedate skip
        # string2 =   "That is" + end_time_comp(self.goalid) + "days faster/slower than anticipated"
        # string3 =   "You spend on average" + time_per_day_summed(self.goalid) + "hours a day working on your goal"

        # greater_val = max(before_due_num(self.model), after_due_num(self.model))
        
        # #should this calculation take into account all of the goals?
        # #right now I divide the goals that didnt have to be rescheduled from the number of goals
        # #should i add the requirement of the goal having a duedate?
        # if greater_val == before_due_num(self.model):
        #     sting4 =  "You completed %" + greater_val + "of your goals faster than aniticpated!"
        #     string5 =  "Great job, keep up the good work!"
        #     string6 =  ""

        # if greater_val != before_due_num(self.model):
        #     string4 =  "You completed %" + greater_val + "of your goals slower than aniticpated."
        #     string5 =  "You seem to have trouble sticking to your goals. Consider giving"
        #     string6 =  "yourself more time next time!"

        # self.label_daystook.setText(string1)
        # self.label_fasterslower.setText(string2)
        # self.label_numhours.setText(string3)
        # self.label_lowerlinetext_1.setText(string4)
        # self.label_lowerlinetext_2.setText(string5)
        # self.label_lowerlinetext_3.setText(string6)

        #need to make graph into a picture.


class UncompletedAnalysis(QDialog):
    def __init__(self, _model): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        super(UncompletedAnalysis, self).__init__()
        
        loadUi(UI_PATHS["UncompletedAnalysis"], self) # Load the AddEditViewSubGoal UI

        self.model = _model
        
        #should this calculation take into account all of the goals?
        #right now I divide the goals that didnt have to be rescheduled from the number of goals
        #should i add the requirement of the goal having a duedate?
        # if greater_val == before_due_num(self.model):
        #     sting1 =  "You completed %" + greater_val + "of your goals faster than aniticpated!"
        #     string2 =  "Great job, keep up the good work!"
        #     string3 =  ""

        # if greater_val != before_due_num(self.model):
        #     string1 =  "You completed %" + greater_val + "of your goals slower than aniticpated."
        #     string2 =  "You seem to have trouble sticking to your goals. Consider giving"
        #     string3 =  "yourself more time next time!"

        # self.label_lowerlinetext_1.setText(string1)
        # self.label_lowerlinetext_2.setText(string2)
        # self.label_lowerlinetext_3.setText(string3)
