# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agentKeuomi.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc
import resource_rc
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1085, 862)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.menubtn = QPushButton(self.widget_4)
        self.menubtn.setObjectName(u"menubtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu-bar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menubtn.setIcon(icon)
        self.menubtn.setIconSize(QSize(30, 30))
        self.menubtn.setCheckable(True)

        self.horizontalLayout.addWidget(self.menubtn)

        self.horizontalSpacer_2 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.mainlogo = QLabel(self.widget_4)
        self.mainlogo.setObjectName(u"mainlogo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainlogo.sizePolicy().hasHeightForWidth())
        self.mainlogo.setSizePolicy(sizePolicy)
        self.mainlogo.setMinimumSize(QSize(50, 50))
        self.mainlogo.setMaximumSize(QSize(100, 71))
        self.mainlogo.setSizeIncrement(QSize(0, 0))
        self.mainlogo.setPixmap(QPixmap(u":/icons/icons/agent-high-resolution-logo.png"))
        self.mainlogo.setScaledContents(True)
        self.mainlogo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.mainlogo)

        self.horizontalSpacer = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.supportbtn = QPushButton(self.widget_4)
        self.supportbtn.setObjectName(u"supportbtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/support.png", QSize(), QIcon.Normal, QIcon.Off)
        self.supportbtn.setIcon(icon1)
        self.supportbtn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.supportbtn)


        self.verticalLayout_54.addWidget(self.widget_4)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_89 = QHBoxLayout(self.page_3)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 919, 1360))
        self.horizontalLayout_57 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.verticalLayout_61 = QVBoxLayout()
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.widget_10 = QWidget(self.scrollAreaWidgetContents)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.widget_22 = QWidget(self.widget_10)
        self.widget_22.setObjectName(u"widget_22")
        self.verticalLayout_28 = QVBoxLayout(self.widget_22)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.accountbalancelabel = QLabel(self.widget_22)
        self.accountbalancelabel.setObjectName(u"accountbalancelabel")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.accountbalancelabel.setFont(font)
        self.accountbalancelabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.accountbalancelabel)

        self.flaccountbalance = QLabel(self.widget_22)
        self.flaccountbalance.setObjectName(u"flaccountbalance")
        font1 = QFont()
        font1.setBold(True)
        self.flaccountbalance.setFont(font1)
        self.flaccountbalance.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.flaccountbalance)


        self.verticalLayout_28.addLayout(self.verticalLayout_26)


        self.horizontalLayout_37.addWidget(self.widget_22)

        self.widget_24 = QWidget(self.widget_10)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_30 = QVBoxLayout(self.widget_24)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.dailyperformancelabel = QLabel(self.widget_24)
        self.dailyperformancelabel.setObjectName(u"dailyperformancelabel")
        self.dailyperformancelabel.setFont(font)
        self.dailyperformancelabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.dailyperformancelabel)

        self.fldailyperformace = QLabel(self.widget_24)
        self.fldailyperformace.setObjectName(u"fldailyperformace")
        self.fldailyperformace.setFont(font1)
        self.fldailyperformace.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.fldailyperformace)


        self.verticalLayout_30.addLayout(self.verticalLayout_36)


        self.horizontalLayout_37.addWidget(self.widget_24)

        self.widget_23 = QWidget(self.widget_10)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_29 = QVBoxLayout(self.widget_23)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.weekyperformancelabel = QLabel(self.widget_23)
        self.weekyperformancelabel.setObjectName(u"weekyperformancelabel")
        self.weekyperformancelabel.setFont(font)
        self.weekyperformancelabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.weekyperformancelabel)

        self.flweeklyprofit = QLabel(self.widget_23)
        self.flweeklyprofit.setObjectName(u"flweeklyprofit")
        self.flweeklyprofit.setFont(font1)
        self.flweeklyprofit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.flweeklyprofit)


        self.verticalLayout_29.addLayout(self.verticalLayout_37)


        self.horizontalLayout_37.addWidget(self.widget_23)

        self.widget_25 = QWidget(self.widget_10)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_31 = QVBoxLayout(self.widget_25)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.monthlyperformancelablel = QLabel(self.widget_25)
        self.monthlyperformancelablel.setObjectName(u"monthlyperformancelablel")
        self.monthlyperformancelablel.setFont(font)
        self.monthlyperformancelablel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.monthlyperformancelablel)

        self.flmonthlyperformance = QLabel(self.widget_25)
        self.flmonthlyperformance.setObjectName(u"flmonthlyperformance")
        self.flmonthlyperformance.setFont(font1)
        self.flmonthlyperformance.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.flmonthlyperformance)


        self.verticalLayout_31.addLayout(self.verticalLayout_38)


        self.horizontalLayout_37.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.widget_10)
        self.widget_26.setObjectName(u"widget_26")
        self.verticalLayout_32 = QVBoxLayout(self.widget_26)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.growthratelabel = QLabel(self.widget_26)
        self.growthratelabel.setObjectName(u"growthratelabel")
        self.growthratelabel.setFont(font)
        self.growthratelabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.growthratelabel)

        self.flgrowthrate = QLabel(self.widget_26)
        self.flgrowthrate.setObjectName(u"flgrowthrate")
        self.flgrowthrate.setFont(font1)
        self.flgrowthrate.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.flgrowthrate)


        self.verticalLayout_32.addLayout(self.verticalLayout_39)


        self.horizontalLayout_37.addWidget(self.widget_26)


        self.verticalLayout_61.addWidget(self.widget_10)

        self.widget_16 = QWidget(self.scrollAreaWidgetContents)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_58 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.widget = QWidget(self.widget_16)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_26 = QHBoxLayout(self.widget)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.weeklyspotlightlabel = QLabel(self.widget)
        self.weeklyspotlightlabel.setObjectName(u"weeklyspotlightlabel")
        self.weeklyspotlightlabel.setFont(font)
        self.weeklyspotlightlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.weeklyspotlightlabel)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.weeklybuylabel = QLabel(self.widget_9)
        self.weeklybuylabel.setObjectName(u"weeklybuylabel")
        self.weeklybuylabel.setFont(font1)
        self.weeklybuylabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.weeklybuylabel)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.weekyprofdaylabel = QLabel(self.widget_9)
        self.weekyprofdaylabel.setObjectName(u"weekyprofdaylabel")
        self.weekyprofdaylabel.setFont(font1)
        self.weekyprofdaylabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.weekyprofdaylabel)

        self.flweekyprofday = QLabel(self.widget_9)
        self.flweekyprofday.setObjectName(u"flweekyprofday")
        self.flweekyprofday.setFont(font1)
        self.flweekyprofday.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.flweekyprofday)


        self.verticalLayout_17.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.weeklyprofammountlabel = QLabel(self.widget_9)
        self.weeklyprofammountlabel.setObjectName(u"weeklyprofammountlabel")
        self.weeklyprofammountlabel.setFont(font1)
        self.weeklyprofammountlabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.weeklyprofammountlabel)

        self.flweeklyprofammount = QLabel(self.widget_9)
        self.flweeklyprofammount.setObjectName(u"flweeklyprofammount")
        self.flweeklyprofammount.setFont(font1)
        self.flweeklyprofammount.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.flweeklyprofammount)


        self.verticalLayout_17.addLayout(self.horizontalLayout_29)


        self.horizontalLayout_41.addLayout(self.verticalLayout_17)


        self.horizontalLayout_22.addWidget(self.widget_9)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.weelylosslabel = QLabel(self.widget_2)
        self.weelylosslabel.setObjectName(u"weelylosslabel")
        self.weelylosslabel.setFont(font1)
        self.weelylosslabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.weelylosslabel)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.weekylossdaylabel = QLabel(self.widget_2)
        self.weekylossdaylabel.setObjectName(u"weekylossdaylabel")
        self.weekylossdaylabel.setFont(font1)
        self.weekylossdaylabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.weekylossdaylabel)

        self.flweekylossday = QLabel(self.widget_2)
        self.flweekylossday.setObjectName(u"flweekylossday")
        self.flweekylossday.setFont(font1)
        self.flweekylossday.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.flweekylossday)


        self.verticalLayout_16.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.weeklylossammountlabel = QLabel(self.widget_2)
        self.weeklylossammountlabel.setObjectName(u"weeklylossammountlabel")
        self.weeklylossammountlabel.setFont(font1)
        self.weeklylossammountlabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.weeklylossammountlabel)

        self.flweeklylossammount = QLabel(self.widget_2)
        self.flweeklylossammount.setObjectName(u"flweeklylossammount")
        self.flweeklylossammount.setFont(font1)
        self.flweeklylossammount.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.flweeklylossammount)


        self.verticalLayout_16.addLayout(self.horizontalLayout_25)


        self.horizontalLayout_23.addLayout(self.verticalLayout_16)


        self.horizontalLayout_22.addWidget(self.widget_2)


        self.verticalLayout_15.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_26.addLayout(self.verticalLayout_15)


        self.horizontalLayout_58.addWidget(self.widget)

        self.widget_8 = QWidget(self.widget_16)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.monthlyspotlightlabel = QLabel(self.widget_8)
        self.monthlyspotlightlabel.setObjectName(u"monthlyspotlightlabel")
        self.monthlyspotlightlabel.setFont(font)
        self.monthlyspotlightlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.monthlyspotlightlabel)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.widget_12 = QWidget(self.widget_8)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.monthlosslabel = QLabel(self.widget_12)
        self.monthlosslabel.setObjectName(u"monthlosslabel")
        self.monthlosslabel.setFont(font1)
        self.monthlosslabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.monthlosslabel)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.monthlossdaylabel = QLabel(self.widget_12)
        self.monthlossdaylabel.setObjectName(u"monthlossdaylabel")
        self.monthlossdaylabel.setFont(font1)
        self.monthlossdaylabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_34.addWidget(self.monthlossdaylabel)

        self.flmonthlossday = QLabel(self.widget_12)
        self.flmonthlossday.setObjectName(u"flmonthlossday")
        self.flmonthlossday.setFont(font1)
        self.flmonthlossday.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.flmonthlossday)


        self.verticalLayout_22.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.monthlossammountlabel = QLabel(self.widget_12)
        self.monthlossammountlabel.setObjectName(u"monthlossammountlabel")
        self.monthlossammountlabel.setFont(font1)
        self.monthlossammountlabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.monthlossammountlabel)

        self.flmonthlossammount = QLabel(self.widget_12)
        self.flmonthlossammount.setObjectName(u"flmonthlossammount")
        self.flmonthlossammount.setFont(font1)
        self.flmonthlossammount.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.flmonthlossammount)


        self.verticalLayout_22.addLayout(self.horizontalLayout_35)


        self.horizontalLayout_33.addLayout(self.verticalLayout_22)


        self.horizontalLayout_20.addWidget(self.widget_12)

        self.widget_11 = QWidget(self.widget_8)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.montbuylabel = QLabel(self.widget_11)
        self.montbuylabel.setObjectName(u"montbuylabel")
        self.montbuylabel.setFont(font1)
        self.montbuylabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.montbuylabel)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.montprofdaylabel_2 = QLabel(self.widget_11)
        self.montprofdaylabel_2.setObjectName(u"montprofdaylabel_2")
        self.montprofdaylabel_2.setFont(font1)
        self.montprofdaylabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.montprofdaylabel_2)

        self.flmontprofday = QLabel(self.widget_11)
        self.flmontprofday.setObjectName(u"flmontprofday")
        self.flmontprofday.setFont(font1)
        self.flmontprofday.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.flmontprofday)


        self.verticalLayout_21.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.monthprofammountlabel = QLabel(self.widget_11)
        self.monthprofammountlabel.setObjectName(u"monthprofammountlabel")
        self.monthprofammountlabel.setFont(font1)
        self.monthprofammountlabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.monthprofammountlabel)

        self.flmonthprofammount = QLabel(self.widget_11)
        self.flmonthprofammount.setObjectName(u"flmonthprofammount")
        self.flmonthprofammount.setFont(font1)
        self.flmonthprofammount.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.flmonthprofammount)


        self.verticalLayout_21.addLayout(self.horizontalLayout_32)


        self.horizontalLayout_30.addLayout(self.verticalLayout_21)


        self.horizontalLayout_20.addWidget(self.widget_11)


        self.verticalLayout_19.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_21.addLayout(self.verticalLayout_19)


        self.horizontalLayout_58.addWidget(self.widget_8)


        self.verticalLayout_61.addWidget(self.widget_16)

        self.widget_27 = QWidget(self.scrollAreaWidgetContents)
        self.widget_27.setObjectName(u"widget_27")
        self.verticalLayout_85 = QVBoxLayout(self.widget_27)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.widget_72 = QWidget(self.widget_27)
        self.widget_72.setObjectName(u"widget_72")
        self.verticalLayout_20 = QVBoxLayout(self.widget_72)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.maiaccbalancelabel = QLabel(self.widget_72)
        self.maiaccbalancelabel.setObjectName(u"maiaccbalancelabel")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.maiaccbalancelabel.setFont(font2)
        self.maiaccbalancelabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.maiaccbalancelabel)

        self.filmainaccountbalance = QLabel(self.widget_72)
        self.filmainaccountbalance.setObjectName(u"filmainaccountbalance")
        self.filmainaccountbalance.setFont(font)
        self.filmainaccountbalance.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.filmainaccountbalance)


        self.verticalLayout_20.addLayout(self.verticalLayout_27)


        self.horizontalLayout_59.addWidget(self.widget_72)

        self.widget_71 = QWidget(self.widget_27)
        self.widget_71.setObjectName(u"widget_71")
        self.verticalLayout_33 = QVBoxLayout(self.widget_71)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.opentradelabel = QLabel(self.widget_71)
        self.opentradelabel.setObjectName(u"opentradelabel")
        self.opentradelabel.setFont(font2)
        self.opentradelabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.opentradelabel)

        self.filopentradeprofit = QLabel(self.widget_71)
        self.filopentradeprofit.setObjectName(u"filopentradeprofit")
        self.filopentradeprofit.setFont(font)
        self.filopentradeprofit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.filopentradeprofit)


        self.verticalLayout_33.addLayout(self.verticalLayout_35)


        self.horizontalLayout_59.addWidget(self.widget_71)


        self.verticalLayout_85.addLayout(self.horizontalLayout_59)


        self.verticalLayout_61.addWidget(self.widget_27)

        self.widget_67 = QWidget(self.scrollAreaWidgetContents)
        self.widget_67.setObjectName(u"widget_67")
        self.horizontalLayout_53 = QHBoxLayout(self.widget_67)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_40 = QWidget(self.widget_67)
        self.widget_40.setObjectName(u"widget_40")
        self.horizontalLayout_75 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.weeklyreportlabel = QLabel(self.widget_40)
        self.weeklyreportlabel.setObjectName(u"weeklyreportlabel")
        self.weeklyreportlabel.setFont(font)
        self.weeklyreportlabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.weeklyreportlabel)


        self.verticalLayout_23.addWidget(self.widget_40)

        self.widget_41 = QWidget(self.widget_67)
        self.widget_41.setObjectName(u"widget_41")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.weeklyreport_total_label = QLabel(self.widget_41)
        self.weeklyreport_total_label.setObjectName(u"weeklyreport_total_label")
        self.weeklyreport_total_label.setFont(font)
        self.weeklyreport_total_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_45.addWidget(self.weeklyreport_total_label)

        self.filweeklyreport_totalprofit = QLabel(self.widget_41)
        self.filweeklyreport_totalprofit.setObjectName(u"filweeklyreport_totalprofit")
        self.filweeklyreport_totalprofit.setFont(font1)

        self.horizontalLayout_45.addWidget(self.filweeklyreport_totalprofit)


        self.horizontalLayout_40.addLayout(self.horizontalLayout_45)


        self.verticalLayout_23.addWidget(self.widget_41)

        self.widget_66 = QWidget(self.widget_67)
        self.widget_66.setObjectName(u"widget_66")
        self.horizontalLayout_83 = QHBoxLayout(self.widget_66)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.widget_51 = QWidget(self.widget_66)
        self.widget_51.setObjectName(u"widget_51")
        self.horizontalLayout_77 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_52 = QWidget(self.widget_51)
        self.widget_52.setObjectName(u"widget_52")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.verticalLayout_62 = QVBoxLayout()
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.monthreporttutalbuyprofitlabel_2 = QLabel(self.widget_52)
        self.monthreporttutalbuyprofitlabel_2.setObjectName(u"monthreporttutalbuyprofitlabel_2")
        self.monthreporttutalbuyprofitlabel_2.setFont(font)
        self.monthreporttutalbuyprofitlabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.monthreporttutalbuyprofitlabel_2)

        self.filweekreporttotalbuyprofit = QLabel(self.widget_52)
        self.filweekreporttotalbuyprofit.setObjectName(u"filweekreporttotalbuyprofit")
        self.filweekreporttotalbuyprofit.setFont(font1)
        self.filweekreporttotalbuyprofit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.filweekreporttotalbuyprofit)


        self.horizontalLayout_38.addLayout(self.verticalLayout_62)


        self.verticalLayout_3.addWidget(self.widget_52)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.widget_42 = QWidget(self.widget_51)
        self.widget_42.setObjectName(u"widget_42")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.monthreporttutalbuylabel_2 = QLabel(self.widget_42)
        self.monthreporttutalbuylabel_2.setObjectName(u"monthreporttutalbuylabel_2")
        self.monthreporttutalbuylabel_2.setFont(font)

        self.verticalLayout_24.addWidget(self.monthreporttutalbuylabel_2)

        self.filweekreporttotalbuy = QLabel(self.widget_42)
        self.filweekreporttotalbuy.setObjectName(u"filweekreporttotalbuy")
        self.filweekreporttotalbuy.setFont(font1)
        self.filweekreporttotalbuy.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.filweekreporttotalbuy)


        self.horizontalLayout_56.addLayout(self.verticalLayout_24)


        self.horizontalLayout_39.addWidget(self.widget_42)

        self.widget_36 = QWidget(self.widget_51)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_72 = QVBoxLayout()
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.monthreporttutalbuyprofitlabel_10 = QLabel(self.widget_36)
        self.monthreporttutalbuyprofitlabel_10.setObjectName(u"monthreporttutalbuyprofitlabel_10")
        self.monthreporttutalbuyprofitlabel_10.setFont(font)
        self.monthreporttutalbuyprofitlabel_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_72.addWidget(self.monthreporttutalbuyprofitlabel_10)

        self.filweekreporttotalbuyprofit_9 = QLabel(self.widget_36)
        self.filweekreporttotalbuyprofit_9.setObjectName(u"filweekreporttotalbuyprofit_9")
        self.filweekreporttotalbuyprofit_9.setFont(font1)
        self.filweekreporttotalbuyprofit_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_72.addWidget(self.filweekreporttotalbuyprofit_9)


        self.horizontalLayout_13.addLayout(self.verticalLayout_72)


        self.horizontalLayout_39.addWidget(self.widget_36)


        self.verticalLayout_3.addLayout(self.horizontalLayout_39)

        self.widget_30 = QWidget(self.widget_51)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_46 = QWidget(self.widget_30)
        self.widget_46.setObjectName(u"widget_46")
        self.horizontalLayout_79 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.monthreporttutalbuylabel_3 = QLabel(self.widget_46)
        self.monthreporttutalbuylabel_3.setObjectName(u"monthreporttutalbuylabel_3")
        self.monthreporttutalbuylabel_3.setFont(font)

        self.verticalLayout_55.addWidget(self.monthreporttutalbuylabel_3)

        self.filweekreporttotalbuy_2 = QLabel(self.widget_46)
        self.filweekreporttotalbuy_2.setObjectName(u"filweekreporttotalbuy_2")
        self.filweekreporttotalbuy_2.setFont(font1)
        self.filweekreporttotalbuy_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_55.addWidget(self.filweekreporttotalbuy_2)


        self.horizontalLayout_79.addLayout(self.verticalLayout_55)


        self.horizontalLayout_14.addWidget(self.widget_46)

        self.widget_47 = QWidget(self.widget_30)
        self.widget_47.setObjectName(u"widget_47")
        self.horizontalLayout_80 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.verticalLayout_66 = QVBoxLayout()
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.monthreporttutalbuyprofitlabel_3 = QLabel(self.widget_47)
        self.monthreporttutalbuyprofitlabel_3.setObjectName(u"monthreporttutalbuyprofitlabel_3")
        self.monthreporttutalbuyprofitlabel_3.setFont(font)
        self.monthreporttutalbuyprofitlabel_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_66.addWidget(self.monthreporttutalbuyprofitlabel_3)

        self.filweekreporttotalbuyprofit_2 = QLabel(self.widget_47)
        self.filweekreporttotalbuyprofit_2.setObjectName(u"filweekreporttotalbuyprofit_2")
        self.filweekreporttotalbuyprofit_2.setFont(font1)
        self.filweekreporttotalbuyprofit_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_66.addWidget(self.filweekreporttotalbuyprofit_2)


        self.horizontalLayout_80.addLayout(self.verticalLayout_66)


        self.horizontalLayout_14.addWidget(self.widget_47)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)


        self.verticalLayout_3.addWidget(self.widget_30)


        self.horizontalLayout_77.addLayout(self.verticalLayout_3)


        self.horizontalLayout_78.addWidget(self.widget_51)

        self.widget_38 = QWidget(self.widget_66)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_32 = QWidget(self.widget_38)
        self.widget_32.setObjectName(u"widget_32")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_69 = QVBoxLayout()
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.monthreporttutalbuyprofitlabel_4 = QLabel(self.widget_32)
        self.monthreporttutalbuyprofitlabel_4.setObjectName(u"monthreporttutalbuyprofitlabel_4")
        self.monthreporttutalbuyprofitlabel_4.setFont(font)
        self.monthreporttutalbuyprofitlabel_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.monthreporttutalbuyprofitlabel_4)

        self.filweekreporttotalbuyprofit_3 = QLabel(self.widget_32)
        self.filweekreporttotalbuyprofit_3.setObjectName(u"filweekreporttotalbuyprofit_3")
        self.filweekreporttotalbuyprofit_3.setFont(font1)
        self.filweekreporttotalbuyprofit_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.filweekreporttotalbuyprofit_3)


        self.horizontalLayout_16.addLayout(self.verticalLayout_69)


        self.verticalLayout_18.addWidget(self.widget_32)

        self.widget_35 = QWidget(self.widget_38)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.widget_43 = QWidget(self.widget_35)
        self.widget_43.setObjectName(u"widget_43")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_68 = QVBoxLayout()
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.monthreporttutalbuylabel_4 = QLabel(self.widget_43)
        self.monthreporttutalbuylabel_4.setObjectName(u"monthreporttutalbuylabel_4")
        self.monthreporttutalbuylabel_4.setFont(font)

        self.verticalLayout_68.addWidget(self.monthreporttutalbuylabel_4)

        self.filweekreporttotalbuy_3 = QLabel(self.widget_43)
        self.filweekreporttotalbuy_3.setObjectName(u"filweekreporttotalbuy_3")
        self.filweekreporttotalbuy_3.setFont(font1)
        self.filweekreporttotalbuy_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_68.addWidget(self.filweekreporttotalbuy_3)


        self.horizontalLayout_18.addLayout(self.verticalLayout_68)


        self.horizontalLayout_42.addWidget(self.widget_43)

        self.widget_37 = QWidget(self.widget_35)
        self.widget_37.setObjectName(u"widget_37")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_81 = QVBoxLayout()
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.monthreporttutalbuyprofitlabel_11 = QLabel(self.widget_37)
        self.monthreporttutalbuyprofitlabel_11.setObjectName(u"monthreporttutalbuyprofitlabel_11")
        self.monthreporttutalbuyprofitlabel_11.setFont(font)
        self.monthreporttutalbuyprofitlabel_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_81.addWidget(self.monthreporttutalbuyprofitlabel_11)

        self.filweekreporttotalbuyprofit_10 = QLabel(self.widget_37)
        self.filweekreporttotalbuyprofit_10.setObjectName(u"filweekreporttotalbuyprofit_10")
        self.filweekreporttotalbuyprofit_10.setFont(font1)
        self.filweekreporttotalbuyprofit_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_81.addWidget(self.filweekreporttotalbuyprofit_10)


        self.horizontalLayout_17.addLayout(self.verticalLayout_81)


        self.horizontalLayout_42.addWidget(self.widget_37)


        self.horizontalLayout_43.addLayout(self.horizontalLayout_42)


        self.verticalLayout_18.addWidget(self.widget_35)

        self.widget_48 = QWidget(self.widget_38)
        self.widget_48.setObjectName(u"widget_48")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.widget_49 = QWidget(self.widget_48)
        self.widget_49.setObjectName(u"widget_49")
        self.horizontalLayout_81 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.verticalLayout_70 = QVBoxLayout()
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.monthreporttutalbuylabel_5 = QLabel(self.widget_49)
        self.monthreporttutalbuylabel_5.setObjectName(u"monthreporttutalbuylabel_5")
        self.monthreporttutalbuylabel_5.setFont(font)

        self.verticalLayout_70.addWidget(self.monthreporttutalbuylabel_5)

        self.filweekreporttotalbuy_4 = QLabel(self.widget_49)
        self.filweekreporttotalbuy_4.setObjectName(u"filweekreporttotalbuy_4")
        self.filweekreporttotalbuy_4.setFont(font1)
        self.filweekreporttotalbuy_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_70.addWidget(self.filweekreporttotalbuy_4)


        self.horizontalLayout_81.addLayout(self.verticalLayout_70)


        self.horizontalLayout_36.addWidget(self.widget_49)

        self.widget_50 = QWidget(self.widget_48)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_82 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.verticalLayout_71 = QVBoxLayout()
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.monthreporttutalbuyprofitlabel_5 = QLabel(self.widget_50)
        self.monthreporttutalbuyprofitlabel_5.setObjectName(u"monthreporttutalbuyprofitlabel_5")
        self.monthreporttutalbuyprofitlabel_5.setFont(font)
        self.monthreporttutalbuyprofitlabel_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_71.addWidget(self.monthreporttutalbuyprofitlabel_5)

        self.filweekreporttotalbuyprofit_4 = QLabel(self.widget_50)
        self.filweekreporttotalbuyprofit_4.setObjectName(u"filweekreporttotalbuyprofit_4")
        self.filweekreporttotalbuyprofit_4.setFont(font1)
        self.filweekreporttotalbuyprofit_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_71.addWidget(self.filweekreporttotalbuyprofit_4)


        self.horizontalLayout_82.addLayout(self.verticalLayout_71)


        self.horizontalLayout_36.addWidget(self.widget_50)


        self.horizontalLayout_27.addLayout(self.horizontalLayout_36)


        self.verticalLayout_18.addWidget(self.widget_48)


        self.horizontalLayout_44.addLayout(self.verticalLayout_18)


        self.horizontalLayout_78.addWidget(self.widget_38)


        self.horizontalLayout_83.addLayout(self.horizontalLayout_78)


        self.verticalLayout_23.addWidget(self.widget_66)


        self.horizontalLayout_53.addLayout(self.verticalLayout_23)


        self.verticalLayout_61.addWidget(self.widget_67)

        self.widget_70 = QWidget(self.scrollAreaWidgetContents)
        self.widget_70.setObjectName(u"widget_70")
        self.verticalLayout_84 = QVBoxLayout(self.widget_70)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_83 = QVBoxLayout()
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.widget_45 = QWidget(self.widget_70)
        self.widget_45.setObjectName(u"widget_45")
        self.verticalLayout_76 = QVBoxLayout(self.widget_45)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.weeklyreportlabel_2 = QLabel(self.widget_45)
        self.weeklyreportlabel_2.setObjectName(u"weeklyreportlabel_2")
        self.weeklyreportlabel_2.setFont(font)
        self.weeklyreportlabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.weeklyreportlabel_2)


        self.verticalLayout_83.addWidget(self.widget_45)

        self.widget_53 = QWidget(self.widget_70)
        self.widget_53.setObjectName(u"widget_53")
        self.horizontalLayout_55 = QHBoxLayout(self.widget_53)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.weeklyreport_total_label_2 = QLabel(self.widget_53)
        self.weeklyreport_total_label_2.setObjectName(u"weeklyreport_total_label_2")
        self.weeklyreport_total_label_2.setFont(font)
        self.weeklyreport_total_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_60.addWidget(self.weeklyreport_total_label_2)

        self.filweeklyreport_totalprofit_2 = QLabel(self.widget_53)
        self.filweeklyreport_totalprofit_2.setObjectName(u"filweeklyreport_totalprofit_2")
        self.filweeklyreport_totalprofit_2.setFont(font1)

        self.horizontalLayout_60.addWidget(self.filweeklyreport_totalprofit_2)


        self.horizontalLayout_55.addLayout(self.horizontalLayout_60)


        self.verticalLayout_83.addWidget(self.widget_53)

        self.widget_54 = QWidget(self.widget_70)
        self.widget_54.setObjectName(u"widget_54")
        self.horizontalLayout_51 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.widget_60 = QWidget(self.widget_54)
        self.widget_60.setObjectName(u"widget_60")
        self.verticalLayout_60 = QVBoxLayout(self.widget_60)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.widget_69 = QWidget(self.widget_60)
        self.widget_69.setObjectName(u"widget_69")
        self.verticalLayout_40 = QVBoxLayout(self.widget_69)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_64 = QVBoxLayout()
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.monthreporttutalbuyprofitlabel_6 = QLabel(self.widget_69)
        self.monthreporttutalbuyprofitlabel_6.setObjectName(u"monthreporttutalbuyprofitlabel_6")
        self.monthreporttutalbuyprofitlabel_6.setFont(font)
        self.monthreporttutalbuyprofitlabel_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_64.addWidget(self.monthreporttutalbuyprofitlabel_6)

        self.filweekreporttotalbuyprofit_5 = QLabel(self.widget_69)
        self.filweekreporttotalbuyprofit_5.setObjectName(u"filweekreporttotalbuyprofit_5")
        self.filweekreporttotalbuyprofit_5.setFont(font1)
        self.filweekreporttotalbuyprofit_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_64.addWidget(self.filweekreporttotalbuyprofit_5)


        self.verticalLayout_40.addLayout(self.verticalLayout_64)


        self.verticalLayout_59.addWidget(self.widget_69)

        self.widget_55 = QWidget(self.widget_60)
        self.widget_55.setObjectName(u"widget_55")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.widget_56 = QWidget(self.widget_55)
        self.widget_56.setObjectName(u"widget_56")
        self.horizontalLayout_84 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.verticalLayout_63 = QVBoxLayout()
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.monthreporttutalbuylabel_6 = QLabel(self.widget_56)
        self.monthreporttutalbuylabel_6.setObjectName(u"monthreporttutalbuylabel_6")
        self.monthreporttutalbuylabel_6.setFont(font)

        self.verticalLayout_63.addWidget(self.monthreporttutalbuylabel_6)

        self.filweekreporttotalbuy_5 = QLabel(self.widget_56)
        self.filweekreporttotalbuy_5.setObjectName(u"filweekreporttotalbuy_5")
        self.filweekreporttotalbuy_5.setFont(font1)
        self.filweekreporttotalbuy_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_63.addWidget(self.filweekreporttotalbuy_5)


        self.horizontalLayout_84.addLayout(self.verticalLayout_63)


        self.horizontalLayout_50.addWidget(self.widget_56)

        self.widget_61 = QWidget(self.widget_55)
        self.widget_61.setObjectName(u"widget_61")
        self.horizontalLayout_49 = QHBoxLayout(self.widget_61)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.verticalLayout_67 = QVBoxLayout()
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.monthreporttutalbuyprofitlabel_13 = QLabel(self.widget_61)
        self.monthreporttutalbuyprofitlabel_13.setObjectName(u"monthreporttutalbuyprofitlabel_13")
        self.monthreporttutalbuyprofitlabel_13.setFont(font)
        self.monthreporttutalbuyprofitlabel_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.monthreporttutalbuyprofitlabel_13)

        self.filweekreporttotalbuyprofit_12 = QLabel(self.widget_61)
        self.filweekreporttotalbuyprofit_12.setObjectName(u"filweekreporttotalbuyprofit_12")
        self.filweekreporttotalbuyprofit_12.setFont(font1)
        self.filweekreporttotalbuyprofit_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.filweekreporttotalbuyprofit_12)


        self.horizontalLayout_49.addLayout(self.verticalLayout_67)


        self.horizontalLayout_50.addWidget(self.widget_61)


        self.verticalLayout_59.addWidget(self.widget_55)

        self.widget_57 = QWidget(self.widget_60)
        self.widget_57.setObjectName(u"widget_57")
        self.horizontalLayout_85 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.widget_58 = QWidget(self.widget_57)
        self.widget_58.setObjectName(u"widget_58")
        self.horizontalLayout_87 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.verticalLayout_74 = QVBoxLayout()
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.monthreporttutalbuylabel_7 = QLabel(self.widget_58)
        self.monthreporttutalbuylabel_7.setObjectName(u"monthreporttutalbuylabel_7")
        self.monthreporttutalbuylabel_7.setFont(font)

        self.verticalLayout_74.addWidget(self.monthreporttutalbuylabel_7)

        self.filweekreporttotalbuy_6 = QLabel(self.widget_58)
        self.filweekreporttotalbuy_6.setObjectName(u"filweekreporttotalbuy_6")
        self.filweekreporttotalbuy_6.setFont(font1)
        self.filweekreporttotalbuy_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_74.addWidget(self.filweekreporttotalbuy_6)


        self.horizontalLayout_87.addLayout(self.verticalLayout_74)


        self.horizontalLayout_86.addWidget(self.widget_58)

        self.widget_59 = QWidget(self.widget_57)
        self.widget_59.setObjectName(u"widget_59")
        self.horizontalLayout_88 = QHBoxLayout(self.widget_59)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.verticalLayout_75 = QVBoxLayout()
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.monthreporttutalbuyprofitlabel_7 = QLabel(self.widget_59)
        self.monthreporttutalbuyprofitlabel_7.setObjectName(u"monthreporttutalbuyprofitlabel_7")
        self.monthreporttutalbuyprofitlabel_7.setFont(font)
        self.monthreporttutalbuyprofitlabel_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_75.addWidget(self.monthreporttutalbuyprofitlabel_7)

        self.filweekreporttotalbuyprofit_6 = QLabel(self.widget_59)
        self.filweekreporttotalbuyprofit_6.setObjectName(u"filweekreporttotalbuyprofit_6")
        self.filweekreporttotalbuyprofit_6.setFont(font1)
        self.filweekreporttotalbuyprofit_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_75.addWidget(self.filweekreporttotalbuyprofit_6)


        self.horizontalLayout_88.addLayout(self.verticalLayout_75)


        self.horizontalLayout_86.addWidget(self.widget_59)


        self.horizontalLayout_85.addLayout(self.horizontalLayout_86)


        self.verticalLayout_59.addWidget(self.widget_57)


        self.verticalLayout_60.addLayout(self.verticalLayout_59)


        self.horizontalLayout_51.addWidget(self.widget_60)

        self.widget_63 = QWidget(self.widget_54)
        self.widget_63.setObjectName(u"widget_63")
        self.verticalLayout_73 = QVBoxLayout(self.widget_63)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.widget_68 = QWidget(self.widget_63)
        self.widget_68.setObjectName(u"widget_68")
        self.horizontalLayout_52 = QHBoxLayout(self.widget_68)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.verticalLayout_78 = QVBoxLayout()
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.monthreporttutalbuyprofitlabel_8 = QLabel(self.widget_68)
        self.monthreporttutalbuyprofitlabel_8.setObjectName(u"monthreporttutalbuyprofitlabel_8")
        self.monthreporttutalbuyprofitlabel_8.setFont(font)
        self.monthreporttutalbuyprofitlabel_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_78.addWidget(self.monthreporttutalbuyprofitlabel_8)

        self.filweekreporttotalbuyprofit_7 = QLabel(self.widget_68)
        self.filweekreporttotalbuyprofit_7.setObjectName(u"filweekreporttotalbuyprofit_7")
        self.filweekreporttotalbuyprofit_7.setFont(font1)
        self.filweekreporttotalbuyprofit_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_78.addWidget(self.filweekreporttotalbuyprofit_7)


        self.horizontalLayout_52.addLayout(self.verticalLayout_78)


        self.verticalLayout_58.addWidget(self.widget_68)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.widget_62 = QWidget(self.widget_63)
        self.widget_62.setObjectName(u"widget_62")
        self.horizontalLayout_46 = QHBoxLayout(self.widget_62)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.verticalLayout_77 = QVBoxLayout()
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.monthreporttutalbuylabel_8 = QLabel(self.widget_62)
        self.monthreporttutalbuylabel_8.setObjectName(u"monthreporttutalbuylabel_8")
        self.monthreporttutalbuylabel_8.setFont(font)

        self.verticalLayout_77.addWidget(self.monthreporttutalbuylabel_8)

        self.filweekreporttotalbuy_7 = QLabel(self.widget_62)
        self.filweekreporttotalbuy_7.setObjectName(u"filweekreporttotalbuy_7")
        self.filweekreporttotalbuy_7.setFont(font1)
        self.filweekreporttotalbuy_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_77.addWidget(self.filweekreporttotalbuy_7)


        self.horizontalLayout_46.addLayout(self.verticalLayout_77)


        self.horizontalLayout_48.addWidget(self.widget_62)

        self.widget_39 = QWidget(self.widget_63)
        self.widget_39.setObjectName(u"widget_39")
        self.horizontalLayout_47 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.verticalLayout_82 = QVBoxLayout()
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.monthreporttutalbuyprofitlabel_12 = QLabel(self.widget_39)
        self.monthreporttutalbuyprofitlabel_12.setObjectName(u"monthreporttutalbuyprofitlabel_12")
        self.monthreporttutalbuyprofitlabel_12.setFont(font)
        self.monthreporttutalbuyprofitlabel_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_82.addWidget(self.monthreporttutalbuyprofitlabel_12)

        self.filweekreporttotalbuyprofit_11 = QLabel(self.widget_39)
        self.filweekreporttotalbuyprofit_11.setObjectName(u"filweekreporttotalbuyprofit_11")
        self.filweekreporttotalbuyprofit_11.setFont(font1)
        self.filweekreporttotalbuyprofit_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_82.addWidget(self.filweekreporttotalbuyprofit_11)


        self.horizontalLayout_47.addLayout(self.verticalLayout_82)


        self.horizontalLayout_48.addWidget(self.widget_39)


        self.verticalLayout_58.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.widget_64 = QWidget(self.widget_63)
        self.widget_64.setObjectName(u"widget_64")
        self.horizontalLayout_95 = QHBoxLayout(self.widget_64)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.verticalLayout_79 = QVBoxLayout()
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.monthreporttutalbuylabel_9 = QLabel(self.widget_64)
        self.monthreporttutalbuylabel_9.setObjectName(u"monthreporttutalbuylabel_9")
        self.monthreporttutalbuylabel_9.setFont(font)

        self.verticalLayout_79.addWidget(self.monthreporttutalbuylabel_9)

        self.filweekreporttotalbuy_8 = QLabel(self.widget_64)
        self.filweekreporttotalbuy_8.setObjectName(u"filweekreporttotalbuy_8")
        self.filweekreporttotalbuy_8.setFont(font1)
        self.filweekreporttotalbuy_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_79.addWidget(self.filweekreporttotalbuy_8)


        self.horizontalLayout_95.addLayout(self.verticalLayout_79)


        self.horizontalLayout_94.addWidget(self.widget_64)

        self.widget_65 = QWidget(self.widget_63)
        self.widget_65.setObjectName(u"widget_65")
        self.horizontalLayout_96 = QHBoxLayout(self.widget_65)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.verticalLayout_80 = QVBoxLayout()
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.monthreporttutalbuyprofitlabel_9 = QLabel(self.widget_65)
        self.monthreporttutalbuyprofitlabel_9.setObjectName(u"monthreporttutalbuyprofitlabel_9")
        self.monthreporttutalbuyprofitlabel_9.setFont(font)
        self.monthreporttutalbuyprofitlabel_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_80.addWidget(self.monthreporttutalbuyprofitlabel_9)

        self.filweekreporttotalbuyprofit_8 = QLabel(self.widget_65)
        self.filweekreporttotalbuyprofit_8.setObjectName(u"filweekreporttotalbuyprofit_8")
        self.filweekreporttotalbuyprofit_8.setFont(font1)
        self.filweekreporttotalbuyprofit_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_80.addWidget(self.filweekreporttotalbuyprofit_8)


        self.horizontalLayout_96.addLayout(self.verticalLayout_80)


        self.horizontalLayout_94.addWidget(self.widget_65)


        self.verticalLayout_58.addLayout(self.horizontalLayout_94)


        self.verticalLayout_73.addLayout(self.verticalLayout_58)


        self.horizontalLayout_51.addWidget(self.widget_63)


        self.verticalLayout_83.addWidget(self.widget_54)


        self.verticalLayout_84.addLayout(self.verticalLayout_83)


        self.verticalLayout_61.addWidget(self.widget_70)

        self.widget_29 = QWidget(self.scrollAreaWidgetContents)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMinimumSize(QSize(300, 260))
        self.horizontalLayout_54 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.tableWidget = QTableWidget(self.widget_29)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(False)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_54.addWidget(self.tableWidget)


        self.verticalLayout_61.addWidget(self.widget_29)


        self.horizontalLayout_57.addLayout(self.verticalLayout_61)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_89.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_3)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_46 = QVBoxLayout(self.page_6)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.frame_2 = QFrame(self.page_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_2)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.splitter_2 = QSplitter(self.frame_2)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.horizontalLayout_62 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.layoutWidget2)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_41 = QVBoxLayout(self.widget_14)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.accountpageperfotmancelabel = QLabel(self.widget_14)
        self.accountpageperfotmancelabel.setObjectName(u"accountpageperfotmancelabel")
        self.accountpageperfotmancelabel.setFont(font2)
        self.accountpageperfotmancelabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.accountpageperfotmancelabel)

        self.accountpagestatsbtb = QPushButton(self.widget_14)
        self.accountpagestatsbtb.setObjectName(u"accountpagestatsbtb")
        self.accountpagestatsbtb.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/development.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountpagestatsbtb.setIcon(icon2)
        self.accountpagestatsbtb.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.accountpagestatsbtb)


        self.verticalLayout_41.addLayout(self.verticalLayout_4)


        self.horizontalLayout_62.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.layoutWidget2)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_61 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.accountspagemt5label = QLabel(self.widget_15)
        self.accountspagemt5label.setObjectName(u"accountspagemt5label")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.accountspagemt5label.setFont(font4)
        self.accountspagemt5label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.accountspagemt5label)

        self.accountspagesetupbtn = QPushButton(self.widget_15)
        self.accountspagesetupbtn.setObjectName(u"accountspagesetupbtn")
        self.accountspagesetupbtn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/user (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountspagesetupbtn.setIcon(icon3)
        self.accountspagesetupbtn.setIconSize(QSize(20, 20))

        self.verticalLayout_42.addWidget(self.accountspagesetupbtn)


        self.horizontalLayout_61.addLayout(self.verticalLayout_42)


        self.horizontalLayout_62.addWidget(self.widget_15)

        self.splitter.addWidget(self.layoutWidget2)
        self.splitter_2.addWidget(self.splitter)

        self.verticalLayout_43.addWidget(self.splitter_2)


        self.verticalLayout_46.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.horizontalLayout_65 = QHBoxLayout(self.page_7)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.frame = QFrame(self.page_7)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.splitter_4 = QSplitter(self.frame)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.splitter_3 = QSplitter(self.splitter_4)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.widget_13 = QWidget(self.splitter_3)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_63 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.algoadjustparamlabel = QLabel(self.widget_13)
        self.algoadjustparamlabel.setObjectName(u"algoadjustparamlabel")
        self.algoadjustparamlabel.setFont(font1)
        self.algoadjustparamlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.algoadjustparamlabel)

        self.algoparamsbtn = QPushButton(self.widget_13)
        self.algoparamsbtn.setObjectName(u"algoparamsbtn")
        self.algoparamsbtn.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/adjustment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.algoparamsbtn.setIcon(icon4)
        self.algoparamsbtn.setIconSize(QSize(20, 20))

        self.verticalLayout_44.addWidget(self.algoparamsbtn)


        self.horizontalLayout_63.addLayout(self.verticalLayout_44)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.algoactivationlabel = QLabel(self.widget_13)
        self.algoactivationlabel.setObjectName(u"algoactivationlabel")
        self.algoactivationlabel.setFont(font1)
        self.algoactivationlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.algoactivationlabel)

        self.algoactivalebtn = QPushButton(self.widget_13)
        self.algoactivalebtn.setObjectName(u"algoactivalebtn")
        self.algoactivalebtn.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/power-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.algoactivalebtn.setIcon(icon5)
        self.algoactivalebtn.setIconSize(QSize(20, 20))

        self.verticalLayout_45.addWidget(self.algoactivalebtn)


        self.horizontalLayout_63.addLayout(self.verticalLayout_45)

        self.splitter_3.addWidget(self.widget_13)
        self.splitter_4.addWidget(self.splitter_3)

        self.horizontalLayout_64.addWidget(self.splitter_4)


        self.horizontalLayout_65.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_7)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_51 = QVBoxLayout(self.page_5)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.widget_21 = QWidget(self.page_5)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_50 = QVBoxLayout(self.widget_21)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.statuslabel = QLabel(self.widget_21)
        self.statuslabel.setObjectName(u"statuslabel")
        self.statuslabel.setFont(font)
        self.statuslabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.statuslabel)

        self.filstatus = QLabel(self.widget_21)
        self.filstatus.setObjectName(u"filstatus")
        self.filstatus.setFont(font)
        self.filstatus.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.filstatus)


        self.verticalLayout_50.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.widget_19 = QWidget(self.widget_21)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_48 = QVBoxLayout(self.widget_19)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.activateagentbtn = QPushButton(self.widget_19)
        self.activateagentbtn.setObjectName(u"activateagentbtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/switch-on (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.activateagentbtn.setIcon(icon6)
        self.activateagentbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_48.addWidget(self.activateagentbtn)


        self.horizontalLayout_67.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.widget_21)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_49 = QVBoxLayout(self.widget_20)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.deactivateagentbtn = QPushButton(self.widget_20)
        self.deactivateagentbtn.setObjectName(u"deactivateagentbtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/switch-off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deactivateagentbtn.setIcon(icon7)
        self.deactivateagentbtn.setIconSize(QSize(30, 30))

        self.verticalLayout_49.addWidget(self.deactivateagentbtn)


        self.horizontalLayout_67.addWidget(self.widget_20)


        self.verticalLayout_50.addLayout(self.horizontalLayout_67)


        self.verticalLayout_51.addWidget(self.widget_21)

        self.stackedWidget.addWidget(self.page_5)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_74 = QHBoxLayout(self.page_4)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.widget_17 = QWidget(self.page_4)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_70 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.metatraderadjlabel = QLabel(self.widget_17)
        self.metatraderadjlabel.setObjectName(u"metatraderadjlabel")
        self.metatraderadjlabel.setFont(font4)
        self.metatraderadjlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.metatraderadjlabel)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.lotsizelabel = QLabel(self.widget_17)
        self.lotsizelabel.setObjectName(u"lotsizelabel")
        self.lotsizelabel.setFont(font)

        self.horizontalLayout_68.addWidget(self.lotsizelabel)

        self.horizontalSpacer_27 = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_27)

        self.lotsizeinp = QLineEdit(self.widget_17)
        self.lotsizeinp.setObjectName(u"lotsizeinp")

        self.horizontalLayout_68.addWidget(self.lotsizeinp)

        self.horizontalSpacer_28 = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_28)

        self.lotsizebtn = QPushButton(self.widget_17)
        self.lotsizebtn.setObjectName(u"lotsizebtn")
        self.lotsizebtn.setFont(font1)

        self.horizontalLayout_68.addWidget(self.lotsizebtn)


        self.verticalLayout_52.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.deviationlabel = QLabel(self.widget_17)
        self.deviationlabel.setObjectName(u"deviationlabel")
        self.deviationlabel.setFont(font)

        self.horizontalLayout_69.addWidget(self.deviationlabel)

        self.horizontalSpacer_30 = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer_30)

        self.deviationinp = QLineEdit(self.widget_17)
        self.deviationinp.setObjectName(u"deviationinp")

        self.horizontalLayout_69.addWidget(self.deviationinp)

        self.horizontalSpacer_29 = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer_29)

        self.updatedeviationbtn = QPushButton(self.widget_17)
        self.updatedeviationbtn.setObjectName(u"updatedeviationbtn")
        self.updatedeviationbtn.setFont(font1)

        self.horizontalLayout_69.addWidget(self.updatedeviationbtn)


        self.verticalLayout_52.addLayout(self.horizontalLayout_69)


        self.horizontalLayout_70.addLayout(self.verticalLayout_52)


        self.horizontalLayout_74.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.page_4)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_73 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.mtexistingvaueslabel = QLabel(self.widget_18)
        self.mtexistingvaueslabel.setObjectName(u"mtexistingvaueslabel")
        self.mtexistingvaueslabel.setFont(font2)
        self.mtexistingvaueslabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.mtexistingvaueslabel)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.exlotsizelabel = QLabel(self.widget_18)
        self.exlotsizelabel.setObjectName(u"exlotsizelabel")
        self.exlotsizelabel.setFont(font)

        self.horizontalLayout_72.addWidget(self.exlotsizelabel)

        self.horizontalSpacer_32 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_32)

        self.filexlotsize = QLabel(self.widget_18)
        self.filexlotsize.setObjectName(u"filexlotsize")
        self.filexlotsize.setFont(font1)
        self.filexlotsize.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.filexlotsize)

        self.horizontalSpacer_31 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_31)

        self.resetlotsizebtn = QPushButton(self.widget_18)
        self.resetlotsizebtn.setObjectName(u"resetlotsizebtn")
        self.resetlotsizebtn.setFont(font1)

        self.horizontalLayout_72.addWidget(self.resetlotsizebtn)


        self.verticalLayout_53.addLayout(self.horizontalLayout_72)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.exdeviationlabel = QLabel(self.widget_18)
        self.exdeviationlabel.setObjectName(u"exdeviationlabel")
        self.exdeviationlabel.setFont(font)

        self.horizontalLayout_71.addWidget(self.exdeviationlabel)

        self.horizontalSpacer_33 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_71.addItem(self.horizontalSpacer_33)

        self.filexdeviation = QLabel(self.widget_18)
        self.filexdeviation.setObjectName(u"filexdeviation")
        self.filexdeviation.setFont(font1)
        self.filexdeviation.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.filexdeviation)

        self.horizontalSpacer_34 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_71.addItem(self.horizontalSpacer_34)

        self.resetexdeviation = QPushButton(self.widget_18)
        self.resetexdeviation.setObjectName(u"resetexdeviation")
        self.resetexdeviation.setFont(font1)

        self.horizontalLayout_71.addWidget(self.resetexdeviation)


        self.verticalLayout_53.addLayout(self.horizontalLayout_71)


        self.horizontalLayout_73.addLayout(self.verticalLayout_53)


        self.horizontalLayout_74.addWidget(self.widget_18)

        self.stackedWidget.addWidget(self.page_4)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_47 = QVBoxLayout(self.page)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_7 = QWidget(self.page)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.accountslabel = QLabel(self.widget_7)
        self.accountslabel.setObjectName(u"accountslabel")
        font5 = QFont()
        font5.setFamilies([u"Sitka Text"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.accountslabel.setFont(font5)
        self.accountslabel.setCursor(QCursor(Qt.ArrowCursor))
        self.accountslabel.setMouseTracking(True)
        self.accountslabel.setFocusPolicy(Qt.StrongFocus)
        self.accountslabel.setFrameShape(QFrame.StyledPanel)
        self.accountslabel.setFrameShadow(QFrame.Plain)
        self.accountslabel.setAlignment(Qt.AlignCenter)
        self.accountslabel.setWordWrap(False)
        self.accountslabel.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_6.addWidget(self.accountslabel)

        self.Algolabel = QLabel(self.widget_7)
        self.Algolabel.setObjectName(u"Algolabel")
        font6 = QFont()
        font6.setFamilies([u"Sitka"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.Algolabel.setFont(font6)
        self.Algolabel.setMouseTracking(True)
        self.Algolabel.setFocusPolicy(Qt.StrongFocus)
        self.Algolabel.setFrameShape(QFrame.StyledPanel)
        self.Algolabel.setLineWidth(0)
        self.Algolabel.setMidLineWidth(0)
        self.Algolabel.setTextFormat(Qt.PlainText)
        self.Algolabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.Algolabel)


        self.verticalLayout_10.addWidget(self.widget_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_5 = QWidget(self.page)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.performancelabel = QLabel(self.widget_5)
        self.performancelabel.setObjectName(u"performancelabel")
        self.performancelabel.setFont(font2)
        self.performancelabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.performancelabel)

        self.statsbtn = QPushButton(self.widget_5)
        self.statsbtn.setObjectName(u"statsbtn")
        self.statsbtn.setFont(font1)
        self.statsbtn.setIcon(icon2)
        self.statsbtn.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.statsbtn)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.mt5label = QLabel(self.widget_5)
        self.mt5label.setObjectName(u"mt5label")
        self.mt5label.setFont(font4)
        self.mt5label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.mt5label)

        self.setupbtn = QPushButton(self.widget_5)
        self.setupbtn.setObjectName(u"setupbtn")
        self.setupbtn.setFont(font1)
        self.setupbtn.setIcon(icon3)
        self.setupbtn.setIconSize(QSize(20, 20))

        self.verticalLayout_7.addWidget(self.setupbtn)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.horizontalLayout_5.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.page)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.adjustparamslabel = QLabel(self.widget_6)
        self.adjustparamslabel.setObjectName(u"adjustparamslabel")
        self.adjustparamslabel.setFont(font1)
        self.adjustparamslabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.adjustparamslabel)

        self.paramspagebtn = QPushButton(self.widget_6)
        self.paramspagebtn.setObjectName(u"paramspagebtn")
        self.paramspagebtn.setFont(font1)
        self.paramspagebtn.setIcon(icon4)
        self.paramspagebtn.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.paramspagebtn)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.activationlabel = QLabel(self.widget_6)
        self.activationlabel.setObjectName(u"activationlabel")
        self.activationlabel.setFont(font1)
        self.activationlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.activationlabel)

        self.activatebtn = QPushButton(self.widget_6)
        self.activatebtn.setObjectName(u"activatebtn")
        self.activatebtn.setFont(font1)
        self.activatebtn.setIcon(icon5)
        self.activatebtn.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.activatebtn)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.horizontalLayout_5.addWidget(self.widget_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)


        self.verticalLayout_47.addLayout(self.verticalLayout_10)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_12 = QHBoxLayout(self.page_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_34 = QWidget(self.page_2)
        self.widget_34.setObjectName(u"widget_34")
        self.verticalLayout_14 = QVBoxLayout(self.widget_34)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.adjustparamlabel = QLabel(self.widget_34)
        self.adjustparamlabel.setObjectName(u"adjustparamlabel")
        self.adjustparamlabel.setFont(font4)
        self.adjustparamlabel.setScaledContents(False)
        self.adjustparamlabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.adjustparamlabel)

        self.setvalueslabel = QLabel(self.widget_34)
        self.setvalueslabel.setObjectName(u"setvalueslabel")
        self.setvalueslabel.setFont(font4)
        self.setvalueslabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.setvalueslabel)


        self.verticalLayout_14.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_31 = QWidget(self.widget_34)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.distancelabel = QLabel(self.widget_31)
        self.distancelabel.setObjectName(u"distancelabel")
        self.distancelabel.setFont(font)

        self.verticalLayout_57.addWidget(self.distancelabel)

        self.candlesizelabel = QLabel(self.widget_31)
        self.candlesizelabel.setObjectName(u"candlesizelabel")
        self.candlesizelabel.setFont(font)

        self.verticalLayout_57.addWidget(self.candlesizelabel)

        self.tplabel = QLabel(self.widget_31)
        self.tplabel.setObjectName(u"tplabel")
        self.tplabel.setFont(font)

        self.verticalLayout_57.addWidget(self.tplabel)

        self.slwindowlabel = QLabel(self.widget_31)
        self.slwindowlabel.setObjectName(u"slwindowlabel")
        self.slwindowlabel.setFont(font)

        self.verticalLayout_57.addWidget(self.slwindowlabel)

        self.start_timelabel = QLabel(self.widget_31)
        self.start_timelabel.setObjectName(u"start_timelabel")
        self.start_timelabel.setFont(font)

        self.verticalLayout_57.addWidget(self.start_timelabel)

        self.stoptimelabel = QLabel(self.widget_31)
        self.stoptimelabel.setObjectName(u"stoptimelabel")
        self.stoptimelabel.setFont(font)

        self.verticalLayout_57.addWidget(self.stoptimelabel)


        self.horizontalLayout_7.addLayout(self.verticalLayout_57)

        self.verticalLayout_65 = QVBoxLayout()
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.maxdistanceinp = QLineEdit(self.widget_31)
        self.maxdistanceinp.setObjectName(u"maxdistanceinp")
        self.maxdistanceinp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.maxdistanceinp)

        self.candlesizeinp = QLineEdit(self.widget_31)
        self.candlesizeinp.setObjectName(u"candlesizeinp")
        self.candlesizeinp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.candlesizeinp)

        self.tpinp = QLineEdit(self.widget_31)
        self.tpinp.setObjectName(u"tpinp")
        self.tpinp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.tpinp)

        self.slwindowinp = QLineEdit(self.widget_31)
        self.slwindowinp.setObjectName(u"slwindowinp")
        self.slwindowinp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.slwindowinp)

        self.start_timeinp = QLineEdit(self.widget_31)
        self.start_timeinp.setObjectName(u"start_timeinp")
        self.start_timeinp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.start_timeinp)

        self.stoptimeinp = QLineEdit(self.widget_31)
        self.stoptimeinp.setObjectName(u"stoptimeinp")

        self.verticalLayout_65.addWidget(self.stoptimeinp)


        self.horizontalLayout_7.addLayout(self.verticalLayout_65)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.updatemaxdistance = QPushButton(self.widget_31)
        self.updatemaxdistance.setObjectName(u"updatemaxdistance")
        self.updatemaxdistance.setFont(font1)

        self.verticalLayout_13.addWidget(self.updatemaxdistance)

        self.updatecandlesize = QPushButton(self.widget_31)
        self.updatecandlesize.setObjectName(u"updatecandlesize")
        self.updatecandlesize.setFont(font1)

        self.verticalLayout_13.addWidget(self.updatecandlesize)

        self.updatetakeprofit = QPushButton(self.widget_31)
        self.updatetakeprofit.setObjectName(u"updatetakeprofit")
        self.updatetakeprofit.setFont(font1)

        self.verticalLayout_13.addWidget(self.updatetakeprofit)

        self.updateslwindow = QPushButton(self.widget_31)
        self.updateslwindow.setObjectName(u"updateslwindow")
        self.updateslwindow.setFont(font1)

        self.verticalLayout_13.addWidget(self.updateslwindow)

        self.updatestart_time = QPushButton(self.widget_31)
        self.updatestart_time.setObjectName(u"updatestart_time")
        self.updatestart_time.setFont(font1)

        self.verticalLayout_13.addWidget(self.updatestart_time)

        self.updatestoptime = QPushButton(self.widget_31)
        self.updatestoptime.setObjectName(u"updatestoptime")
        self.updatestoptime.setFont(font1)

        self.verticalLayout_13.addWidget(self.updatestoptime)


        self.horizontalLayout_7.addLayout(self.verticalLayout_13)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_11.addWidget(self.widget_31)

        self.widget_33 = QWidget(self.widget_34)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.rnmaxdistancelabel = QLabel(self.widget_33)
        self.rnmaxdistancelabel.setObjectName(u"rnmaxdistancelabel")
        self.rnmaxdistancelabel.setFont(font)
        self.rnmaxdistancelabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.rnmaxdistancelabel)

        self.rnstarttimelabel = QLabel(self.widget_33)
        self.rnstarttimelabel.setObjectName(u"rnstarttimelabel")
        self.rnstarttimelabel.setFont(font)

        self.verticalLayout_25.addWidget(self.rnstarttimelabel)

        self.rncandlesizelabel = QLabel(self.widget_33)
        self.rncandlesizelabel.setObjectName(u"rncandlesizelabel")
        self.rncandlesizelabel.setFont(font)
        self.rncandlesizelabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.rncandlesizelabel)

        self.rnslwindowlabel = QLabel(self.widget_33)
        self.rnslwindowlabel.setObjectName(u"rnslwindowlabel")
        self.rnslwindowlabel.setFont(font)
        self.rnslwindowlabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.rnslwindowlabel)

        self.rntplabel = QLabel(self.widget_33)
        self.rntplabel.setObjectName(u"rntplabel")
        self.rntplabel.setFont(font)
        self.rntplabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.rntplabel)

        self.rnstoptimelabel = QLabel(self.widget_33)
        self.rnstoptimelabel.setObjectName(u"rnstoptimelabel")
        self.rnstoptimelabel.setFont(font)
        self.rnstoptimelabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.rnstoptimelabel)


        self.horizontalLayout_19.addLayout(self.verticalLayout_25)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.exmaxdistance = QLabel(self.widget_33)
        self.exmaxdistance.setObjectName(u"exmaxdistance")
        self.exmaxdistance.setFont(font1)
        self.exmaxdistance.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.exmaxdistance)

        self.exstart_time = QLabel(self.widget_33)
        self.exstart_time.setObjectName(u"exstart_time")
        self.exstart_time.setFont(font1)
        self.exstart_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.exstart_time)

        self.excandlesize = QLabel(self.widget_33)
        self.excandlesize.setObjectName(u"excandlesize")
        self.excandlesize.setFont(font1)
        self.excandlesize.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.excandlesize)

        self.exslwindow = QLabel(self.widget_33)
        self.exslwindow.setObjectName(u"exslwindow")
        self.exslwindow.setFont(font1)
        self.exslwindow.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.exslwindow)

        self.extakeprofit = QLabel(self.widget_33)
        self.extakeprofit.setObjectName(u"extakeprofit")
        self.extakeprofit.setFont(font1)
        self.extakeprofit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.extakeprofit)

        self.exstoptime = QLabel(self.widget_33)
        self.exstoptime.setObjectName(u"exstoptime")
        self.exstoptime.setFont(font1)
        self.exstoptime.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.exstoptime)


        self.horizontalLayout_19.addLayout(self.verticalLayout_34)

        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.resetmaxdistance = QPushButton(self.widget_33)
        self.resetmaxdistance.setObjectName(u"resetmaxdistance")
        self.resetmaxdistance.setFont(font1)

        self.verticalLayout_56.addWidget(self.resetmaxdistance)

        self.resetstarttime = QPushButton(self.widget_33)
        self.resetstarttime.setObjectName(u"resetstarttime")
        self.resetstarttime.setFont(font1)

        self.verticalLayout_56.addWidget(self.resetstarttime)

        self.resetcandlesize = QPushButton(self.widget_33)
        self.resetcandlesize.setObjectName(u"resetcandlesize")
        self.resetcandlesize.setFont(font1)

        self.verticalLayout_56.addWidget(self.resetcandlesize)

        self.resetslwindow = QPushButton(self.widget_33)
        self.resetslwindow.setObjectName(u"resetslwindow")
        self.resetslwindow.setFont(font1)

        self.verticalLayout_56.addWidget(self.resetslwindow)

        self.reset_takeprofit = QPushButton(self.widget_33)
        self.reset_takeprofit.setObjectName(u"reset_takeprofit")
        self.reset_takeprofit.setFont(font1)

        self.verticalLayout_56.addWidget(self.reset_takeprofit)

        self.resetstoptime = QPushButton(self.widget_33)
        self.resetstoptime.setObjectName(u"resetstoptime")
        self.resetstoptime.setFont(font1)

        self.verticalLayout_56.addWidget(self.resetstoptime)


        self.horizontalLayout_19.addLayout(self.verticalLayout_56)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_11.addWidget(self.widget_33)


        self.verticalLayout_14.addLayout(self.horizontalLayout_11)

        self.resetallbtn_ = QPushButton(self.widget_34)
        self.resetallbtn_.setObjectName(u"resetallbtn_")
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setItalic(True)
        self.resetallbtn_.setFont(font7)

        self.verticalLayout_14.addWidget(self.resetallbtn_)

        self.resetallbtn = QPushButton(self.widget_34)
        self.resetallbtn.setObjectName(u"resetallbtn")
        self.resetallbtn.setFont(font7)

        self.verticalLayout_14.addWidget(self.resetallbtn)


        self.horizontalLayout_12.addWidget(self.widget_34)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_54.addWidget(self.stackedWidget)


        self.gridLayout.addLayout(self.verticalLayout_54, 1, 2, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logosub = QLabel(self.widget_3)
        self.logosub.setObjectName(u"logosub")
        self.logosub.setMinimumSize(QSize(50, 50))
        self.logosub.setMaximumSize(QSize(70, 70))
        self.logosub.setPixmap(QPixmap(u":/icons/icons/agent-high-resolution-logo.png"))
        self.logosub.setScaledContents(True)
        self.logosub.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.logosub)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 128, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.homesub = QPushButton(self.widget_3)
        self.homesub.setObjectName(u"homesub")
        self.homesub.setFont(font3)
        self.homesub.setMouseTracking(True)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homesub.setIcon(icon8)
        self.homesub.setIconSize(QSize(20, 16))
        self.homesub.setCheckable(True)
        self.homesub.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.homesub)

        self.accountssub = QPushButton(self.widget_3)
        self.accountssub.setObjectName(u"accountssub")
        self.accountssub.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountssub.setIcon(icon9)
        self.accountssub.setCheckable(True)
        self.accountssub.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.accountssub)

        self.algosub = QPushButton(self.widget_3)
        self.algosub.setObjectName(u"algosub")
        self.algosub.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/ai.png", QSize(), QIcon.Normal, QIcon.Off)
        self.algosub.setIcon(icon10)
        self.algosub.setCheckable(True)
        self.algosub.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.algosub)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 158, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.closesub = QPushButton(self.widget_3)
        self.closesub.setObjectName(u"closesub")
        self.closesub.setFont(font1)
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closesub.setIcon(icon11)
        self.closesub.setCheckable(True)
        self.closesub.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.closesub)

        self.verticalSpacer_3 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout.addWidget(self.widget_3, 1, 1, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.gridLayout.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menubtn.toggled.connect(self.widget_3.setHidden)
        self.menubtn.toggled.connect(self.widget_3.setVisible)
        self.closesub.toggled.connect(self.widget_3.setHidden)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menubtn.setText("")
        self.mainlogo.setText("")
        self.supportbtn.setText("")
        self.accountbalancelabel.setText(QCoreApplication.translate("MainWindow", u"Account Balance", None))
        self.flaccountbalance.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.dailyperformancelabel.setText(QCoreApplication.translate("MainWindow", u"Today Returns", None))
        self.fldailyperformace.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.weekyperformancelabel.setText(QCoreApplication.translate("MainWindow", u"Weeks Returns", None))
        self.flweeklyprofit.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthlyperformancelablel.setText(QCoreApplication.translate("MainWindow", u"Monthly Returns", None))
        self.flmonthlyperformance.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.growthratelabel.setText(QCoreApplication.translate("MainWindow", u"Growth Rate", None))
        self.flgrowthrate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.weeklyspotlightlabel.setText(QCoreApplication.translate("MainWindow", u"Weeky Spotlight", None))
        self.weeklybuylabel.setText(QCoreApplication.translate("MainWindow", u"Profit", None))
        self.weekyprofdaylabel.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.flweekyprofday.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.weeklyprofammountlabel.setText(QCoreApplication.translate("MainWindow", u"Ammount", None))
        self.flweeklyprofammount.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.weelylosslabel.setText(QCoreApplication.translate("MainWindow", u"Loss", None))
        self.weekylossdaylabel.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.flweekylossday.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.weeklylossammountlabel.setText(QCoreApplication.translate("MainWindow", u"Ammount", None))
        self.flweeklylossammount.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthlyspotlightlabel.setText(QCoreApplication.translate("MainWindow", u"Month Spotlight", None))
        self.monthlosslabel.setText(QCoreApplication.translate("MainWindow", u"Loss", None))
        self.monthlossdaylabel.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.flmonthlossday.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthlossammountlabel.setText(QCoreApplication.translate("MainWindow", u"Ammount", None))
        self.flmonthlossammount.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.montbuylabel.setText(QCoreApplication.translate("MainWindow", u"Profit", None))
        self.montprofdaylabel_2.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.flmontprofday.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthprofammountlabel.setText(QCoreApplication.translate("MainWindow", u"Ammount", None))
        self.flmonthprofammount.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.maiaccbalancelabel.setText(QCoreApplication.translate("MainWindow", u"Account Balance", None))
        self.filmainaccountbalance.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.opentradelabel.setText(QCoreApplication.translate("MainWindow", u"Open Trade Profit", None))
        self.filopentradeprofit.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.weeklyreportlabel.setText(QCoreApplication.translate("MainWindow", u"Weeky Report", None))
        self.weeklyreport_total_label.setText(QCoreApplication.translate("MainWindow", u"Total Profit", None))
        self.filweeklyreport_totalprofit.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuyprofitlabel_2.setText(QCoreApplication.translate("MainWindow", u"Total Buy Profit", None))
        self.filweekreporttotalbuyprofit.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuylabel_2.setText(QCoreApplication.translate("MainWindow", u"Total Profitable Buys", None))
        self.filweekreporttotalbuy.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuyprofitlabel_10.setText(QCoreApplication.translate("MainWindow", u"Profitable Buys Total", None))
        self.filweekreporttotalbuyprofit_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuylabel_3.setText(QCoreApplication.translate("MainWindow", u"Total Lost Buys", None))
        self.filweekreporttotalbuy_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuyprofitlabel_3.setText(QCoreApplication.translate("MainWindow", u"Lost Buys Total", None))
        self.filweekreporttotalbuyprofit_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuyprofitlabel_4.setText(QCoreApplication.translate("MainWindow", u"Total Sell Profit", None))
        self.filweekreporttotalbuyprofit_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuylabel_4.setText(QCoreApplication.translate("MainWindow", u"Total Profitable Sells", None))
        self.filweekreporttotalbuy_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuyprofitlabel_11.setText(QCoreApplication.translate("MainWindow", u"Profitable sells Total", None))
        self.filweekreporttotalbuyprofit_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuylabel_5.setText(QCoreApplication.translate("MainWindow", u"Total Lost Sells", None))
        self.filweekreporttotalbuy_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuyprofitlabel_5.setText(QCoreApplication.translate("MainWindow", u"Lost Sells Total", None))
        self.filweekreporttotalbuyprofit_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.weeklyreportlabel_2.setText(QCoreApplication.translate("MainWindow", u"Monthly Report", None))
        self.weeklyreport_total_label_2.setText(QCoreApplication.translate("MainWindow", u"Total Profit", None))
        self.filweeklyreport_totalprofit_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuyprofitlabel_6.setText(QCoreApplication.translate("MainWindow", u"Total Buy Profit", None))
        self.filweekreporttotalbuyprofit_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuylabel_6.setText(QCoreApplication.translate("MainWindow", u"Total Profitable Buys", None))
        self.filweekreporttotalbuy_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuyprofitlabel_13.setText(QCoreApplication.translate("MainWindow", u"Profitable Buys Total", None))
        self.filweekreporttotalbuyprofit_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuylabel_7.setText(QCoreApplication.translate("MainWindow", u"Total Lost Buys", None))
        self.filweekreporttotalbuy_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuyprofitlabel_7.setText(QCoreApplication.translate("MainWindow", u"Lost Buy Total", None))
        self.filweekreporttotalbuyprofit_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuyprofitlabel_8.setText(QCoreApplication.translate("MainWindow", u"Total Sell Profit", None))
        self.filweekreporttotalbuyprofit_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuylabel_8.setText(QCoreApplication.translate("MainWindow", u"Total Profitable Sells", None))
        self.filweekreporttotalbuy_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuyprofitlabel_12.setText(QCoreApplication.translate("MainWindow", u"Profitable Sells Total", None))
        self.filweekreporttotalbuyprofit_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuylabel_9.setText(QCoreApplication.translate("MainWindow", u"Total Lost Sells", None))
        self.filweekreporttotalbuy_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.monthreporttutalbuyprofitlabel_9.setText(QCoreApplication.translate("MainWindow", u"lost Sell Total", None))
        self.filweekreporttotalbuyprofit_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Day", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Open Time", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Total Profit", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Lot size", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Close Time", None));
        self.accountpageperfotmancelabel.setText(QCoreApplication.translate("MainWindow", u"Performance", None))
        self.accountpagestatsbtb.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.accountspagemt5label.setText(QCoreApplication.translate("MainWindow", u"Mt5 Setup", None))
        self.accountspagesetupbtn.setText(QCoreApplication.translate("MainWindow", u"setup", None))
        self.algoadjustparamlabel.setText(QCoreApplication.translate("MainWindow", u"Adjust parameters", None))
        self.algoparamsbtn.setText(QCoreApplication.translate("MainWindow", u"Params", None))
        self.algoactivationlabel.setText(QCoreApplication.translate("MainWindow", u"Activation", None))
        self.algoactivalebtn.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.statuslabel.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.filstatus.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.activateagentbtn.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.deactivateagentbtn.setText(QCoreApplication.translate("MainWindow", u"Deactivate", None))
        self.metatraderadjlabel.setText(QCoreApplication.translate("MainWindow", u"Mt5 Adjustment", None))
        self.lotsizelabel.setText(QCoreApplication.translate("MainWindow", u"Lotsize", None))
        self.lotsizebtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.deviationlabel.setText(QCoreApplication.translate("MainWindow", u"Deviation", None))
        self.updatedeviationbtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.mtexistingvaueslabel.setText(QCoreApplication.translate("MainWindow", u"Running Values", None))
        self.exlotsizelabel.setText(QCoreApplication.translate("MainWindow", u"Lot Size", None))
        self.filexlotsize.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.resetlotsizebtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.exdeviationlabel.setText(QCoreApplication.translate("MainWindow", u"Deviation", None))
        self.filexdeviation.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.resetexdeviation.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.accountslabel.setText(QCoreApplication.translate("MainWindow", u"Account Control", None))
        self.Algolabel.setText(QCoreApplication.translate("MainWindow", u"Algorithim Setup", None))
        self.performancelabel.setText(QCoreApplication.translate("MainWindow", u"Performance", None))
        self.statsbtn.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.mt5label.setText(QCoreApplication.translate("MainWindow", u"Mt5 Setup", None))
        self.setupbtn.setText(QCoreApplication.translate("MainWindow", u"setup", None))
        self.adjustparamslabel.setText(QCoreApplication.translate("MainWindow", u"Adjust parameters", None))
        self.paramspagebtn.setText(QCoreApplication.translate("MainWindow", u"Params", None))
        self.activationlabel.setText(QCoreApplication.translate("MainWindow", u"Activation", None))
        self.activatebtn.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
        self.adjustparamlabel.setText(QCoreApplication.translate("MainWindow", u"Adjust Parameter", None))
        self.setvalueslabel.setText(QCoreApplication.translate("MainWindow", u"Running Values", None))
        self.distancelabel.setText(QCoreApplication.translate("MainWindow", u"Max Distance", None))
        self.candlesizelabel.setText(QCoreApplication.translate("MainWindow", u"Candle Size", None))
        self.tplabel.setText(QCoreApplication.translate("MainWindow", u"Take Profit", None))
        self.slwindowlabel.setText(QCoreApplication.translate("MainWindow", u"Sl window", None))
        self.start_timelabel.setText(QCoreApplication.translate("MainWindow", u"Start Time", None))
        self.stoptimelabel.setText(QCoreApplication.translate("MainWindow", u"Stop Time", None))
        self.updatemaxdistance.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.updatecandlesize.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.updatetakeprofit.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.updateslwindow.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.updatestart_time.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.updatestoptime.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.rnmaxdistancelabel.setText(QCoreApplication.translate("MainWindow", u"Max Distance", None))
        self.rnstarttimelabel.setText(QCoreApplication.translate("MainWindow", u"Starttime", None))
        self.rncandlesizelabel.setText(QCoreApplication.translate("MainWindow", u"Candle Size", None))
        self.rnslwindowlabel.setText(QCoreApplication.translate("MainWindow", u"Sl window", None))
        self.rntplabel.setText(QCoreApplication.translate("MainWindow", u"TP", None))
        self.rnstoptimelabel.setText(QCoreApplication.translate("MainWindow", u"Stop Time", None))
        self.exmaxdistance.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.exstart_time.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.excandlesize.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.exslwindow.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.extakeprofit.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.exstoptime.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.resetmaxdistance.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.resetstarttime.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.resetcandlesize.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.resetslwindow.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.reset_takeprofit.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.resetstoptime.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.resetallbtn_.setText(QCoreApplication.translate("MainWindow", u"Update All", None))
        self.resetallbtn.setText(QCoreApplication.translate("MainWindow", u"Restore all defaults", None))
        self.logosub.setText("")
        self.homesub.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.accountssub.setText(QCoreApplication.translate("MainWindow", u"Acc", None))
        self.algosub.setText(QCoreApplication.translate("MainWindow", u"Algo", None))
        self.closesub.setText(QCoreApplication.translate("MainWindow", u"Close", None))
    # retranslateUi

