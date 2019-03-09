"""
    Names: Holly Hardin (HH)
    CIS 422
    GoalTracker
        Reference [0]: https://stackoverflow.com/questions/21213853/pyside-how-to-delete-widgets-from-gridlayout

"""
#System Imports
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime, timedelta
import pyqtgraph as pg

#Module Imports
from Goal import Goal, SubGoal
from Model import Model
from FileManager import FileManager
from AnalysisGenerator import AnalysisGenerator
from GenerateGraph import Canvas

# Global variable for storing UI files (HH)
UI_PATHS = {"MainWindow": "../UI/MainWindow.ui", "AddEditViewGoal": "../UI/AddEditViewGoal.ui", "AddEditViewSubgoal": "../UI/AddEditViewSubgoal.ui", "Analysis": "../UI/Analysis.ui", "UncompletedAnalysis": "../UI/UncompletedAnalysis.ui"}

class AddEditViewGoal(QDialog):
    def __init__(self, _model, _goalid = None):
        '''
        @param: _model (Model)
        @param: _goalid (integer) - defaults to None

        @return: None

        @purpose:
        '''
        super(AddEditViewGoal, self).__init__()
        
        loadUi(UI_PATHS["AddEditViewGoal"], self) # Load the AddEditViewGoal UI

        #Class Variables
        self.model = _model
        self.goalid = _goalid
        self.selectedListItemId = None
        self.hasDueDate = True

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
        self.dateTimeEdit_due_date.dateTimeChanged.connect(self.setDueDateText)

        if self.goalid == None:
            self.setWindowTitle('Add Goal')
            self.goalid = self.model.addGoal()
            self.dateTimeEdit_due_date.setDate(QDate.currentDate())
            self.dateTimeEdit_due_date.setTime(QTime.currentTime())
            self.label_goal_name_4.setText("")
        else:
            self.setWindowTitle('Edit/View Goal')
            goal = self.model.getGoal(self.goalid)
            self.lineEdit_goal_name.setText(goal.getName())
            if self.model.isEffortTracking(self.goalid):
                self.push_effort.setText("Stop Effort Tracker")

            if goal.isComplete():
                self.label_status.setText("Status: Complete")
            else:
                self.label_status.setText("Status: Incomplete")

            if goal.getPriority() == 3:
                self.radio_priority_low.isChecked()
            elif goal.getPriority() == 2:
                self.radio_priority_medium.isChecked()
            else:
                self.radio_priority_high.isChecked()

            self.lineEdit_category.setText(goal.getCategory())
            self.textEdit.setText(goal.getMemo())
            self.refreshListView()
            if goal.getDueDate() == None:
                self.hasDueDate = False
                self.checkBox_due_date.setCheckState(True)
                self.dateTimeEdit_due_date.setDate(QDate.currentDate())
                self.dateTimeEdit_due_date.setTime(QTime.currentTime())
            else:
                self.dateTimeEdit_due_date.setDate(goal.getDueDate())
                self.dateTimeEdit_due_date.setTime(goal.getDueDate().time()) 
            self.setDueDateText()

        if self.model.getGoal(self.goalid).isComplete():
            self.dateTimeEdit_due_date.setDisabled(True)
            self.checkBox_due_date.setDisabled(True)
            self.push_effort.setDisabled(True)
            self.push_add_subgoal.setDisabled(True)
            self.label_goal_name_4.setText("")



    '''********************PYQTSLOT OPERATIONS********************'''

    @pyqtSlot()
    def toggleEffortTracker(self):
        '''
        @param: None

        @return: None

        @purpose:
        '''
        if self.model.isEffortTracking(self.goalid):
            self.model.stopEffortTracker(self.goalid)
            self.push_effort.setText("Start Effort Tracker")
        else:
            self.model.startEffortTracker(self.goalid)
            self.push_effort.setText("Stop Effort Tracker")

    @pyqtSlot()
    def toggleDueDate(self):
        '''
        @param: None

        @return: None

        @purpose:
        '''
        if self.hasDueDate:
            self.dateTimeEdit_due_date.setDisabled(False)
        else:
            self.dateTimeEdit_due_date.setDisabled(True)
        self.hasDueDate = not self.hasDueDate
        self.setDueDateText()

    @pyqtSlot()
    def loadAddSubGoal(self):
        '''
        @param: None

        @return: None

        @purpose:
        '''
        window = AddEditViewSubGoal(self.model, self.goalid) #open add AddEditViewGoal window, pass it model
        if window.exec():
            self.refreshListView()
        else:
            self.model.deleteSubGoal(self.goalid, self.model.getCurrSGID())

    @pyqtSlot()
    def loadCompleteSubGoal(self):
        '''
        @param: None

        @return: None

        @purpose:
        '''
        if self.subGoalIsSelected():
            subgoalid = self.selectedListItemId
            self.model.completeSubGoal(self.goalid, subgoalid)
            self.refreshListView()

    @pyqtSlot()
    def loadEditViewSubGoal(self):
        '''
        @param: None

        @return: None

        @purpose:
        '''
        if self.subGoalIsSelected():
            subgoalid = self.selectedListItemId
            window = AddEditViewSubGoal(self.model, self.goalid, subgoalid) #open AddEditViewSubGoal window, passes it model and subgoal id
            if window.exec():
                self.refreshListView()
            else:
                self.lineEdit_category.setStyleSheet("border: 1px solid red;")

    @pyqtSlot()
    def loadDeleteSubGoal(self):
        '''
        @param: None

        @return: None

        @purpose:
        '''
        if self.subGoalIsSelected():
            subgoalid = self.selectedListItemId
            self.model.deleteSubGoal(self.goalid, subgoalid)
            self.refreshListView()

    @pyqtSlot()
    def loadSaveGoal(self):
        '''
        @param: None

        @return: None

        @purpose:
        '''
        goalName = self.lineEdit_goal_name.text()
        date = self.dateTimeEdit_due_date.date()
        time = self.dateTimeEdit_due_date.time()
        dueDate = None if not self.hasDueDate else datetime(date.year(), date.month(), date.day(), time.hour(), time.minute(), time.second())
        category = self.lineEdit_category.text()
        if self.radio_priority_low.isChecked():
            priority = 3
        elif self.radio_priority_medium.isChecked():
            priority = 2
        else:
            priority = 1
        memo = self.textEdit.toPlainText()

        if goalName.strip() != "" and category.strip() != "":
            self.model.editGoal(self.goalid, {"name": goalName, "category": category, "priority": priority, "memo": memo, "dueDate": dueDate})
            self.accept() #exit dialog
        else:
            if goalName.strip() == "":
                self.lineEdit_goal_name.setStyleSheet("border: 1px solid red;")
            else:
                self.lineEdit_goal_name.setStyleSheet("border: none;")
            if category.strip() == "":
                self.lineEdit_category.setStyleSheet("border: 1px solid red;")
            else:
                self.lineEdit_category.setStyleSheet("border: none")
                
 

    @pyqtSlot()
    def loadCancelGoal(self):
        '''
        @param: None

        @return: None

        @purpose:
        '''
        self.close() #exit dialog

    @pyqtSlot()
    def setDueDateText(self):
        '''
        @param: None

        @return: None

        @purpose:
        '''
        date = self.dateTimeEdit_due_date.date()
        time = self.dateTimeEdit_due_date.time()
        dueDate = datetime(date.year(), date.month(), date.day(), time.hour(), time.minute(), time.second())
        if not self.hasDueDate:
            self.label_goal_name_4.setText("No Due Date")
            self.dateTimeEdit_due_date.setDisabled(True)
        elif dueDate > datetime.now():
            self.label_goal_name_4.setText(str((dueDate - datetime.now()).days) + " Days Until Due")
            self.dateTimeEdit_due_date.setDisabled(False)
        else:
            self.label_goal_name_4.setText("Overdue")
            self.dateTimeEdit_due_date.setDisabled(False)

    '''********************CLASS METHODS OPERATIONS********************'''
    def subGoalIsSelected(self):
        '''
        @param: None

        @return: (boolean)

        @purpose:
        '''
        return self.selectedListItemId != None

    def setChosenItem(self):
        '''
        @param: None

        @return: None

        @purpose:
        '''
        selectedlist = [item.data(Qt.UserRole) for item in self.listWidget.selectedItems()]
        if not selectedlist:
            self.selectedListItemId = None
        else:
            self.selectedListItemId = selectedlist[0]

    def addToListView(self, _subGoalList):
        '''
        @param: _subGoalList (List)

        @return: None

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
        @param: None

        @return: None

        @purpose:
        '''
        if len(self.model.getGoalList()) != 0:
            subGoalList = self.model.getSubGoalList(self.goalid)
            self.addToListView(subGoalList)


