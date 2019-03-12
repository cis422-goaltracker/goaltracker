"""
    Authors: Noah Palmer, Holly Hardin, Jiazhen Cao, Kellie Hawks, Isaac Lance, Weigang An
    Date: 03/10/2019
    CIS 422
    GoalTracker

    Reference [0]: https://stackoverflow.com/questions/41772092/how-can-i-get-all-selected-items-for-a-qlistwidget-when-the-user-interacts-with

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
                self.effortStopWatch_lcd = QTimer() #create a QTimer object
                self.effortStopWatch_lcd.start() #start the Timer
                self.effortStopWatch_lcd.timeout.connect(lambda : self.onTimerOut(goalstarttime)) #comment on the next line:
                #calculate the time difference between the current time and the last time used the effort tracker
                #display it on the LCD widget

            if goal.isComplete(): #if the goal is complete
                self.label_status.setText("Status: Complete") #set the status as complete
            else:
                self.label_status.setText("Status: Incomplete") #else, set the status as incomplete
            print(goal.getPriority())
            if goal.getPriority() == 3: #if the priority is 3
                self.radio_priority_low.setChecked(True) #set low as checked
            elif goal.getPriority() == 2: #if the priority is 2
                self.radio_priority_medium.setChecked(True) #set medium as checked
            else:
                self.radio_priority_high.setChecked(True) #else, set high as checked

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
            self.dateTimeEdit_due_date.setDisabled(True) #disable the due date editor
            self.checkBox_due_date.setDisabled(True) #disable the checkbox editor
            self.push_effort.setDisabled(True) #disable the effort tracker
            self.push_add_subgoal.setDisabled(True) #disable the add subgoal button
            self.label_goal_name_4.setText("") #set status to blank
        self.push_effort.setMinimumWidth(400)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.display("0:00:00")

    '''********************PYQTSLOT OPERATIONS********************'''

    @pyqtSlot()
    def toggleEffortTracker(self):
        '''
        @param: None

        @return: None

        @purpose: Toggles the effort tracker from on to off depending if it is currently running or not.
        '''
        self.effortStopWatch_lcd = QTimer() #initialize a new QTimer object upon stop.
        if self.model.isEffortTracking(self.goalid): #if the effort tracker is current running for the goalid
            self.model.stopEffortTracker(self.goalid) #stop the effort tracker
            self.push_effort.setText("Start Effort Tracker") #set text to say start effort tracker
            #time.sleep(1)
            self.lcdNumber.display("0:00:00")
            self.effortStopWatch_lcd.setSingleShot(True) #set the QTimer Object only use once
            self.effortStopWatch_lcd.stop() #stop the QTimer
        else:
            self.model.startEffortTracker(self.goalid) #start the effort tracker
            self.push_effort.setText("Stop Effort Tracker") #set the text to say stop effort tracker        
            self.effortStopWatch_lcd.start() #start the QTimer counting time
            temp = datetime.now() #assign the current time to temp for future subtraction
            self.effortStopWatch_lcd.timeout.connect(lambda : self.onTimerOut(temp))
            #calculate the time difference between the current time and the time started the effort tracker
            #display it on the LCD widget

    @pyqtSlot()
    def toggleDueDate(self):
        '''
        @param: None

        @return: None

        @purpose: Toggles the duedate editing ability
        '''
        if self.hasDueDate: #if has duedate
            self.dateTimeEdit_due_date.setDisabled(False) #set disabled to false
        else:
            self.dateTimeEdit_due_date.setDisabled(True) #otherwise, set disabled to true
        self.hasDueDate = not self.hasDueDate #flip hasDueDate value
        self.setDueDateText() #reset status

    @pyqtSlot()
    def loadAddSubGoal(self):
        '''
        @param: None

        @return: None

        @purpose: opens the add subgoal window
        '''
        window = AddEditViewSubGoal(self.model, self.goalid) #open add AddEditViewGoal window, pass it model and a goalid
        if window.exec(): #if accepted upon exit
            self.refreshListView() #refresh list
        else:
            self.model.deleteSubGoal(self.goalid, self.model.getCurrSGID()) #otherwise, delete the subgoal

    @pyqtSlot()
    def loadCompleteSubGoal(self):
        '''
        @param: None

        @return: None

        @purpose: Completes the subgoal that is selected
        '''
        if self.subGoalIsSelected(): #if a subgoal is selected
            subgoalid = self.selectedListItemId #get the subgoal id of selected item
            self.model.completeSubGoal(self.goalid, subgoalid) #complete the subgoal
            self.refreshListView() #refresh the list view of subgoals

    @pyqtSlot()
    def loadEditViewSubGoal(self):
        '''
        @param: None

        @return: None

        @purpose: opens the editor for the subgoal
        '''
        if self.subGoalIsSelected(): #if a subgoal is selected
            subgoalid = self.selectedListItemId #get the selected subgoal's id
            window = AddEditViewSubGoal(self.model, self.goalid, subgoalid) #open AddEditViewSubGoal window, passes it model and subgoal id
            if window.exec(): #if accepted
                self.refreshListView() #refresh the list

    @pyqtSlot()
    def loadDeleteSubGoal(self):
        '''
        @param: None

        @return: None

        @purpose: deletes the selected subgoal
        '''
        if self.subGoalIsSelected(): #if a subgoal is selected
            subgoalid = self.selectedListItemId #get the subgoal id
            self.model.deleteSubGoal(self.goalid, subgoalid) #delete the subgoal
            self.refreshListView() #refresh the list view

    @pyqtSlot()
    def loadSaveGoal(self):
        '''
        @param: None

        @return: None

        @purpose: saves the goal state information
        '''
        goalName = self.lineEdit_goal_name.text() #gets the name
        date = self.dateTimeEdit_due_date.date() #gets the date
        time = self.dateTimeEdit_due_date.time() #gets the time
        dueDate = None if not self.hasDueDate else datetime(date.year(), date.month(), date.day(), time.hour(), time.minute(), time.second()) #creates a datetime object
        category = self.lineEdit_category.text() #gets the category
        if self.radio_priority_low.isChecked(): #if low priority is checked
            priority = 3 #set priority to 3
        elif self.radio_priority_medium.isChecked(): #if medium priority is checked
            priority = 2 #set priority to 2
        else:
            priority = 1 #else, set priority to 1
        memo = self.textEdit.toPlainText() #get the memo

        overDue = False #sets overdue to false
        if dueDate != None: #if duedate doesn't equal none
            if dueDate <= datetime.now(): #if duedate is less than or equal to now
                overDue = True #overdue is true

        if goalName.strip() != "" and category.strip() != "" and not overDue: #if valid
            self.model.editGoal(self.goalid, {"name": goalName, "category": category, "priority": priority, "memo": memo, "dueDate": dueDate}) #save goal information
            self.accept() #exit dialog
        else:
            if goalName.strip() == "": #if goal is empty
                self.lineEdit_goal_name.setStyleSheet("border: 1px solid red;") #highlight in red
            else:
                self.lineEdit_goal_name.setStyleSheet("border: none;") #else reset
            if category.strip() == "": #if category is empty
                self.lineEdit_category.setStyleSheet("border: 1px solid red;") #highlight in red
            else:
                self.lineEdit_category.setStyleSheet("border: none") #else, reset
            if overDue: #if it is overdue
                self.dateTimeEdit_due_date.setStyleSheet("border: 1px solid red;") #highlight in red
            else:
                self.dateTimeEdit_due_date.setStyleSheet("border: none") #else, reset
                
    @pyqtSlot()
    def loadCancelGoal(self):
        '''
        @param: None

        @return: None

        @purpose: closes the dialog
        '''
        self.close() #exit dialog

    @pyqtSlot()
    def setDueDateText(self):
        '''
        @param: None

        @return: None

        @purpose: sets the status of the goal as a notification depending on status
        '''
        date = self.dateTimeEdit_due_date.date() #gets the date
        time = self.dateTimeEdit_due_date.time() #gets the time
        dueDate = datetime(date.year(), date.month(), date.day(), time.hour(), time.minute(), time.second()) #creates datetime object
        if not self.hasDueDate: #if doesn't have due date
            self.label_goal_name_4.setText("No Due Date") #set status as no due date
            self.dateTimeEdit_due_date.setDisabled(True) #disable date editor
        elif dueDate > datetime.now(): #if not overdue
            self.label_goal_name_4.setText(str((dueDate - datetime.now()).days) + " Days Until Due") #tell how many days till due
            self.dateTimeEdit_due_date.setDisabled(False) #enable date editor
        else:
            self.label_goal_name_4.setText("Overdue") #else, set status as ovedue
            self.dateTimeEdit_due_date.setDisabled(False) #enable date editor

    '''********************CLASS METHODS OPERATIONS********************'''
    def onTimerOut(self, start_time):
        '''
        @param: start_time

        @return: void function

        @purpose: calculate the time difference between the current time and the effort tracker start time,
                  display it on the LCD widget.
        '''
        self.lcdNumber.display(str(datetime.now() - start_time).split('.', 2)[0])
        #split()[0] format the datetime object into a format used by LCD widget

    def subGoalIsSelected(self):
        '''
        @param: None

        @return: (boolean)

        @purpose: returns if a subgoal is selected
        '''
        return self.selectedListItemId != None #returns true if not equal to none, else false

    def setChosenItem(self):
        '''
        @param: None

        @return: None

        @purpose: sets the selected item id when an item gets selected
        Reference [0]: https://stackoverflow.com/questions/41772092/how-can-i-get-all-selected-items-for-a-qlistwidget-when-the-user-interacts-with
        '''
        selectedlist = [item.data(Qt.UserRole) for item in self.listWidget.selectedItems()] #gets list of selected items
        if not selectedlist: #if selected list is empty
            self.selectedListItemId = None #set id to none
        else:
            self.selectedListItemId = selectedlist[0] #else, set id to selected id

    def addToListView(self, _subGoalList):
        '''
        @param: _subGoalList (List)

        @return: None

        @purpose: adds a subgoallist to the listview
        '''
        self.listWidget.clear() #clears the list widget
        for subGoal in _subGoalList: #cycles through subgoal list
            item = QListWidgetItem() #creats a list widget item
            item.setText(subGoal.toString()) #sets the text of the item
            item.setData(Qt.UserRole, subGoal.getId()) #sets the data (id) of the item
            self.listWidget.addItem(item) #adds the item to the list widget

    def refreshListView(self):
        '''
        @param: None

        @return: None

        @purpose: refreshes the list view
        '''
        if len(self.model.getGoalList()) != 0: #if the length of the goal list doesn't equal 0
            subGoalList = self.model.getSubGoalList(self.goalid) #gets the goal's subgoal list
            self.addToListView(subGoalList) #adds the subgoal list  to the the list view


class AddEditViewSubGoal(QDialog):
    def __init__(self, _model, _goalid, _subgoalid = None):
        '''
        @param: _model (Model)
        @param: _goalid (integer)
        @param: _subgoalid (integer) - defaults to None

        @return: None

        @purpose: intializes the add edit view subgoal window, setting it to either add subgoal or editview subgoal
        '''
        super(AddEditViewSubGoal, self).__init__() #initializes the parent window
        
        loadUi(UI_PATHS["AddEditViewSubgoal"], self) # Load the AddEditViewSubGoal UI

        #Class Variables
        self.model = _model #initializes the model
        self.goalid = _goalid #sets the goalid
        self.subgoalid = _subgoalid #set the subgoal id

        #Signals
        self.push_save.clicked.connect(self.loadSaveSubGoal) #sets save subgoal signal
        self.push_cancel.clicked.connect(self.loadCancelSubGoal) #sets cancel subgoal signal

        if self.subgoalid == None: #if subgoal id is none, its an add operation
            self.setWindowTitle('Add Subgoal') #sets window title
            self.subgoalid = self.model.addSubGoal(self.goalid) #retrieves the subgoal id from the model
        else: #otherwise, its an edit view operation
            self.setWindowTitle('Edit/View Subgoal') #sets the window title
            subgoal = self.model.getSubGoal(self.goalid, self.subgoalid) #gets the subgoal from the model
            self.lineEdit.setText(subgoal.getName()) #sets the subgoal name
            if subgoal.isComplete(): #if its complete
                self.label_status.setText("Status: Complete") #sets status as complete
            else:
                self.label_status.setText("Status: Incomplete") #otherwise, incomplete

    '''********************PYQTSLOT OPERATIONS********************'''
    @pyqtSlot()
    def loadSaveSubGoal(self):
        '''
        @param: None

        @return: None

        @purpose: saves the subgoal
        '''
        if self.lineEdit.text().strip() != "": #if goal name isn't blank
            self.model.editSubGoal(self.goalid, self.subgoalid, {"name": str(self.lineEdit.text())}) #update subGoal information model
            self.accept() #exit dialog
        else:
            self.lineEdit.setStyleSheet("border: 1px solid red;")    #otherwise, highlights 

    @pyqtSlot()
    def loadCancelSubGoal(self):
        '''
        @param: None

        @return: None

        @purpose: closes dialog
        '''
        self.close() #exit dialog


class Analysis(QDialog):
    def __init__(self, _model, _goalid):
        '''
        @param: _model (Model)
        @param: _goalid (integer)

        @return: None

        @purpose: Analysis the data of the model, the completed goal selected, display graph analysis, and statistics.
        '''
        super(Analysis, self).__init__()
        
        loadUi(UI_PATHS["Analysis"], self) # Load the AddEditViewSubGoal UI
        self.setWindowTitle("Completed Goal Analysis") # set the child window title
        self.model = _model # assign model object
        self.goalid = _goalid # assign goalid
        self.ag = AnalysisGenerator(_goalid, _model) # create AnalysisGenerator to process data
        #FAKE TESTING EFFORT DATA
        '''
        for i in range(6):
            start = datetime(2019, 2, 17 + i, 0 + i, 30, 30, 400000)
            end = datetime(2019, 2, 17 + i, 4 + 2 * i, 30, 30, 400000)
            self.model.manuallyInputEffort(self.goalid, start, end)
        '''
        self.datesList = self.ag.tranformDatesList() # get a list of dates that have effort tracker data
        self.valuesList = self.ag.tranformValuesList() # get a list of effort tracker durations related to dates in datesList
        self.canvas = Canvas(self) # create a Canvas object
        self.canvas.plot_bar(self.datesList, self.valuesList) # call the plot_bar function to plot bar chart
        layout = self.gridLayout # get the layout named 'gridLayout' of the ui file
        layout.addWidget(self.canvas, 0, 0) # add the canvas widget to layout
        string1 = "This Goal took you {0:.2f} days to complete.".format(self.ag.getActiveTime()) # assign a string with a goals' active time
        if self.ag.getFasterSlower() == False: # check if a goal has due date
            string2 = "This Goal doesn't have an anticipated due date." # assign a string for message
        else: # if a goal has due date
            if self.ag.getFasterSlower() > 0: # if a goal finished before the due date
                string2 = "That is {0:.2f} days faster than anticipated.".format(self.ag.getFasterSlower())
                # assign the message string to show how many days before the due date
            else: # if a goal finished after the anticipated due date
                string2 = "That is {0:.2f} days slower than anticipated.".format(self.ag.getFasterSlower())
                # assign the message string to show how many days late than the due date.
        string3 =   "You spend on average {0:.1f} hours a day working on your goal.".format(self.ag.getAverageTime())
        # assign the message string to show the average hours spent on the goal

        greater_val = max(self.ag.getBeforeDuedate(), self.ag.getAfterDuedate())
        # get the greater one of the two dates
        
        if greater_val == self.ag.getBeforeDuedate(): # if the greater date is the beforeDueDate
            string4 =  "You completed {0:.2f}% of your goals faster than anticipated!".format(greater_val)
            # assign a message string that display what percentage faster than the anticipated date
            string5 =  "Great job, keep up the good work!" # assign message string
            string6 =  "" # assign message string

        if greater_val != self.ag.getBeforeDuedate(): # if the greater date is the afterDueDate
            string4 =  "You completed {0:.2f}% of your goals slower than anticipated.".format(greater_val)
            # assign a message string that display what percentage slower than the anticipated date
            string5 =  "You seem to have trouble sticking to your goals. Consider giving" # assign message string
            string6 =  "yourself more time next time!" # assign message string

        self.label_daystook.setText(string1) # set the label text 
        self.label_fasterslower.setText(string2) # set the label text 
        self.label_numhours.setText(string3) # set the label text 
        self.label_lowerlinetext_1.setText(string4) # set the label text 
        self.label_lowerlinetext_2.setText(string5) # set the label text 
        self.label_lowerlinetext_3.setText(string6) # set the label text 
        #self.aboutToQuit.connect(stopAnimationOnExit)
    
    def closeEvent(self, event):
        '''
        Override the closeEvent function of the qt
        @param: event

        @return: None

        @purpose: close the child window with animation stoped
        '''
        if len(self.valuesList) != 0: # if percentage is not 0
            self.stopAnimationOnExit() # stop the animation
        event.accept() # close the child window

    def stopAnimationOnExit(self):
        '''
        @param: None

        @return: None

        @purpose: call the stopAnimation function
        '''
        self.canvas.stopAnimation() # call the stopAnimation of the canvas object


class UncompletedAnalysis(QDialog):
    def __init__(self, _model, _goalid):
        '''
        @param: _model (Model)
        @param: _goalid (integer)

        @return: None

        @purpose: Analysis the data of the model, the incompleted goal selected, display graph analysis, and statistics.
        '''
        super(UncompletedAnalysis, self).__init__()

        loadUi(UI_PATHS["UncompletedAnalysis"], self) # Load the AddEditViewSubGoal UI
        self.setWindowTitle("Uncompleted Goal Analysis") # set the child window title
        self.model = _model # assign model object
        self.goalid = _goalid # assign goalid
        self.ag = AnalysisGenerator(_goalid, _model) # create an AnalysisGenerator object
        self.finished_percentage = self.ag.trackProgress() * 100 # get finished subgoal percentage 
        self.canvas = Canvas(self) # create a Canvas object
        layout = self.gridLayout_2 # get the layout named 'gridLayout_2' of the ui file
        layout.addWidget(self.canvas, 0, 0) # add the widget to the layout
        self.canvas.plot_ring(self.finished_percentage, 100 - self.finished_percentage) # call the plot_ring to plot the ring chart

        greater_val = max(self.ag.getBeforeDuedate(), self.ag.getAfterDuedate())
        # get the greater one of the two dates

        if greater_val == self.ag.getBeforeDuedate(): # if the greater date is the beforeDueDate
            string1 =  "You completed {0:.2f}% of your goals faster than aniticpated!".format(greater_val)
            # assign a message string that display what percentage faster than the anticipated date
            string2 =  "Great job, keep up the good work!" # assign a message string
            string3 =  "" # assign a message string

        if greater_val != self.ag.getBeforeDuedate(): # if the greater date is the afterDueDate
            string1 =  "You completed {0:.2f}% of your goals slower than aniticpated.".format(greater_val)
            # assign a message string that display what percentage slower than the anticipated date
            string2 =  "You seem to have trouble sticking to your goals. Consider giving" # assign a message string
            string3 =  "yourself more time next time!" # assign a message string

        self.label_lowerlinetext_1.setText(string1) # set the text to the label
        self.label_lowerlinetext_2.setText(string2 + string3) # set the text to the label
        #self.label_lowerlinetext_3.setText(string3)

    def closeEvent(self, event):
        '''
        Override the closeEvent function of the qt
        @param: event

        @return: None

        @purpose: close the child window with animation stoped
        '''
        if self.finished_percentage != 0: # if percentage is not 0
            self.stopAnimationOnExit() # stop the animation
        event.accept() # close the child window

    def stopAnimationOnExit(self):
        '''
        @param: None

        @return: None

        @purpose: call the stopAnimation function
        '''
        self.canvas.stopAnimation() # call the stopAnimation of the canvas object
