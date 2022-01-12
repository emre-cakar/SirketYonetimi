from qt_core import *
from gui.widgets.app_widgets import  *

class hazirlamaSayfasi(object):


    def setupUi(self, StackedWidget):

        #Variable
        self.stacked=StackedWidget
        self.sayfanumarasi=0
    
################### Variable Finish #################################################
################### PAGE-1 Start ####################################################

        self.sayfa1=QWidget()
        self.sayfa1.setObjectName(u"islemTuru")
        self.sayfa1.setStyleSheet("""
            margin:25px;
            background-color:#2C394B;
            border:1px solid #3498db;
        """)
        self.sayfa1_layout=QHBoxLayout()
        self.sayfa1_layout.setContentsMargins(0,0,0,0)
        self.sayfa1_layout.setSpacing(0)
        self.sayfa1.setLayout(self.sayfa1_layout)
        
        self.baslik=QLabel(self.sayfa1)
        self.baslik.setText(" SAYFA HAZIRLANIYOR ")
        self.baslik.setStyleSheet("""
            padding-bottom:20px;
            border:0;
            border:1px solid #3498db;
            font-size:40pt;
            color:white;
            font-family:"Times New Roman";
            letter-spacing:15px;
        """)
        self.baslik.setAlignment(Qt.AlignCenter)


        self.sayfa1_layout.addWidget(self.baslik)

        StackedWidget.addWidget(self.sayfa1)
        
################### PAGE-1 Finish ###################################################


        StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def geri(self):
        self.sayfanumarasi-=1
        self.stacked.setCurrentIndex(self.sayfanumarasi)
    def ileri(self):
        self.sayfanumarasi+=1
        self.stacked.setCurrentIndex(self.sayfanumarasi)