class AddEditViewSubGoal(QDialog):
    def __init__(self, _model, _goalid, _subgoalid = None):
        '''
        @param: _model (Model)
        @param: _goalid (integer)
        @param: _subgoalid (integer) - defaults to None

        @return: None

        @purpose:
        '''
        super(AddEditViewSubGoal, self).__init__()
        
        loadUi(UI_PATHS["AddEditViewSubgoal"], self) # Load the AddEditViewSubGoal UI

        #Class Variables
        self.model = _model
        self.goalid = _goalid
        self.subgoalid = _subgoalid

        #Signals
        self.push_save.clicked.connect(self.loadSaveSubGoal)
        self.push_cancel.clicked.connect(self.loadCancelSubGoal)

        if self.subgoalid == None:
            self.setWindowTitle('Add Subgoal')
            self.subgoalid = self.model.addSubGoal(self.goalid)
        else:
            self.setWindowTitle('Edit/View Subgoal')
            subgoal = self.model.getSubGoal(self.goalid, self.subgoalid)
            self.lineEdit.setText(subgoal.getName())
            if subgoal.isComplete():
                self.label_status.setText("Status: Complete")
            else:
                self.label_status.setText("Status: Incomplete")

    @pyqtSlot()
    def loadSaveSubGoal(self):
        '''
        @param: None

        @return: None

        @purpose:
        '''
        if self.lineEdit.text().strip() != "":
            self.model.editSubGoal(self.goalid, self.subgoalid, {"name": str(self.lineEdit.text())}) #update subGoal information model
            self.accept() #exit dialog
        else:
            self.lineEdit.setStyleSheet("border: 1px solid red;")    

    @pyqtSlot()
    def loadCancelSubGoal(self):
        '''
        @param: None

        @return: None

        @purpose:
        '''
        self.close() #exit dialog


