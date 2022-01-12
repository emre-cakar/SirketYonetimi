from qt_core import *

class Saat(QLabel):
    def __init__(self):
        super().__init__()
        timer=QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        self.showtime()
    def showtime(self):
        get_time=QDateTime.currentDateTime()
        get_text=get_time.toString('dd MMMM yyyy dddd hh:mm:ss')
        self.setText(get_text)

class buttonSpeacial(QToolButton):
    mouseHover = QtCore.pyqtSignal(bool)
    def __init__(self, liste ):
        QToolButton.__init__(self, )
        self.metin=liste[0]
        self.objeismi=liste[1]
        self.adres=liste[2]
        self.genislik=liste[3]
        self.yukseklik=liste[4]
        self.hoverAdres=liste[5]
        
        self.setMouseTracking(True)
        self.setIcon(QIcon(self.adres))
        self.setIconSize(QtCore.QSize(self.genislik,self.genislik))
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.setText(self.metin)
        self.setObjectName(self.objeismi)
        self.setCursor(QCursor(Qt.PointingHandCursor))
    def enterEvent(self, event):
        self.mouseHover.emit(True)
        self.setIcon(QIcon(self.hoverAdres))
        self.setIconSize(QtCore.QSize(self.genislik,self.yukseklik))
    def leaveEvent(self, event):
        self.mouseHover.emit(False)
        self.setIcon(QIcon(self.adres))
        self.setIconSize(QtCore.QSize(self.genislik,self.yukseklik))



class Takvim(QFrame):
    def setupUi(self, frame):
        self.frame=frame
        self.frame_layout=QVBoxLayout(self.frame)
        self.cal=QCalendarWidget(self)
        self.cal.setGridVisible(True)

        self.cal_btn=QPushButton()
        self.today=QDate().currentDate().toString('dd.MM.yyyy')
        self.cal_btn.setText(self.today)
        self.cal_btn.clicked.connect(self.calender_showHide)
        self.cal.clicked[QtCore.QDate].connect(self.showDate)

        self.frame_layout.addWidget(self.cal_btn)
        self.frame_layout.addWidget(self.cal)
        

    
    def showDate(self, date):
        self.cal_btn.setText(date.toString('dd.MM.yyyy'))
        self.cal.hide()

    def calender_showHide(self):
        if self.cal.isVisible():
            self.cal.hide()
        else:
            self.cal.show()
            

