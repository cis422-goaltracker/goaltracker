"""
    Authors: Noah Palmer, Holly Hardin, Jiazhen Cao, Kellie Hawks, Isaac Lance, Weigang An
    Date: 03/09/2019
    CIS 422
    GoalTracker

"""
#System Imports
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime, timedelta
import pyqtgraph as pg
import time
import threading

#Module Imports
from Goal import Goal, SubGoal
from Model import Model
from FileManager import FileManager
from AnalysisGenerator import AnalysisGenerator
from GenerateGraph import Canvas

# Global variable for storing UI files
UI_PATHS = {"MainWindow": "../UI/MainWindow.ui", "AddEditViewGoal": "../UI/AddEditViewGoal.ui", "AddEditViewSubgoal": "../UI/AddEditViewSubgoal.ui", "Analysis": "../UI/Analysis.ui", "UncompletedAnalysis": "../UI/UncompletedAnalysis.ui"}

class AddEditViewGoal(QDialog):
    def __init__(self, _model, _goalid = None):
        '''
        @param: _model (Model)
        @param: _goalid (integer) - defaults to None

        @return: None

        @purpose: Initializes the Add/Edit/View Goal window to either Add Goal or Edit/View Goal
        '''
        super(AddEditViewGoal, self).__init__() #Initializes parent constructor
        
        loadUi(UI_PATHS["AddEditViewGoal"], self) # Load the AddEditViewGoal UI

        #Class Variables
        self.model = _model #intializes the model
        self.goalid = _goalid #initializes the goal id
        self.selectedListItemId = None #starts the selected item as none
        self.hasDueDate = True #defaults hasDueDate to true
        self.timerOn = False #defaults timeOn to False

        #Signals
        self.push_effort.clicked.connect(self.toggleEffortTracker) #set up effort tracker signal
        self.checkBox_due_date.clicked.connect(self.toggleDueDate) #set up toggle due date signal
        self.push_add_subgoal.clicked.connect(self.loadAddSubGoal) # set up add subgoal signal
        self.push_complete_subgoal.clicked.connect(self.loadCompleteSubGoal) #set up complete subgoal signal
        self.push_edit_view_subgoal.clicked.connect(self.loadEditViewSubGoal) #set up edit view subgoal signal
        self.push_delete_subgoal.clicked.connect(self.loadDeleteSubGoal) #set up delete subgoal signal
        self.push_save.clicked.connect(self.loadSaveGoal) #set up save goal signal
        self.push_cancel.clicked.connect(self.loadCancelGoal) #set up cancel goal signal
        self.listWidget.itemSelectionChanged.connect(self.setChosenItem) #set up chosen item signal
        self.dateTimeEdit_due_date.dateTimeChanged.connect(self.setDueDateText) #set up due date text signal

        if self.goalid == None: #if there is no goal id, its an add goal process
            self.setWindowTitle('Add Goal') #sets the window title
            self.goalid = self.model.addGoal() #gets a new goalid for this new goal
            self.dateTimeEdit_due_date.setDate(QDate.currentDate()) #sets date to the current date
            self.dateTimeEdit_due_date.setTime(QTime.currentTime()) #sets time to the current time
            self.label_goal_name_4.setText("") #hides the status text
        else: #if there is a goal id, its an edit/view goal process
            self.setWindowTitle('Edit/View Goal') #sets the window title
            goal = self.model.getGoal(self.goalid) #retrieves the goal from the model
            self.lineEdit_goal_name.setText(goal.getName()) #sets the goal name section of the editor
            if self.model.isEffortTracking(self.goalid): #if the goal is currently tracking
                self.push_effort.setText("Stop Effort Tracker") #set the effort tracker to say stop effort tracker
                goalstarttime = self.model.peekEffortTracker(self.goalid) #retrieve the start time of the goal track from the effort tracker
                #@JIAZHEN, PUT CODE HERE TO SET THE TIMER
                #@JIAZHEN "goalstarttime" is when the goal started the effort tracker
                #@JIAZHEN I put your function "onTimerOut" in the Class Methods Section rather than the PyQTSlot Section, no code changed

            if goal.isComplete(): #if the goal is complete
                self.label_status.setText("Status: Complete") #set the status as complete
            else:
                self.label_status.setText("Status: Incomplete") #else, set the status as incomplete

            if goal.getPriority() == 3: #if the priority is 3
                self.radio_priority_low.isChecked() #set low as checked
            elif goal.getPriority() == 2: #if the priority is 2
                self.radio_priority_medium.isChecked() #set medium as checked
            else:
                self.radio_priority_high.isChecked() #else, set high as checked

            self.lineEdit_category.setText(goal.getCategory()) #set the category as the goal's category
            self.textEdit.setText(goal.getMemo()) #set the memo as the goal's memo
            self.refreshListView() #refresh the listview
            if goal.getDueDate() == None: #if no due date
                self.hasDueDate = False #set has due date to false
                self.checkBox_due_date.setChecked(True) #check the no due date checkbox
                self.dateTimeEdit_due_date.setDate(QDate.currentDate()) #set the date as the current date
                self.dateTimeEdit_due_date.setTime(QTime.currentTime()) #set the time as the current time
            else: #otherwise
                self.dateTimeEdit_due_date.setDate(goal.getDueDate()) #set date as the current duedate
                self.dateTimeEdit_due_date.setTime(goal.getDueDate().time()) #set time as the current due time
            self.setDueDateText() #update status

        if self.model.getGoal(self.goalid).isComplete(): #if the goal is complete
            self.dateTimeEdit_due_date.setDisabled(True)
            self.checkBox_due_date.setDisabled(True)
            self.push_effort.setDisabled(True)
            self.push_add_subgoal.setDisabled(True)
            self.label_goal_name_4.setText("")

        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.display("0:00:00")

    '''********************PYQTSLOT OPERATIONS********************'''

    @pyqtSlot()
    def toggleEffortTracker(self):
        '''
        @param: None

        @return: None

        @purpose:
        '''
        self.effortTimer_lcd = QTimer()
        self.lcdNumber.display("0:00:00")
        if self.model.isEffortTracking(self.goalid):
            self.model.stopEffortTracker(self.goalid)
            self.push_effort.setText("Start Effort Tracker")
            self.effortTimer_lcd.setSingleShot(True)
            self.effortTimer_lcd.stop()
        else:
            self.model.startEffortTracker(self.goalid)
            self.push_effort.setText("Stop Effort Tracker")          
            self.effortTimer_lcd.start()
            temp = datetime.now()
            self.effortTimer_lcd.timeout.connect(lambda : self.onTimerOut(temp))

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

        overDue = False
        if dueDate != None:
            if dueDate <= datetime.now():
                overDue = True

        if goalName.strip() != "" and category.strip() != "" and not overDue:
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
            if overDue:
                self.dateTimeEdit_due_date.setStyleSheet("border: 1px solid red;")
            else:
                self.dateTimeEdit_due_date.setStyleSheet("border: none")
                
 

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
    def onTimerOut(self, start_time):
        '''
        @param: None

        @return: (boolean)

        @purpose:
        '''
        self.lcdNumber.display(str(datetime.now() - start_time).split('.', 2)[0])

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
        self.listWidget.clear() #clears the list widget
        for subGoal in _subGoalList: #cycles through subgoal list
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
        self.model = _model
        self.goalid = _goalid
        self.ag = AnalysisGenerator(_goalid, _model)
        # ************************************ FAKE TESTING EFFORT DATA ******************************************************
        '''
        for i in range(6):
            start = datetime(2019, 2, 17 + i, 0 + i, 30, 30, 400000)
            end = datetime(2019, 2, 17 + i, 4 + 2 * i, 30, 30, 400000)
            self.model.manuallyInputEffort(self.goalid, start, end)
        '''
        # ************************************ Finish Faking *****************************************************************
        self.datesList = self.ag.tranformDatesList()
        self.valuesList = self.ag.tranformValuesList()
        self.canvas = Canvas(self, width=4.5, height=4)
        self.canvas.plot_bar(self.datesList, self.valuesList)
        layout = self.gridLayout
        layout.addWidget(self.canvas, 0, 0)
        string1 = "This Goal took you {0:.2f} days to complete.".format(self.ag.getActiveTime())
        if self.ag.getFasterSlower() == False:
            string2 = "This Goal doesn't have an anticipated due date."
        else:
            if self.ag.getFasterSlower() > 0:
                string2 = "That is {0:.2f} days faster than anticipated.".format(self.ag.getFasterSlower())
            else:
                string2 = "That is {0:.2f} days slower than anticipated.".format(self.ag.getFasterSlower())
        string3 =   "You spend on average {0:.1f} hours a day working on your goal.".format(self.ag.getAverageTime())

        greater_val = max(self.ag.getBeforeDuedate(), self.ag.getAfterDuedate())
        
        if greater_val == self.ag.getBeforeDuedate():
            string4 =  "You completed {0:.2f}% of your goals faster than aniticpated!".format(greater_val)
            string5 =  "Great job, keep up the good work!"
            string6 =  ""

        if greater_val != self.ag.getBeforeDuedate():
            string4 =  "You completed {0:.2f}% of your goals slower than aniticpated.".format(greater_val)
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
    def __init__(self, _model, _goalid): #FUNCTION NEEDS TO BE BUILT
        '''
        @param:

        @return:

        @purpose:
        '''
        super(UncompletedAnalysis, self).__init__()

        loadUi(UI_PATHS["UncompletedAnalysis"], self) # Load the AddEditViewSubGoal UI
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setWindowTitle("Analysis")
        self.model = _model
        self.goalid = _goalid
        self.ag = AnalysisGenerator(_goalid, _model)
        self.finished_percentage = self.ag.trackProgress() * 100
        self.canvas = Canvas(self, width=7, height=4)
        layout = self.gridLayout_2
        layout.addWidget(self.canvas, 0, 0)
        self.canvas.plot_ring(self.finished_percentage, 100 - self.finished_percentage)

        greater_val = max(self.ag.getBeforeDuedate(), self.ag.getAfterDuedate())
        
        if greater_val == self.ag.getBeforeDuedate():
            string1 =  "You completed {0:.2f}% of your goals faster than aniticpated!".format(greater_val)
            string2 =  "Great job, keep up the good work!"
            string3 =  ""

        if greater_val != self.ag.getBeforeDuedate():
            string1 =  "You completed {0:.2f}% of your goals slower than aniticpated.".format(greater_val)
            string2 =  "You seem to have trouble sticking to your goals. Consider giving"
            string3 =  "yourself more time next time!"

        self.label_lowerlinetext_1.setText(string1)
        self.label_lowerlinetext_2.setText(string2 + string3)
        #self.label_lowerlinetext_3.setText(string3)

    def closeEvent(self, event):
        if self.finished_percentage != 0:
            self.stopAnimationOnExit()
        event.accept()

    def stopAnimationOnExit(self):
        self.canvas.stopAnimation()