class Analysis(QDialog):
    def __init__(self, _model, _goalid): #FUNCTION NEEDS TO BE BUILT
        '''
        @param: _model (Model)
        @param: _goalid (integer)

        @return:

        @purpose:
        '''
        #how do I access these functions? ask noah. is everything connected right

        super(Analysis, self).__init__()
        
        loadUi(UI_PATHS["Analysis"], self) # Load the AddEditViewSubGoal UI

        self.ag = AnalysisGenerator()

        self.canvas = Canvas(self, width=4.5, height=4)
        self.canvas.move(0,0)
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        self.resize(width + 1, height)
        #print(self.frameGeometry().width(), height)
        self.canvas.plot_bar()

        self.model = _model
        self.goalid = _goalid

        string1 = "This Goal took you " + self.ag.getActiveTime(self.goalid, self.model) + " days to complete"
        if self.ag.getFasterSlower(self.goalid, self.model) == -10000:
            string2 = ""
        else:
            if self.ag.getFasterSlower(self.goalid, self.model) > 0:
                string2 = "That is " + str(self.ag.getFasterSlower(self.goalid, self.model)) + " days faster than anticipated"
            else:
                string2 = "That is " + str(self.ag.getFasterSlower(self.goalid, self.model)) + " days slower than anticipated" 
        string3 =   "You spend on average " + self.ag.getAverageTime(self.goalid, self.model) + " hours a day working on your goal"

        greater_val = max(self.ag.getBeforeDuedate(self.model), self.ag.getAfterDuedate(self.model))
        
        if greater_val == self.ag.getBeforeDuedate(self.model):
            string4 =  "You completed " + str(greater_val) + "% of your goals faster than aniticpated!"
            string5 =  "Great job, keep up the good work!"
            string6 =  ""

        if greater_val != self.ag.getBeforeDuedate(self.model):
            string4 =  "You completed " + str(greater_val) + "% of your goals slower than aniticpated."
            string5 =  "You seem to have trouble sticking to your goals. Consider giving"
            string6 =  "yourself more time next time!"

        self.label_daystook.setText(string1)
        self.label_fasterslower.setText(string2)
        self.label_numhours.setText(string3)
        self.label_lowerlinetext_1.setText(string4)
        self.label_lowerlinetext_2.setText(string5)
        self.label_lowerlinetext_3.setText(string6)
        #self.aboutToQuit.connect(stopAnimationOnExit)
    
    def closeEvent(self, event):
        self.stopAnimationOnExit()
        event.accept()

    def stopAnimationOnExit(self):
        self.canvas.stopAnimation()


class UncompletedAnalysis(QDialog):
    def __init__(self, _model): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        super(UncompletedAnalysis, self).__init__()
        
        self.ui = loadUi(UI_PATHS["UncompletedAnalysis"], self) # Load the AddEditViewSubGoal UI

        self.model = _model
        self.ag = AnalysisGenerator()
        self.canvas = Canvas(self, width=7, height=4)
        self.canvas.move(0,0)
        self.canvas.plot_ring()

        greater_val = max(self.ag.getBeforeDuedate(self.model), self.ag.getAfterDuedate(self.model))
        
        if greater_val == self.ag.getBeforeDuedate(self.model):
            string1 =  "You completed " + str(greater_val) + "% of your goals faster than aniticpated!"
            string2 =  "Great job, keep up the good work!"
            string3 =  ""

        if greater_val != self.ag.getBeforeDuedate(self.model):
            string1 =  "You completed " + str(greater_val) + "% of your goals slower than aniticpated."
            string2 =  "You seem to have trouble sticking to your goals. Consider giving"
            string3 =  "yourself more time next time!"

        self.label_lowerlinetext_1.setText(string1)
        self.label_lowerlinetext_2.setText(string2)
        self.label_lowerlinetext_3.setText(string3)

    def closeEvent(self, event):
        self.stopAnimationOnExit()
        event.accept()

    def stopAnimationOnExit(self):
        self.canvas.stopAnimation()
