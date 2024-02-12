import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import pandas as pd
import random
import MetaTrader5 as mt5
import datetime
from pytz import timezone
from apscheduler.schedulers.qt import QtScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from finalui import Ui_MainWindow
from pymongo import MongoClient
import certifi
import ssl 

mt5.initialize()

styles="""
QPushButton{
    /* background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #3498db, stop:1 #297fb8); */

    color: white;
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    /* background-color: #0096FF;      */
    margin: 5px;
     
    background-color:#343434
}

/* Hover state styles */
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #36454F, stop:1 #343434);
}

QMainWindow {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #5F9EA0,    /* Dark blue */
                                stop:1 #40E0D0);   /* Concentrated light blue */
}


#widget_3 {
    /*background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #78999f,    
                                stop:1 #9ac5cc);   */
     
    border: 1px solid#abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
    padding: 10px;         
}
#widget_4 {
    /*background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #78999f,    
                                stop:1 #9ac5cc);   */
     
    border: 1px solid#abdbe3;  
    border-radius: 5px;      
    margin: 20px;
    padding: 10px;            
}
#stackedWidget {
    /*background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #78999f,    
                                stop:1 #9ac5cc);   */
    /* background-color:#343434;
  */
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    /* background-color:#343434;
       */
    margin: 5px;   
}
#accountslabel {
    /*background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #78999f,    
                                stop:1 #9ac5cc);   */
     
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#Algolabel {
    /*background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #78999f,    
                                stop:1 #9ac5cc);   */
    /* background-color: #89afb6;  */
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#mt5label{
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#performancelabel
{
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
/* #widget_5 { */
    /*background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #78999f,    
                                stop:1 #9ac5cc);   */
    /* background-color: #89afb6;  */
    /* border: 1px solid #abdbe3;   */
    /* border-radius: 5px;       */
    /* margin: 5px;
            */
/* } */
#adjustparamslabel {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#activationlabel {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#accountpageperfotmancelabel {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#accountspagemt5label {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#mainlogo {
    /*background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #78999f,    
                                stop:1 #9ac5cc);   */
    /* background-color: #89afb6;  */
    /* border: 1px solid #abdbe3;   */
    border-radius: 5px;      
    margin: 12px;       
}
#logosub {
    /*background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #78999f,    
                                stop:1 #9ac5cc);   */
    /* background-color: #89afb6;  */
    /* border: 1px solid #abdbe3;   */
    border-radius: 5px;      
    margin-top: 15;       
}
#widget_34 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_33 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
QLineEdit {
    border: 1px solid #abdbe3;  
    border-radius: 5px;      
    margin: 2px; 
    padding: 3px;           
}
QLabel {
    color: white;
    text-align: center;
    margin: 8px; /* or other preferred alignment */
    /* Additional styles for QLabel */
}
#widget_72 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_8 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_51 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_14 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_15 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#frame2 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_13 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_36 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#algoadjustparamlabel {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#algoactivationlabel {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#statuslabel {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#filstatus {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_19 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_20 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_21 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_17 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_18 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}

#widget_2 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_9 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_12 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_11 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_24 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_23 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_25 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_26 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_9 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_2 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_71 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_41 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_46 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_47 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_46 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_49 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_50 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_53 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_60 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_56 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_58 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_59 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_63 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_46 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_62 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_39 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_64 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_65 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_12 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_36 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_37 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_38 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_39 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_40 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_22 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}

#widget_42 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_43 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_44 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
#widget_45 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}

QScrollArea {
    background: transparent;
}
QScrollArea > QWidget > QWidget {
    background: transparent;
}

/* QScrollBar:horizontal {
    height: 10;
} */

#widget_31 {
   
    border: 1px solid #abdbe3;  
    border-radius: 5px; 
    background-color:#343434;
      
    margin: 5px;
           
}
QTableWidget {
    background-color: transparent;  /* Ensure transparency from step 1 */
    border: none;  /* Remove default border */
    gridline-color: blue;  /* Set alternate row background color */
}

QHeaderView::section {
    padding: 0px;  /* Remove padding for cleaner lines */
    background-color: lightblue;  /* Optional custom header background */
}

QHeaderView::section[orientation="horizontal"] {
    border-bottom: 1px solid blue;  /* Set horizontal line color */
}
"""

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ca=certifi.where()
        self.client =MongoClient()
        self.db=self.client["agent_1"]
        self.trades=list(self.db["trades"].find())
        self.trades_df=pd.DataFrame(self.trades)
        self.scheduler=QtScheduler(timezone=timezone('Africa/Nairobi'))
        self.begin_max_value=0
        self.begin_min_value=0
        self.agent_activation_status=False
        
        
        self.setStyleSheet(styles)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialize_agent_data(self.get_balance())
        QtCore.QTimer.singleShot(10000, lambda:None )
        
    
        self.set_up_button()
        self.set_perforamnce_weekly_labels()
        self.set_perforamnce_monthly_labels()
        self.setdata()
        self.resetparans_btn()
        self.updateprams_btn()
        self.displayparameters()
        self.accountvalues()
        self.updateaccountvalues_btn()
        self.resetaccountvalues_btn()
        self.uiupdates()
        self.setliveprice()
        
        self.dynamicactivation()
        self.real_acivate_deactivate_btn()
        self.dynamic_month_date()
        self.setgrowthpercentage()
        QtCore.QCoreApplication.instance().aboutToQuit.connect(self.cleanup)
        
    def setliveprice(self):
        self.ui.filopentradeprofit.setText(str(self.get_open_profit()))
    def updatelivebalance(self):
        
        self.ui.filmainaccountbalance.setText(str(self.get_balance()))
        self.ui.flaccountbalance.setText(str(self.get_balance()))
        self.ui.fldailyperformace.setText(str(self.get_today_profit()))
    def updatelivetodaysprofit(self):
        self.ui.fldailyperformace.setText(str(self.get_today_profit()))
    
    
        
        
        
        
       
    def setdata(self):
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setRowCount(len(list(self.trades)))
        self.ui.tableWidget.setHorizontalHeaderLabels(["Time", "Lot Size", "Trade Type", "Profit"])
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode( QtWidgets.QHeaderView.Stretch)
        count=0
        for trade in self.trades:
            self.ui.tableWidget.setItem(count,0, QtWidgets.QTableWidgetItem(str(trade["trade_open"])))
            self.ui.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(str(trade["lot_size"])))
            self.ui.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(str(trade["trade_type"])))
            self.ui.tableWidget.setItem(count, 3, QtWidgets.QTableWidgetItem(str(trade["profit"])))
     
            count+=1
      
    def set_perforamnce_weekly_labels(self):
        if self.trades is None or len(self.trades)==0:
            self.ui.flweeklyprofit.setText(str(None))
            self.ui.flweekyprofday.setText(str(None))
            self.ui.flweeklyprofammount.setText(str(None))
            self.ui.flweekylossday.setText(str(None))
            self.ui.flweeklylossammount.setText(str(None))
            self.ui.filweeklyreport_totalprofit.setText(str(None))
            self.ui.filweekreporttotalbuy.setText(str(None))
            self.ui.filweekreporttotalbuyprofit.setText(str(None))
            self.ui.filweekreporttotalbuy_2.setText(str(None))
            self.ui.filweekreporttotalbuyprofit_2.setText(str(None))
            self.ui.filweekreporttotalbuy_3.setText(str(None))
            self.ui.filweekreporttotalbuy_4.setText(str(None))
            self.ui.filweekreporttotalbuyprofit_10.setText(str(None))
            self.ui.filweekreporttotalbuyprofit_9.setText(str(None))
            
            self.ui.filweekreporttotalbuyprofit_3.setText(str(None))
            self.ui.filweekreporttotalbuyprofit_4.setText(str(None))
            self.ui.filmainaccountbalance.setText(str(self.get_balance()))
            self.ui.filopentradeprofit.setText(str(self.get_open_profit()))
            self.ui.flaccountbalance.setText(str(self.get_balance()))
            self.ui.fldailyperformace.setText(str(self.get_today_profit()))
        
            
            
        else:
            self.ui.filmainaccountbalance.setText(str(self.get_balance()))
            self.ui.filopentradeprofit.setText(str(self.get_open_profit()))
            self.ui.flaccountbalance.setText(str(self.get_balance()))
            self.ui.fldailyperformace.setText(str(self.get_today_profit()))
            self.ui.flweeklyprofit.setText(str(self.get_weekly_data()[13]))
            self.ui.flweekyprofday.setText(str(self.get_weekly_data()[3]))
            self.ui.flweeklyprofammount.setText(str(self.get_weekly_data()[0]))
            self.ui.flweekylossday.setText(str(self.get_weekly_data()[2]))
            self.ui.flweeklylossammount.setText(str(self.get_weekly_data()[1]))
            self.ui.filweeklyreport_totalprofit.setText(str(self.get_weekly_data()[13]))
            self.ui.filweekreporttotalbuy.setText(str(self.get_weekly_data()[7]))
            self.ui.filweekreporttotalbuyprofit.setText(str(self.get_weekly_data()[6]))
            self.ui.filweekreporttotalbuy_2.setText(str(self.get_weekly_data()[10]))
            self.ui.filweekreporttotalbuyprofit_2.setText(str(self.get_weekly_data()[9]))
            self.ui.filweekreporttotalbuy_3.setText(str(self.get_weekly_data()[5]))
            self.ui.filweekreporttotalbuy_4.setText(str(self.get_weekly_data()[11]))
            self.ui.filweekreporttotalbuyprofit_10.setText(str(self.get_weekly_data()[14]))
            self.ui.filweekreporttotalbuyprofit_9.setText(str(self.get_weekly_data()[8]))
            
            self.ui.filweekreporttotalbuyprofit_3.setText(str(self.get_weekly_data()[4]))
            self.ui.filweekreporttotalbuyprofit_4.setText(str(self.get_weekly_data()[12]))
        
        
    def set_perforamnce_monthly_labels(self):
        if self.trades is None or len(self.trades)==0:
            # set all values to None
            self.ui.flmonthlyperformance.setText(str(None))
            self.ui.flmonthlossday.setText(str(None))
            self.ui.flmonthlossammount.setText(str(None))
            self.ui.flmontprofday.setText(str(None))
            self.ui.flmonthprofammount.setText(str(None))
            self.ui.filweeklyreport_totalprofit_2.setText(str(None))
            self.ui.filweekreporttotalbuy_5.setText(str(None))
            self.ui.filweekreporttotalbuy_6.setText(str(None))
            self.ui.filweekreporttotalbuyprofit_6.setText(str(None))
            self.ui.filweekreporttotalbuyprofit_12.setText(str(None))
            self.ui.filweekreporttotalbuyprofit_5.setText(str(None))
            self.ui.filweekreporttotalbuy_7.setText(str(None))
            self.ui.filweekreporttotalbuy_8.setText(str(None))
            self.ui.filweekreporttotalbuyprofit_8.setText(str(None))
            self.ui.filweekreporttotalbuyprofit_11.setText(str(None))
            self.ui.filweekreporttotalbuyprofit_7.setText(str(None))
     
        else:
            self.ui.flmonthlyperformance.setText(str(self.get_monthly_data()[14]))
            self.ui.flmonthlossday.setText(str(self.get_monthly_data()[15]))
            self.ui.flmonthlossammount.setText(str(self.get_monthly_data()[1]))
            self.ui.flmontprofday.setText(str(self.get_monthly_data()[16]))
            self.ui.flmonthprofammount.setText(str(self.get_monthly_data()[0]))
            self.ui.filweeklyreport_totalprofit_2.setText(str(self.get_monthly_data()[14]))
            self.ui.filweekreporttotalbuy_5.setText(str(self.get_monthly_data()[11]))
            self.ui.filweekreporttotalbuy_6.setText(str(self.get_monthly_data()[7]))
            self.ui.filweekreporttotalbuyprofit_6.setText(str(self.get_monthly_data()[6]))
            self.ui.filweekreporttotalbuyprofit_12.setText(str(self.get_monthly_data()[10]))
            self.ui.filweekreporttotalbuyprofit_5.setText(str(self.get_monthly_data()[4]))
            self.ui.filweekreporttotalbuy_7.setText(str(self.get_monthly_data()[13]))
            self.ui.filweekreporttotalbuy_8.setText(str(self.get_monthly_data()[9]))
            self.ui.filweekreporttotalbuyprofit_8.setText(str(self.get_monthly_data()[8]))
            self.ui.filweekreporttotalbuyprofit_11.setText(str(self.get_monthly_data()[12]))
            self.ui.filweekreporttotalbuyprofit_7.setText(str(self.get_monthly_data()[2]))
        
    def uiupdates(self):
        """
        Sets the general ui updates and appsregular database updates
        """
        
        accountbalancecronn=CronTrigger(minute=30)
        livepricecron=CronTrigger(second=30)
        profcronn=CronTrigger(hour=1)
        updateweeklycron=CronTrigger(hour=23,minute=30)
        updatetradescron=CronTrigger(minute=59)
        
        self.scheduler.add_job(self.set_perforamnce_weekly_labels,updateweeklycron)
        self.scheduler.add_job(self.set_perforamnce_monthly_labels, updateweeklycron)
        self.scheduler.add_job(self.setliveprice, livepricecron)
        self.scheduler.add_job(self.updatelivebalance, accountbalancecronn)
        self.scheduler.add_job(self.updatelivetodaysprofit, profcronn)
        self.scheduler.add_job(self.updatetrades, updatetradescron)
        self.scheduler.add_job(self.setgrowthpercentage, updateweeklycron)
        self.scheduler.start()


         
            
    def startagent(self):
        '''
        sets the apps agent parameters and running time of agent
        '''
        
        agentdata=self.db["agent_client_data"].find_one()
        appcode=agentdata['appcode']
        parameters_collection = self.db["agent_parameters"].find_one( {"appcode":appcode})
        maxdistance=parameters_collection['default_maxdistance']
        candlesize=parameters_collection['default_candlesize']
        df_profit=parameters_collection['default_profit']
        lotsize=agentdata['defaultlotsize']
        deviat=agentdata['defaultdeviation']
        
        tradetriger=CronTrigger(minute=15)
        updatetriger=CronTrigger(minute=17)
        closetriger=CronTrigger(hour=23 ,minute=45)
        self.scheduler.add_job(self.agent1,tradetriger,id='agent1',args=[maxdistance,candlesize,df_profit,lotsize,deviat]) 
        self.scheduler.add_job(self.closetrade,closetriger,id='closetrade')
        self.scheduler.add_job(self.update_min_max,updatetriger,id='updateminmax') 
        
    def deactivateagent(self):
        """dectivates agent and stops all agent jobs
        """
        
        self.scheduler.remove_job('agent1')
        self.scheduler.remove_job('closetrade')
        self.scheduler.remove_job('updateminmax')
        
    def get_first_values(self):
        """Used by agent to get anchor points for the day
        returns:None but updates global values
        """
        
        
        nowd=self.fget_data('GOLD',110)
        nowd['mtime']=pd.to_datetime(nowd['time'],unit='s')
        last_row = nowd.iloc[-2]
        target_date = last_row['mtime'].date()
        print('activated')
        # Filter the DataFrame for the specific day
        day_data = nowd[nowd['mtime'].dt.date == target_date]

        # Find the maximum and minimum points for the day
        max_price = day_data['High'].max()
        min_price = day_data['Low'].min()
        self.begin_max_value = max_price
        self.begin_min_value = min_price
    
    def update_min_max(self):
        """Updates the global max and min values for the day
        """
        
        nowd=self.fget_data('GOLD',110)
        nowd['mtime']=pd.to_datetime(nowd['time'],unit='s')
        last_row = nowd.iloc[-2]
        minv=self.begin_min_value
        maxv=self.begin_max_value
        price=last_row['Close']
        if price>maxv:
            self.begin_max_value=last_row['High']
            # print('updated upside')
        elif price<minv:
            # print('updated downside')
            self.begin_min_value=last_row['Low']
    def agent1(self,maxdistance,candlesize,df_profit,lotsize,deviat):
        """"
        Agent 1 Maain Trading Algorithm
        """
        
        nowd=self.fget_data('GOLD',110)
        nowd['mtime']=pd.to_datetime(nowd['time'],unit='s')
        last_row = nowd.iloc[-2]
        pg=last_row['mtime'].time()

        if datetime.time(3, 0) <= pg <= datetime.time(16, 30):
            
            maxv=begin_max_value
                    # print(maxv)
            minv=begin_min_value
            pos_info = mt5.positions_total()
            if pos_info is None:
                pass

            # Check if there are open positions or active orders
            elif pos_info==0:
                price=last_row['Close']
                if price>maxv:
                        if self.distance_checker(price,maxv,maxdistance)==0:
                            begin_max_value=last_row['High']
                        elif self.distance_checker(price,maxv,maxdistance)==1:
                            # print('i am here 4')
                            win_data=nowd.tail(6)
                            if self.find_status(win_data,candlesize):

                                sl_data=nowd.tail(3)
                                sl=int(self.find_sl(sl_data,1))-1.5
                                tp=price+df_profit
                                begin_max_value=last_row['High']
                                lot=lotsize
                                deviation=deviat
                                request = {"action": mt5.TRADE_ACTION_DEAL,"symbol": 'GOLD',"volume": lot,"type": mt5.ORDER_TYPE_BUY,"price": price,"sl": sl,"tp": tp,"deviation": deviation,"magic": 20022,"comment": "python script open","type_time": mt5.ORDER_TIME_GTC,"type_filling": mt5.ORDER_FILLING_IOC,}
                                mt5.order_send(request)

                elif price<minv:
                    if self.distance_checker(price,minv,maxdistance)==0:
                        begin_min_value=last_row['Low']

                    elif self.distance_checker(price,maxv,maxdistance)==1:
                        # print('i am here 4')
                        win_data=nowd.tail(6)
                        if self.find_status(win_data,candlesize):

                            sl_data=nowd.tail(3)
                            sl=int(self.find_sl(sl_data,-1))+1.5
                            tp=price-df_profit
                            begin_min_value=last_row['Low']
                            lot=lotsize
                            deviation=deviat
                            request = {"action": mt5.TRADE_ACTION_DEAL,"symbol": 'GOLD',"volume": lot,"type": mt5.ORDER_TYPE_SELL,"price": price,"sl": sl,"tp": tp,"deviation": deviation,"magic": 20022,"comment": "python script open","type_time": mt5.ORDER_TIME_GTC,"type_filling": mt5.ORDER_FILLING_IOC,}
                            mt5.order_send(request)



     
      
             
    def set_up_button(self):
        self.ui.homesub.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.accountssub.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_6))
        self.ui.algosub.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_7))
        self.ui.statsbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.setupbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.paramspagebtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.activatebtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))
        self.ui.algoparamsbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.algoactivalebtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))
        self.ui.accountpagestatsbtb.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.accountspagesetupbtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        
    def fget_data(self,currency,num_c):
        mt5.initialize()
        if not mt5.initialize():
            
            error_message = mt5.last_error()  # Store error message

    # Create a QMessageBox to display the error
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("MT5 Error")
            error_dialog.setText("MT5 initialization failed:")
            error_dialog.setDetailedText(error_message)
            error_dialog.exec()
            QtCore.QTimer.singleShot(120000, QtWidgets.QApplication.instance().quit)
            
        else:
        
            
            ohlc_data = pd.DataFrame(mt5.copy_rates_from_pos(currency, mt5.TIMEFRAME_M15, 0,num_c))
            ohlc_data.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close'}, inplace=True)
            ohlc_data.dropna(inplace=True)

            return ohlc_data
    def get_balance(self):
        hd=self.fget_data('GOLD',110)
        account_info = mt5.account_info()
        balance = account_info.balance
        return balance
    def get_open_profit(self):
        nowd=self.fget_data('GOLD',110)
        pos_info = mt5.positions_total()

        for position in mt5.positions_get():
            
            
            if position.symbol.startswith('GOLD'):
                return position.profit
    def get_today_profit(self):
        if self.trades is None or len(self.trades)==0:
            return None
        else:
            hd=self.fget_data('GOLD',110)
            today_value=self.trades[self.trades['trade_open'].dt.date == datetime.date.today()]
            today_profit=today_value['profit'].sum()
            return today_profit
    
                    
    def initialize_agent_data(self,initial_balance):
        agent_collection = self.db["agent_client_data"]
        
        
        if agent_collection.find_one() is None:
            if initial_balance < 10 or initial_balance is None:
                error_message = "Your Account dosent have adequate !//n Balance For full functioning please deposit and restart application //n Application will close After this message"

    # Create a QMessageBox to display the error
                error_dialog = QtWidgets.QMessageBox()
                error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                error_dialog.setWindowTitle("Balance Error")
                error_dialog.setText("Inadequate Balance:")
                error_dialog.setDetailedText(error_message)
                error_dialog.exec()
                QtCore.QTimer.singleShot(120000, QtWidgets.QApplication.instance().quit)
            else:
                agent_activation_date = datetime.datetime.now()
                defaultlotsize=0.01
                defaultdeviation=1
                app_code=random.randint(100000, 999999)
                defaultcomment="agent_1 D.N.G"
                post = {"agent_activation_date": agent_activation_date, "defaultlotsize": defaultlotsize, "defaultdeviation": defaultdeviation, "defaultcomment": defaultcomment,'appcode':app_code}
                agent_collection.insert_one(post)
                parameters_collection = self.db["agent_parameters"]
                default_maxdistance=1.5
                default_activationtime="03:00"
                default_stoptime="16:30"
                default_profit=5
                default_slwindow=2
                default_candlesize=1.5
                parameter_post = {"appcode":app_code,"default_maxdistance": default_maxdistance, "default_activationtime": default_activationtime, "default_stoptime": default_stoptime, "default_profit": default_profit, "default_slwindow": default_slwindow, "default_candlesize": default_candlesize,'initial_balance':initial_balance}
                parameters_collection.insert_one(parameter_post)
    
    def generate_profitdata(self,act_time,todays_date,symbol='GOLD'):
        hd=self.fget_data('GOLD',110)
        trade_history=mt5.history_deals_get(act_time, todays_date, symbol=symbol)
        if trade_history is None:
            return None
        else:
            columns = ['ticket', 'order', 'time', 'time_msc', 'type', 'entry', 'magic', 'position_id', 'reason', 'volume', 'price', 'commission', 'swap', 'profit', 'fee', 'symbol', 'comment', 'external_id']

            # Create a pandas DataFrame
            df = pd.DataFrame(trade_history, columns=columns)
            return df
    def generate_timedata(self,act_time,todays_date,symbol='GOLD'):
        hd=self.fget_data('GOLD',110)
        trade_history=mt5.history_orders_get(act_time, todays_date, symbol=symbol)
        if trade_history is None:
            return None
        else:
            data = {
                "ticket": [order.ticket for order in trade_history],
                "time_setup": [order.time_setup for order in trade_history],
                "time_setup_msc": [order.time_setup_msc for order in trade_history],
                "time_done": [order.time_done for order in trade_history],
                "time_done_msc": [order.time_done_msc for order in trade_history],
                "time_expiration": [order.time_expiration for order in trade_history],
                "type": [order.type for order in trade_history],
                "type_time": [order.type_time for order in trade_history],
                "type_filling": [order.type_filling for order in trade_history],
                "state": [order.state for order in trade_history],
                "magic": [order.magic for order in trade_history],
                "position_id": [order.position_id for order in trade_history],
                "position_by_id": [order.position_by_id for order in trade_history],
                "reason": [order.reason for order in trade_history],
                "volume_initial": [order.volume_initial for order in trade_history],
                "volume_current": [order.volume_current for order in trade_history],
                "price_open": [order.price_open for order in trade_history],
                "sl": [order.sl for order in trade_history],
                "tp": [order.tp for order in trade_history],
                "price_current": [order.price_current for order in trade_history],
                "price_stoplimit": [order.price_stoplimit for order in trade_history],
                "symbol": [order.symbol for order in trade_history],
                "comment": [order.comment for order in trade_history],
                "external_id": [order.external_id for order in trade_history],
            }

            # Creating DataFrame
            df = pd.DataFrame(data)
            return df
        
    # 

    def make_newdata(self,df1,df2):
        
        new_df = pd.DataFrame(columns=['open_date', 'close_date', 'profit', 'ticket', 'lot_size','trade_type'])

        rows_to_append = []

        for _, i in df1.iterrows():
            for _, j in df2.iterrows():
                if i['order'] == j['ticket']:
                    if i['profit'] != 0.0:
                        new_row = {
                            'open_date': j['time_setup'],
                            'close_date': j['time_done'],
                            'profit': i['profit'],
                            'ticket': i['ticket'],
                            'lot_size': i['volume'],
                            'trade_type': i["type"]
                        }
                        rows_to_append.append(new_row)

        new_df = pd.concat([new_df, pd.DataFrame(rows_to_append)], ignore_index=True)

        return new_df
    def finished_data(self,act_time,todays_date):
        profit_data=self.generate_profitdata(act_time,todays_date)
        time_data=self.generate_timedata(act_time,todays_date)
        if profit_data is None or time_data is None:
            return None
        else:
            final_data=self.make_newdata(profit_data,time_data)
            return final_data
    
    def updatetrades(self):
        agent_data=self.db.agent_client_data.find_one()
        appcode=agent_data['appcode']
        agent_activation_date=agent_data['agent_activation_date']
        todays_date=datetime.datetime.now()
        trade_history=self.finished_data(agent_activation_date,todays_date)
        # print(trade_history)    
        if trade_history is None:
            pass
        else:
            

        # Create a pandas DataFrame
            df = trade_history
            df.drop(index=0, inplace=True)
            df['open_date'] = pd.to_datetime(df['open_date'],unit='s')

            trades_collection = self.db["trades"]
            for index, row in df.iterrows():
                # print(row['ticket'])
                trade_exist_check=trades_collection.find_one({"ticket":row['ticket']})
                # print(trade_exist_check)
                if trade_exist_check is None:
                    if row['trade_type']==0:
                        row['trade_type']="Sell"
                    elif row['trade_type']==1:
                        row['trade_type']="Buy"
                    

                    post = {"ticket": row['ticket'], "trade_open":row['open_date'] ,"profit": row['profit'],"lot_size": row['lot_size'],"appcode":appcode,"trade_type":row['trade_type']}
                    trades_collection.insert_one(post)

    def get_weekly_data(self):

    # Get the current week's start and end dates
        if self.trades is None or len(self.trades)==0:
            return None
        else:
            today = datetime.date.today()
            start_of_week = today - datetime.timedelta(days=today.weekday())
            end_of_week = start_of_week + datetime.timedelta(days=6)

            # Filter the DataFrame to include values belonging to this week only
            week_values = self.trades_df[(self.trades_df['trade_open'].dt.date >= start_of_week) & (self.trades_df['trade_open'].dt.date <= end_of_week)]
            week_values
            profit_value=week_values['profit'].max()
            loss_value=week_values['profit'].min()
            lowest_profit_row = week_values.loc[week_values['profit'].idxmin()]
            lowest_profit_datevalue15=lowest_profit_row['trade_open']
            week_total_profit=week_values['profit'].sum()


            highest_profit_row = week_values.loc[week_values['profit'].idxmax()]
            highestprofit_datevalue=highest_profit_row['trade_open']
            week_sell_values = week_values[week_values['trade_type'] == 'Sell']
            week_sell_profit = week_sell_values['profit'].sum()
            weeks_total_sells=len(week_sell_values)

            week_buy_values = week_values[week_values['trade_type'] == 'Buy']
            week_buy_profit = week_buy_values['profit'].sum()
            weeks_total_buys=len(week_buy_values)
            week_profitablebuys = week_values[(week_values['trade_type'] == 'Buy') & (week_values['profit'] > 0)]
            week_buyprofit = week_profitablebuys['profit'].sum()
            weeks_total_profitable_buys = len(week_buy_values)

            week_profitablesells = week_values[(week_values['trade_type'] == 'Sell') & (week_values['profit'] > 0)]
            week_sellprofit = week_profitablesells['profit'].sum()
            weeks_total_profitable_sells = len(week_sell_values)

            week_buy_loss=week_values[(week_values['trade_type'] == 'Buy') & (week_values['profit'] < 0)]
            week_buy_total_loss=week_buy_loss['profit'].sum()
            week_totalbuy_loss=len(week_buy_loss)

            week_sell_loss=week_values[(week_values['trade_type'] == 'Sell') & (week_values['profit'] < 0)]
            week_sell_total_loss=week_sell_loss['profit'].sum()
            week_totalsell_loss=len(week_sell_loss)

            return (profit_value,loss_value,lowest_profit_datevalue15,highestprofit_datevalue,week_sell_profit,weeks_total_profitable_sells,week_buy_profit,weeks_total_profitable_buys,week_buyprofit,week_buy_total_loss,week_totalbuy_loss,week_sell_total_loss,week_totalsell_loss,week_total_profit,week_sellprofit)
    def get_monthly_data(self):
        if self.trades is None or len(self.trades)==0:
            return None

    # Get the current month's start and end dates
        else:
            today = datetime.date.today()
            start_of_month = datetime.date(today.year, today.month, 1)
            end_of_month = datetime.date(today.year, today.month + 1, 1) - datetime.timedelta(days=1)

            # Filter the DataFrame to include values belonging to this month only
            this_month_values = self.trades_df[(self.trades_df['trade_open'].dt.date >= start_of_month) & (self.trades_df['trade_open'].dt.date <= end_of_month)]

            month_profit_value0=this_month_values['profit'].max()
            month_loss_value1=this_month_values['profit'].min()
            lowest_profit_row = this_month_values.loc[this_month_values['profit'].idxmin()]
            lowest_profit_datevalue15=lowest_profit_row['trade_open']
            high_profit_row = this_month_values.loc[this_month_values['profit'].idxmax()]
            high_profit_datevalue16=high_profit_row['trade_open']
            month_total_profit14=this_month_values['profit'].sum()

            month_sell_values = this_month_values[this_month_values['trade_type'] == 'Sell']
            month_sell_profit2 = month_sell_values['profit'].sum()
            months_total_sells3=len(month_sell_values)

            month_buy_values = this_month_values[this_month_values['trade_type'] == 'Buy']
            month_buy_profit4 = month_buy_values['profit'].sum()
            months_total_buys5=len(month_buy_values)

            month_profitablebuys = this_month_values[(this_month_values['trade_type'] == 'Buy') & (this_month_values['profit'] > 0)]
            month_buyprofit10 = month_profitablebuys['profit'].sum()
            months_total_profitable_buys11 = len(month_buy_values)

            month_profitablesells = this_month_values[(this_month_values['trade_type'] == 'Sell') & (this_month_values['profit'] > 0)]
            month_sellprofit12 = month_profitablesells['profit'].sum()
            months_total_profitable_sells13 = len(month_sell_values)

            month_buy_loss=this_month_values[(this_month_values['trade_type'] == 'Buy') & (this_month_values['profit'] < 0)]
            month_buy_total_loss6=month_buy_loss['profit'].sum()
            month_totalbuy_loss7=len(month_buy_loss)
            
            monthly_sell_loss=this_month_values[(this_month_values['trade_type'] == 'Sell') & (this_month_values['profit'] < 0)]
            month_sell_total_loss8=monthly_sell_loss['profit'].sum()
            month_totalsell_loss9=len(monthly_sell_loss)
            
            
            return (month_profit_value0,month_loss_value1,month_sell_profit2,months_total_sells3,month_buy_profit4,months_total_buys5,month_buy_total_loss6,month_totalbuy_loss7,month_sell_total_loss8,month_totalsell_loss9,month_buyprofit10,months_total_profitable_buys11,month_sellprofit12,months_total_profitable_sells13,month_total_profit14,lowest_profit_datevalue15,high_profit_datevalue16)

    def updateparameters(self):
        maxdistance=self.ui.maxdistanceinp.text()
        candlesize=self.ui.candlesizeinp.text()
        tp=self.ui.tpinp.text()
        slwindow=self.ui.slwindowinp.text()
        starttime=self.ui.start_timeinp.text()
        stoptime=self.ui.stoptimeinp.text()
        if maxdistance !="":
            self.update_db("default_maxdistance",int(maxdistance))
            self.ui.maxdistanceinp.setText("")
        if candlesize !="":
            self.update_db("default_candlesize",int(candlesize))
            self.ui.candlesizeinp.setText("")
        if tp !="":
            self.update_db("default_profit",int(tp))
            self.ui.tpinp.setText("")
        if slwindow !="":
            self.update_db("default_slwindow",int(slwindow))
            self.ui.slwindowinp.setText("")
        if starttime !="":
            self.update_db("default_activationtime",starttime)
            self.ui.start_timeinp.setText("")
        if stoptime !="":
            self.update_db("default_stoptime",stoptime)
            self.ui.stoptimeinp.setText("")
            
        self.displayparameters()
            
    def restore_defaults(self,param,all_params=False):
        agentdata=self.db["agent_client_data"].find_one()
        appcode=agentdata['appcode']
        parameters_collection = self.db["agent_parameters"]
        if param=="maxdistance":
            query={"appcode":appcode}
            newvalues={"$set":{"default_maxdistance":1.5}}
            parameters_collection.update_one(query,newvalues)
        if param=="candlesize":
            query={"appcode":appcode}
            newvalues={"$set":{"default_candlesize":1.5}}
            parameters_collection.update_one(query,newvalues)
        if param=="tp":
            query={"appcode":appcode}
            newvalues={"$set":{"default_profit":5}}
            parameters_collection.update_one(query,newvalues)
        if param=="slwindow":
            query={"appcode":appcode}
            newvalues={"$set":{"default_slwindow":2}}
            parameters_collection.update_one(query,newvalues)
        if param=="starttime":
            query={"appcode":appcode}
            newvalues={"$set":{"default_activationtime":"03:00"}}
            parameters_collection.update_one(query,newvalues)
        if param=="stoptime":
            query={"appcode":appcode}
            newvalues={"$set":{"default_stoptime":"16:30"}}
            parameters_collection.update_one(query,newvalues)
            
        if all_params:
            query={"appcode":appcode}
            newvalues={"$set":{"default_maxdistance":1.5,"default_candlesize":1.5,"default_profit":5,"default_slwindow":2,"default_activationtime":"03:00","default_stoptime":"16:30"}}
            parameters_collection.update_one(query,newvalues)
        self.displayparameters()
            
    def updateprams_btn(self):
        self.ui.updatemaxdistance.clicked.connect(lambda: self.updateparameters())
        self.ui.updatecandlesize.clicked.connect(lambda: self.updateparameters())
        self.ui.updatetakeprofit.clicked.connect(lambda: self.updateparameters())
        self.ui.updateslwindow.clicked.connect(lambda: self.updateparameters())
        self.ui.updatestart_time.clicked.connect(lambda: self.updateparameters())
        self.ui.updatestoptime.clicked.connect(lambda: self.updateparameters())
        self.ui.resetallbtn_.clicked.connect(lambda: self.updateparameters())
    def resetparans_btn(self):
        self.ui.resetmaxdistance.clicked.connect(lambda: self.restore_defaults("maxdistance"))
        self.ui.resetstarttime.clicked.connect(lambda: self.restore_defaults("starttime"))
        self.ui.resetcandlesize.clicked.connect(lambda: self.restore_defaults("candlesize"))
        self.ui.resetslwindow.clicked.connect(lambda: self.restore_defaults("slwindow"))
        self.ui.reset_takeprofit.clicked.connect(lambda: self.restore_defaults("tp"))
        self.ui.resetstoptime.clicked.connect(lambda: self.restore_defaults("stoptime"))
        self.ui.resetallbtn.clicked.connect(lambda: self.restore_defaults("all",True))
        
    def accountvalues(self):
        agentdata=self.db["agent_client_data"].find_one()
        lotsize=agentdata['defaultlotsize']
        deviation=agentdata['defaultdeviation']
        self.ui.filexlotsize.setText(str(lotsize))
        self.ui.filexdeviation.setText(str(deviation))
        
    def updateaccountvalues_btn(self):
        self.ui.lotsizebtn.clicked.connect(lambda: self.updateaccountvalues())
        self.ui.updatedeviationbtn.clicked.connect(lambda: self.updateaccountvalues())
        
    def resetaccountvalues(self ,param):
        if param=="lotsize":
            agentdata=self.db["agent_client_data"].find_one()
            appcode=agentdata['appcode']
            agent_collection = self.db["agent_client_data"]
            query={"appcode":appcode}
            newvalues={"$set":{"defaultlotsize":0.01}}
            agent_collection.update_one(query,newvalues)
            self.accountvalues()
        if param=="deviation":
            agentdata=self.db["agent_client_data"].find_one()
            appcode=agentdata['appcode']
            agent_collection = self.db["agent_client_data"]
            query={"appcode":appcode}
            newvalues={"$set":{"defaultdeviation":1}}
            agent_collection.update_one(query,newvalues)
            self.accountvalues()
    def resetaccountvalues_btn(self):
        self.ui.resetlotsizebtn.clicked.connect(lambda: self.resetaccountvalues("lotsize"))
        self.ui.resetexdeviation.clicked.connect(lambda: self.resetaccountvalues("deviation"))
     
    def dynamicactivation(self):
        
        if  self.agent_activation_status==False:
            self.ui.widget_21.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #9A2A2A, stop:1 #ADD8E6);")
            self.ui.deactivateagentbtn.setEnabled(False)
            self.ui.activateagentbtn.setEnabled(True)
            self.ui.filstatus.setText("deactivated")
        if self.agent_activation_status==True:
            self.ui.widget_21.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #50C878, stop:1  #ADD8E6);")
            #set .activateagentbtn (set button to not pressable)
            self.ui.activateagentbtn.setEnabled(False)
            self.ui.deactivateagentbtn.setEnabled(True)
        
            self.ui.filstatus.setText("activated")
    def dynamic_month_date(self):
        month=datetime.datetime.now().strftime("%B")
        dayofweek=datetime.datetime.now().strftime("%A")
        # weekdaterange=datetime.datetime.now().strftime("%d")
        self.ui.dailyperformancelabel.setText(f"{dayofweek} returns")
        self.ui.weeklyspotlightlabel.setText(f"Weekly Spotlight")
        self.ui.monthlyspotlightlabel.setText(f"{month} Spotlight")
        self.ui.weeklyreportlabel.setText(f"Weekly Report")
        self.ui.weeklyreportlabel_2.setText(f"{month} Report")
        self.ui.monthlyperformancelablel.setText(f"{month} Returns")
        
        
        
    def setgrowthpercentage(self):
        agentdata=self.db["agent_client_data"].find_one()
        appcode=agentdata['appcode']
        agentparams=self.db["agent_parameters"].find_one({"appcode":appcode})
        initial_balance=agentparams['initial_balance']
        now_balance=self.get_balance()
        growth_percentage=((now_balance-initial_balance)/initial_balance)*100
        self.ui.flgrowthrate.setText(str(growth_percentage))
        
            
    def real_acivate_deactivate_btn(self):
        self.ui.activateagentbtn.clicked.connect(lambda: self.activateagentbtn())
        self.ui.deactivateagentbtn.clicked.connect(lambda: self.deactivateagentbtn())
        
    def activateagentbtn(self):
        if  self.agent_activation_status==False:
            self.agent_activation_status=True
            self.dynamicactivation()
            self.startagent()
            #activated popup
            error_message = "Activate " # Store error message

    # Create a QMessageBox to display the error
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Information)
            error_dialog.setWindowTitle("Activated Agent")
            error_dialog.setText("Agent Status:")
            error_dialog.setDetailedText(error_message)
            error_dialog.exec()
            
            
            
    def deactivateagentbtn(self):
        if self.agent_activation_status==True:
        
            self.deactivateagent()
            self.agent_activation_status=False
            self.dynamicactivation()
            error_message = "Inactive  " # Store error message

    # Create a QMessageBox to display the error
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Information)
            error_dialog.setWindowTitle("Deactivated Agent")
            error_dialog.setText("Agent Status:")
            error_dialog.setDetailedText(error_message)
            error_dialog.exec()
            
        
        
    def updateaccountvalues(self):
        lotsize=self.ui.lotsizeinp.text()
        deviation=self.ui.deviationinp.text()
        agentdata=self.db["agent_client_data"].find_one()
        appcode=agentdata['appcode']
        agent_collection = self.db["agent_client_data"]
        query={"appcode":appcode}
        if lotsize !="":
            newvalues={"$set":{"defaultlotsize":int(lotsize)}}
            agent_collection.update_one(query,newvalues)
            self.ui.lotsizeinp.setText("")
        if deviation !="":
            newvalues={"$set":{"defaultdeviation":int(deviation)}}
            agent_collection.update_one(query,newvalues)
            self.ui.deviationinp.setText("")
        self.accountvalues()
                    
            

    def displayparameters(self):
        agentdata=self.db["agent_client_data"].find_one()
        appcode=agentdata['appcode']
        parameters_collection = self.db["agent_parameters"].find_one( {"appcode":appcode})
        self.ui.exmaxdistance.setText(str(parameters_collection['default_maxdistance']))
        self.ui.exstart_time.setText(str(parameters_collection['default_activationtime']))
        self.ui.excandlesize.setText(str(parameters_collection['default_candlesize']))
        self.ui.exslwindow.setText(str(parameters_collection['default_slwindow']))
        self.ui.extakeprofit.setText(str(parameters_collection['default_profit']))
        self.ui.exstoptime.setText(str(parameters_collection['default_stoptime']))
    
    def update_db(self,parameter,new_value):
        agentdata=self.db["agent_client_data"].find_one()
        appcode=agentdata['appcode']
        parameters_collection = self.db["agent_parameters"]
        querry={"appcode":appcode}
        newvalues={"$set":{parameter:new_value}}
        parameters_collection.update_one(querry,newvalues)
        
        
    def distance_checker(self,price,value,lim):
        plh=price-value
        plh=abs(plh)
        if plh >lim:
            return 1
        else:
            return 0
    
    def find_status(self,data,size):
        data['AbsDiff'] = abs(data['Close'] - data['Open'])

    # Find the maximum value among the calculated differences
        max_diff = data['AbsDiff'].max()
        if max_diff>size:
            return 1
        else:
            return 0
    
    def find_sl(self,data,tp):
        if tp==-1:
            max_value = data['High'].max()
            return max_value
        else:
            min_value = data['Low'].min()
            return min_value   
      
    def closetrade(self):
        nowd=self.fget_data('GOLD',110)
        pos_info = mt5.positions_total()
        if pos_info is None:
            pass
        elif pos_info>1:
            for position in mt5.positions_get():
                for position in mt5.positions_get():
                    if position.symbol.startswith('GOLD'):
                        if position.profit>5:
                    # Your existing code
                            order_type = position.type
                            symbol = position.symbol
                            volume = position.volume
                            if order_type == mt5.ORDER_TYPE_BUY:
                                order_type = mt5.ORDER_TYPE_SELL
                                price = mt5.symbol_info_tick(symbol).bid
                            else:
                                order_type = mt5.ORDER_TYPE_BUY
                                price = mt5.symbol_info_tick(symbol).ask

                            close_request = {
                                "action": mt5.TRADE_ACTION_DEAL,
                                "symbol": symbol,
                                "volume": float(volume),
                                "type": order_type,
                                "position": position.ticket,
                                "price": price,
                                "magic": 20022,
                                "comment": "Close trade",
                                "type_time": mt5.ORDER_TIME_GTC,
                                "type_filling": mt5.ORDER_FILLING_IOC,
                            }

                            mt5.order_send(close_request)
    
    def cleanup(self):
        self.scheduler.shutdown() 
        

app = QtWidgets.QApplication([])
app.processEvents()
window = MainWindow()
window.show()
app.exec()